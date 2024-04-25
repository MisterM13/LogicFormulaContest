#!/usr/bin/env python3

###############################  FormulaProperties.py ###############################
#                                                                                   #
#                                                                                   #
#       This App analyses the truthvalues from a logic formula and creates a        #
#       truthtable for it. From there it derives the properties of the formula.      #
#                                                                                   #
#       Made by Matthias alias MisterM (https://github.com/MisterM13),              #
#       analyzing and learning from it is allowed ;-)                               #
#       Disclaimer: variable names are not mathematically accurate                  #
#                                                                                   #
#                                                                                   #
#####################################################################################

concat = ["\\land","\\lor","\\rightarrow", "\\leftrightarrow" ]

def getAtomOp(i):
	return ["1 "+concat[i]+" 1", "1 "+concat[i]+" 0","0 "+concat[i]+" 1","0 "+concat[i]+" 0"]

def insertValues(formula,var,values):
	for i in range(0,len(var)):
		formula = formula.replace(var[i], values[i])
	formula = formula.replace("\\lnot 1", "0")
	formula = formula.replace("\\lnot 0", "1")
	return formula

# shorten the values of atomic operations with hardcoded truth values
def shortenValues(formula,op):
	AtomOp = getAtomOp(op)
	#print(AtomOp)
	formula = formula.replace("\\lnot 1", "0")
	formula = formula.replace("\\lnot 0", "1")
	formula = formula.replace("( 0 )", "0")
	formula = formula.replace("( 1 )", "1")
	
	if(op==0): # \land
		formula = formula.replace(AtomOp[0], "1")	# 1 and 1
		formula = formula.replace(AtomOp[1], "0")	# 1 and 0
		formula = formula.replace(AtomOp[2], "0")	# 0 and 1
		formula = formula.replace(AtomOp[3], "0")	# 0 and 0
	if(op==1): # \lor
		formula = formula.replace(AtomOp[0], "1")	# 1 or 1
		formula = formula.replace(AtomOp[1], "1")	# 1 or 0
		formula = formula.replace(AtomOp[2], "1")	# 0 or 1
		formula = formula.replace(AtomOp[3], "0")	# 0 or 0
	if(op==2): # \rightarrow
		formula = formula.replace(AtomOp[0], "1")	# 1 -> 1
		formula = formula.replace(AtomOp[1], "0")	# 1 -> 0
		formula = formula.replace(AtomOp[2], "1")	# 0 -> 1
		formula = formula.replace(AtomOp[3], "1")	# 0 -> 0
	if(op==3): # \leftrightarrow
		formula = formula.replace(AtomOp[0], "1")	# 1 <-> 1
		formula = formula.replace(AtomOp[1], "0")	# 1 <-> 0
		formula = formula.replace(AtomOp[2], "0")	# 0 <-> 1
		formula = formula.replace(AtomOp[3], "1")	# 0 <-> 0
	
	formula = formula.replace("\lnot 1", "0")
	formula = formula.replace("\lnot 0", "1")
	formula = formula.replace("( 0 )", "0")
	formula = formula.replace("( 1 )", "1")
#	formula = formula.replace("1 1", "1")		should not be used in correct notation
#	formula = formula.replace("0 0", "0")		as brackets are determining here
	if(len(formula) == 3):
		formula = formula.replace(" 1 ", "1")
		formula = formula.replace(" 0 ", "0")
	return formula

# shortens down the formula and prints its truth values
def truthValueFromFormula(formula,values):
	formula = insertValues(formula, var, values)	
	erc = -1000 # Error Counter to exit after 1000 loops, if formula can't be solved
	while(len(formula) > 1 and erc < len(formula)):
		erc+=1
		formula = shortenValues(formula, 0)
		formula = shortenValues(formula, 1)
		formula = shortenValues(formula, 2)
		formula = shortenValues(formula, 3)
		#print(formula,len(formula), erc)
	if(erc >= len(formula)):
		print("---------------------- Error ------------------------------")
		print(" Interrupted endless loop, the Formula couldn't get solved ")
		print("Please make shure the Formula is logically correctly formed")
		print("----------------------- !!! -------------------------------")
		print(formula,len(formula), erc)
		formula = -1
	return formula

#normalizes any formula
def cleanFormula(formula):
	# Cleaning the Formula, bringing them in right spaces:
	for i in range(2):
		formula = formula.replace("  ", " ")
		formula = formula.replace("(", " ( ")
		formula = formula.replace(")", " ) ")
		formula = formula.replace("\\", " \\")
	formula = formula.split(" ")
	c = 0
	for i in formula:
		if i == "":
			c+=1
	for j in range(c):
		formula.remove("")
	formula = " ".join(formula)
	print("cleaned formula:",formula)
	return formula

#creates the truthtable
def printTruthTable(formula):
	global chilen
	phi = [0]*chilen
	print() 
	print("--------- Truth table -------------")
	print(var, "| phi")
	print("-----------------------------------")
	values = [-1]*len(var)
	z = chilen
	c = -1
	for i in range(0,z):
		d = 2
		n = False
		for j in range(0,len(values)):
			e = (z/d)-1	# binary exponents -1 -> ... 15, 7, 3, 1
			if(n):
				values[j] = " 0 "
			elif(i>e):
				if(i%(e+1)==0):
					values[j] = " 1 "
					n = True
			else:
				values[j] = " 0 "
			d*=2
		#print(values)
		phi[i] = truthValueFromFormula(formula, values)
		if(phi[i]==-1):
			break
		print(values,"| ",phi[i])
	return phi 

#automatic recognition of variables used in the formula
def getVar(formula):
	for i in concat:
		formula = formula.replace(i,"")
	formula = formula.replace("\\lnot","")
	formula = formula.replace("(","")
	formula = formula.replace(")","")
	formula = formula.split(" ")
	var = list(set(formula))
	var.remove("")
	for v in range(len(var)):
		var[v] = " "+var[v]+" "
	return var

#returns the properties of the formula
def getProperties(phi):
	properties = "Properties: "
	phi = list(set(phi))
	if(len(phi))==1:
		if phi[0]==1:
			properties += "valid, satisfiable"
		else:
			properties += "unsatisfiable, falsifiable"
	else:
		properties += "satisfiable, falsifiable"
	print(properties)
	
formula = input("insert the formula: ")
#cleanFormula(formula)
var = getVar(formula)
print("variables:",var)
chilen = 2**len(var)
phi = printTruthTable(cleanFormula(formula))
print()
getProperties(phi)