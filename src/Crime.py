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
    name = doc.createElement("Name")
    parent.appendChild(name)

    age = doc.createElement("Age")
    parent.appendChild(age)

    address = doc.createElement("Address")
    parent.appendChild(address)

    phone = doc.createElement("Phone")
    parent.appendChild(phone)
    return doc

def addVictims(doc, victims):
    victim = doc.createElement("Victim")
    victims.appendChild(victim)

    doc = addPerson(doc, victim)

    relatedPerson = doc.createElement("RelatedPerson")
    victim.appendChild(relatedPerson)

    description = doc.createElement("Description")
    victim.appendChild(description)

    return doc

def addWitness(doc, witness):
    witnes = doc.createElement("Witnes")
    witness.appendChild(witnes)

    doc = addPerson(doc, witnes)

    description = doc.createElement("Description")
    witnes.appendChild(description)

    return doc

def addEvidence(doc, evidence):
    pieceOfevidence = doc.createElement("Evidence")
    evidence.appendChild(pieceOfevidence)

    owner = doc.createElement("Owner")
    pieceOfevidence.appendChild(owner)

    doc = addPerson(doc, owner)

    id = doc.createElement("ID")
    pieceOfevidence.appendChild(id)

    description = doc.createElement("Description")
    pieceOfevidence.appendChild(description)

    return doc

def addItemStolen(doc, itemsStolen):
    item = doc.createElement("Item")
    itemsStolen.appendChild(item)

    owner = doc.createElement("Owner")
    item.appendChild(owner)

    doc = addPerson(doc, owner)

    id = doc.createElement("ID")
    item.appendChild(id)

    value = doc.createElement("Value")
    item.appendChild(value)

    description = doc.createElement("Description")
    item.appendChild(description)

    return doc

def store():
    doc = Document()

    crime = doc.createElement("Crime")
    doc.appendChild(crime)

    victims = doc.createElement("Victims")
    crime.appendChild(victims)

    doc = addVictims(doc, victims)

    witness = doc.createElement("Witness")
    crime.appendChild(witness)

    doc = addWitness(doc, witness)

    evidence = doc.createElement("Evidence")
    crime.appendChild(evidence)

    doc = addEvidence(doc, evidence)

    itemsStolen = doc.createElement("ItemsStolen")
    crime.appendChild(itemsStolen)

    doc = addItemStolen(doc, itemsStolen)

    addressOfCrimeScene = doc.createElement("addressOfCrimeScene")
    crime.appendChild(addressOfCrimeScene)

    text = doc.createTextNode("Some Text")
    victims.appendChild(text)

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

