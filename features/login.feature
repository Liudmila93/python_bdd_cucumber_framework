Feature: Login Functionality

  Scenario: Login with valid credentials
    Given I launch chrome browser
    When I got navigated to login page
    And I enter in Email with "ludo4ka.th@mail.ru"
    And I enter in Password with "test12345!"
    And I press "Login"
    Then I should be in loggen in url
    Then I should see logged in user icon
    And I should see "Logout" button

#  Scenario: Login with invalid credentials
#    Given I launch chrome browser
#    When I got navigated to login page
#    When I enter in "Email" with "test@test.com"
#    And I enter in "Password" with "test123pass"
#    And I press "Login"
#    Then I should see error message
    And I should see "Logout" button