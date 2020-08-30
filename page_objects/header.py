import time

from selene.api import *

from helpers.helpers import wait_for_angular
from page_elements.matrixcloud.lists import PopoverList


class Header:

    def __init__(self):
        self._logo_matrix_css_selector = 'div.logo-matrix'
        self._project_title_css_selector = 'span.project-title'
        self._user_info_icon_css_selector = 'span.icon-face'

    @property
    def _logo_matrix(self):
        return s(self._logo_matrix_css_selector)

    @property
    def _project_title(self):
        return s(self._project_title_css_selector)

    @property
    def _user_info_icon(self):
        return s(self._user_info_icon_css_selector)

    def open_user_info(self):
        self._user_info_icon.click()
        wait_for_angular()
        time.sleep(0.5)
        return PopoverList()

    def get_project_title(self):
        return self._project_title.get(query.text)

    def go_to_dashboard(self):
        self._logo_matrix.click()
