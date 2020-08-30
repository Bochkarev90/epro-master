Feature: Smoke
  As a test engineer I want to quick check all ePRO functionality

    @android
    Scenario: Smoke
        Given Browser is started
        And I take a screenshot
        And I logged in as crfdesigner
        And I take a screenshot
        And I expand main menu
        And I expand CRF designer menu
        And I take a screenshot
        And I open CRF submenu
        And I take a screenshot
        And I click on button with Go to visit structure title
        And I take a screenshot
        When I click on ADD VISIT button
        And I take a screenshot
        And I put Smoke Visit Title in Visit Name field
        And I put Smoke Visit Code in Visit Code field
        And I choose Common option in Visit Type field
        And I put 1 in Order field
        Then I see that SAVE button is active
        And I take a screenshot of SAVE button
        And I click on SAVE button
        Then Add Visit popup disappears
        When I filter visits table by Code column with Smoke Visit Code value
        And I see record in visits table with params
            | column header     | td value               |
            | Epoch             |                        |
            | Epoch Description |                        |
            | Name              | Smoke Visit Title      |
            | Code              | Smoke Visit Code       |
            | Type              | Common                 |
            | Order             | 1                      |
            | Shift Day         |                        |
            | Start Day         |                        |
            | End Day           |                        |
            | Is Repeating      | false                  |
            | Is Mandatory      | false                  |
            | Site              |                        |
        And I take a screenshot of this row
        When I click on CRF DESIGNING button
        And I take a screenshot
        And I click on ADD FORM button
        And I take a screenshot
        And I choose Smoke Visit Title option in Visit field
        And I put Smoke Form Title in Form Name field
        And I put Smoke Form Code in Form Code field
        And I choose ePRO option in Form Type field
        And I put 1 in Order field
        Then I see that is repeated checkbox is marked
        Then I see that is repeated checkbox is disabled
        And I take a screenshot of is repeated checkbox
        Then I see that is mandatory checkbox is unmarked
        Then I see that is repeated checkbox is disabled
        And I take a screenshot of is mandatory checkbox
        Then I see that SAVE button is active
        And I take a screenshot of SAVE button
        And I click on SAVE button
        Then Add New Form popup disappears
        And I see record in forms table with params
            | column header        | td value               |
            | Visit Name           | Smoke Visit Title      |
            | Visit Code           | Smoke Visit Code       |
            | Form Code            | Smoke Form Code        |
            | Form Title           | Smoke Form Title       |
            | Form Description     |                        |
            | Order                | 1                      |
            | Form Is Repeating    | true                   |
            | Form Is Mandatory    | false                  |
            | Section Code         | ePRO                   |
            | Section Title        | eRPO collection dates  |
            | Section Order        | 1                      |
            | Section Is Repeating | false                  |
            | Section Is Mandatory | false                  |
            | SDV                  |                        |
        And I take a screenshot of this row
        When I expand this record
        And I take a screenshot
        Then I see 2 records in items table with params
            | column header        | td value               |
            | Data Type            | Date                   |
            | Control Type         | DateTime               |
        And I take a screenshot of whole "items" table
        And I see record in items table with params
            | column header        | td value                   |
            | Field Code           | EPROSHCD                   |
            | Title                | Scheduled collection date  |
            | Description          | Scheduled collection date  |
            | Order                | 1                          |
            | Is Mandatory         | false                      |
            | Is Lab               | false                      |
            | Is Critical          | false                      |
            | Data Type            | Date                       |
            | Length               |                            |
            | CodeList             |                            |
            | Control Type         | DateTime                   |
            | Default              |                            |
        And I take a screenshot of this row
        And I see record in items table with params
            | column header        | td value                   |
            | Field Code           | EPROACD                    |
            | Title                | Actual collection date     |
            | Description          | Actual collection date     |
            | Order                | 2                          |
            | Is Mandatory         | true                       |
            | Is Lab               | false                      |
            | Is Critical          | false                      |
            | Data Type            | Date                       |
            | Length               |                            |
            | CodeList             |                            |
            | Control Type         | DateTime                   |
            | Default              |                            |
        And I take a screenshot of this row
        When I click on ADD SECTION button
        And I take a screenshot
        And I put Smoke Section Title in Section Name field
        And I put Smoke Section Code in Section Code field
        And I put 2 in Order field
        Then I see that SAVE button is active
        And I take a screenshot of SAVE button
        And I click on SAVE button
        Then Add New Section popup disappears
        And I see 2 records in sections table with params
            | column header        | td value               |
        And I take a screenshot of whole "sections" table
        And I see record in sections table with params
            | column header        | td value               |
            | Section Code         | Smoke Section Code     |
            | Section Title        | Smoke Section Title    |
            | Section Order        | 2                      |
            | Section Is Repeating | false                  |
            | Section Is Mandatory | false                  |
            | SDV                  |                        |
        And I take a screenshot of this row
        When I expand this record
        And I take a screenshot
        And I click on ADD NEW ITEM button
        And I take a screenshot
        And I put Smoke Item Title in Title field
        And I put Smoke Item Code in Code field
        And I put 1 in Order field
        Then I see that SAVE button is active
        And I take a screenshot of SAVE button
        And I click on SAVE button
        And Add New Item popup disappears
        And I see record in items table with params
            | column header        | td value                   |
            | Field Code           | Smoke Item Code            |
            | Title                | Smoke Item Title           |
            | Description          |                            |
            | Order                | 1                          |
            | Is Mandatory         | false                      |
            | Is Lab               | false                      |
            | Is Critical          | false                      |
            | Data Type            | Text                       |
            | Length               |                            |
            | CodeList             |                            |
            | Control Type         | TextInput                  |
            | Default              |                            |
        And I take a screenshot of this row
        When I create schedule for record with params in forms table
            | column header        | td value               |
            | Form Code            | Smoke Form Code        |
        And I take a screenshot
        And I choose Individual option in Schedule Type field
        Then I see that CREATE button is active
        And I take a screenshot of CREATE button
        And I click on CREATE button
        And I take a screenshot
        And I close Create Schedule popup
        # TODO Should be deleted
        And I click on SYNC button
        And I see that create schedule icon for form with Smoke Form Code code became yellow
        And I take a screenshot of this row
        When I click on CRF TO REVIEW button
        And I take a screenshot
        And I click on YES button
        And I take a screenshot
        And I logout
        And I take a screenshot
        And I log in as crfreviewer
        And I click on APPROVE button
        And I take a screenshot
        And I click on TEST button
        And I take a screenshot
        And I click on YES button
        And I take a screenshot
        And I click on APPROVE button
        And I take a screenshot
        And I click on DEPLOY button
        And I take a screenshot
        And I choose Training option in Please select an Environment type field
        And I put Training in Edc Name field
        And I mark Automatically update CRF for all subjects checkbox
        Then I see that CREATE button is active
        And I take a screenshot of CREATE button
        And I click on CREATE button
        And I take a screenshot
        And I click on REJECT button
        And I take a screenshot
        And I logout
        And I take a screenshot
        When I log in as investigator
        And I expand main menu
        And I take a screenshot
        And I expand EDC menu
        And I take a screenshot
        And I open Environment submenu
        And I take a screenshot
        When I click on ADD SUBJECT button
        And I take a screenshot
        When I click on ADD button
        And I take a screenshot
        Then I see that access code icon is grey for last subject
        # TODO last subject is not visible:(
#        And I take a screenshot of last subject
        When I click on generate access code icon for last subject
        And I take a screenshot
        And I click on GENERATE button
        Then I see access code
        And I take a screenshot of access code
        When I click on CANCEL button
        # TODO Doesn't work
#        Then I see that access code icon is yellow for last subject
#        And I take a screenshot of last subject
        When I click on issue diary icon for last subject in Smoke Visit Code visit
        And I take a screenshot
        And I select Smoke Form Title form
        And I take a screenshot
        And I click on ADD button
        Then I see that ISSUE button is active
        And I take a screenshot of ISSUE button
        And I click on ISSUE button
        Then I see that CHANGE button is active
        And I take a screenshot of CHANGE button
        Then I see that WITH DRAW button is active
        And I take a screenshot of WITH DRAW button
        And I close Issue eDiary popup
        When I switch to the app
        And I take a screenshot
        And I tap on Registration button
        Then I see Registration page
        And I take a screenshot
        And I put this access code in access code field
        Then I see that NEXT button is active
        And I take a screenshot of NEXT button
        When I tap on NEXT button
        And I take a screenshot
        And I put somepwd in Password field
        And I put somepwd in Repeat Password field
        Then I see that NEXT button is active
        And I take a screenshot of NEXT button
        When I tap on NEXT button
        And I take a screenshot
        And I choose Your favorite musician's surname? question in questions list
        Then I see that NEXT button is active
        And I take a screenshot of NEXT button
        When I tap on NEXT button
        And I take a screenshot
        And I put q in Secret Answer field
        Then I see that NEXT button is active
        And I take a screenshot of NEXT button
        When I tap on NEXT button
        And I take a screenshot
        And I put 1111 pin code
        And I put 1111 repeat pin code
        Then I see that FINISH button is active
        And I take a screenshot of FINISH button
        When I tap on FINISH button
        Then I see permission alert with Allow MATRIX | ePRO to access your calendar? text
        And I take a screenshot
        When I click on ALLOW button
        Then I see My dashboard page
        And I sleep for 60 seconds
        And I take a screenshot
        And I see Smoke Form Title form
        And I take a screenshot of this form
        When I open this form
        And I switch to webview
        And I take a screenshot
        And I put test answer answer
        And I take a screenshot
        And I go to the next page
        And I take a screenshot
        And I go to the next page
        And I go to the next page
        And I switch to native
        And I take a screenshot
        And I put somepwd password
        And I take a screenshot
        And I tap on OK button
        And I take a screenshot
        Then I am on My dashboard page
        And I take a screenshot
        And I sleep for 5 seconds
        And I see that Smoke Form Title form has Sent status
        And I take a screenshot of this form
        And I switch to the browser
        When I expand last subject
        Then I see that this subject has filled Smoke Form Code form in Smoke Visit Code visit
        And I take a screenshot of this subject
        When I click on this form
        Then I see Smoke Form Title form in locked status
        And I take a screenshot