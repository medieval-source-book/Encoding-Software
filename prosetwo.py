# Jordan Rosen-Kaplan
# Global Medieval Sourcebook, Stanford University
# 9 August 2017
#
# Prose Transcribers
# 2 file version (one for transcription, one for translation)
#
# This is built for files that transcribe and translate a document in SEPARATE FILES:
# For example:
# 
# File 1:
# Yo digo gracias todos los días
# Si no digo gracias, estoy enfermo
# 
# Esto es la empieza de un párafaro nuevo
# 
# File 2:
# I say thank you everyday
# If I don't say thank you, I am sick
#
# This is the beginning of a new paragraph
#
# HOW TO CALL ME:
# # # ---> python prosetwo.py transc.txt transl.txt output.xml
# 
# Additional Specs: (VERY IMPORTANT THAT THESE ARE FOLLOWED ... TO A "T"!)
# Use UTF-16 for conversion to .txt files
# You can drag the files into your terminal window to get their full path!
# Lines should be matching and separated by a new line
# This program will break the text into sentence pieces
# IN THE EVENT OF A PARAGRAPH CHANGE: Include a blank line in both the transcription and the translation documents!
# Make sure that there are no spaces or new lines at the end of the document (your cursor should be immediately after the last letter at furthest)

import sys

def transcribe(transcription, translation, output):
	with open(output, 'w') as out:
		header = "<?xml-stylesheet href=\"../src/vmachine.xsl\" type=\"text/xsl\" ?><?xml-model href=\"../schema/vmachine.rng\" type=\"application/xml\" schematypens=\"http://relaxng.org/ns/structure/1.0\"?><?xml-model href=\"../schema/vmachine.rng\" type=\"application/xml\" schematypens=\"http://purl.oclc.org/dsdl/schematron\"?>\n<!DOCTYPE TEI SYSTEM \"http://www.menota.org/menotaP5.dtd\"\n[\n<!ENTITY % Menota_entities SYSTEM\n'http://www.menota.org/menota-entities.txt' >\n%\Menota_entities;]\n>\n<TEI xmlns=\"http://www.tei-c.org/ns/1.0\">\n<teiHeader>\n<fileDesc>\n<titleStmt>\n<title>TITLE HERE</title>\n<author>AUTHOR</author>\n<respStmt>\n<resp>Transcription by</resp>\n<name></name>\n</respStmt>\n<respStmt>\n<resp>Translation by</resp>\n<name></name>\n</respStmt>\n<respStmt>\n<resp>Encoded in TEI P5 XML by</resp>\n<name></name>\n</respStmt>\n</titleStmt>\n<notesStmt>\n<note anchored=\"true\"></note>\n</notesStmt>\n<sourceDesc>\n<listWit>\n<witness xml:id=\"Transcription\">TITLE</witness>\n<witness xml:id=\"Translation\">TITLE Translation</witness>\n</listWit>\n</sourceDesc>\n</fileDesc>\n<encodingDesc>\n<editorialDecl>\n<p></p>\n</editorialDecl>\n<variantEncoding method=\"parallel-segmentation\" location=\"internal\"/>\n</encodingDesc>\n</teiHeader>\n<text>\n<front>\n<head>\n<title>\n<app>\n<lem wit=\"#Transcription\">TITLE</lem>\n<rdg wit=\"#Translation\">TITLE Translation</rdg>\n</app>\n</title>\n</head>\n</front>\n<body>\n<div n=\"1\">\n<p n=\"1\">"
		out.write(header)

		with open(transcription, 'r') as transc:
			with open(translation, 'r') as transl:

				paragraph = 1
				transcLines = transc.read().decode('utf-16').split("\n")
				translLines = transl.read().decode('utf-16').split("\n")

				for i in range(len(transcLines) - 1):

					if len(transcLines[i]) == 1:
						# Paragraph break
						paragraph += 1
						out.write("\n</p>\n<p n=\"%d\">" % paragraph)
					else:
						#Take off the final "\n" character
						transcLines[i] = transcLines[i][:len(transcLines[i])-1]
						translLines[i] = translLines[i][:len(translLines[i])-1]

						out.write("\n<s>\n<app>\n<lem wit=\"#Transcription\">%s</lem>\n<rdg wit=\"#Translation\">%s</rdg>\n</app>\n</s>\n" % (transcLines[i], translLines[i]))

		footer = "\n</p>\n</div>\n</body>\n</text>\n</TEI>"
		out.write(footer)

def main():
	if len(sys.argv) != 4:
		# Function called with incorrect number of parameters
		raise AssertionError("Incorrect format. Try this: \"python prosetwo.py transcription.txt translation.txt output.xml\"")
	transcribe(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
	main()