Feature: Cancel my account

  Background:
    Given I navigated to 'https://www.atresplayer.com/' and I logged into my account

  @cancel
  Scenario:
    When I access the 'My Account' section and select 'Configuration' and click 'dar de baja' I see a new page where I can click 'Eliminar cuenta'
    Then I see a confirmation message that my account has been deleted