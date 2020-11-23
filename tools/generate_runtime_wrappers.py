import sys
import os
template_cleminbox = """#!/bin/bash
cd CLEMINDIR
python3 cleminbox.py $@"""
cleminbox_bin_dir = sys.argv[1]
cleminbox_code_dir = sys.argv[2]
tmp_file = open(cleminbox_bin_dir + "/cleminbox", "w")
tmp_file.write(template_cleminbox.replace("CLEMINDIR", cleminbox_code_dir))
tmp_file.close()
os.system("chmod +x " + cleminbox_bin_dir + "/cleminbox")
