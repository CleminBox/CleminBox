import sys
import os
import time
import random
def mb2b(mbint):
	return 100000 * mbint
base_char_num = 200
#program_memory_size = mb2b(400)
variable_memory_size = mb2b(15)

reverse_mapping = {
chr(base_char_num + 1): "prnt", 
chr(base_char_num + 2): "move",
chr(base_char_num + 3): "copy",
chr(base_char_num + 4): "addv",
chr(base_char_num + 5): "setv"
#chr(base_char_num + 6): "sysc"
}

mapping = {
"prnt": chr(base_char_num + 1).encode(), #Print address contents on screen.
"move": chr(base_char_num + 2).encode(), #Move contents from one address to another.
"copy": chr(base_char_num + 3).encode(), #Copy contents from one address to another.
"addv": chr(base_char_num + 4).encode(), #Add Address 1's contents and Address 2's contents to Address 3.
"setv": chr(base_char_num + 5).encode() #Set Address to a string or int.
#"sysc": chr(base_char_num + 6).encode() #Sandbox syscall that allows the program to break out of the VM, but with limited access.
}

internal_mapping = {
"endln": chr(base_char_num + 90).encode(),
"newarg": chr(base_char_num + 91).encode()
}

def CleminLangAssemble(code):
	bytesvar = b""
	line = 1
	for i in code.split('\n'):
		code_line = i.split("	")
		instr = code_line[0]
		if instr == "":
			pass
		else:
			bytesvar = bytesvar + mapping[instr]
			for i2 in code_line[1].split('-'):
				bytesvar = bytesvar + internal_mapping["newarg"]
				bytesvar = bytesvar + i2.encode()
			bytesvar = bytesvar + internal_mapping["endln"] #End line
			line = line + 1
	return bytesvar
