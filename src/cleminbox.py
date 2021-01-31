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
	try:
		tmpvar = int(couldbenum)
	except:
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
				try:
					variable_memory[int(code_line[1])] = code_line[2]
				except:
					pass
			if code_line[0] == "addv":
				try:
					isnums = True
					if IsNumInCode(variable_memory[int(code_line[1])]) == False or IsNumInCode(variable_memory[int(code_line[2])]) == False:
						isnums = False
					if isnums:
						variable_memory[int(code_line[3])] = int(variable_memory[int(code_line[1])]) + int(variable_memory[int(code_line[2])])
					else:
						variable_memory[int(code_line[3])] = str(variable_memory[int(code_line[1])]) + str(variable_memory[int(code_line[2])])
				except:
					pass
			if code_line[0] == "prnt":
				try:
					print(variable_memory[int(code_line[1])])
				except:
					pass
			#print(code_line)
if __name__ == "__main__":
	codefile = None
	try:
		codefile = open(sys.argv[1], "rb")
	except:
		print("CleminBox - Making programming fun")
		print("Usage: cleminbox [filename]")
		exit(-1)
	RunCode(codefile.read())
	codefile.close()
