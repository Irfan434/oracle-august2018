#!/usr/bin/env python3

'''
Given a string, write a function that returns a "cleaned" string where adjacent chars 
that are the same have been reduced to a single char.
So "yyzzza" yields "yza".
'''
def stringClean(iStr):
	output = ''
	prevChar = ''
	for char in iStr:
		if char != prevChar:
			output += char
		prevChar = char
	return output

def testStringClean():
	assert "yza" == stringClean("yyzzza")
	assert "abcd" == stringClean("abbbcdd")
	assert "Helo" == stringClean("Hello")

def maxBlock(iStr):
	finalMax = 0
	curMax = 0
	prevChar = ''
	for char in iStr:
		if char == prevChar:
			curMax += 1
		else:
			curMax = 1
		prevChar = char
		finalMax = max(finalMax, curMax)
	return finalMax

def testMaxBlock():
	assert 2 == maxBlock("hoopla")
	assert 3 == maxBlock("abbCCCddBBBxx")
	assert 0 == maxBlock("")

def reorderBlock(iStr):
	chars = list(iStr)
	chars = sorted(chars, key=lambda s: s.lower())
	return ''.join(chars)

def testReorderBlock():
	assert "AAAabbccdF" == reorderBlock("bbAAccAadF")
	assert "ahloop" == reorderBlock("hoopla")

def runTests():
	print("Running tests...\n")
	print("Testing stringClean()")
	testStringClean()
	print("stringClean() OK!\n")
	print("Testing maxBlock()")
	testMaxBlock()
	print("maxBlock() OK!\n")
	print("Testing reorderBlock()")
	testReorderBlock()
	print("reorderBlock() OK!\n")

if __name__ == "__main__":
	runTests()
