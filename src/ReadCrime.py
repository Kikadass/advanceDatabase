#!/usr/bin/python

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.currentData = ""
        self.name = ""
        self.age = ""
        self.address = ""
        self.phone = ""
        self.currentState = ""
        self.relationship = ""
        self.value = ""
        self.description = ""
        self.addressOfCrimeScene = ""


    # Call when an element starts
    def startElement(self, tag, attributes):
        self.currentData = tag
        if tag == "Theft":
            print "*****Theft*****"
        if tag == "Victims":
            print "*****Victims*****"
        if tag == "Victim":
            id = attributes["id"]
            print "*****Victim " + id + "*****"


    # Call when an elements ends
    def endElement(self, tag):
        if self.currentData == "Name":
            print "Name:", self.name
        elif self.currentData == "Age":
            print "Age:", self.age
        elif self.currentData == "Address":
            print "Address:", self.address
        elif self.currentData == "Phone":
            print "Phone:", self.phone
        elif self.currentData == "stars":
            print "Stars:", self.stars
        elif self.currentData == "Description":
            print "Description:", self.description
        elif self.currentData == "CurrentState":
            print "Current State:", self.description
        self.currentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.currentData == "Name":
            self.name = content
        elif self.currentData == "Age":
            self.age = content
        elif self.currentData == "Address":
            self.address = content
        elif self.currentData == "Phone":
            self.phone = content
        elif self.currentData == "stars":
            self.stars = content
        elif self.currentData == "Description":
            self.description = content

if ( __name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    parser.parse("../XML/crime.xml")