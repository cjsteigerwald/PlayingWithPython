#!/usr/bin/python

# https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.dom.minidom
def main():
    # use the pars() function to load and parse an XML file
    doc = xml.dom.minidom.parse("Myxml.xml")

    print_xml(doc)
    append_xml(doc)
    print_xml(doc)

# print xml data
def print_xml(doc):
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # get a list of XML tags from the document and print each
    expertise = doc.getElementsByTagName("expertise")
    print("%d expertise: " % expertise.length)
    for skill in expertise:
        print(skill.getAttribute("name"))

# append an element to XML document
def append_xml(doc):
    new_expertise = doc.createElement("expertise")
    new_expertise.setAttribute("name", "BigData")
    doc.firstChild.appendChild(new_expertise)
    print (" ")



if __name__ == "__main__":
  main()