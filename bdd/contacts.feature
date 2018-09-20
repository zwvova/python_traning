Scenario Outline: Add new contact
	Given a contact list
	Given a contact with <firstname>, <lastname> and <address>
	When I add the contact to the list
	Then the new contact list is equal to the old contact list with the added contact

	Examples:
	| firstname  | lastname  | address  |
	| firstname1 | lastname1 | address1 |

Scenario: Delete a contact
	Given a non-empty contact list
	Given a random contact from the list
	When I delete the contact from the list
	Then the new contact list is equal to the old contact list without the contact

Scenario Outline: Modify a contact
    Given a contact with <firstname>, <lastname> and <address>
	Given a non-empty contact list
	Given a random contact from the list
	When I modify the contact from the list
	Then the new contact list is equal to the old contact list with the modified contact

    Examples:
	| firstname        | lastname        | address        |
    | firstname_modify | lastname_modify | address_modify |