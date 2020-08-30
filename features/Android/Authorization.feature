Feature: Authorization
    As a patient with tablet and access-code I want to be able to log in

    Scenario: Check Login page content
        Given I load the app
        And I am on Login page
        Then I see Language Choosing button
        And I see Registration button
        And I see that Registration button has If you don't have an account yet, please register  Registration text
        And I see Access code field
        And I see Password field
        And I see QR_code button
        And I see Forgot you access code button
        And I see Forgot_your_password button
        And I see Login button
        And I see Version field
        And I see that Version field has exact Version 1.0.9 build 2 test text

    @C16593
    Scenario: Try to login with invalid Access Code: empty
        Given I load the app
        And I am on Login page
        When I put somepwd in password field
        And I tap on Login button
        Then I see error message with Wrong Access Code text
        And I tap on OK button

    @C16594
    Scenario: Try to login with invalid Access Code: only space
        Given I load the app
        And I am on Login page
        When I put   in access code field
        And I put somepwd in password field
        And I tap on Login button
        Then I see error message with Incorrect Request text
        And I tap on OK button

    @C16596
    Scenario: Try to login with invalid Access Code: 9 random characters
        Given I load the app
        And I am on Login page
        When I put random in access code field
        And I put somepwd in password field
        And I tap on Login button
        Then I see error message with Invalid credentials text
        And I tap on OK button

#    @C16603
#    Scenario: Login using valid login, password, PIN-code
#        Given I get access code of last subject
#        And I see access code
#        And I load the app
#        And I am on Login page
#        When I put this access code in access code field
#        And I put somepwd in password field
#        And I click on LOGIN button
#        And I sleep for 5 seconds
#        And I put 11111111 pin code
#        And I click on FINISH button
#        Then I sleep for 15 seconds

