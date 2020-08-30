Feature: Access Code
    As an Investigator I want to be able to generate an access code for a new subject

    Background: Login, go to EDC -> Subject Matrix
#        Given I deploy crf to Training using api
        Given I start the browser
        And I logged in as investigator
        And I expand main menu
        And I expand EDC menu
        And I open Environment submenu

    @C16551
    Scenario: Generate access code
        When I click on ADD SUBJECT button
        And I click on ADD button
        And I click on generate access code icon for last subject
        And I click on GENERATE button
        Then I see access code
        And I take a screenshot of access code
        When I click on CANCEL button
        Then I see that Subject access code for ePRO popup disappears
        Then I see that access code icon is yellow for last subject

    @C16552
    Scenario: Export generated code to pdf
        When I click on ADD SUBJECT button
        And I click on ADD button
        When I click on generate access code icon for last subject
        And I click on GENERATE button
        Then I see access code
        When I click on EXPORT TO PDF button
