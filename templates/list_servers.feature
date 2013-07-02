Feature: Multiline strings

  Scenario: Multiline strings containing code
    Given I have a password available
    When I execute the following code:
    """python
    from random import randint
    print randint(2,9)
    print "Hello, World!"
    print randint(9,18)
    print "Hello, World!"
    print randint(18,32)
    print "Hello, World!"
    """
    Then it should succeed
