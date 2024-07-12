Feature: Watch live content

  Background:
    Given I navigated to 'https://www.atresplayer.com/' and I logged into my account

  @live
  Scenario: Watch live content
    When I click on 'Directos' in the banner and click on 'Continuar Directo'
    Then I should see the live content