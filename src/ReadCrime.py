#!/usr/bin/python

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
    def __init__(self):
        self.currentData = ""
        self.array = ["Crime", "Type", "Name", "Age", "Address", "Phone", "CurrentState", "Description", "EconomicValue", "Relationship", "IP", "ISP", "Storage", "OS", "TypeOfFile"]
        self.arrayOfContents1 = [""] * (len(self.array) - 1)
        self.array2 = ["addressOfCrimeScene", "Ransom", "Rule"]
        self.arrayOfContents2 = [""] * (len(self.array2))

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
            print "*****", self.unknown(self.arrayOfContents1[0]), "******"
        for i in range(0,len(self.array2)):
            if self.currentData == self.array2[i]:
                print self.unknown(self.arrayOfContents2[i])
        for i in range(0,len(self.array)):
            if self.currentData == self.array[i] and self.currentData != "Type":
                print self.array[i] + ": " + self.unknown(self.arrayOfContents1[i - 1])
        self.currentData = ""

    # Call when a character is read
    def characters(self, content):
        for i in range(0, len(self.array2)):
            if self.currentData == self.array2[i]:
                self.arrayOfContents2[i] = content
        for i in range(1, len(self.array)):
            if self.currentData == self.array[i]:
                self.arrayOfContents1[i - 1] = content


if  __name__ == "__main__":
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler( Handler )

    parser.parse("../XML/crime.xml")