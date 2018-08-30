class Contact:

    def __init__(self, firstname, middlename, lastname, nickname, photo, home, email):
        """ photo - сылка на файл картинку, home - дом.телефон"""
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.home = home
        self.email = email