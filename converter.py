from yaml import load
from os.path import split

"""
Authored by: Diolor


This file compiles the README.md file based on list.yaml file.
It also adds a header and a table of contents.

"""


with open("list.yaml","r") as f:
	data = load(f.read())


header = open("header.md","r").read()
toc = ["\n####Table of Contents","The topics are in alphabetical order.\n"]
body = []



for k,v in sorted(data.items()):

	toc.append("[%s](#%s)" % (k,k.replace(" ","-").lower()) )
	body.append("\n##%s\n" % k)


	v = sorted(v, key=lambda x: split(x)[1])
	for link in v:
		path = split(link)

		body.append( "+ **[%s](%s)** by **%s**" %
			(path[1], link, split(path[0])[1] )  
		)




with open("README.md", "wb") as w:
	w.write(header)
	w.write("---")
	w.write("  \n".join(toc))
	w.write("\n\n---")
	w.write("\n".join(body))

	