# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="qwe", lastname="qwert", homephone="445544", mobilephone="0505554444",
                               workphone="0998884455", secondaryphone="555444"))


# def test_add_empty_contact(app):
#     app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
#                              photo="", home="", email=""))
