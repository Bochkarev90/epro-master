Feature: Creation
    As a CRF designer I want to be able lo create ePRO forms in CRF

    Background: Login, go to CRF Designing
        Given I start the browser
        And I logged in as crfdesigner
        And I expand main menu
        And I expand CRF designer menu
        And I open CRF submenu
        And I click on button with Go to visit structure title

    @C30105
    Scenario: Check Is Repeated and Is Mandatory properties for ePRO form
        When I click on CRF DESIGNING button
        And I click on ADD FORM button
        Then I see that SAVE button is inactive
        Then I see that CANCEL button is active
        When I choose ePRO option in Form Type field
        Then is repeated checkbox is disabled
        And is repeated checkbox is marked
        And is mandatory checkbox is disabled
        And is mandatory checkbox is unmarked

    @C19113
    Scenario: Try to create ePRO form with invalid Visit: empty
        When I click on CRF DESIGNING button
        And I click on ADD FORM button
        Then I see Add New Form popup
        When I put C19113_name in Form Name field
        And I put C19113_code in Form Code field
        And I choose ePRO option in Form Type field
        And I put 19113 in Order field
        Then I see that Save button is inactive

    @C19237
    Scenario: Try to create ePRO form with invalid Visit: repeated
        Given I create visit with params
            | param             | value                             |
            | Visit Name        | Repeated_C19237                   |
            | Visit Code        | C19237                            |
            | Visit Type        | Common                            |
            | Is Repeated       | true                              |
            | Max Repeat Number | 237                               |
        When I click on CRF DESIGNING button
        And I click on ADD FORM button
        When I put C19237_name in Form Name field
        And I put C19237 in Form Code field
        And I choose ePRO option in Form Type field
        And I put 19237 in Order field
        And I choose Repeated_C19237 option in Visit field
        Then I see that SAVE button is active
        When I click on SAVE button
        Then I see error message with Epro form cannot relate with repeating visit text and close it

    @C19130
    Scenario: Create ePRO form
        Given I create visit with params
            | param             | value                             |
            | Visit Name        | Common_C19130                     |
            | Visit Code        | C19130                            |
            | Visit Type        | Common                            |
        When I click on CRF DESIGNING button
        And I click on ADD FORM button
        And I put form for C19130 test in Form Name field
        And I put C19130 in Form Code field
        And I choose ePRO option in Form Type field
        And I put 130 in Order field
        And I choose Common_C19130 option in Visit field
        Then I see that SAVE button is active
        When I click on SAVE button
        Then Add new form popup disappears
        And I see record in forms table with params
            | column header     | td value               |
            | Visit Name        | Common_C19130          |
            | Visit Code        | C19130                 |
            | Form Code         | C19130                 |
            | Form Title        | form for C19130 test   |
            | Order             | 130                    |
            | Form Is Repeating | true                   |
            | Form Is Mandatory | false                  |

    @C19114
    Scenario: Check if ePRO form creates with ePRO section
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C19114             |
            | Visit Code        | C19114                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C19114             |
            | Form Code         | C19114                    |
            | Form Name         | ePRO form for C19114 test |
            | Form Type         | ePRO                      |
            | Order             | 114                       |
        When I expand record with params in forms table
            | column header     | td value                  |
            | Form Code         | C19114                    |
            | Section Code      | ePRO                      |
            | Section Title     | eRPO collection dates     |
        Then I see record in items table with params
            | column header     | td value                  |
            | Field Code        | EPROSHCD                  |
            | Title             | Scheduled collection date |
            | Description       | Scheduled collection date |
            | Order             | 1                         |
            | Data Type         | Date                      |
            | Control Type      | DateTime                  |
        And I see record in items table with params
            | column header     | td value                  |
            | Field Code        | EPROACD                   |
            | Title             | Actual collection date    |
            | Description       | Actual collection date    |
            | Order             | 2                         |
            | Data Type         | Date                      |
            | Control Type      | DateTime                  |

    @C19131
    Scenario: Create section in ePRO form
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C19131             |
            | Visit Code        | C19131                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C19131             |
            | Form Code         | C19131                    |
            | Form Name         | ePRO form for C19131 test |
            | Form Type         | ePRO                      |
            | Order             | 131                       |
        When I expand record with params in forms table
            | column header     | td value                  |
            | Form Code         | C19131                    |
        And I click on ADD SECTION button
        And I put section for C19131 test in Section Name field
        And I put C19131 in Section Code field
        And I put 131 in Order field
        Then I see that SAVE button is active
        When I click on SAVE button
        Then Add new section popup disappears
        And I see record in sections table with params
            | column header     | td value                           |
            | Section Code      | C19131                             |
            | Section Title     | section for C19131 test            |
            | Section Order     | 131                                |

    @C19137
    Scenario: Create item in ePRO form
        Given I create visit with params
            | param             | value                     |
            | Visit Name        | Common_C19137             |
            | Visit Code        | C19137                    |
            | Visit Type        | Common                    |
        And I create form with params
            | param             | value                     |
            | Visit             | Common_C19137             |
            | Form Code         | C19137                    |
            | Form Name         | ePRO form for C19137 test |
            | Form Type         | ePRO                      |
            | Order             | 137                       |
        And I create section with params in form with C19137 code
            | param             | value                     |
            | Section Name      | Common_C19137             |
            | Section Code      | C19137                    |
            | Order             | 137                       |
        When I expand record with params in sections table
            | column header     | td value                  |
            | Section Code      | C19137                    |
        And I click on Add new item button
        And I put item for C19137 test in Title field
        And I put C19137 in Code: field
        And I put 137 in Order field
        Then I see that SAVE button is active
        When I click on SAVE button
        Then Add New Item popup disappears
        Then I see record in items table with params
            | column header          | td value                 |
            | Title                  | item for C19137 test     |
            | Field Code             | C19137                   |
            | Order                  | 137                      |