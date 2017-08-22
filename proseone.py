# Jordan Rosen-Kaplan
# Global Medieval Sourcebook, Stanford University
# 10 August 2017
#
# Prose Transcribers
# 1 file version (one for both transcription and translation)
#
# HOW TO CALL ME:
# # # ---> python proseone.py text.txt output.xml
#
# This is built for files that transcribe and translate a document in ALTERNATING LINES:
# For example:
#
# Yo digo gracias todos los días
# I say thank you everyday
# Si no digo gracias, estoy enfermo
# If I don't say thank you, I am sick
#
# Esto es la empieza de un párafaro nuevo
# This is the beginning of a new paragraph
#
# Additional Specs: (VERY IMPORTANT THAT THESE ARE FOLLOWED ... TO A "T"!)
# Use UTF-8 for conversion to .txt files
# The should also be saved with the option "LF only" for new lines
# You can drag the files into your terminal window to get their full path!
# IN THE EVENT OF A PARAGRAPH CHANGE: Include a blank line!
# Make sure that there are no spaces or new lines at the end of the document (your cursor should be immediately after the last letter at furthest)

import sys

def transcribe(text, output):
	with open(output, 'w') as out:
		header = "<?xml-stylesheet href=\"../src/vmachine.xsl\" type=\"text/xsl\" ?><?xml-model href=\"../schema/vmachine.rng\" type=\"application/xml\" schematypens=\"http://relaxng.org/ns/structure/1.0\"?><?xml-model href=\"../schema/vmachine.rng\" type=\"application/xml\" schematypens=\"http://purl.oclc.org/dsdl/schematron\"?>\n<!DOCTYPE TEI SYSTEM \"http://www.menota.org/menotaP5.dtd\"\n[\n<!ENTITY %Menota_entities SYSTEM\n'http://www.menota.org/menota-entities.txt' >\n%\Menota_entities;]\n>\n<TEI xmlns=\"http://www.tei-c.org/ns/1.0\">\n<teiHeader>\n<fileDesc>\n<titleStmt>\n<title>TITLE HERE</title>\n<author>AUTHOR</author>\n<respStmt>\n<resp>Transcription by</resp>\n<name></name>\n</respStmt>\n<respStmt>\n<resp>Translation by</resp>\n<name></name>\n</respStmt>\n<respStmt>\n<resp>Encoded in TEI P5 XML by</resp>\n<name></name>\n</respStmt>\n</titleStmt>\n<notesStmt>\n<note anchored=\"true\"></note>\n</notesStmt>\n<sourceDesc>\n<listWit>\n<witness xml:id=\"Transcription\">TITLE</witness>\n<witness xml:id=\"Translation\">TITLE Translation</witness>\n</listWit>\n</sourceDesc>\n</fileDesc>\n<encodingDesc>\n<editorialDecl>\n<p></p>\n</editorialDecl>\n<variantEncoding method=\"parallel-segmentation\" location=\"internal\"/>\n</encodingDesc>\n</teiHeader>\n<text>\n<front>\n<head>\n<title>\n<app>\n<lem wit=\"#Transcription\">TITLE</lem>\n<rdg wit=\"#Translation\">TITLE Translation</rdg>\n</app>\n</title>\n</head>\n</front>\n<body>\n<div n=\"1\">\n<p n=\"1\">"
		out.write(header)

		with open(text, 'r') as textFile:

			even = True
			paragraph = 1
			textLines = textFile.read().decode('utf-8').split("\n")

			for i in range(len(textLines) - 1):
				if even and i % 2 != 0:
					continue
				if not even and i % 2 == 0:
					continue

				if len(textLines[i]) == 1:
					# Paragraph break
					paragraph += 1
					out.write("\n</p>\n<p n=\"%d\">" % paragraph)
					even = not even
				else:
					#Take off the final "\n" character and any additional whitespace
					textLines[i] = textLines[i].strip()
					textLines[i+1] = textLines[i+1].strip()
					out.write("\n<s>\n<app>\n<lem wit=\"#Transcription\">%s</lem>\n<rdg wit=\"#Translation\">%s</rdg>\n</app>\n</s>" % (textLines[i].encode('utf-8'), textLines[i+1].encode('utf-8')))

		footer = "\n</p>\n</div>\n</body>\n</text>\n</TEI>"
		out.write(footer)

def main():
	if len(sys.argv) != 3:
		# Function called with incorrect number of parameters
		raise AssertionError("Incorrect format. Try this: \"python proseone.py text.txt output.xml\"")
	transcribe(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
	main()