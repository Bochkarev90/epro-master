Feature: ePRO forms in EDC
  As an Investigator I want to be able to see forms that were sent from tablet in EDC

    @C17770 @android
    Scenario: Check if status of filled ePro form is Locked
        Given I start the browser
        And I logged in as crfdesigner
        And I go to CRF structure
        And I create visit: type=Common, title=Common visit for C17770 test, code=C17770 using web
        And I create form in this visit: type=ePRO, title=ePRO form for C17770 test, code=C17770, order=15 using web
        And I create section in this form: title=Section text, code=C17770, order=70 using web
        And I create individual schedule for this form using web
        And I create item in this section: title=Text item, code=C17770, order=70 using web
        And I logout
        And I deploy crf to Training using api
        And I add new subject with access code
        And I see access code
        And I click on CANCEL button
        And I click on issue diary icon for last subject in C17770 visit
        And I select ePRO form for C17770 test form
        And I click on ADD button
        And I click on ISSUE button
        And I load the app
        And I am on Login page
        And I tap on Registration button
        And I see Registration page
        And I put this access code in access code field
        And I tap on NEXT button
        And I put somepwd in Password field
        And I put somepwd in Repeat Password field
        And I click on NEXT button
        And I choose Your favorite musician's surname? question in questions list
        And I click on NEXT button
        And I put q in Secret Answer field
        And I click on NEXT button
        And I put 1111 pin code
        And I put 1111 repeat pin code
        And I click on FINISH button
        And I see permission alert with Allow MATRIX | ePRO to access your calendar? text
        And I click on ALLOW button
        And I see My dashboard page
        And I sleep for 30 seconds
        And I open ePRO form for C17770 test form
        And I switch to webview
        And I put test answer answer
        And I go to the next page
        And I go to the next page
        And I switch to native
        And I put somepwd password
        And I tap on OK button
        Then I am on My dashboard page
        And I see that ePRO form for C17770 test form has Sent status
        And I switch to the browser
        And I close Issue eDiary popup
        And I expand last subject
        And I see that this subject has filled C17770 form in C17770 visit
        And I click on this form
        Then I see ePRO form for C17770 test form in locked status