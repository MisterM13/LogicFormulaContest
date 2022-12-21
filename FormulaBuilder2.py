#!/usr/bin/env python3

#Formulabuilder 2.0
#made by MisterM

#builds a consistent random generic formula

#this application was made for the Logic Formula Contest at the 
#lecture of Discrete Mathematics from Basel University

random = 404 #change this to generate different Formula

op = ["\\land","\\lor","\\rightarrow", "\\leftrightarrow" ]
var = ["a","b","c","d"]


formula = " X "
rules = ["( X O X )","( X O Y )","( Y O X )","( Y O Y )","\\lnot X"]


# makes the formula evolutions due to the rules
def envolve(f,r): # f formula pattern (3points wide), r random pattern
	#print(f)
	ret = ""
	if(f=="X"):
		ret = rules[r%len(rules)]
	elif(f=="Y"):
		ret = var[r%len(var)]
	elif(f=="O"):
		ret = op[r%len(op)]
	else:
		ret = f
	return ret

#tests if the formula evolution is already finished
def testFinish(formula):
	finished = True
	for i in formula:
		if i == "X" or i=="Y" or i=="O":
			finished = False
	return finished


for j in range(0,100):
	for i in range(0,len(formula)):
		f = formula[i]
		formula = formula[0:i]+envolve(f, i+j+random)+formula[i+1:len(formula)]
	if(testFinish(formula)):
		print(formula)
		break
