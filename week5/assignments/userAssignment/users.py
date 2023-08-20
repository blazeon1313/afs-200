import requests

class Users():
    def __init__(self, firstName, lastName, email, userName, password, uuid, phone, cell, pictureLarge, pictureThumbnail, nationality):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.uName = userName
        self.password = password
        self.uuid = uuid
        self.phone = phone
        self.cell = cell
        self.pictureLarge = pictureLarge
        self.pictureThumbnail = pictureThumbnail
        self.nationality = nationality

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setEmail(self, email):
        self.email = email

    def setUserName(self, userName):
        self.userName = userName

    def setPassword(self, password):
        self.password = password

    def setUuid(self, uuid):
        self.uuid = uuid

    def setPhone(self, Phone):
        self.Phone = Phone

    def setCell(self, cell):
        self.cell = cell

    def setPictureLarge(self, pictureLarge):
        self.pictureLarge = pictureLarge

    def setPictureThumbnail(self, pictureThumbnail):
        self.pictureThumbnail = pictureThumbnail

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password

    def getUuid(self):
        return self.uuid

    def getPhone(self):
        return self.Phone

    def getCell(self):
        return self.cell

    def getPictureLarge(self):
        return self.pictureLarge

    def getPictureThumbnail(self):
        return self.pictureThumbnail

    def nationality(self):
        return self.nationality

    def __str__(self):
        retStr = self.firstName
        retStr += " "
        retStr += self.lastName
        retStr += " ("
        retStr += self.email
        retStr += ")"

        return retStr

class AuthorizedUsers():
    def __init__(self):
        self.users = []

    def appendUser(self, user):
        self.users.append(user)

    def showUsers(self):
        for user in self.users:
            print(user.__str__())

def getData(userInfo):
    URL = "https://randomuser.me/api/?nat=us"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON

    except requests.exceptions.HTTPError as errc:
        print(errc)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

myAuthorizedUsers = AuthorizedUsers()

for u in range(0,10):

    jsonUserData = getData("userInfo")

    for currentUser in jsonUserData["results"]:
        firstName = currentUser["name"] ["first"]
        lastName = currentUser["name"] ["last"]
        email = currentUser["email"]
        userName = currentUser["login"] ["username"]
        password = currentUser["login"] ["password"]
        uuid = currentUser["login"] ["uuid"]
        phone = currentUser["phone"]
        cell = currentUser["cell"]
        pictureLarge = currentUser["picture"] ["large"]
        pictureThumbnail = currentUser["picture"] ["thumbnail"]
        nationality = currentUser["nat"]
        
        newUser = Users(firstName, lastName, email, userName, password, uuid, phone, cell, pictureLarge, pictureThumbnail, nationality)
        
        myAuthorizedUsers.appendUser(newUser)

myAuthorizedUsers.showUsers()