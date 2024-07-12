Feature: Add a channel to my favorites

  Background:
    Given I navigated to 'https://www.atresplayer.com/' and I logged into my account


  @favorites
  Scenario: Add a channel to my favorites
    When I navigate to the program of the chosen channel and by clicking on 'Details' I can 'follow' the program
    Then I should see the program in my favorites list