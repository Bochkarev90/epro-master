from selene.api import *


class Page:

    @property
    def _page_title_locator(self):
        return 'com.dmmatrix.epro.test:id/toolbar_title'

    @property
    def _page_title_element(self):
        return s(by.id(self._page_title_locator))

    @property
    def page_title(self):
        return self._page_title_element.get(query.text)

    def wait_for_page_loaded(self):
        self._page_title_element.wait_until(be.visible)

    def page_has_title(self, page_title):
        return self._page_title_element.should(have.exact_text(page_title))
