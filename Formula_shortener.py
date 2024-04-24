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
#		Version 2.0: making new knowledge base with formulas including 3000         #
#       different truth values. As this needs much calculation Power, try to        #
#		use PyPy                                                                    #
#                                                                                   #
#####################################################################################

import sys



var = [" a "," b "," c "," d "] #the original var
originalvar = True  #if not using the original var put this to false
#!!! IMPORTANT: if making own var array, make shure you make spaces on the left and the right of the variable !!!
#var = [" A "," B "," C "]
#var = [" x "," y "," z "]
concat = ["\\land","\\lor","\\rightarrow", "\\leftrightarrow" ]
neg = "\\lnot"
chilen = 2**len(var)
kbformula = []

def cleanFormula(formula):
	# Cleaning the Formula, bringing them in right spaces:
	for i in range(2):
		formula = formula.replace("  ", " ")
		formula = formula.replace("((", "( (")
		formula = formula.replace("))", ") )")
	
	vard = ''.join(var)				# vard = ["a","b","c","d"] but in dependence of var
	vard = vard.replace(" ", "")
	
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
	return formula


######################### Formulas ###################################
#Ground formulas database
chiForm = [""]*190 # short formulas

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
chiForm[12] = "( ( \\lnot ( a \\lor b ) \\land c ) \\land d )" #short for: "( ( ( \\lnot a \\land \\lnot b ) \\land c ) \\land d )"
chiForm[13] = "( \\lnot ( ( a \\lor b ) \\lor d ) \\land c )" # short for: "( ( ( \\lnot a \\land \\lnot b ) \\land c ) \\land \\lnot d )"
chiForm[14] = "( \\lnot ( ( a \\lor b ) \\lor c ) \\land d )" # short for "( ( ( \\lnot a \\land \\lnot b ) \\land \\lnot c ) \\land d )"
chiForm[15] = "\\lnot ( ( ( a \\lor b ) \\lor c ) \\lor d )" # short for "( ( ( \\lnot a \\land \\lnot b ) \\land \\lnot c ) \\land \\lnot d )"

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
chiForm[30] = "( \lnot ( ( a \land b ) \land c ) \lor d )"
chiForm[31] = "\lnot ( ( ( a \land b ) \land c ) \land d )"

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

chiForm[118] = "( ( a \\land b ) \\land c )"
chiForm[119] = "( ( a \\land c ) \\land b )"
chiForm[120] = "( ( a \\land b ) \\land d )"
chiForm[121] = "( ( a \\land c ) \\land d )"
chiForm[122] = "( ( b \\land c ) \\land d )"
chiForm[123] = "( ( b \\land d ) \\land c )"
chiForm[124] = "( ( b \\land d ) \\land a )"
chiForm[125] = "( ( b \\land c ) \\land a )"
chiForm[126] = "( ( a \\land d ) \\land b )"
chiForm[127] = "( ( c \\land d ) \\land a )"
chiForm[128] = "( ( c \\land d ) \\land b )"
chiForm[129] = "( ( a \\land d ) \\land c )"
					
chiForm[130] = "( ( a \\land b ) \\lor c )"
chiForm[131] = "( ( a \\land c ) \\lor b )"
chiForm[132] = "( ( a \\land b ) \\lor d )"
chiForm[133] = "( ( a \\land c ) \\lor d )"
chiForm[134] = "( ( b \\land c ) \\lor d )"
chiForm[135] = "( ( b \\land d ) \\lor c )"
chiForm[136] = "( ( b \\land d ) \\lor a )"
chiForm[137] = "( ( b \\land c ) \\lor a )"
chiForm[138] = "( ( a \\land d ) \\lor b )"
chiForm[139] = "( ( c \\land d ) \\lor a )"
chiForm[140] = "( ( c \\land d ) \\lor b )"
chiForm[141] = "( ( a \\land d ) \\lor c )"

chiForm[142] = "( ( a \\land b ) \\rightarrow c )"
chiForm[143] = "( ( a \\land c ) \\rightarrow b )"
chiForm[144] = "( ( a \\land b ) \\rightarrow d )"
chiForm[145] = "( ( a \\land c ) \\rightarrow d )"
chiForm[146] = "( ( b \\land c ) \\rightarrow d )"
chiForm[147] = "( ( b \\land d ) \\rightarrow c )"
chiForm[148] = "( ( b \\land d ) \\rightarrow a )"
chiForm[149] = "( ( b \\land c ) \\rightarrow a )"
chiForm[150] = "( ( a \\land d ) \\rightarrow b )"
chiForm[151] = "( ( c \\land d ) \\rightarrow a )"
chiForm[152] = "( ( c \\land d ) \\rightarrow b )"
chiForm[153] = "( ( a \\land d ) \\rightarrow c )"

chiForm[154] = "( ( a \\land b ) \\leftrightarrow c )"
chiForm[155] = "( ( a \\land c ) \\leftrightarrow b )"
chiForm[156] = "( ( a \\land b ) \\leftrightarrow d )"
chiForm[157] = "( ( a \\land c ) \\leftrightarrow d )"
chiForm[158] = "( ( b \\land c ) \\leftrightarrow d )"
chiForm[159] = "( ( b \\land d ) \\leftrightarrow c )"
chiForm[160] = "( ( b \\land d ) \\leftrightarrow a )"
chiForm[161] = "( ( b \\land c ) \\leftrightarrow a )"
chiForm[162] = "( ( a \\land d ) \\leftrightarrow b )"
chiForm[163] = "( ( c \\land d ) \\leftrightarrow a )"
chiForm[164] = "( ( c \\land d ) \\leftrightarrow b )"
chiForm[165] = "( ( a \\land d ) \\leftrightarrow c )"

chiForm[166] = "( ( a \\lor b ) \\rightarrow c )"
chiForm[167] = "( ( a \\lor c ) \\rightarrow b )"
chiForm[168] = "( ( a \\lor b ) \\rightarrow d )"
chiForm[169] = "( ( a \\lor c ) \\rightarrow d )"
chiForm[170] = "( ( b \\lor c ) \\rightarrow d )"
chiForm[171] = "( ( b \\lor d ) \\rightarrow c )"
chiForm[172] = "( ( b \\lor d ) \\rightarrow a )"
chiForm[173] = "( ( b \\lor c ) \\rightarrow a )"
chiForm[174] = "( ( a \\lor d ) \\rightarrow b )"
chiForm[175] = "( ( c \\lor d ) \\rightarrow a )"
chiForm[176] = "( ( c \\lor d ) \\rightarrow b )"
chiForm[177] = "( ( a \\lor d ) \\rightarrow c )"

chiForm[178] = "( ( a \\lor b ) \\leftrightarrow c )"
chiForm[179] = "( ( a \\lor c ) \\leftrightarrow b )"
chiForm[180] = "( ( a \\lor b ) \\leftrightarrow d )"
chiForm[181] = "( ( a \\lor c ) \\leftrightarrow d )"
chiForm[182] = "( ( b \\lor c ) \\leftrightarrow d )"
chiForm[183] = "( ( b \\lor d ) \\leftrightarrow c )"
chiForm[184] = "( ( b \\lor d ) \\leftrightarrow a )"
chiForm[185] = "( ( b \\lor c ) \\leftrightarrow a )"
chiForm[186] = "( ( a \\lor d ) \\leftrightarrow b )"
chiForm[187] = "( ( c \\lor d ) \\leftrightarrow a )"
chiForm[188] = "( ( c \\lor d ) \\leftrightarrow b )"
chiForm[189] = "( ( a \\lor d ) \\leftrightarrow c )"
					
# creating separate knowledgebase with most common short formulas					
def kbBuilderFind(phi):
	global var
	#vars = ["a","b","c","d","\\lnot a","\\lnot b","\\lnot c","\\lnot d"]
	vars = []
	for v in var:
		vars.append(v)
		vars.append("\\lnot"+v)
	maxform = "n o f o r m u l a h a s b e e n f o u n d s o f a r y o u h a v e a v e r y h u g e p r o b l e m"
	print("ground vars for building formulas: ",vars)
	# Do not make more than 4 X and 3 O in baseForms !!! As we would need mor loops, which means more calculation power/time needed.
	baseForms = ["( X O X )", "( ( X O X ) O X )","( ( ( X O X ) O X ) O X )", "( ( X O X ) O ( X O X ) )"," X ","\\lnot ( X O X )","\\lnot ( ( X O X ) O X )","\\lnot ( ( ( X O X ) O X ) O X )","\\lnot ( ( X O X ) O ( X O X ) )"]
	kblen = 2**chilen #len(vars)**4*len(concat)**3*len(baseForms) # can not get more than 2^16 different truth values
	if(len(var)>4):
		print("This Formula has too many variables for the formula builder...")
	else:
		print("Assigning the Arrays...")
		kbformula = [""]*kblen 				#array for formulas
		kbTruthArrays = [[""]*chilen]*kblen #array for truthvalues
		print("Arrays assigned. Generating Formulas...")
		z = 0
		rd = 0
		for a in vars:
			for b in vars:
				print(z, "of",kblen,"done... Round:",rd,"/64")
				rd+=1
				for c in vars:
					for d in vars:
						for o1 in concat:
							for o2 in concat:
								for o3 in concat:
									for f in baseForms: # inserting all the Values into the generic base Formulas (arr baseForms)
										kformula = f
										x = kformula.find("X")
										#print(kformula,x,a)
										#print(kformula[0:x] + a +kformula[x+1::])
										r = 0
										while(x > 0):
											if(r == 0):
												kformula = kformula[0:x] + d +kformula[x+1::] 
												r+=1
											elif(r == 1):
												kformula = kformula[0:x] + c +kformula[x+1::]
												r+=1
											elif(r == 2):
												kformula = kformula[0:x] + b +kformula[x+1::]
												r+=1
											else:
												kformula = kformula[0:x] + a +kformula[x+1::]
												r+=1
											x = kformula.find("X")
											#print("kx",kformula)
										r = 0
										o = kformula.find("O")
										while(o > 0):
											if(r == 0):
												kformula = kformula[0:o] +" "+ o3 +kformula[o+1::]
												r+=1
											elif(r == 1):
												kformula = kformula[0:o] +" "+ o2 +kformula[o+1::]
												r+=1
											else:
												kformula = kformula[0:o] +" "+ o1 +kformula[o+1::]
												r+=1
											o = kformula.find("O")
											#print("k",kformula)
										cleanformula = kformula.replace("  "," ")
										cleanformula = cleanformula.replace("  "," ")
										truthArray = getTruthArray(cleanformula)
										same = False
										for i in range(0,z):
											if(cleanformula == kbformula[i]):
												same = True
												break
											elif(kbTruthArrays[i] == truthArray):
												#print("sametruth")
												same = True
												if(getLen(cleanformula) < getLen(kbformula[i])):
													#print("shorter formula found", kbformula[i],"  |||  ",cleanformula)
													kbformula[i] = cleanformula
												break
										if(not same):		
											kbformula[z] = cleanformula
											#print("kb",kbformula[z])
											kbTruthArrays[z] = truthArray
											#print(kbTruthArrays[z],kbformula[z])
											z+=1
										if(z==2**chilen):
											break
											break

		print("successfully built Formulas :-)")
		print("total Formulas:",z)
		print("Calculating TruthArrays")
		p = int(z/8)
		s = 0
		maxchi = [-1]*chilen
		for i in range(0,z):
			if(i == p):
				print("1/8 done")
			elif(i == 2*p):
				print("2/8 done")
			elif(i == 3*p):
				print("3/8 done")
			elif(i == 4*p):
				print("4/8 done")
			elif(i == 5*p):
				print("5/8 done")
			elif(i == 6*p):
				print("6/8 done")
			elif(i == 7*p):
				print("7/8 done")
			score = scoreForm(phi, kbTruthArrays[i])
			print(kbTruthArrays[i],score,getLen(kbformula[i]),kbformula[i])  #printout all formulas
			if(score > s ):	#finds nearest formula
				s = score
				#print(len(cleanformula),len(maxform),cleanformula,maxform)
				maxform = kbformula[i]
				maxchi = kbTruthArrays[i]
			elif(score == s): #finds equal formula
				if(getLen(cleanformula) < getLen(maxform)): #takes shorter equal formula
					maxform = kbformula[i]
					maxchi = kbTruthArrays[i]
		print("TruthArrays Built")
		print("phi:",phi)
		print("chi:",maxchi,maxform,s)
	
		print("search for combined formulas with AND ad OR...")
		#combining any two formulas in the knowledgebase together to find equal formula
		found = False
		for i in range(0,z):
			if(i == p):
				print("1/8 done")
			elif(i == 2*p):
				print("2/8 done")
			elif(i == 3*p):
				print("3/8 done")
			elif(i == 4*p):
				print("4/8 done")
			elif(i == 5*p):
				print("5/8 done")
			elif(i == 6*p):
				print("6/8 done")
			elif(i == 7*p):
				print("7/8 done")
			for j in range(i,z):
				chi = andArray(kbTruthArrays[i], kbTruthArrays[j]) # AND the two arrays
			#Integrating Formulas also into the knowledge base... As it takes to long, i commented it out
			#IsChiInArr = False
			#for r in range(0,z):
			#	if(kbTruthArrays[r] == chi):
			#		if(getLen(kbformula[r]) > len("( "+kbformula[i]+" \\land "+kbformula[j]+" )")):
			#			kbformula == "( "+kbformula[i]+" \\land "+kbformula[j]+" )"
			#		IsChiInArr = True 
			#if(not IsChiInArr):
			#	kbformula[z] = "( "+kbformula[i]+" \\land "+kbformula[j]+" )"
			#	kbTruthArrays[z] = chi
			#	z+=1
				if(chi==phi):
					found = True
					form = "( "+kbformula[i]+" \\land "+kbformula[j]+" )"
					if(s < chilen or getLen(maxform) > getLen(form)):
						maxform = form
						maxchi = getTruthArray(form)
					break
			
				chi = orArray(kbTruthArrays[i], kbTruthArrays[j]) # OR the two arrays
			#Integrating Formulas also into the knowledge base... As it takes to long, i commented it out
			#IsChiInArr = False
			#for r in range(0,z):
			#	if(kbTruthArrays[r] == chi):
			#		if(getLen(kbformula[r]) > len("( "+kbformula[i]+" \\lor "+kbformula[j]+" )")):
			#			kbformula == "( "+kbformula[i]+" \\lor "+kbformula[j]+" )"
			#		IsChiInArr = True 
			#if(not IsChiInArr):
			#	kbformula[z] = "( "+kbformula[i]+" \\land "+kbformula[j]+" )"
			#	kbTruthArrays[z] = chi
			#	z+=1
				if(chi==phi):
					found = True
					form = "( "+kbformula[i]+" \\lor "+kbformula[j]+" )"
					if(s < chilen or getLen(maxform) > getLen(form)):
						maxform = form
						maxchi = getTruthArray(form)
					break
		print("used ",z,"different formulas/chivalues")
		if(found):		
			print("Formula found: ",maxform)
		else:
			print("nearest Formula found: ",maxform)
		print("Length:",getLen(maxform),"Score:",scoreForm(phi, maxchi),"/",chilen)
		print("phi",phi)
		print("chi",maxchi)
	return maxform
	

######################################################################

#returns length of formula
def getLen(formula):
	x = formula.split(" ")
	return len(x)

def getAtomOp(i):
	return ["1 "+concat[i]+" 1", "1 "+concat[i]+" 0","0 "+concat[i]+" 1","0 "+concat[i]+" 0"]

def insertValues(formula,var,values):
	for i in range(0,len(var)):
		formula = formula.replace(var[i], values[i])
	formula = formula.replace("\lnot 1", "0")
	formula = formula.replace("\lnot 0", "1")
	return formula

# shorten the values of atomic operations with hardcoded truth values
def shortenValues(formula,op):
	AtomOp = getAtomOp(op)
	#print(AtomOp)
	formula = formula.replace("\lnot 1", "0")
	formula = formula.replace("\lnot 0", "1")
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

def v(i):
	x = " x "
	if (i%2==0):
		x = " 0 "
	elif (i%2==1):
		x = " 1 "
	return x

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
		print("--------------------- Error -----------------------------")
		print("Interrupted endless loop, the Formula couldn't get solved")
		print("---------------------- !!! ------------------------------")
		print(formula,len(formula), erc)
		formula = -1
	return formula


def formulaClassifier(phi):
	global chiForm
	kblen = len(chiForm)
	print("used Formulas:",kblen)
	chiMax = ""
	chivalues = ['0']*16
	y = 0
	classF =[-1]*len(chiForm)
	for f in range(kblen):
		chi = getTruthArray(chiForm[f])
		#print("chi:",chi,"Formula:",chiForm[f])
		x = scoreForm2(phi, chi)
		classF[f] = x
	print("classification:", classF)

def buildAndOrformula(phi):
	global chiForm
	kblen = len(chiForm)
	print("used Formulas:",kblen)
	chiMax = ""
	chivalues = ['0']*16
	chiArr = [0]*len(chiForm)
	form = "No And combined Formula found..."
	for f in range(kblen):
		chiArr[f] = getTruthArray(chiForm[f])
		#print("chiArr",chiArr)
	for i in range(0,len(chiArr)):
		for j in range(i,len(chiArr)):
			chi = andArray(chiArr[i], chiArr[j]) # and the two arrays
			#print("chiArr3",chi,scoreForm(phi, chi))
			if(chi==phi):
				form = "("+chiForm[i]+"\\land"+chiForm[j]+")"
				print("Formula found: ",form)
				print("Length:",getLen(form))
				print("phi",phi)
				print("chi",getTruthArray(form))
				break
	for i in range(0,len(chiArr)):
		for j in range(i,len(chiArr)):
			chi = orArray(chiArr[i], chiArr[j]) # or the two arrays
			#print("chiArr3",chi,scoreForm(phi, chi))
			if(chi==phi):
				form = "("+chiForm[i]+"\\lor"+chiForm[j]+")"
				print("Formula found: ",form)
				print("Length:",getLen(form))
				print("phi",phi)
				print("chi",getTruthArray(form))
				break
	return form

# TODO: finish
def buildWithNearest(phi):
	formulas = [""]*3
	formChi = [""]*3
	candidate = ""
	(formulas[0], formChi[0], y) = getNearestFormulas(phi, 0)
	(formulas[1], formChi[1], y) = getNearestFormulas(phi, 1)
	(formulas[2], formChi[2], y) = getNearestFormulas(phi, 2)
	diff = diffArray(phi, formChi[0])
	print("phi: ",phi)
	print("chi: ",formChi[0],formulas[0])
	print("diff:",diff)
	print("nearest Formulas:")
	for i in range(0, len(formulas)):
		print("chi:",formChi[i],formulas[i])
	

def getNearestFormulas(phi,art):
	kblen = len(chiForm)
	chiArr= [["-1"]*chilen]*kblen
	chiMax = [-1]*chilen
	for f in range(kblen):
		chiArr[f] = getTruthArray(chiForm[f])
	y = 0
	if(art == 0):										#normal scoring
		for i in range(0,len(chiArr)):
			x = scoreForm(phi, chiArr[i])
			if(x > y):
				y = x
				chiMax = chiForm[i]
				chivalues = chiArr[i]
			elif(x == y):
				if(len(chiForm[f]) < len(chiMax)):
					chiMax = chiForm[i]
					chivalues = chiArr[i]
	elif(art == 1):										# scoring 2 -> for OR-ing
		for i in range(0,len(chiArr)):
			x = scoreForm2(phi, chiArr[i])
			if(x > y):
				y = x
				chiMax = chiForm[i]
				chivalues = chiArr[i]
			elif(x == y):
				if(len(chiForm[f]) < len(chiMax)):
					chiMax = chiForm[i]
					chivalues = chiArr[i]
	elif(art > 1):										# scoring 3 -> for AND-ing
		for i in range(0,len(chiArr)):
			x = scoreForm3(phi, chiArr[i])
			if(x > y):
				y = x
				chiMax = chiForm[i]
				chivalues = chiArr[i]
			elif(x == y):
				if(len(chiForm[f]) < len(chiMax)):
					chiMax = chiForm[i]
					chivalues = chiArr[i]
	return (chiMax, chivalues, y)
		
		
	
# returns truth array of a formula
def getTruthArray(formula):
	chi = ['']*chilen
	values = [-1]*len(var)
	z = chilen
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
		chi[i] = truthValueFromFormula(formula, values)
	return chi

# all differences = 1
def diffArray(arr1, arr2):
	arr3 = [0]*len(arr1)
	for i in range(0,len(arr1),1):
		arr3[i] =  diffStr(arr1[i], arr2[i])
	return arr3

# differences:
# 0 0 = 0
# 1 0 = 0
# 1 1 = 0
# 0 1 = 1
def diffzeroArray(arr1, arr2):
	arr3 = [0]*len(arr1)
	for i in range(0,len(arr1),1):
		arr3[i] =  diffzeroStr(arr1[i], arr2[i])
	return arr3

def andArray(arr1, arr2):
	arr3 = [0]*len(arr1)
	for i in range(0,len(arr1),1):
		arr3[i] =  andStr(arr1[i], arr2[i])
	return arr3

def orArray(arr1, arr2):
	arr3 = [0]*len(arr1)
	for i in range(0,len(arr1),1):
		arr3[i] =  orStr(arr1[i], arr2[i])
	return arr3

def andStr(a, b):
	r = "0"
	if(a == "1" and b == "1"):
		r = "1"
	return r

def orStr(a,b):
	r = "1"
	if(a == "0" and b == "0"):
		r = "0"
	return r

def diffStr(a,b):
	r = "1"
	if(a == b):
		r = "0"
	return r

def diffzeroStr(a,b):
	r = "0"
	if(a == "0" and b == "1"):
		r = "1"
	return r

# TODO
#def rightStr(a,b):
#	r = "1"
#	if(a == "0" and b == "0"):
#		r = "0"
#	return r
#
#def leftrightStr(a,b):
#	r = "1"
#	if(a == "0" and b == "0"):
#		r = "0"
#	return r

#Building the formula with lor
def buildFormulaIntelOr(phi):
	global chiForm
	kblen = len(chiForm)
	print("used Formulas:",kblen)
	chiMax = ""
	chivalues = ['0']*16
	y = 0
	for f in range(kblen):
		chi = getTruthArray(chiForm[f])
		#print("chi:",chi,scoreForm2(phi, chi),scoreForm(phi, chi),scoreForm3(phi, chi),"Formula:",chiForm[f])
		x = scoreForm2(phi, chi)
		#print(x,y)
		if(x > y):
			y = x
			chiMax = chiForm[f]
			chivalues = chi
		elif(x == y):
			if(len(chiForm[f]) < len(chiMax)):
				chiMax = chiForm[f]
				chivalues = chi
	form = chiMax
	if(chivalues==phi):
		print("Formula found:",chiMax,"with score",y)
		print("phi:   ",phi)
		print("chimax:",chivalues)
	else:
		print("Formula not found...")
		print("phi:   ",phi)
		print("chimax:",chivalues)
		print("choosen nearest Formula:",chiMax, "with score",y)
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
	global chilen
	#print("Warning: this Formula shortening function may not be in any cases correct")
	#print("please double check the result by inserting the result string again")
	#print("or change the function at shortenFormula(phi)")
	global chiForm
	kblen = len(chiForm)
	print("used Formulas:",kblen)
	chiMax = ""
	chivalues = ['0']*chilen
	y = 0
	for j in range(kblen):
		chi = getTruthArray(chiForm[j])
		x = scoreForm(phi, chi)
		#print("chi:",chi,scoreForm2(phi, chi),x,scoreForm3(phi, chi),"Formula:",chiForm[j])
		#print(x,y)
		if(x > y):
			y = x
			chiMax = chiForm[j]
			chivalues = chi
		elif(x == y):
			if(len(chiForm[j])<len(chiMax)):
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
	for i in range(0,16):
		if(phi[i]=='0' and chivalues[i]=='1'):
				form += " \\land \\lnot"
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
	global originalvar
	global chiForm
	kblen = len(chiForm)
	chi = [0]*kblen # truthtable values of short formulas
	score = [0]*kblen
	outForm = "No accurate short formula found for: "+str(phi)
	#outForm = buildFormula(phi)
	#print(outForm)
	#outForm = buildAndOrformula(phi)
	if originalvar:
		formulaClassifier(phi)
		#outForm = buildFormulaIntelOr(phi)
		buildWithNearest(phi)
		outForm = buildFormulaIntelAndOr(phi) # may not be correct in any case
	outForm = kbBuilderFind(phi)
	return outForm
	
# scoring the differences between the forms
# Normal scoring 1 hit 0 miss
# Max = 16
# Min = 0
def scoreForm(phi, chi):
	global var
	score = 0
	if len(chi) == len(phi):
		for i in range(0,len(chi)):
			if(chi[i]==phi[i]):
				score+=1
	else:
		print("error in scoreForm, len not the same: chi:",len(chi),"phi:",len(phi))
	return score

# Punish false positive -> phi = 0, chi = 1
# Max: 32
# Min: -512
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

# Punish false negative -> phi = 1, chi = 0
# Max: 32
# Min: -512
def scoreForm3(phi, chi):
	score = 0
	for i in range(0,16):
		if(phi[i]=='0'):
			if(chi[i]=='0'):
				score+=2
		else:
			if(chi[i]=='1'):
				score+=1
			else:
				score-=32
	return score

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
		print(values,"| ",phi[i])
	return phi 
	

def getFormulaFromPhi():
	phi = ['0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '0', '0', '1', '0', '1', '0']
	print("Using Truth Values:\n",phi)
	form = buildFormulaIntelAndOr(phi)
	print(form)
	shortenFormula(phi)
	
	
	
def main():
	print("####################################")
	print("Welcome to the Formula Shortener 2.0")
	print("        Made by MisterM")
	print("####################################")
	print("")
	try:
		formula  = sys.argv[1]
	except:
		choose = input("What do you want to do? \nShorten formula (s) \nBuild formula from phi (b)\n")
		if(choose == "s"):
			formula = input("insert the formula: ")
			phi = printTruthTable(cleanFormula(formula))
			print()
			print("-----------------------------------")
			print(shortenFormula(phi))
		else:
			getFormulaFromPhi()
			
			
main()