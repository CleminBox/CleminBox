import sys
import os
import time
import random
from cleminlang import *
#program_memory = []
variable_memory = []
for i in range(variable_memory_size):
	variable_memory.append("")
def IsNumInCode(couldbenum):
	num_chars = list("1234567890")
	for i in list(couldbenum):
		if i in num_chars:
			pass
		else:
			return False
	return True
def RunCode(codebytes):
	code = codebytes.decode()
	for i in code.split(internal_mapping["endln"].decode()):
		if not i == "":
			code_line = i.split(internal_mapping["newarg"].decode())
			code_line[0] = reverse_mapping[code_line[0]]
			#print(code_line)
			if code_line[0] == "setv":
				variable_memory[int(code_line[1])] = code_line[2]
			if code_line[0] == "addv":
				isnums = True
				if IsNumInCode(variable_memory[int(code_line[1])]) == False or IsNumInCode(variable_memory[int(code_line[2])]) == False:
					isnums = False
				if isnums:
					variable_memory[int(code_line[3])] = int(variable_memory[int(code_line[1])]) + int(variable_memory[int(code_line[2])])
				else:
					variable_memory[int(code_line[3])] = str(variable_memory[int(code_line[1])]) + str(variable_memory[int(code_line[2])])
			if code_line[0] == "prnt":
				print(variable_memory[int(code_line[1])])
			#print(code_line)
if __name__ == "__main__":
	codefile = None
	try:
		codefile = open(sys.argv[1], "rb")
		codefile.close()
	except:
		print("CleminBox - Making programming fun")
		print("Usage: cleminbox [filename]")
	RunCode(codefile.read())
