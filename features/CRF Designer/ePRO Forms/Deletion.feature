Feature: Deletion
    As a CRF designer I want to be able to delete ePRO forms in CRF

    Background: Login, go to CRF Designing
        Given I start the browser
        And I logged in as crfdesigner
        And I expand main menu
        And I expand CRF designer menu
        And I open CRF submenu
        And I click on button with Go to visit structure title

    @C19120
    Scenario: Try to delete standard ePRO section by untying it from form
        Given I create visit: type=Common, title=Common_C19120, code=C19120 using api
        And I create form in this visit: type=ePRO, title=ePRO form for C19120 test, code=C19120, order=120 using api
        When I click on CRF DESIGNING button
        And I edit record with params in forms table
            | column header     | td value               |
            | Form Code         | C19120                 |
        And I delete eRPO collection dates option from Selected Sections field
        And I click on SAVE button
        Then I see error message with You can't delete ePRO section text and close it

    @C19121 @restart
    Scenario: Delete ePRO form
        Given I create visit: type=Common, title=Common_C19121, code=C19121 using api
        And I create form in this visit: type=ePRO, title=ePRO form for C19121 test, code=C19121, order=121 using api
        When I click on CRF DESIGNING button
        And I delete record with params in forms table
            | column header     | td value                  |
            | Form Code         | C19121                    |
        Then I see 0 records in forms table with params
            | column header     | td value                  |
            | Form Code         | C19122                    |
        When I click on VISIT STRUCTURE button
        And I edit record with params in visits table
            | column header     | td value                  |
            | Code              | C19121                    |
        Then I don't see ePRO form for C19121 test option in Forms field

    @C19128
    Scenario: Try to untie ePRO form from last visit
        Given I create visit: type=Common, title=Common_C19128, code=C19128 using api
        And I create form in this visit: type=ePRO, title=ePRO form for C19128 test, code=C19128, order=128 using web
        When I click on VISIT STRUCTURE button
        And I edit record with params in visits table
            | column header     | td value               |
            | Code              | C19128                 |
        And I delete ePRO form for C19128 test option from Forms field
        Then I see that UPDATE button is active
        When I click on UPDATE button
        Then I see error message with You can't delete link to this form type text and close it

    @C19129
    Scenario: Delete record about ePRO form by untying it from visit
        Given I create visit: type=Common, title=first visit for C19129 test, code=C19129_1 using api
        And I create form in this visit: type=ePRO, title=ePRO form for C19129 test, code=C19129, order=129 using web
        And I create visit with params
            | param             | value                             |
            | Visit Name        | second visit for C19129 test      |
            | Visit Code        | C19129_2                          |
            | Visit Type        | Common                            |
            | Forms             | ePRO form for C19129 test         |
        When I click on CRF DESIGNING button
        Then I see 2 records in forms table with params
            | column header     | td value                          |
            | Form Title        | ePRO form for C19129 test         |
            | Form Code         | C19129                            |
        When I click on VISIT STRUCTURE button
        And I edit record with params in visits table
            | column header     | td value                          |
            | Code              | C19129_2                          |
        And I delete ePRO form for C19129 test option from Forms field
        And I click on UPDATE button
        Then Edit Visit popup disappears
        When I click on CRF DESIGNING button
        Then I see 1 records in forms table with params
            | column header     | td value                          |
            | Form Title        | ePRO form for C19129 test         |
            | Form Code         | C19129                            |

#    @C19135
#    Scenario: Try to delete ePRO section by delete button
#        Given I create visit: type=Common, title=Common_C19135, code=C19135 using api
#        And I create form in this visit: type=ePRO, title=ePRO form for C19135 test, code=C19135, order=135 using api
#        And I create section in this form: title=Common_C19135, code=C19135, order=135 using web
#        When I delete record with params in sections table
#            | column header     | td value                  |
#            | Section Title     | eRPO collection dates     |
#        Then I see popup with error message You can't delete ePro section and close it

    @C19134 @restart
    Scenario: Delete section in ePRO form
        Given I create visit: type=Common, title=Common_C19134, code=C19134 using api
        And I create form in this visit: type=ePRO, title=ePRO form for C19134 test, code=C19134, order=134 using api
        And I create section in this form: title=Common_C19134, code=C19134, order=134 using web
        When I delete record with params in sections table
            | column header     | td value                  |
            | Section Code      | C19134                    |
        Then I see 2 records in items table with params
            | column header     | td value                  |
            | Data Type         | Date                      |
            | Control Type      | DateTime                  |

    @C30106
    Scenario: Try to delete ePRO item
        Given I create visit: type=Common, title=Common_C30106, code=C30106 using api
        And I create form in this visit: type=ePRO, title=ePRO form for C30106 test, code=C30106, order=106 using api
        When I click on CRF DESIGNING button
        When I expand record with params in forms table
            | column header     | td value                  |
            | Form Code         | C30106                    |
        Then I don't see delete button opposite record with params in items table
            | column header     | td value                  |
            | Title             | Scheduled collection date |
        And I don't see delete button opposite record with params in items table
            | column header     | td value                  |
            | Title             | Actual collection date    |

    @C19141
    Scenario: Delete item in ePRO form
        Given I create visit: type=Common, title=Common_C19141, code=C19141 using api
        And I create form in this visit: type=ePRO, title=ePRO form C19141 test, code=C19141, order=141 using api
        And I create section: title=Common_C19141, code=C19141, order=141, form code=C19141 using web
        And I create item in this section: title=first item for C19141 test, code=C19141_1, order=1411 using api
        And I create item in this section: title=second item for C19141 test, code=C19141_2, order=1412 using web
        When I delete record with params in items table
            | column header     | td value                  |
            | Field Code        | C19141_1                  |
        Then I see 0 records in items table with params
            | column header     | td value                  |
            | Field Code        | C19141_1                  |