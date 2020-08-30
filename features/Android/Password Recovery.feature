Feature: Password Recovery
    As a forgetful patient I want to be able to recover a password

    @android
    Scenario: Recover a password with valid Secret answer
        Given I add new subject with access code
        And I see access code
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
        And I logout
        When I put this access code in access code field
        And I tap on forgot your password button
        And I put q in secret answer field
        And I tap on Recover button
        And I put somepwd1 in Password field
        And I put somepwd1 in Repeat Password field
        And I click on CREATE button
        And I put 1111 pin code
        And I put 1111 repeat pin code
        And I click on FINISH button
        Then I see My dashboard page