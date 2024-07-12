Feature: Activate parental control for children under 12 years of age

  Background:
    Given I navigated to 'https://www.atresplayer.com/' and I logged into my account

  @parental_control
  Scenario:
    When I acces to edit my profile y select the option to activate parental control by adding the pin
    Then I should see a message that confirms that my profile has been update