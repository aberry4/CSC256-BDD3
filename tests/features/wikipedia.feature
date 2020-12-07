Feature: Wake Tech Page
  As a user,
  I want to search Wikipedia for "wake tech".

Scenario: Search Wikipedia for Wake Tech
  Given the Wikipedia home page is displayed
  When the user types in 'wake tech' to the search bar
  Then the Wake Tech page is displayed
