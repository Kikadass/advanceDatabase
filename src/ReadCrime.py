#!/usr/bin/python

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.currentData = ""
        self.arrayOfContents = [""]*9
        self.addressOfCrimeScene = ""
        self.array = ["Crime", "Type", "Name", "Age", "Address", "Phone", "CurrentState", "Description", "EconomicValue", "Relationship"]

    def unknown(self, string):
        if not string or string == "-1" or string == "NULL":
            return "Unknown"
        else:
            return string

    def found(self, tag):
        for i in range(0, len(self.array)):
            if tag == self.array[i]:
                return True
        return False

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.currentData = tag
        if not attributes and not self.found(tag):
            print "**" + tag + "**"
        elif not self.found(tag):
            id = attributes["id"]
            print "*" + tag + " " + id + "*"

    # Call when an elements ends
    def endElement(self, tag):
        if self.currentData == "Type":
            print "*****", self.unknown(self.arrayOfContents[0]), "******"
        for i in range(0,len(self.array)):
            if self.currentData == self.array[i] and self.currentData != "Type":
                print self.array[i] + ": " + self.unknown(self.arrayOfContents[i-1])
        # elif self.currentData == "Age":
        #     print "Age:", self.unknown(self.age)
        # elif self.currentData == "Address":
        #     print "Address:", self.unknown(self.address)
        # elif self.currentData == "Phone":
        #     print "Phone:", self.unknown(self.phone)
        # elif self.currentData == "Description":
        #     print "Description:", self.unknown(self.description)
        # elif self.currentData == "CurrentState":
        #     print "Current State:", self.unknown(self.currentState)
        self.currentData = ""

    # Call when a character is read
    def characters(self, content):
        for i in range(1, len(self.array)):
            if self.currentData == self.array[i]:
                self.arrayOfContents[i-1] = content
        # elif self.currentData == "Name":
        #     self.name = content
        # elif self.currentData == "Age":
        #     self.age = content
        # elif self.currentData == "Address":
        #     self.address = content
        # elif self.currentData == "Phone":
        #     self.phone = content
        # elif self.currentData == "Description":
        #     self.description = content

if  __name__ == "__main__":
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    parser.parse("../XML/crime.xml")