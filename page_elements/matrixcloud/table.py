from selene.api import *

from helpers.helpers import take_element_screenshot


class Table:

    def __getitem__(self, key):
        table_css_selector = getattr(self, key)
        s(table_css_selector).wait_until(be.visible)
        return _BaseTable(ss(table_css_selector).element_by(be.visible))

    @property
    def forms(self):
        return 'dmx-forms > div > div > dmx-flat-data-grid > div > dmx-ui-data-grid > div > div > table'

    @property
    def sections(self):
        return 'dmx-crf-sections > div > dmx-flat-data-grid > div > dmx-ui-data-grid > div > div > table'

    @property
    def items(self):
        return 'dmx-crf-items table'

    @property
    def visits(self):
        return 'table'

    @property
    def environments(self):
        return 'table'


class _BaseTable:

    def __init__(self, table_element):
        self._table_element = table_element
        self._rows = (_Row(tr, self._headers) for tr in self._table_element.ss('./tbody[1]/tr').filtered_by(be.visible))

    @property
    def table_element(self):
        return self._table_element

    @property
    def header_row(self):
        header_rows = self.table_element.ss('./thead').filtered_by(be.visible)
        if len(header_rows) != 1:
            raise
        return _HeaderRow(header_rows[0])

    @property
    def _headers(self):
        return [header.text for header in self.table_element.ss('./thead/tr/th/div').filtered_by(be.visible)]

    # TODO Is it useful?
    def row_by_order(self, index):
        return _Row(self._table_element.ss('./tbody[1]/tr').filtered_by(be.visible).element(index), self._headers)

    def row_by_params(self, **params):
        for row in self._rows:
            is_matching = True
            for column_header, cell_value in params.items():
                if row[column_header].text != cell_value:
                    is_matching = False
                    break
            if is_matching:
                return row
        raise Exception('No row with this params!')

    def count_rows_by_params(self, **params) -> int:
        count = 0
        for row in self._rows:
            is_matching = True
            for column_header, cell_value in params.items():
                if row[column_header].text != cell_value:
                    is_matching = False
                    break
            if is_matching:
                count += 1
        return count

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self._table_element)
        return self


class _HeaderRow:

    def __init__(self, header_row_element):
        self._header_row_element = header_row_element

    @property
    def _row_with_headers(self):
        return self._header_row_element.ss('./tr')[0]

    @property
    def _headers(self):
        return self._row_with_headers.ss('./th/div').filtered_by(be.visible)

    @property
    def _row_with_filters(self):
        return self._header_row_element.ss('./tr')[1]

    def header_by_text(self, header_text):
        i = 0
        for header in self._headers:
            if header.text == header_text:
                return _Header(header, i)
            i += 1
        exception = f'No header with {header_text} text'
        raise Exception(exception)

    def filter_input_field_by_header_text(self, header_text):
        column_index = self.header_by_text(header_text).index
        return self._row_with_filters.ss('./td').filtered_by(be.visible)[column_index].\
            s('.//div/dmx-ui-input/div/input')

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self._header_row_element)
        return self


class _Header:

    def __init__(self, header_element, index):
        self._header_element = header_element
        self._index = index

    @property
    def index(self):
        return self._index

    @property
    def sort_icon(self):
        return self._header_element.s('./dmx-ui-column-sort-icon[@class="sort-icon"]')

    @property
    def filter_icon(self):
        return self._header_element.s('./span[contains(@class, "filter-icon")]')

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self._header_element)
        return self


class _Row:

    def __init__(self, row_element, headers):
        self._row_element = row_element

        self._cells = []
        for td in self._row_element.ss('td').filtered_by(be.visible):
            colspan = int(td.attribute('colspan')) if td.attribute('colspan') else 1
            for _ in range(colspan):
                self._cells.append(td)

        self._properties = {headers[i]: self._cells[i] for i in range(len(headers))}

    def __getitem__(self, value):
        return self._properties[value]

    @property
    def element(self):
        return self._row_element

    @property
    def cells(self):
        return self._cells

    @property
    def properties(self):
        return self._properties

    @property
    def text(self):
        return [cell.text for cell in self.cells]

    @property
    def is_expanded(self):
        expand_btn_classes = self.expand_btn().get(query.attribute('class'))
        if 'icon-down' in expand_btn_classes:
            return True
        elif 'icon-right' in expand_btn_classes:
            return False
        raise Exception("I shouldn't be here...")

    def take_screenshot(self, img_title):
        take_element_screenshot(img_title=img_title, element=self.element)
        return self

    def expand_btn(self) -> Element:
        return self._row_element.s('.//span[contains(@class, "expandIcon")]')

    def edit_btn(self):
        return self._row_element.s('.//dmx-ui-button[contains(@title, "dit")]')

    def delete_btn(self):
        return self._row_element.s('.//dmx-ui-button[contains(@title, "elete")]')

    def copy_btn(self):
        return self._row_element.s('.//dmx-ui-button[contains(@title, "Copy")]')

    def run_btn(self):
        return self._row_element.s('.//dmx-ui-button[@title="Run"]')

    def create_schedule_btn(self):
        return self._row_element.s('.//dmx-ui-button[contains(@title, "Create Schedule")]')

    def cell_by_index(self, index):
        return self._row_element.ss('td').filtered_by(be.visible).element(index)

    def cell_by_column_header(self, column_header):
        return self._properties[column_header]

    def cell_value_by_column_header(self, column_header):
        return self._properties[column_header].text


if __name__ == '__main__':
    from selene.api import browser
    import time
    from page_elements.matrixcloud.field import FieldByLabel
    from page_elements.matrixcloud.button import ButtonByText, ButtonByTitle
    from page_objects.leftmenu import LeftMenu
    from selenium.common.exceptions import NoSuchElementException

    browser.open('https://dmxtest.dm-matrix.com/')
    browser.driver.maximize_window()
    browser.config.hold_browser_open = True
    browser.open_url('https://dmxtest.dm-matrix.com/client/login')
    FieldByLabel('Email').field.type('crfdesigner@behave.test')
    FieldByLabel('Password').field.type('Somepwd123')
    ButtonByText('Login').click()

    try:
        s(by.xpath('//span[contains(text(), "Yes")]')).click()
    except NoSuchElementException:
        pass

    LeftMenu().toggle_button().click()
    LeftMenu().click_menu('CRF designer')
    LeftMenu().click_menu('CRF')
    ButtonByTitle('Go to visit structure').click()
    ButtonByText('CRF DESIGNING').click()
    # FormsTable().row_by_params(**{'Form Code': 'C19399'}).expand_btn().click()
    # print(FormsTable().row_by_params(**{'Form Code': 'C19399'}).text)
    # data = {'Section Code': 'ePRO', 'Section Title': 'eRPO collection dates'}
    # sections_table = SectionsTable()
    # print(sections_table.row_by_params(**data).text)
    header_row = Table()['forms'].header_row
    header_row.header_by_text('Form Code').filter_icon.click()
    # FormsTable().header_row.filter_input_field_by_header_text('Form Code').get(query.screenshot('wqdkqolghwolrhjlwjcn.png'))
    header_row.filter_input_field_by_header_text('Form Code').type('C19399')
    print(Table()['forms'].count_rows_by_params(**{'Form Code': 'C191399_1'}))
    # print(forms_table.row_by_params(**data).text)
    # forms_table.row_by_params(**data).expand()
    #
    # data2 = {'Section Code': '3'}
    # sections_table = Tables()['sections'][0]
    # sections_table.row_by_params(**data2).edit()
    # Buttons().button_by_text('Cancel').click()
    # sections_table.row_by_params(**data2).expand()
    #
    # items_table = Tables()['items'][0]
    # print(items_table.row_by_order(1).text)
    # print('\n\n\n\n\n\n', items_table.row_by_order(1).cell_by_column_header('Field Code').text)
    # print(items_table.row_by_params(**{'Order': '9'}).text)
    # items_table.row_by_params(**{'Order': '9'}).cell_by_column_header('Action').s(by.xpath('./*[contains(@title, "Edit")]')).click()
    time.sleep(50)
