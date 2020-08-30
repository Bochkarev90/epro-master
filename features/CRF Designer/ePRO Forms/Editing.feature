Feature: Editing
    As a CRF designer I want to be able to edit ePRO forms in CRF

    Background: Login, go to CRF Designing
        Given I start the browser
        And I logged in as crfdesigner
        And I expand main menu
        And I expand CRF designer menu
        And I open CRF submenu
        And I click on button with Go to visit structure title

    @C30104
    Scenario: Check that Is Repeated, Is Mandatory, Visit and Field Type fields are disabled when editing ePRO form
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C30104             |
            | Visit Code        | C30104                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C30104             |
            | Form Code         | C30104                    |
            | Form Name         | ePRO form for C30104 test |
            | Form Type         | ePRO                      |
            | Order             | 104                       |
        When I edit record with params in forms table
            | column header     | td value                  |
            | Form Code         | C30104                    |
        Then is repeated checkbox is disabled
        And is repeated checkbox is marked
        And is mandatory checkbox is disabled
        And is mandatory checkbox is unmarked
        And I see that Visit field is disabled
        And I see that Form Type field is disabled

    @C19123 @restart
    Scenario: Edit ePRO form with valid Code/Name/Order
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C19123             |
            | Visit Code        | C19123                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C19123             |
            | Form Code         | C19123                    |
            | Form Name         | ePRO form for C19123 test |
            | Form Type         | ePRO                      |
            | Order             | 123                       |
        When I edit record with params in forms table
            | column header     | td value               |
            | Form Code         | C19123                 |
        And I put C19123_new in Form Code field
        And I put changed_name in Form Name field
        And I put 321 in Order field
        And I click on SAVE button
        Then Edit Form popup disappears
        And I see record in forms table with params
            | column header     | td value               |
            | Visit Name        | Common_C19123          |
            | Form Code         | C19123_new             |
            | Form Title        | changed_name           |
            | Order             | 321                    |

    @C19399
    Scenario: Edit ePRO form with valid Code/Name/Order in new CRF version
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C19399             |
            | Visit Code        | C19399                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C19399             |
            | Form Code         | C19399                    |
            | Form Name         | ePRO form for C19399 test |
            | Form Type         | ePRO                      |
            | Order             | 399                       |
        When I click on CREATE NEW VERSION button
        And I put 0.4 in Version Name field
        And I click on SAVE button
        Then Create New CRF Version popup disappears
        When I edit record with params in forms table
            | column header     | td value               |
            | Form Code         | C19399                 |
        And I put name changed on new version in Form Name field
        And I put C19399 new crf in Form Code field
        And I put 963 in Order field
        And I click on SAVE button
        Then Edit Form popup disappears
        And I see record in forms table with params
            | column header     | td value                     |
            | Form Title        | name changed on new version  |
            | Form Code         | C19399 new crf               |
            | Order             | 963                          |

#    @C19133
#    Scenario: Try to edit ePRO section
#        Given I create visit with params
#            | param             | value                     |
#            | Visit Name        | Common_C19133             |
#            | Visit Code        | C19133                    |
#            | Visit Type        | Common                    |
#        And I create form with params
#            | param             | value                     |
#            | Visit             | Common_C19133             |
#            | Form Code         | C19133                    |
#            | Form Name         | ePRO form for C19133 test |
#            | Form Type         | ePRO                      |
#            | Order             | 133                       |
#        When I expand record with params in forms table
#            | column header     | td value                  |
#            | Form Code         | C19133                    |
#        And I click on EDIT SECTION button
#        And I put non-editable in Section Name field
#        When I click on SAVE button
#        Then I see popup with error message You can't change ePRO standard section and close it

    @C19132
    Scenario: Edit section in ePRO form
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C19132             |
            | Visit Code        | C19132                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C19132             |
            | Form Code         | C19132                    |
            | Form Name         | ePRO form for C19132 test |
            | Form Type         | ePRO                      |
            | Order             | 132                       |
        And I create section with params in form with C19132 code
            | param             | value                     |
            | Section Name      | Common_C19132             |
            | Section Code      | C19132                    |
            | Order             | 132                       |
        When I edit record with params in sections table
            | column header         | td value              |
            | Section Code          | C19132                |
        And I put C19132 edited in Section Name field
        And I put C19132 edited in Section Code field
        And I put 231 in Order field
        Then I see that SAVE button is active
        When I click on SAVE button
        Then Edit Section popup disappears
        And I see record in sections table with params
            | column header         | td value          |
            | Section Code          | C19132 edited     |
            | Section Title         | C19132 edited     |
            | Section Order         | 231               |

    @C19138
    Scenario: Edit item in ePRO form
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C19138             |
            | Visit Code        | C19138                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C19138             |
            | Form Code         | C19138                    |
            | Form Name         | ePRO form for C19138 test |
            | Form Type         | ePRO                      |
            | Order             | 138                       |
        And I create section with params in form with C19138 code
            | param             | value                     |
            | Section Name      | Common_C19138             |
            | Section Code      | C19138                    |
            | Order             | 138                       |
        And I create item with params in section with C19138 code
            | param             | value                     |
            | Title             | Common_C19138             |
            | Code:             | C19138                    |
            | Order             | 138                       |
        When I edit record with params in items table
            | column header         | td value              |
            | Field Code            | C19138                |
        And I put C19138 edited in Title field
        And I put C19138 edited in Code: field
        And I put 831 in Order field
        And I choose Date option in Data Type field
        And I choose DateTime option in Control Type field
        Then I see that UPDATE button is active
        When I click on UPDATE button
        Then Edit Form Item popup disappears
        And I see record in items table with params
            | column header         | td value                |
            | Field Code            | C19138 edited           |
            | Title                 | C19138 edited           |
            | Order                 | 831                     |
            | Data Type             | Date                    |
            | Control Type          | DateTime                |

    @C19396
    Scenario: Try to edit visit with linked ePRO form with invalid property: Is Repeated
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C19396             |
            | Visit Code        | C19396                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C19396             |
            | Form Code         | C19396                    |
            | Form Name         | ePRO form for C19396 test |
            | Form Type         | ePRO                      |
            | Order             | 396                       |
        When I click on VISIT STRUCTURE button
        And I edit record with params in visits table
            | column header     | td value               |
            | Code              | C19396                 |
        And I click on Is Repeated checkbox
        And I put 10 in Max Repeat Number field
        And I click on UPDATE button
        Then I see error message with You cannot create repeating visit with epro form text and close it