# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="qwe", middlename="qwert", lastname="qwerty", nickname="qaz",
                             photo="C:\\Users\\Vova\\Desktop\\qaz.png", home="123456", email="qwe@qwe.qw"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                             photo="", home="", email=""))
    app.session.logout()
