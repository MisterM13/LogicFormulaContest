#!/usr/bin/env python3

###############################  makeLogicFormula.py  ###############################
#                                                                                   #
#       This Program was made to win the Discrete Mathematics                       #
#       logic contest at Unibas or at least to give a little bit Challenge          #
#       to other students which also created Scripts for it.                        #
#                                                                                   #
#       It makes a random logic formula with a fix length (maxlen)                  #
#                                                                                   #
#       Made by Matthias alias MisterM (https://github.com/MisterM13),              #
#       this Program may not be used by other students to win the contest,          #
#       because everyone learns by making his own program.                          #
#       analyzing and learning from it is allowed ;-)                               #
#       Disclaimer: variable names are not mathematically accurate                  #
#                                                                                   #
#####################################################################################

import random
sentence = []
var = ["a","b","c","d"]
concat = ["\\land","\\lor","\\leftrightarrow","\\rightarrow"]
neg = "\\lnot"

def makeBrackets(sentence):
	res = [""] *(len(sentence)+2)
	res[0] = "("
	for i in range(len(sentence)):
		res[i+1] = sentence[i]
	res[len(sentence)+1] = ")"
	return res
	
def makeGroundStatement(num):
	sentence = [] * 1
	if(num == 1):
		sentence = getVar(sentence,0)
	else:
		sentence = makeBrackets(getVar(getRandCon(makeGroundStatement(num-1)),num-1))
	return sentence

def getVar(sentence,num):
	j = random.randint(0, 1)
	if(j==1):
		sentence.append(neg)
	sentence.append(var[num])
	return sentence

def getRandVar(sentence):
	i = random.randint(0, 4)
	j = random.randint(0, 1)
	if(j==1):
		sentence.append(neg)
	sentence.append(var[i])
	return sentence

def getRandCon(sentence):
	i = random.randint(0, 3)
	sentence.append(concat[i])
	#print("concat: ",sentence, concat[i])
	return sentence

def addStatements(statement1, statement2):
	statement1 = getRandCon(statement1)
	len1 = len(statement1)
	len2 = len(statement2)
	if(concat.count(statement2[len2-1]) > 0):
		statement2[len2-1] = ""
		len2 = len(statement2)
	sentence = [""]*(len1+len2+1)
	for i in range(0,len1):
		sentence[i] = statement1[i]
	for j in range(0,len2):
		#print(len1,len2,len1+j, j, len(sentence))
		sentence[len1+j] = statement2[j]
		
	sentence = makeBrackets(sentence)
	#print("-------------",len(sentence), "---------------------")
	#print(" ".join(sentence))
	#print("-------------- statement1: -----------------")
	#print(" ".join(statement1))
	#print("-------------- statement2: -----------------")
	#print(" ".join(statement2))
	#print("-------------------------------------")
	return sentence

#sentence = makeGroundStatement(4)

def getLen(formula):
	x = len(formula)
	l = formula.count("(")
	r = formula.count(")")
	s = formula.count("")
	return x - (l+r+s)


def getLogicFormula():
	statements = [""]*20
	#print("---------- statements ---------------")
	for i in range(20):
		statements[i] = makeGroundStatement(4)
		#print(" ".join(statements[i]))
		#print("-------------------------------------")
	
	i = random.randint(0, 19)
	j = random.randint(0, 19)
	sentence = addStatements(statements[i], statements[j])
	while(getLen(sentence) < maxlen):
		j = random.randint(0, 19)
		sentence = addStatements(sentence, statements[j])
		#print("Statement:", j)
	return sentence

maxlen = 1000
while(getLen(sentence)!=maxlen):
	sentence = getLogicFormula()
	#print(sentence)
print(" ".join(sentence))
print(getLen(sentence))