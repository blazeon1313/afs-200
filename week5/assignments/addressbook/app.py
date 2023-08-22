from flask import Flask, request, render_template
import requests
import addressbook

app = Flask(__name__)

def userContacts():
    URL =  "https://randomuser.me/api/?nat=us&results=25"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON
    
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

newAddressBook = addressbook.AddressBook()
newContacts = userContacts()

for contacts in newContacts ['results']:
    firstName = contacts ['name'] ['first']
    lastName = contacts ['name'] ['last']
    emailAddress = contacts ['email']
    phoneNumber = contacts ['phone']
    digitalPhoto = contacts ['picture'] ['thumbnail']

    userContact = addressbook.Contact(firstName, lastName, emailAddress, phoneNumber, digitalPhoto)
    newAddressBook.addAddress(userContact)

@app.route("/", methods = ['GET'])
def home():
    return render_template('index.html', contacts = newAddressBook.getAllAddresses())

@app.route("/search", methods = ['POST'])
def search():
    searchUser = request.form.get('search')
    results = newAddressBook.findAllMatching(searchUser)
    return render_template('index.html', contacts = results)

if __name__ == "__main__":
    app.run()