from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(orm):
    return orm.get_contact_list()


@given('a contact with <firstname>, <lastname> and <address>')
def new_contact(firstname, lastname, address):
    return Contact(firstname=firstname, lastname=lastname, address=address)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old contact list with the added contact')
def verify_contact_added(orm, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = orm.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(app, orm):
    if len(orm.get_contact_list()) < 0:
        app.group.create(Contact(firstname='some firstname'))
    return orm.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.del_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old contact list without the contact')
def verify_contact_del(orm, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = orm.get_contact_list()
    old_contacts.remove(random_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@when('I modify the contact from the list')
def modify_contact(app, new_contact, random_contact):
    new_contact.id = random_contact.id
    app.contact.mod_contact_by_id(new_contact)


@then('the new contact list is equal to the old contact list with the modified contact')
def verify_contact_del(orm, non_empty_contact_list, random_contact, new_contact):
    old_contacts = non_empty_contact_list
    non_empty_contact_list.remove(random_contact)
    random_contact.firstname = new_contact.firstname
    random_contact.lastname = new_contact.lastname
    random_contact.address = new_contact.address
    old_contacts.append(new_contact)
    new_contacts = orm.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
