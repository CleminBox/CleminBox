# generate_wrappers.py - A tool to generate Shell Script based wrappers for CleminBox.
import sys
import os
template_clemincomp = """#!/bin/bash
cd CLEMINDIR
python3 clemincomp.py $@"""
cleminbox_bin_dir = sys.argv[1]
cleminbox_code_dir = sys.argv[2]
tmp_file = open(cleminbox_bin_dir + "/clemincomp", "w")
tmp_file.write(template_clemincomp.replace("CLEMINDIR", cleminbox_code_dir))
tmp_file.close()
os.system("chmod +x " + cleminbox_bin_dir + "/clemincomp")
