Feature: Register account functionality

  Background:
    Given I navigated to 'https://www.atresplayer.com/'

  @register
  Scenario: Register with mandatory fields
    When I navigate to register page, I fill in the mandatory fields and click button Continuar
    Then I should see a confirmation page

  @register
  Scenario: Register with invalid email
    When I navigate to register page, I fill in the mandatory fields with an invalid email and click button Continuar
    Then I can´t click button Continuar