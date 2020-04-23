# PL_HW2_WHILE

An interpreter for the While language, using python 3

I used my code for HW1. In HW1 I used the code in the following link as a reference:
https://ruslanspivak.com/lsbasi-part7/


You only need to run "make". By doing so, the Makefile makes a file called while with
a command written in it. This file, when executed as "./while", runs the HW2.py file 
which reads an expression from input, parses it to an AST, evaluates the resulting 
AST, and writes the result to stdout.

New testcases are placed in the "tests" directory. To the best of my knowledge, these 
testcases covers all of the features needed. It also tests the new feature added to 
the language which is e1 > e2.
