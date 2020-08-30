#Feature: 1
#
#    Scenario: 1
#        Given I start the browser
#        And I logged in as crfdesigner
#        And I expand main menu
#        And I expand CRF designer menu
#        And I open CRF submenu
#        And I click on button with Go to visit structure title
#        And I create visit: type=Common, title=Demo, code=Demo using api
#        And I create form in this visit: type=ePRO, title=Questionnaire, code=Questionnaire, order=1 using api
#        And I create section in this form: title=Text Field, code=Text Field, order=2 using web
#        And I create item with params in section with Text Field code
#            | param             | value                     |
#            | Title             | 1             |
#            | Code:             | 1                    |
#            | Order             | 1                       |
#            | Data Type            | Text                       |
#            | Control Type            | Text Input                      |
#        And I create section in this form: title=Text Area, code=Text Area, order=3 using web
#        And I create item with params in section with Text Field code
#            | param             | value                     |
#            | Title             | 1             |
#            | Code:             | 1                    |
#            | Order             | 1                       |
#            | Data Type            | Text                       |
#            | Control Type            | Text Area                      |
#        And I create section in this form: title=Select, code=Select, order=4 using web
#        And I create item with params in section with Text Field code
#            | param             | value                     |
#            | Title             | 1             |
#            | Code:             | 1                    |
#            | Order             | 1                       |
#            | Data Type            | Text                       |
#            | Control Type            | Select                      |
#            | Codelist            | Race                      |