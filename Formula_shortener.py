#!/usr/bin/env python3

###############################  Formula_shortener.py ###############################
#                                                                                   #
#       This Program was made to win the Discrete Mathematics                       #
#       logic contest at Unibas or at least to give a little bit Challenge          #
#       to other students which also created Scripts for it.                        #
#                                                                                   #
#       It analyses the truthvalues from a logic formula and creates an             #
#       accurate and hopefully shorter formula from it.                             #
#                                                                                   #
#       Made by Matthias alias MisterM (https://github.com/MisterM13),              #
#       this Program may not be used by other students to win the contest,          #
#       because everyone learns by making his own program.                          #
#       analyzing and learning from it is allowed ;-)                               #
#       Disclaimer: variable names are not mathematically accurate                  #
#                                                                                   #
#####################################################################################

import sys

var = [" a "," b "," c "," d "]
concat = ["\\land","\\lor","\\rightarrow", "\\leftrightarrow" ]
neg = "\\lnot"
try:
	formula  = sys.argv[1]
except:
	formula = input("insert the formula:")

for i in range(2):
	formula = formula.replace("  ", " ")
	formula = formula.replace("((", "( (")
	formula = formula.replace("))", ") )")
vard = ["a","b","c","d"]
for j in vard:
	formula = formula.replace("(\\lnot","( \\lnot")
	formula = formula.replace("\\lnot(","\\lnot (")
	formula = formula.replace("("+j,"( "+j)
	formula = formula.replace(j+")",j+" )")
	
for i in concat:
	formula = formula.replace("("+i, "( "+i)
	formula = formula.replace(i+")", i+" )")
	formula = formula.replace(")"+i, ") "+i)
	formula = formula.replace(i+"(", i+" (")
	
print(formula)


######################### Formulas ###################################
#Ground formulas database
chiForm = [""]*118 # short formulas

#and
chiForm[0] = "( ( ( a \\land b ) \\land c ) \\land d )"
chiForm[1] = "( ( ( a \\land b ) \\land c ) \\land \\lnot d )"
chiForm[2] = "( ( ( a \\land b ) \\land \\lnot c ) \\land d )"
chiForm[3] = "( ( ( a \\land b ) \\land \\lnot c ) \\land \\lnot d )"
chiForm[4] = "( ( ( a \\land \\lnot b ) \\land c ) \\land d )"
chiForm[5] = "( ( ( a \\land \\lnot b ) \\land c ) \\land \\lnot d )"
chiForm[6] = "( ( ( a \\land \\lnot b ) \\land \\lnot c ) \\land d )"
chiForm[7] = "( ( ( a \\land \\lnot b ) \\land \\lnot c ) \\land \\lnot d )"
chiForm[8] = "( ( ( \\lnot a \\land b ) \\land c ) \\land d )"
chiForm[9] = "( ( ( \\lnot a \\land b ) \\land c ) \\land \\lnot d )"
chiForm[10] = "( ( ( \\lnot a \\land b ) \\land \\lnot c ) \\land d )"
chiForm[11] = "( ( ( \\lnot a \\land b ) \\land \\lnot c ) \\land \\lnot d )"
chiForm[12] = "( ( ( \\lnot a \\land \\lnot b ) \\land c ) \\land d )"
chiForm[13] = "( ( ( \\lnot a \\land \\lnot b ) \\land c ) \\land \\lnot d )"
chiForm[14] = "( ( ( \\lnot a \\land \\lnot b ) \\land \\lnot c ) \\land d )"
chiForm[15] = "( ( ( \\lnot a \\land \\lnot b ) \\land \\lnot c ) \\land \\lnot d )"

#or
chiForm[16] = "( ( ( a \\lor b ) \\lor c ) \\lor d )"
chiForm[17] = "( ( ( a \\lor b ) \\lor c ) \\lor \\lnot d )"
chiForm[18] = "( ( ( a \\lor b ) \\lor \\lnot c ) \\lor d )"
chiForm[19] = "( ( ( a \\lor b ) \\lor \\lnot c ) \\lor \\lnot d )"
chiForm[20] = "( ( ( a \\lor \\lnot b ) \\lor c ) \\lor d )"
chiForm[21] = "( ( ( a \\lor \\lnot b ) \\lor c ) \\lor \\lnot d )"
chiForm[22] = "( ( ( a \\lor \\lnot b ) \\lor \\lnot c ) \\lor d )"
chiForm[23] = "( ( ( a \\lor \\lnot b ) \\lor \\lnot c ) \\lor \\lnot d )"
chiForm[24] = "( ( ( \\lnot a \\lor b ) \\lor c ) \\lor d )"
chiForm[25] = "( ( ( \\lnot a \\lor b ) \\lor c ) \\lor \\lnot d )"
chiForm[26] = "( ( ( \\lnot a \\lor b ) \\lor \\lnot c ) \\lor d )"
chiForm[27] = "( ( ( \\lnot a \\lor b ) \\lor \\lnot c ) \\lor \\lnot d )"
chiForm[28] = "( ( ( \\lnot a \\lor \\lnot b ) \\lor c ) \\lor d )"
chiForm[29] = "( ( ( \\lnot a \\lor \\lnot b ) \\lor c ) \\lor \\lnot d )"
chiForm[30] = "( ( ( \\lnot a \\lor \\lnot b ) \\lor \\lnot c ) \\lor d )"
chiForm[31] = "( ( ( \\lnot a \\lor \\lnot b ) \\lor \\lnot c ) \\lor \\lnot d )"

chiForm[32] = " a "
chiForm[33] = " b "
chiForm[34] = " c "
chiForm[35] = " d "

chiForm[36] = "( a \\land b )"
chiForm[37] = "( a \\land c )"
chiForm[38] = "( a \\land d )"
chiForm[39] = "( b \\land c )"
chiForm[40] = "( b \\land d )"
chiForm[41] = "( c \\land d )"
chiForm[42] = "( a \\lor b )"
chiForm[43] = "( a \\lor c )"
chiForm[44] = "( a \\lor d )"
chiForm[45] = "( b \\lor c )"
chiForm[46] = "( b \\lor d )"
chiForm[47] = "( c \\lor d )"

chiForm[48] = "( \\lnot a \\land b )"
chiForm[49] = "( \\lnot a \\land c )"
chiForm[50] = "( \\lnot a \\land d )"
chiForm[51] = "( \\lnot b \\land c )"
chiForm[52] = "( \\lnot b \\land d )"
chiForm[53] = "( \\lnot b \\land a )"
chiForm[54] = "( \\lnot c \\land a )"
chiForm[55] = "( \\lnot c \\land b )"
chiForm[56] = "( \\lnot c \\land d )"
chiForm[57] = "( \\lnot d \\land a )"
chiForm[58] = "( \\lnot d \\land b )"
chiForm[59] = "( \\lnot d \\land c )"

chiForm[60] = "( \\lnot a \\lor b )"
chiForm[61] = "( \\lnot a \\lor c )"
chiForm[62] = "( \\lnot a \\lor d )"
chiForm[63] = "( \\lnot b \\lor c )"
chiForm[64] = "( \\lnot b \\lor d )"
chiForm[65] = "( \\lnot b \\lor a )"
chiForm[66] = "( \\lnot c \\lor a )"
chiForm[67] = "( \\lnot c \\lor b )"
chiForm[68] = "( \\lnot c \\lor d )"
chiForm[69] = "( \\lnot d \\lor a )"
chiForm[70] = "( \\lnot d \\lor b )"
chiForm[71] = "( \\lnot d \\lor c )"

chiForm[72] = "( a \\lor \\lnot a )"

chiForm[73] = "( \\lnot b \\rightarrow c )"
chiForm[74] = "( \\lnot b \\rightarrow d )"
chiForm[75] = "( \\lnot b \\rightarrow a )"
chiForm[76] = "( \\lnot c \\rightarrow a )"
chiForm[77] = "( \\lnot c \\rightarrow b )"
chiForm[78] = "( \\lnot c \\rightarrow d )"
chiForm[79] = "( \\lnot d \\rightarrow a )"
chiForm[80] = "( \\lnot d \\rightarrow b )"
chiForm[81] = "( \\lnot d \\rightarrow c )"
chiForm[82] = "( \\lnot a \\rightarrow c )"
chiForm[83] = "( \\lnot a \\rightarrow d )"
chiForm[84] = "( \\lnot a \\rightarrow b )"

chiForm[85] = "( b \\rightarrow a )"
chiForm[86] = "( c \\rightarrow a )"
chiForm[87] = "( c \\rightarrow b )"
chiForm[88] = "( c \\rightarrow d )"
chiForm[89] = "( d \\rightarrow a )"
chiForm[90] = "( d \\rightarrow b )"
chiForm[91] = "( d \\rightarrow c )"
chiForm[92] = "( a \\rightarrow c )"
chiForm[93] = "( a \\rightarrow d )"
chiForm[94] = "( a \\rightarrow b )"

chiForm[95] = "( \\lnot b \\leftrightarrow a )"
chiForm[96] = "( \\lnot c \\leftrightarrow a )"
chiForm[97] = "( \\lnot c \\leftrightarrow b )"
chiForm[98] = "( \\lnot c \\leftrightarrow d )"
chiForm[99] = "( \\lnot d \\leftrightarrow a )"
chiForm[100] = "( \\lnot d \\leftrightarrow b )"
chiForm[101] = "( \\lnot d \\leftrightarrow c )"
chiForm[102] = "( \\lnot a \\leftrightarrow c )"
chiForm[103] = "( \\lnot a \\leftrightarrow d )"
chiForm[104] = "( \\lnot a \\leftrightarrow b )"
chiForm[105] = "( \\lnot b \\leftrightarrow c )"
chiForm[106] = "( \\lnot b \\leftrightarrow d )"

chiForm[107] = "( c \\leftrightarrow b )"
chiForm[108] = "( c \\leftrightarrow d )"
chiForm[109] = "( d \\leftrightarrow a )"
chiForm[110] = "( d \\leftrightarrow b )"
chiForm[111] = "( d \\leftrightarrow c )"
chiForm[112] = "( a \\leftrightarrow c )"
chiForm[113] = "( a \\leftrightarrow d )"
chiForm[114] = "( a \\leftrightarrow b )"
chiForm[115] = "( b \\leftrightarrow c )"
chiForm[116] = "( b \\leftrightarrow d )"

chiForm[117] = "( a \\land \\lnot a )"

######################################################################

def getAtomOp(i):
	return ["1 "+concat[i]+" 1", "1 "+concat[i]+" 0","0 "+concat[i]+" 1","0 "+concat[i]+" 0"]

def insertValues(formula,var,values):
	for i in range(0,len(var)):
		formula = formula.replace(var[i], values[i])
	formula = formula.replace("\lnot 1", "0")
	formula = formula.replace("\lnot 0", "1")
	return formula

def shortenValues(formula,op):
	AtomOp = getAtomOp(op)
	#print(AtomOp)
	if(op==0):
		formula = formula.replace(AtomOp[0], "1")
		formula = formula.replace(AtomOp[1], "0")
		formula = formula.replace(AtomOp[2], "0")
		formula = formula.replace(AtomOp[3], "0")
	if(op==1):
		formula = formula.replace(AtomOp[0], "1")
		formula = formula.replace(AtomOp[1], "1")
		formula = formula.replace(AtomOp[2], "1")
		formula = formula.replace(AtomOp[3], "0")
	if(op==2):
		formula = formula.replace(AtomOp[0], "1")
		formula = formula.replace(AtomOp[1], "0")
		formula = formula.replace(AtomOp[2], "1")
		formula = formula.replace(AtomOp[3], "1")
	if(op==3):
		formula = formula.replace(AtomOp[0], "1")
		formula = formula.replace(AtomOp[1], "0")
		formula = formula.replace(AtomOp[2], "0")
		formula = formula.replace(AtomOp[3], "1")
	
	formula = formula.replace("\lnot 1", "0")
	formula = formula.replace("\lnot 0", "1")
	formula = formula.replace("( 0 )", "0")
	formula = formula.replace("( 1 )", "1")
	formula = formula.replace("1 1", "1")
	formula = formula.replace("0 0", "0")
	if(len(formula) == 3):
		formula = formula.replace(" 1 ", "1")
		formula = formula.replace(" 0 ", "0")
	return formula

def v(i):
	x = " x "
	if (i==0):
		x = " 0 "
	elif (i==1):
		x = " 1 "
	return x

def truthValueFromFormula(formula,values):
	formula = insertValues(formula, var, values)	
	erc = -1000
	while(len(formula) > 1 and erc < len(formula)):
		erc+=1
		formula = shortenValues(formula, 0)
		formula = shortenValues(formula, 1)
		formula = shortenValues(formula, 2)
		formula = shortenValues(formula, 3)
	if(erc >= len(formula)):
		print("--------------------- Error -----------------------------")
		print("Interrupted endless loop, the Formula couldn't get solved")
		print("---------------------- !!! ------------------------------")
		print(formula,len(formula), erc)
		formula = -1
	return formula

def buildFormulaIntelOr(phi):
	global chiForm
	kblen = len(chiForm)
	print("used Formulas:",kblen)
	chiMax = ""
	chivalues = ['0']*16
	y = 0
	for j in range(kblen):
		t = -1 #two
		f = -1 #four
		e = -1 #eight
		phi2 = [0]*16
		chi = ['']*16
		for i in range(0,16):
			if(i%2==0):
				t+=1
			if(i%4==0):
				f+=1
			if(i%8==0):
				e+=1
			values = [v(e%2),v(f%2),v(t%2),v(i%2)]
			chi[i] = truthValueFromFormula(chiForm[j], values)
		x = scoreForm2(phi, chi)
		#print(x,y)
		if(x > y):
			y = x
			chiMax = chiForm[j]
			chivalues = chi
	print("phi:   ",phi)
	print("chimax:",chivalues)
	print("choosen nearest Formula:",chiMax, "with score",y)
	form = chiMax
	#print(len(phi),len(phi))
	for i in range(0,16):
		if(phi[i]=='1' and chivalues[i]=='0'):
			#print("Added: ",chiForm[15-i],"for digit",i)
			if(form == ""):
				form += chiForm[15-i]
			else:
				form += " \\lor "
				form += chiForm[15-i]
				form = "( "+ form + " )"
	return form

def buildFormulaIntelAndOr(phi):
	print("Warning: this Formula shortening function may not be in any cases correct")
	print("please double check the result by inserting the result string again")
	print("or change the function at shortenFormula(phi)")
	global chiForm
	kblen = len(chiForm)
	print("used Formulas:",kblen)
	chiMax = ""
	chivalues = ['0']*16
	y = 0
	for j in range(kblen):
		t = -1 #two
		f = -1 #four
		e = -1 #eight
		phi2 = [0]*16
		chi = ['']*16
		for i in range(0,16):
			if(i%2==0):
				t+=1
			if(i%4==0):
				f+=1
			if(i%8==0):
				e+=1
			values = [v(e%2),v(f%2),v(t%2),v(i%2)]
			chi[i] = truthValueFromFormula(chiForm[j], values)
		x = scoreForm(phi, chi)
		#print(x,y)
		if(x > y):
			y = x
			chiMax = chiForm[j]
			chivalues = chi
	print("phi:   ",phi)
	print("chimax:",chivalues)
	print("choosen nearest Formula:",chiMax, "with score",y)
	form = chiMax
	#print(len(phi),len(phi))
	for i in range(0,16):
		if(phi[i]=='1' and chivalues[i]=='0'):
			#print("Added: ",chiForm[15-i],"for digit",i)
				form += " \\lor "
				form += chiForm[15-i]
				form = "( "+ form + " )"
		elif(phi[i]=='0' and chivalues[i]=='1'):
				form += " \\land "
				form += chiForm[15-i]
				form = "( "+ form + " )"
	return form

def buildFormula(phi):
	global chiForm
	form = ""
	for i in range(0,16):
		if(phi[i]=='1'):
			if(form == ""):
				form += chiForm[15-i]
			else:
				form += " \\lor "
				form += chiForm[15-i]
				form = "( "+ form + " )"
				#print("Form:",form)
	return form

def shortenFormula(phi):
	
	global chiForm
	kblen = len(chiForm)
	chi = [0]*kblen # truthtable values of short formulas
	score = [0]*kblen
	outForm = "No accurate short formula found for: "+str(phi)
	#outForm = buildFormula(phi)
	#print(outForm)
	#outForm = buildFormulaIntelOr(phi)
	outForm = buildFormulaIntelAndOr(phi) # may not be correct in any case
	#for j in range(0,kblen):
	#	t = -1 #two
	#	f = -1 #four
	#	e = -1 #eight
	#	phi2 = [0]*16
	#	for i in range(0,16):
	#		if(i%2==0):
	#			t+=1
	#		if(i%4==0):
	#			f+=1
	#		if(i%8==0):
	#			e+=1
	#		values = [v(e%2),v(f%2),v(t%2),v(i%2)]
	#		phi2[i] = truthValueFromFormula(chiForm[j], values)
	#	#print(phi2)
	#	chi[j] = phi2
	#	#print(chi)
	#	#print("Compared Formula","|","equality Score")
	#for i in range(0,kblen):
	#	#print(chiForm[i], " | ", chi[i])
	#	#print(chiForm[i], " | ", scoreForm(phi, chi[i]))
	#	if(chi[i] == phi):
	#		outForm = "Short Formula: "+chiForm[i]
	return outForm

def scoreForm(phi, chi):
	score = 0
	for i in range(0,16):
		if(chi[i]==phi[i]):
			score+=1
	return score

def scoreForm2(phi, chi):
	score = 0
	for i in range(0,16):
		if(phi[i]=='1'):
			if(chi[i]=='1'):
				score+=2
		else:
			if(chi[i]=='0'):
				score+=1
			else:
				score-=32
	return score

def printTruthTable(formula):
	phi = [0]*16
	print() 
	print("--------- Truth table -------------")
	print(var, "| phi")
	print("-----------------------------------")
	t = -1 #two
	f = -1 #four
	e = -1 #eight
	for i in range(0,16):
		if(i%2==0):
			t+=1
		if(i%4==0):
			f+=1
		if(i%8==0):
			e+=1
		values = [v(e%2),v(f%2),v(t%2),v(i%2)]
		#print(i,values)
		phi[i] = truthValueFromFormula(formula, values)
		print(values,"| ",phi[i])
	print()
	print("-----------------------------------")
	print(shortenFormula(phi))
	
	
printTruthTable(formula)