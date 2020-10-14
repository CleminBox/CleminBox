#CleminBox compiler
import sys
import os
from cleminlang import *
lang_file = open(sys.argv[1], "r")
compiled_program = CleminLangAssemble(lang_file.read())
lang_file.close()
compiled_lang_file = open(sys.argv[2], "wb")
compiled_lang_file.write(compiled_program)
compiled_lang_file.close()
