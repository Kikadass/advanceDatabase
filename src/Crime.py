from xml.dom.minidom import *


def format(doc):
    return  parseString(doc.toprettyxml())

def tryIt():
    doc = Document()

    newElement = doc.createElement("")

    text = doc.createTextNode("Some Text")
    newElement.appendChild(text)

    environment = doc.createElement("environment")
    newElement.appendChild(environment)


    for i in doc.getElementsByTagName("fish"):
        environment = doc.createElement("environment")
        i.appendChild(environment)
        print i

    doc.appendChild(newElement)

    doc = format(doc)

    out = open("../XML/crime.xml", 'w')
    doc.writexml(out)
    out.flush()
    out.close()

def addPerson(doc, parent):

    print("What is his/her name?")

    name = doc.createElement("Name")
    parent.appendChild(name)
    text = doc.createTextNode(raw_input())
    name.appendChild(text)


    age = doc.createElement("Age")
    parent.appendChild(age)
    x = int()
    while not x:
        try:
            print("How old is he/she?")
            x = int(raw_input())
        except ValueError:
            print 'Invalid Number'

    text = doc.createTextNode(str(x))
    age.appendChild(text)


    print("What is his/her address?")
    address = doc.createElement("Address")
    parent.appendChild(address)
    text = doc.createTextNode(raw_input())
    address.appendChild(text)


    phone = doc.createElement("Phone")
    parent.appendChild(phone)
    x = int()
    while not x:
        try:
            print("What is his/her phone number?")
            x = int(raw_input())

            if (x/10000000000000 > 0 or x/100000000 == 0):
                x = 0;
                print 'Invalid Number'
        except ValueError:
            print 'Invalid Number'

    text = doc.createTextNode(str(x))
    phone.appendChild(text)

    return doc

def addVictims(doc, victims):
    victim = doc.createElement("Victim")
    victims.appendChild(victim)

    doc = addPerson(doc, victim)

    print("Are there details of a victim's related person?")
    check = raw_input();
    if (check[0] == 'y' or check[0] == 'Y'):
        relatedPerson = doc.createElement("RelatedPerson")
        victim.appendChild(relatedPerson)

        print("What is the relationship with the victim?")
        relationship = doc.createElement("Relationship")
        relatedPerson.appendChild(relationship)
        text = doc.createTextNode(raw_input())
        relationship.appendChild(text)

        doc = addPerson(doc, relatedPerson)

    print("Please enter a description of the victim")
    description = doc.createElement("Description")
    victim.appendChild(description)
    text = doc.createTextNode(raw_input())
    description.appendChild(text)

    return doc

def addWitness(doc, witness):
    witnes = doc.createElement("Witnes")
    witness.appendChild(witnes)

    doc = addPerson(doc, witnes)

    print("Please enter a description of what was witnessed")
    description = doc.createElement("Description")
    witnes.appendChild(description)
    text = doc.createTextNode(raw_input())
    description.appendChild(text)

    return doc

def addEvidence(doc, evidence):
    pieceOfevidence = doc.createElement("Evidence")
    evidence.appendChild(pieceOfevidence)

    print("Is there an owner for this piece of evidence?")
    check = raw_input();
    if (check[0] == 'y' or check[0] == 'Y'):
        owner = doc.createElement("Owner")
        pieceOfevidence.appendChild(owner)
        doc = addPerson(doc, owner)


    id = doc.createElement("ID")
    pieceOfevidence.appendChild(id)
    x = int()
    while not x:
        try:
            print("Please enter an ID for this piece of evidence")
            x = int(raw_input())
        except ValueError:
            print 'Invalid Number'

    text = doc.createTextNode(str(x))
    id.appendChild(text)

    print("Please enter a description for the piece of evidence")
    description = doc.createElement("Description")
    pieceOfevidence.appendChild(description)
    text = doc.createTextNode(raw_input())
    description.appendChild(text)

    return doc

def addItemStolen(doc, itemsStolen):
    item = doc.createElement("Item")
    itemsStolen.appendChild(item)

    print("Please enter the details of the owner")
    owner = doc.createElement("Owner")
    item.appendChild(owner)
    doc = addPerson(doc, owner)

    id = doc.createElement("ID")
    item.appendChild(id)
    x = int()
    while not x:
        try:
            print("Please enter an ID for this stolen item")
            x = int(raw_input())
        except ValueError:
            print 'Invalid Number'

    text = doc.createTextNode(str(x))
    id.appendChild(text)

    value = doc.createElement("Value")
    item.appendChild(value)
    x = int()
    while not x:
        try:
            print("Please enter an economic value for this stolen item in GBP")
            x = int(raw_input())
        except ValueError:
            print 'Invalid Number'

    text = doc.createTextNode(str(x))
    value.appendChild(text)


    print("Please enter a description for this stolen item")
    description = doc.createElement("Description")
    item.appendChild(description)
    text = doc.createTextNode(raw_input())
    description.appendChild(text)

    return doc

def store():
    doc = Document()

    crime = doc.createElement("Crime")
    doc.appendChild(crime)

    victims = doc.createElement("Victims")
    crime.appendChild(victims)

    x = int()
    while not x:
        try:
            print("How many victims are there?")
            x = int(raw_input())
            if x == 0:
                x = -1
        except ValueError:
            print 'Invalid Number'

    for i in range(0, x, 1):
        doc = addVictims(doc, victims)



    witness = doc.createElement("Witness")
    crime.appendChild(witness)

    x = int()
    while not x:
        try:
            print("How many witnesses are there?")
            x = int(raw_input())
            if x == 0:
                x = -1
        except ValueError:
            print 'Invalid Number'

    for i in range(0, x, 1):
        doc = addWitness(doc, witness)


    evidence = doc.createElement("Evidence")
    crime.appendChild(evidence)

    x = int()
    while not x:
        try:
            print("How many pieces of evidence are there?")
            x = int(raw_input())
            if x == 0:
                x = -1
        except ValueError:
            print 'Invalid Number'

    for i in range(0, x, 1):
        doc = addEvidence(doc, evidence)

    itemsStolen = doc.createElement("ItemsStolen")
    crime.appendChild(itemsStolen)
    x = int()
    while not x:
        try:
            print("How many stolen items are there?")
            x = int(raw_input())
            if x == 0:
                x = -1
        except ValueError:
            print 'Invalid Number'

    for i in range(0, x, 1):
        doc = addItemStolen(doc, itemsStolen)

    print("What is the address of the crime scene?")
    addressOfCrimeScene = doc.createElement("addressOfCrimeScene")
    crime.appendChild(addressOfCrimeScene)
    text = doc.createTextNode(raw_input())
    addressOfCrimeScene.appendChild(text)

    for i in doc.getElementsByTagName("fish"):
        environment = doc.createElement("environment")
        i.appendChild(environment)
        print i

    doc = format(doc)

    out = open("../XML/crime.xml", 'w')
    doc.writexml(out)
    out.flush()
    out.close()

store()
