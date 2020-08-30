from helpers.helpers import translate
from page_elements.epro.baseelement import BaseEproElement
from selene.api import *


class Field:

    def __getitem__(self, key):
        field_searcher = getattr(self, translate(key))
        if isinstance(field_searcher, str):
            field_searcher = by.id(field_searcher)
        return _BaseField(s(field_searcher))

    # Login page
    @property
    def access_code(self):
        return 'com.dmmatrix.epro.test:id/etAccessCode'

    @property
    def password(self):
        return 'com.dmmatrix.epro.test:id/etPassword'

    @property
    def version(self):
        return 'com.dmmatrix.epro.test:id/appVersionTextView'

    # Registration pages
    @property
    def step(self):
        return 'com.dmmatrix.epro.test:id/step'

    @property
    def hint(self):
        return 'com.dmmatrix.epro.test:id/textHint'

    @property
    def repeat_password(self):
        return 'com.dmmatrix.epro.test:id/etRepeatPassword'

    @property
    def secret_answer(self):
        return 'com.dmmatrix.epro.test:id/answerEditText'

    @property
    def pin_code(self):
        return 'com.dmmatrix.epro.test:id/etPinCode'

    @property
    def repeat_pin_code(self):
        return 'com.dmmatrix.epro.test:id/etRepeatPinCode'

    @property
    def confirm_password(self):
        return by.xpath('//android.widget.EditText')


class _BaseField(BaseEproElement):

    def __init__(self, field_element):
        super().__init__(field_element)

    def send_keys(self, keys):
        self.element.type(keys)

    def type(self, keys):
        self.element.type(keys)
