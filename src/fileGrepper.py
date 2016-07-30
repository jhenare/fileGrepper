#!/usr/bin/env python
import xml.etree.ElementTree as ET


test_log = "/home/jhenare/dev/repo/pythonTools/fileGrepper/src/testLog.log"
test_xml = "/home/jhenare/dev/repo/pythonTools/fileGrepper/src/test.xml"


test_string = '''
This is a test

Random Note
$TOKEN01
$TOKEN02

$USER{searchTerm,splitTerm}


'''

# Read line by line
# with open(test_log) as openLog:
# 	for n, line in enumerate(openLog):
# 		print n, line

print test_xml

tree = ET.parse(test_xml)
root = tree.getroot()


for tok in root:
	print tok.text


print 'yes2'