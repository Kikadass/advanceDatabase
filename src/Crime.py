from xml.dom.minidom import *


def format(doc):
    return  parseString(doc.toprettyxml())

def store():
    myDoc = Document()

    newElement = myDoc.createElement("squid")

    text = myDoc.createTextNode("Some Text")
    newElement.appendChild(text)

    environment = myDoc.createElement("environment")
    newElement.appendChild(environment)


    for i in myDoc.getElementsByTagName("fish"):
        environment = myDoc.createElement("environment")
        i.appendChild(environment)
        print i

    myDoc.appendChild(newElement)

    myDoc = format(myDoc)

    out = open("../XML/crime.xml", 'w')
    myDoc.writexml(out)
    out.flush()
    out.close()


store()

