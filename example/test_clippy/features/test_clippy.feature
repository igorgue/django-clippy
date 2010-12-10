Feature: Test clippy
  As an user
  I should be able to copy text via a clippy button

  Scenario: Show the clippy in action
    Given I go to "/"
    I see "git@github.com:igorgue/django-clippy.git" in the clippy code
