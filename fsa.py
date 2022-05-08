#################################################################
  #Description: This class is used to build out the accepting
  #stage of the legal and illegal input , create to build
  #a DFA GUI, and include many string to generate  a lisp program
  #Author: Tri Pham
  #Course: COP4020
  #Project number: 04
  #Date: 04/15/2022
  #File Name: fsa.py
  #Version 0.720
#################################################################

from pickle import FALSE, TRUE
import tkinter as tk
import sys
import re

class FSA:
    #constructor error if characters are missing in fsa.txt
    def __init__(self, tokens):
        print("Reading FSA\n")
        self.tokens = tokens
        if(len(tokens) == 6) :
            self.states = int(self.tokens[0])
            self.alphabet = self.tokens[1]
            self.transitions = self.tokens[2].split(',')
            self.start = int(self.tokens[3])
            self.accept = self.tokens[4]
        else:
            #error if something missing within FSA
            sys.exit('FSA does not exist, missing characters')

    #function to print tokens input
    def printTokens(self):
        for i in range(0, len(self.tokens)- 1):
            print("TOKEN: " + self.tokens[i])


    #function used to build the gui
    def creatingFSA(self):
        #functions that can draw cirle or line
        def drawCir(x1,y1,x2,y2):
            canvas.create_oval(x1,y1,x2,y2)
            canvas.create_oval(x1+1,y1+1,x2-1,y2-1, fill="white")
            canvas.pack()

        def line (x1, y1, x2, y2):
            canvas.create_line (x1, y1, x2, y2, arrow=tk.LAST)


        root = tk.Tk()
        canvas = tk.Canvas(root, width=500, height=700, borderwidth=0, highlightthickness=0, bg="white")
        canvas.grid()

        #coordinates used
        x1 = 250
        y1 = 50
        dia = 40
        allign = 20
        
        #drawing the circle
        for i in range(0, self.states):
            #starting state line
            if i == self.start:
                line(x1-dia,y1-dia, x1+6, y1+6)
            if str(i) in self.accept:
                drawCir(x1,y1,x1+dia,y1+dia)
                drawCir(x1+3,y1+3,x1+dia-3,y1+dia-3)
                canvas.create_text(x1+allign, y1+allign, text=i)
            else:
                drawCir(x1,y1,x1+dia,y1+dia)
                canvas.create_text(x1+allign, y1+allign, text=i)       
            y1 += 100
        
        #coordinates used
        x1 = 250
        y1 = 150
        y1t = 50
        
        #drawing arrows and arcs
        for i in range(0, len(self.transitions)):
            arcArrows = re.split('[(:)]', self.transitions[i])
            if arcArrows[1] == arcArrows[2]:
                canvas.create_arc((x1+allign*3+5),y1t+3, x1, y1t+allign*2-5, start=-90, extent=180, style = tk.ARC)
                canvas.create_text(x1+allign*3+10, y1t+allign, text=arcArrows[3])
                line((x1+allign*2), y1t+3, x1+allign+10, y1t+3)
            
            elif int(arcArrows[1]) == int(arcArrows[2])-1:
                line(x1+allign,(y1-allign*3), x1+allign, y1)
                canvas.create_text(x1+allign+5, y1-allign, text=arcArrows[3])
                y1 += 100
                y1t += 100
            
            else:
                num = 125
                n = int(arcArrows[1]) - int(arcArrows[2])
                canvas.create_line(x1-allign*2, (y1-allign*4), x1, (y1-allign*4))
                canvas.create_line(x1-allign*2, (y1-allign*4), (x1-allign*2), (y1-num*n-5))
                line(x1-allign*2, (y1-num*n-5), x1, (y1-num*n-5))
                canvas.create_text((x1-allign*2-5), (y1/2), text=arcArrows[3])
            
        
        root.wm_title("FSA GUI VERSION 0.720")
        root.mainloop()

    #error checking on the fsa
    def stateCheck(self) :
        if self.start >= self.states or self.start < 0:
            sys.exit('start state not correct')
        
        self.acceptStates = self.accept.split(',')
        for i in range(0, len(self.acceptStates)):
            if int(self.acceptStates[i]) >= self.states or int(self.acceptStates[i]) < 0:
                sys.exit('accept state not correct')
        
    
    #function to create lisp
    def createLisp(self):
        print("\nGenerating Lisp Program\n")
        #make it easier to create lisp, by initializing strings that are repeated from part1.lsp
        defun = "(defun state"
        l = "(l)\n"
        con = "\t(COND\n"
        illegal = "\t\t((null l) \"illegal\")\n"
        legal = "\t\t((null l) \"legal\")\n"
        bracket = "\")\n\t)\n)\n\n"
        equal = "\t\t((equal '"
        car = " (car l)) (state"
        cdr = " (cdr l)))\n"
        illchar = "\t\t(T \"illegal character at state "

        #Always want to write first
        f = open("part2.lsp", "w")
        begin = ["(defun demo()\n","\t(setq fp (open \"theString.txt\" :direction :input))\n",
                "\t(setq l (read fp \"done\"))\n", "\t(princ \"processing \")\n", "\t(princ l)\n",
                "\t(fsa l)\n)\n\n", "(defun fsa(l)\n"]
        f.writelines(begin) 
        f.close()

        #Append text when the writing are established
        f = open("part2.lsp", "a")
        startState = "\t(state"+str(self.start)+" l)\n)\n\n"
        f.write(startState)
        
        #loop through the states, and used the string provided to create a beautiful lisp program
        for i in range(0, self.states):
            f.write(defun)
            f.write(str(i))
            f.write(l)
            f.write(con)
            
            if(str(i) in self.accept):
                f.write(legal)
            else:
                f.write(illegal)
            
            #transitions of the states
            for u in range(0, len(self.transitions)):
                state = re.split('[(:)]', self.transitions[u])
                if(str(i) == state[1]):
                    f.write(equal)
                    f.write(state[3])
                    f.write(car)
                    f.write(state[2])
                    f.write(cdr)

            f.write(illchar)
            f.write(str(i))
            f.write(bracket)

        f.close()
                    
                    
            

            
        
                
        
        
        
        


