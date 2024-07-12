Feature: Play content from a channel from the featured section

  Background:
    Given I navigated to 'https://www.atresplayer.com/' and I logged into my account

  @play_content
  Scenario:
    When I access the feautured section of a channel and I click on a content
    Then I should be able to play content from a channel from the featured section