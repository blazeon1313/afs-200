class Contact():
    def __init__(self, firstName, lastName, email, phoneNumber, digitalPhoto):
       self.firstName = firstName
       self.lastName = lastName
       self.emailAddress = email
       self.phoneNumber = phoneNumber
       self.digitalPhoto = digitalPhoto 

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmailAddress(self):
        return self.emailAddress

    def getPhoneNumber(self):
        return self.phoneNumber

    def getPhoto(self):
        return self.digitalPhoto

    def __str__(self):
        return f'{self.firstName} + {self.lastName} + {self.emailAddress}'

    def __repr__(self):
        return f'{self.firstName} + {self.lastName} + {self.emailAddress}'

class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results