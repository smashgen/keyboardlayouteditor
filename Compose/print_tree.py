#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Version 0.7

import sys
import pdb
import antlr3
from ComposeLexer import ComposeLexer
from ComposeParser import ComposeParser
from ComposeWalker import ComposeWalker

# Helper function to iterate through all children of a given type
def getChildrenByType(tree, type_value):
	for i in range(tree.getChildCount()):
		child = tree.getChild(i)
		if child.getType() == type_value:
			yield child

# Helper function to iterate through all children of a given type
def getChildrenListByType(tree, type_value):
	list = []
    	for i in range(tree.getChildCount()):
        	child = tree.getChild(i)
        	if child.getType() == type_value:
        		list.append(child)
	return list

xkbfilename = "/usr/share/X11/locale/en_US.UTF-8/Compose"
if len(sys.argv) > 1:
    xkbfilename = sys.argv[1]

try:    
	xkbfile = open(xkbfilename, 'r')
except OSError:
	print "Could not open file ", xkbfilename, ". Aborting..."
	sys.exit(-1)

xkbfile.close

char_stream = antlr3.ANTLRFileStream(xkbfilename, encoding='utf-8')
lexer = ComposeLexer(char_stream)
tokens = antlr3.CommonTokenStream(lexer)
parser = ComposeParser(tokens)

#pdb.set_trace()
result = parser.compose()

print "XXXXXXXXXXXXXXXXXXXXXXX", xkbfilename
print "tree =", result.tree.toStringTree()

nodes = antlr3.tree.CommonTreeNodeStream(result.tree)
nodes.setTokenStream(tokens)
walker = ComposeWalker(nodes)
walker.compose()


MAX = 10
TABS = "\t\t\t\t\t\t\t\t\t\t"

def print_tree(node, depth):
	if depth >= MAX:
		return
	for n in node.getChildren():
		print TABS[:depth], "===", n.getText(), "==="
		print_tree(n, depth + 1)
		

print result.tree.getChild(0).getText()
print
print_tree(result.tree, 0)
