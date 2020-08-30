Feature: Creation
    As a CRF designer I want to be able to create a schedule for ePRO forms in CRF

    Background: Login, go to CRF Designing
        Given I start the browser
        And I logged in as crfdesigner
        And I expand main menu
        And I expand CRF designer menu
        And I open CRF submenu
        And I click on button with Go to visit structure title

    # Todo Add scenario outline with all form types
    @C17319
    Scenario: Try to create schedule for non-ePro form
        Given I create visit with params
            | param             | value                         |
            | Visit Name        | Common_C17319                 |
            | Visit Code        | C17319                        |
            | Visit Type        | Common                        |
        And I create form with params
            | param             | value                         |
            | Visit             | Common_C17319                 |
            | Form Code         | C17319                        |
            | Form Name         | Common form for C17319 test   |
            | Form Type         | Common                        |
            | Order             | 319                           |
        Then I don't see create schedule button opposite record with params in forms table
            | column header     | td value                      |
            | Form Code         | C17319                        |

#    @C19145 @smoke
#    Scenario: Create schedule with Individual schedule type
#        Given I create visit with params
#            | param             | value                         |
#            | Visit Name        | Common_C19145                 |
#            | Visit Code        | C19145                        |
#            | Visit Type        | Common                        |
#        And I create form with params
#            | param             | value                         |
#            | Visit             | Common_C19145                 |
#            | Form Code         | C19145                        |
#            | Form Name         | ePRO form for C19145 test     |
#            | Form Type         | ePRO                          |
#            | Order             | 145                           |
#        When I create schedule for record with params in forms table
#            | column header     | td value                      |
#            | Form Code         | C19145                        |
#        And I choose Individual option in Schedule Type field
#        Then CREATE button is active
#        When I click on CREATE button
#        # Todo Should be deleted
#        And I close Create Schedule popup
#        # Todo Should be uncommented
##        Then Create Schedule popup disappears
#        # Todo Should be deleted
#        And I click on SYNC button
#        Then I see that create schedule icon for this form became yellow
#
#    @C17333
#    Scenario: Check that ePro forms are copying without schedule
#        Given I create visit with params
#            | param             | value                         |
#            | Visit Name        | Common_C17333                 |
#            | Visit Code        | C17333                        |
#            | Visit Type        | Common                        |
#        And I create form with params
#            | param             | value                         |
#            | Visit             | Common_C17333                 |
#            | Form Code         | C17333                        |
#            | Form Name         | Common form for C17333 test   |
#            | Form Type         | ePRO                          |
#            | Order             | 333                           |
#        When I create schedule for record with params in forms table
#            | column header     | td value                      |
#            | Form Code         | C17333                        |
#        And I choose Individual option in Schedule Type field
#        And I click on CREATE button
#        And I close Create Schedule popup
#        And I copy record with params in forms table
#            | column header     | td value                      |
#            | Form Code         | C17333                        |
#        And I click on SAVE button
#        Then I see record in forms table with params
#            | column header     | td value                      |
#            | Form Code         | C17333_copy                   |
#        And I see that create schedule icon for this form is not yellow
#        When I create schedule for this record
#        Then Schedule Type field is enabled
#        And there is Select Value text in Schedule Type field
#
#    @C17358 # Todo What did I want to say with this test??
#    Scenario: Check that schedules are independent for copied forms
#
#    @C19267
#    Scenario: Check schedule in new CRF version
#        Given I create visit with params
#            | param             | value                         |
#            | Visit Name        | Common_C19267                 |
#            | Visit Code        | C19267                        |
#            | Visit Type        | Common                        |
#        And I create form with params
#            | param             | value                         |
#            | Visit             | Common_C19267                 |
#            | Form Code         | C19267                        |
#            | Form Name         | Common form for C19267 test   |
#            | Form Type         | ePRO                          |
#            | Order             | 267                           |
#
#    @C17474 @smoke
#    Scenario: Create pattern schedule with pattern: One or several times per day with one time definition
#        Given I create visit with params
#            | param             | value                         |
#            | Visit Name        | Common_C17474                 |
#            | Visit Code        | C17474                        |
#            | Visit Type        | Common                        |
#        And I create form with params
#            | param             | value                         |
#            | Visit             | Common_C17474                 |
#            | Form Code         | C17474                        |
#            | Form Name         | Common form for C17474 test   |
#            | Form Type         | ePRO                          |
#            | Order             | 474                           |
#        When I create schedule for record with params in forms table
#            | column header     | td value                      |
#            | Form Code         | C17474                        |
#        Then CREATE button is inactive
#        When I choose Pattern option in Schedule Type field
#        And I choose One or several times per day option in Please, define a pattern for your schedule field
#        And I click on ADD button
#        Then CREATE button is active
#        When I click on CREATE button
#        And I close Create Schedule popup
#        # Todo Should be uncommented
##        Then Create Schedule popup disappears
#        # Todo Should be deleted
#        And I click on SYNC button
#        Then I see that create schedule icon for this form became yellow
