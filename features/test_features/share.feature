Feature: Share on social networks

  Background:
    Given I navigated to 'https://www.atresplayer.com/' and I logged into my account

    @share
    Scenario: Share a channel on social networks
      When When I navigate to the program of the chosen channel and by clicking on 'Details' I can 'share' the program
      Then I can see a new window with the social networks to share the program