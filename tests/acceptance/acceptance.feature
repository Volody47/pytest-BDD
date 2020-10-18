Feature: Acceptance test

  Scenario: Validate each product has one sticker
    Given I open url
#    Then I'm on the home page
    When I looking for "products"
    And I count the "stickers"
    Then each product should have only one sticker

