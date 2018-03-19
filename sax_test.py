#Basic exmaple of SAX Handler
import xml.sax
from xml.sax.handler import ContentHandler

class ABContentHandler(ContentHandler):
	def __init__(self):
		ContentHandler.__init__(self)


	def startElement(self,name,attrs):
		print "Start Element is " + name
		if name == "address":
			print "Attribute Type= " +attrs.getValue("type")

	def endElement(self,name):
		print "End Element is " + name

	def characters(self,content):
		print content


def main (sourceFileName):
	source=open(sourceFileName)
	xml.sax.parse(source,ABContentHandler())

if __name__ == "__main__":
	main("etc.xml")
