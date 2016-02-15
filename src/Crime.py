from xml.dom.minidom import *
import socket


def format(doc):
    return parseString(doc.toprettyxml())


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


def isIntNotNull(x):
    while not x:
        try:
            x = int(raw_input())
            if x == 0:
                x = -1
        except ValueError:
            print 'Invalid Number'

    return x


def isInt(x):
    while not x:
        try:
            check = raw_input()
            if check == "":
                x = -1
            else: x = int(check)
        except ValueError:
            print 'Invalid Number'

    return x


def addPerson(doc, parent):

    print("What is his/her name?")

    check = raw_input()
    if check == "":
        check = "NULL"
    name = doc.createElement("Name")
    parent.appendChild(name)
    text = doc.createTextNode(check)
    name.appendChild(text)


    age = doc.createElement("Age")
    parent.appendChild(age)
    print("How old is he/she?")
    x = int()
    x = isInt(x)

    text = doc.createTextNode(str(x))
    age.appendChild(text)


    print("What is his/her address?")
    check = raw_input()
    if check == "":
        check = "NULL"
    address = doc.createElement("Address")
    parent.appendChild(address)
    text = doc.createTextNode(check)
    address.appendChild(text)


    phone = doc.createElement("Phone")
    parent.appendChild(phone)
    x = int()
    while not x:
        try:
            print("What is his/her phone number?")
            check = raw_input()
            if check == "":
                check = "NULL"
                x = -1
            else:
                x = int(check)

            if x/10000000000000 > 0 or x/100000000 == 0:
                x = 0
                print 'Invalid Number'
        except ValueError:
            print 'Invalid Number'

    text = doc.createTextNode(str(x))
    phone.appendChild(text)


def addVictims(doc, victims):
    victim = doc.createElement("Victim")
    victims.appendChild(victim)

    addPerson(doc, victim)

    print("Current state of the victim? (eg. Dead/Injured...)")
    check = raw_input()
    if check == "":
        check = "NULL"
    state = doc.createElement("CurrentState")
    victim.appendChild(state)
    text = doc.createTextNode(check)
    state.appendChild(text)


    print("Are there details of a victim's related person?")
    check = raw_input()
    while check == "":
        print ("Invalid input")
        check = raw_input()

    if check[0] == 'y' or check[0] == 'Y':
        relatedPerson = doc.createElement("RelatedPerson")
        victim.appendChild(relatedPerson)

        print("What is the relationship with the victim?")
        check = raw_input()
        if check == "":
            check = "NULL"
        relationship = doc.createElement("Relationship")
        relatedPerson.appendChild(relationship)
        text = doc.createTextNode(check)
        relationship.appendChild(text)

        addPerson(doc, relatedPerson)

    print("Please enter a description of the victim")
    check = raw_input()
    if check == "":
        check = "NULL"
    description = doc.createElement("Description")
    victim.appendChild(description)
    text = doc.createTextNode(check)
    description.appendChild(text)


def addVictimsNode(doc, crime):
    # Victims
    victims = doc.createElement("Victims")
    crime.appendChild(victims)

    print("How many victims are there?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        print ("Please enter the details of victim number " + str(i+1))
        addVictims(doc, victims)
        doc.getElementsByTagName("Victim")[i].setAttribute("id" , str(i+1))


def addWitness(doc, witnesses):
    witness = doc.createElement("Witness")
    witnesses.appendChild(witness)

    addPerson(doc, witness)

    print("Please enter a description of what was witnessed")
    check = raw_input()
    if check == "":
        check = "NULL"
    description = doc.createElement("Description")
    witness.appendChild(description)
    text = doc.createTextNode(check)
    description.appendChild(text)


def addEvidence(doc, evidence):
    pieceOfevidence = doc.createElement("PieceOfEvidence")
    evidence.appendChild(pieceOfevidence)

    print("Is there an owner for this piece of evidence?")
    check = raw_input()
    while check == "":
        print ("Invalid input")
        check = raw_input()

    if check[0] == 'y' or check[0] == 'Y':
        owner = doc.createElement("Owner")
        pieceOfevidence.appendChild(owner)
        addPerson(doc, owner)

    print("Please enter a description for the piece of evidence")
    check = raw_input()
    if check == "":
        check = "NULL"
    description = doc.createElement("Description")
    pieceOfevidence.appendChild(description)
    text = doc.createTextNode(check)
    description.appendChild(text)


def addEvidenceNode(doc, crime):
    evidence = doc.createElement("Evidence")
    crime.appendChild(evidence)
    print("How many pieces of evidence are there?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        print ("Please enter the details of piece of evidence number " + str(i+1))
        addEvidence(doc, evidence)
        doc.getElementsByTagName("PieceOfEvidence")[i].setAttribute("id", str(i+1))


def addItemStolen(doc, itemsStolen):
    item = doc.createElement("Item")
    itemsStolen.appendChild(item)

    print("Please enter the details of the owner")
    owner = doc.createElement("Owner")
    item.appendChild(owner)
    addPerson(doc, owner)

    economicValue = doc.createElement("EconomicValue")
    item.appendChild(economicValue)
    print("Please enter an economic value for this stolen item in GBP")
    x = int()
    x = isIntNotNull(x)

    text = doc.createTextNode(str(x))
    economicValue.appendChild(text)


    print("Please enter a description for this stolen item")
    check = raw_input()
    if check == "":
        check = "NULL"
    description = doc.createElement("Description")
    item.appendChild(description)
    text = doc.createTextNode(check)
    description.appendChild(text)


def addThief(doc, thiefs):
    thief = doc.createElement("Thief")
    thiefs.appendChild(thief)

    addPerson(doc, thief)

    print("Are there details of a thief's related person?")

    check = raw_input()
    while check == "":
        print ("Invalid input")
        check = raw_input()

    if check[0] == 'y' or check[0] == 'Y':
        relatedPerson = doc.createElement("RelatedPerson")
        thief.appendChild(relatedPerson)

        print("What is the relationship with the thief?")
        check = raw_input()
        if check == "":
            check = "NULL"
        relationship = doc.createElement("Relationship")
        relatedPerson.appendChild(relationship)
        text = doc.createTextNode(check)
        relationship.appendChild(text)

        addPerson(doc, relatedPerson)


    print("Please enter a description of the thief")
    check = raw_input()
    if check == "":
        check = "NULL"
    description = doc.createElement("Description")
    thief.appendChild(description)
    text = doc.createTextNode(check)
    description.appendChild(text)


def addRule(doc, rules):
    print("Describe the rule the criminals requested?")
    check = raw_input()
    while check == "":
        print("Describe the rule the criminals requested?")
        check = raw_input()
    rule = doc.createElement("Rule")
    rules.appendChild(rule)
    text = doc.createTextNode(check)
    rule.appendChild(text)


def addHardDrive(doc, hardDrives):
    print("Is it an SSD or a HDD?")
    check = raw_input()
    while check != "SSD" and check != "HDD":
        print ("Invalid input")
        check = raw_input()

    hardDrive = doc.createElement(check)
    hardDrives.appendChild(hardDrive)





    # Owner
    print("Is there an owner for this hard drive?")
    check = raw_input()
    while check == "":
        print ("Invalid input")
        check = raw_input()

    if check[0] == 'y' or check[0] == 'Y':
        owner = doc.createElement("Owner")
        hardDrive.appendChild(owner)
        addPerson(doc, owner)


    # ID
    # id = doc.createElement("ID")
    # hardDrive.appendChild(id)
    # print("Please enter an ID for this hard drive")
    # x = int()
    # x = isIntNotNull(x)
    #
    # text = doc.createTextNode(str(x))
    # id.appendChild(text)


    # Storage
    print("Please enter the storage of this hard drivein GigaBytes. (eg. 1024 = 1TB)")
    x = int()
    x = isIntNotNull(x)
    storage = doc.createElement("Storage")
    hardDrive.appendChild(storage)
    text = doc.createTextNode(str(x))
    storage.appendChild(text)


    # OS
    print("Please enter the Operating system that the hard drive works on")
    check = raw_input()
    if (check == ""):
        check = "NULL"
    os = doc.createElement("OS")
    hardDrive.appendChild(os)
    text = doc.createTextNode(check)
    os.appendChild(text)


    # type of evidence trying to find
    print("Please enter the type of File that has to be found on this hard drive. (eg. video, text, images...)")
    check = raw_input()
    if (check == ""):
        check = "NULL"
    typeOfFile = doc.createElement("TypeOfFile")
    hardDrive.appendChild(typeOfFile)
    text = doc.createTextNode(check)
    typeOfFile.appendChild(text)


    # Description
    print("Please enter a description for the hard drive")
    check = raw_input()
    if check == "":
        check = "NULL"
    description = doc.createElement("Description")
    hardDrive.appendChild(description)
    text = doc.createTextNode(check)
    description.appendChild(text)


def theft(doc, crime):

    # crime type
    crimeType = doc.createElement("Type")
    crime.appendChild(crimeType)
    text = doc.createTextNode("Theft")
    crimeType.appendChild(text)


    # Victims
    addVictimsNode(doc, crime)


    # witnesses
    witnesses = doc.createElement("Witnesses")
    crime.appendChild(witnesses)

    print("How many witnesses are there?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        print ("Please enter the details of witness number " + str(i+1))
        addWitness(doc, witnesses)
        doc.getElementsByTagName("Witness")[i].setAttribute("id" , str(i+1))


    # Evidence
    addEvidenceNode(doc, crime)


    # Stolen Items
    itemsStolen = doc.createElement("ItemsStolen")
    crime.appendChild(itemsStolen)
    print("How many stolen items are there?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        print ("Please enter the details of item stolen number " + str(i+1))
        addItemStolen(doc, itemsStolen)
        doc.getElementsByTagName("Item")[i].setAttribute("id" , str(i+1))


    # Thiefs
    thiefs = doc.createElement("Thiefs")
    crime.appendChild(thiefs)
    print("How many thiefs are there?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        print ("Please enter the details of thief number " + str(i+1))
        addThief(doc, thiefs)
        doc.getElementsByTagName("Thief")[i].setAttribute("id", str(i+1))


def hostageTaking(doc, crime):

    # Crime type
    crimeType = doc.createElement("Type")
    crime.appendChild(crimeType)
    text = doc.createTextNode("Hostagetaking")
    crimeType.appendChild(text)

    # Hostages
    hostages = doc.createElement("Hostages")
    crime.appendChild(hostages)

    print("How many hostages are there?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        hostage = doc.createElement("Hostage")
        hostages.appendChild(hostage)
        print ("Please enter the details of hostage number " + str(i+1))
        addPerson(doc, hostage)
        doc.getElementsByTagName("Hostage")[i].setAttribute("id", str(i+1))


    # Victims
    addVictimsNode(doc, crime)


    # Evidence
    addEvidenceNode(doc, crime)


    # ransom
    print("Describe the ransom the criminals requested?")
    check = raw_input()
    if check == "":
        check = "NULL"
    ransom = doc.createElement("Ransom")
    crime.appendChild(ransom)
    text = doc.createTextNode(check)
    ransom.appendChild(text)


    # rules negotiated
    rules = doc.createElement("Rules")
    crime.appendChild(rules)
    print("How many rules did the criminals request?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        print ("Please enter the details of rule number " + str(i+1))
        addRule(doc, rules)
        doc.getElementsByTagName("Rule")[i].setAttribute("id", str(i+1))


def cyberCrime(doc, crime):
    # Crime type
    crimeType = doc.createElement("Type")
    crime.appendChild(crimeType)
    text = doc.createTextNode("Cyber crime")
    crimeType.appendChild(text)

    # citizen complaint
    citizenComplaint = doc.createElement("Complaint")
    crime.appendChild(citizenComplaint)


    print("Are there details of the citizen that made the complaint?")
    check = raw_input()
    while check == "":
        print ("Invalid input")
        check = raw_input()

    if check[0] == 'y' or check[0] == 'Y':
        citizen = doc.createElement("Citizen")
        citizenComplaint.appendChild(citizen)
        print("Please enter the details of that citizen")
        addPerson(doc, citizen)

    # description of the complaint
    print("Please enter a description of the complaint")
    check = raw_input()
    if check == "":
        check = "NULL"
    description = doc.createElement("Description")
    citizenComplaint.appendChild(description)
    text = doc.createTextNode(check)
    description.appendChild(text)


    # IP
    check = ""
    while check == "":
        print("Please enter the criminal IP")
        check = raw_input()

        try:
            socket.inet_pton(socket.AF_INET, check)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(check)
            except socket.error:
                print("Invalid input")
                check = ""
                continue
            if check.count('.') != 3:
                print("Invalid input: the IP must have 3 dots")
                check = ""
        except socket.error:  # not a valid address
            print("Invalid input")
            check = ""


    ip = doc.createElement("IP")
    crime.appendChild(ip)
    text = doc.createTextNode(check)
    ip.appendChild(text)


    # ISP
    print("What is the ISP of the criminal?")
    check = raw_input()
    if check == "":
        check = "NULL"
    isp = doc.createElement("ISP")
    crime.appendChild(isp)
    text = doc.createTextNode(check)
    isp.appendChild(text)

    # HardDrives
    hardDrives = doc.createElement("HardDrives")
    crime.appendChild(hardDrives)

    print("How many confiscated hardDrives are there?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        print ("Please enter the details of hard drive number " + str(i+1))
        addHardDrive(doc, hardDrives)
        hardDrives.childNodes[i].setAttribute("id", str(i+1))



def store():
    doc = Document()

    crime = doc.createElement("Crime")
    doc.appendChild(crime)

    print("Is it an theft, a cybercrime or a hostagetaking? (Please write it in lower case)")
    check = raw_input()
    while check != "theft" and check != "cybercrime" and check != "hostagetaking":
        print ("Invalid input")
        check = raw_input()



    # Theft
    if check == "theft":
        theft(doc, crime)

    # Hostage taking
    elif check == "hostagetaking":
        hostageTaking(doc, crime)

    # Cybercrime
    elif check == "cybercrime":
        cyberCrime(doc, crime)

    # Suspects
    suspects = doc.createElement("Suspects")
    crime.appendChild(suspects)

    print("How many suspects are there?")
    x = int()
    x = isIntNotNull(x)

    for i in range(0, x, 1):
        print("Please enter the details of the suspect number " + str(x))
        suspect = doc.createElement("Suspect")
        suspects.appendChild(suspect)
        addPerson(doc, suspect)
        doc.getElementsByTagName("Suspect")[i].setAttribute("id", str(i+1))

    # Crime Scene address
    print("What is the address of the crime scene?")
    check = raw_input()
    if check == "":
        check = "NULL"
    addressOfCrimeScene = doc.createElement("addressOfCrimeScene")
    crime.appendChild(addressOfCrimeScene)
    text = doc.createTextNode(check)
    addressOfCrimeScene.appendChild(text)

    # Format doc
    doc = format(doc)

    # write xml file
    out = open("../XML/crime.xml", 'w')
    doc.writexml(out)
    out.flush()
    out.close()

store()
