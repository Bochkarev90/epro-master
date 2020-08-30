Feature: Registration
    As a patient with tablet and access-code I want to be able to register in ePRO app

    Scenario: Check Registration page content
        Given I load the app
        And I am on Login page
        When I tap on Registration button
        Then I see Registration page
        And I see language choosing button
        And I see step field
        And I see that Step field has exact Step 1 from 5 text
        And I see hint field
        And I see that hint field has exact Scan the QR-code to automatically fill the main fields text
        And I see access code field
        And I see that access code field has exact Access code text
        And I see QR code button
        And I see Next button
        And I see that Next button has NEXT text

    @C16565
    Scenario: Try to register with invalid Access Code: empty
        Given I load the app
        And I am on Login page
        When I tap on Registration button
        Then I see Registration page
        When I tap on Next button
        Then I see error message with Invalid access code text
        And I tap on OK button

    @C16566
    Scenario: Try to register with invalid Access Code: only space
        Given I load the app
        And I am on Login page
        When I tap on Registration button
        Then I see Registration page
        When I put   in access code field
        And I tap on Next button
        Then I see error message with Incorrect Request text
        And I tap on OK button

    @C16567
    Scenario: Try to register with invalid Access Code: 9 random characters
        Given I load the app
        And I am on Login page
        When I tap on Registration button
        Then I see Registration page
        When I put random in access code field
        And I tap on Next button
        Then I see error message with Access code is not valid text
        And I tap on OK button

    @C16592 @android
    Scenario: Try to register with invalid Access Code: regenerated code
        Given I add new subject with access code
        And I see access code
        And I click on GENERATE button
        And I load the app
        And I am on Login page
        When I tap on Registration button
        Then I see Registration page
        When I put this access code in access code field
        And I tap on NEXT button
        Then I see error message with Access code is not valid text
        Given I load the browser

    @C16573 @android
    Scenario: Register using valid Access Code, password, secret question and answer, PIN-code
        Given I add new subject with access code
        And I see access code
        And I load the app
        And I am on Login page
        When I tap on Registration button
        Then I see Registration page
        When I put this access code in access code field
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
        Then I see My dashboard page
