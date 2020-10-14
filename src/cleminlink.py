#This code doesn't currently work. If you can, please fix this for me.
import sys
import os
srcfiles = []
outfile = ""
out_code = ""
srcfiles.append(sys.argv[1])
outfile = sys.argv[2]
functions = {}
current_func = ""
current_func_code = ""
currently_in_func = False
final_code = ""
commands = ["funcdef", "funcend", "callfunc"]
for i in srcfiles:
	srcfile = open(i, "r")
	for i2 in srcfile.read().split("\n"):
		codeline = i2.split("-=-")
		if codeline[0] == "funcdef":
			current_func = codeline[1]
			currently_in_func = True
		elif codeline[0] == "funcend":
			currently_in_func = False
			functions.update({current_func: current_func_code})
		elif currently_in_func:
			if not codeline[0] in commands:
				current_func_code = current_func_code + i2 + "\n"
		elif codeline[0] == "callfunc":
			try:
				final_code = final_code + functions[codeline[1]] + "\n"
			except:
				print("ERROR: Function " + codeline[1] + " does not exist.")
out_file = open(outfile, "w")
out_file.write(final_code)
out_file.close()
