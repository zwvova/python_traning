# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="qwe", middlename="qwert", lastname="qwerty", nickname="qaz",
                             photo="C:\\Users\\Vova\\Desktop\\qaz.png", home="123456", email="qwe@qwe.qw"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                             photo="", home="", email=""))
