Feature: Resolve doubt in help center

  Background:
    Given I navigated to 'https://www.atresplayer.com/' and I logged into my account

    @help
    Scenario:
      When I acces to edit my profile and select the option 'Centro de ayuda'
      And complete the form and click on "enviar"
      Then I should see the option 'Resolve doubt' and I click on it