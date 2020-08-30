from selene.api import *

from helpers.helpers import translate, S
from page_elements.epro.page import Page


class AndroidButtons:

    def __getitem__(self, key: str):
        button_locator = getattr(self, translate(key))
        button_obj = S(button_locator)
        button_obj.description = f"\nANDROID BUTTON ELEMENT FOUND BY TITLE\n" \
                                 f"Search title: {key}\n" \
                                 f"Text on the button: {button_obj.get(query.text)}\n"
        return button_obj

    # Alerts
    @property
    def ok(self):
        return s(by.id('android:id/button1'))

    # Login page
    @property
    def language_choosing(self):
        page_title = Page().page_title
        if page_title == 'Login':
            return s(by.id('com.dmmatrix.epro.test:id/fragment_login_menu_language'))
        elif page_title == 'Registration':
            return s(by.id('com.dmmatrix.epro.test:id/fragment_registration_menu_language'))

    @property
    def registration(self):
        return s(by.id('com.dmmatrix.epro.test:id/step'))

    @property
    def qr_code(self):
        return s(by.id('com.dmmatrix.epro.test:id/qrCodeImageButton'))

    @property
    def forgot_you_access_code(self):
        return s(by.id('com.dmmatrix.epro.test:id/tvForgotAccessCode'))

    @property
    def forgot_your_password(self):
        return s(by.id('com.dmmatrix.epro.test:id/tvForgotPassword'))

    @property
    def login(self):
        return s(by.id('com.dmmatrix.epro.test:id/btnLogin'))

    # Registration pages
    @property
    def back(self):
        return s(by.id('com.dmmatrix.epro.test:id/iv_left_button'))

    @property
    def next(self):
        return s(by.id('com.dmmatrix.epro.test:id/btnNext'))
    #
    # @property
    # def language_choosing_on_registration_page(self):
    #     return s(by.id('com.dmmatrix.epro.test:id/fragment_registration_menu_language'))

    @property
    def finish(self):
        return s(by.id('com.dmmatrix.epro.test:id/btnFinish'))

    # Permission alert
    @property
    def allow(self):
        return s(by.id('com.android.packageinstaller:id/permission_allow_button'))

    @property
    def deny(self):
        return s(by.id('com.android.packageinstaller:id/permission_deny_button'))

    # Main activity
    @property
    def person(self):
        return s(by.id('com.dmmatrix.epro.test:id/iv_left_button'))

    @property
    def help(self):
        return s(by.id('com.dmmatrix.epro.test:id/fragment_event_menu_question'))

    @property
    def choose_a_date(self):
        return 'com.dmmatrix.epro.test:id/btn_choose_date'

    @property
    def events(self):
        return s(by.id('com.dmmatrix.epro.test:id/action_events'))

    @property
    def ediary(self):
        return s(by.id('com.dmmatrix.epro.test:id/action_diary'))

    # Personal settings
    @property
    def logout(self):
        return s(by.id('com.dmmatrix.epro.test:id/fragment_personal_settings_logout'))

    # Password Recovery
    @property
    def recover(self):
        return s(by.id('com.dmmatrix.epro.test:id/recoverButton'))

    @property
    def create(self):
        return s(by.id('com.dmmatrix.epro.test:id/btnCreate'))
