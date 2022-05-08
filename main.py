#################################################################
  #Description: This file is used to input fsa file into tokens
  #which then can be used to generate a GUI and a lisp program
  #that accept a theString.txt
  #Author: Tri Pham
  #Course: COP4020
  #Project number: 04
  #Date: 04/15/2022
  #File Name: main.py
  #Version 0.720
#################################################################

from fsa import FSA
import sys

#Tokens and test to input into FSA class
tokens = []
fname = ""
test = []

#Read in tokens from file
def read():
    with open(fname) as f:
        content = f.readline()
    print("THE FSA: " + content + "\n")
    global tokens
    tokens = content.split(';')

#Read in test from file
def assignTest():
    with open(fname) as f:
        content = f.readline()
    global test
    test = content
    

#input tokens into class and the many functions to generate lisp and GUI        
fname = sys.argv[1]
read()
fa = FSA(tokens)
fa.printTokens()
fa.stateCheck()
fa.createLisp()
fa.creatingFSA()

