from selene.api import *


class WebView:

    @property
    def question_text_fld(self):
        return s('div.question-text')

    @property
    def answer_fld(self):
        return s('div.input-container > *')

    @property
    def select_fld(self):
        return s('div.questions-radio-group')
    
    @property
    def select_answers_fields(self):
        return self.select_fld.ss('label.ctrl-container').filtered_by(be.visible)

    @property
    def previous_btn(self):
        return s('div.buttons > button[type="button"]')

    @property
    def next_btn(self):
        return s('div.buttons > button[type="submit"]')

    @property
    def progress_fld(self):
        return s('div.progress-percent')

    def get_question_text(self):
        return self.question_text_fld.get(query.text)

    def put_answer(self, answer_text):
        self.answer_fld.type(answer_text)
        return self

    def choose_answer(self, answer_text):
        self.select_answers_fields.element_by(have.exact_text(answer_text)).click()
        return self

    def go_previous(self):
        self.previous_btn.click()

    def go_next(self):
        self.next_btn.click()
