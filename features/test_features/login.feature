Feature: Login account functionality

  Background:
    Given I navigated to 'https://www.atresplayer.com/'

  @login
  Scenario: Login with valid credentials
    When I navigated to login section and I enter valid email address, and valid password into the fields and click on Login Button
    Then I should get logged in and redirected to the home page or subscription page

    @login
  Scenario: Login with invalid credentials
    When I navigated to login section and I enter invalid email address, and invalid password into the fields and click on Login Button
    Then I should get an error message and stay on the login page