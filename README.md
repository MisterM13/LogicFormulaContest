


# Propositional Logic Formula Contest

## How it was created
The Applications I made in this directory were made in relation to the Propositional Logic Formula Contest we made at the Lecture Discrete Mathematics at University of Basel. You are welcome to analyze it for educational purposes or to build your own script, please don't just copy it, because it's more fun to compete at a contest if you wrote it yourself.

## Using it

There are two Applications:

- [makeLogicFormula.py](makeLogicFormula.py)
this creates a logic formula of a discrete length (only the mathematic signs are seen as an element, not the brackets and spaces). You can define the length by changing `maxlen`

to run the  file  use 
```
python3 makeLogicFormula.py
 ```
 
 
 
-  [Formula_shortener.py](Formula_shortener.py)
	this script analyzes a formula and returns a (probably) shorter formula back.

when using with small formulas ( < 120 elements) you can use
 ```
Python3 Formula_shortener.py
 ```
 and then copy the formula in

for bigger formulas (> 120 elements) use:
```
Python3 Formula_shortener.py  "insert formula here"
```
if it returns an array of  `-1` and many errors, the formula logic is probably bad formed/wrong

> [repo on github](https://github.com/MisterM13/LogicFormulaContest.git)
