# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:01:53 2017

@author: Carson Hanel
@author: Max Loeffler
"""
import Parser

class CodeWriter():
    def __init__(self, filename):
        self.filename = filename.replace("vm", "asm")
        self.ostream  = open(self.filename, mode = 'w')
        self.i        = 0

    def writeArithmetic(self, command):
        code = ""
        if command.lower() == "add":
            code += "// Add sequence\n"
            #First, decrements stack pointer
            #Then, grabs first data member for add.
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n" 
            #Sets memory to 0; cleans the temporary stack
            code += "M=0\n"
            #First, decrements stack pointer again
            #Then, grabs second data member for add
            code += "@SP\n"
            code += "AM=M-1\n"
            #Adds the two together inplace of the first operond
            code += "M=D+M\n"
            #Increments the stack pointer to where evaluation saved
            code += "@SP\n"
            code += "AM=M+1\n"
            self.ostream.write(code)
            return
            
        if command.lower() == "sub":
            code += "// Sub sequence\n"
            #Decrements stack pointer to right operond
            #Then, grabs first data member for sub.
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            #Sets memory to 0; cleans temporary stack
            code += "M=0\n"
            #Decrements stack pointer to left operond
            code += "@SP\n"
            code += "AM=M-1\n"
            #Subtracts inplace M = left, D = right
            code += "M=M-D\n"
            #Increments the stack pointer
            code += "@SP\n"
            code += "AM=M+1\n"
            self.ostream.write(code)
            return
        
        if command.lower() == "neg":
            code += "// Neg sequence\n"
            #Acquire address
            code += "@SP\n"
            code += "A=M-1\n"
            #Negate memory
            code += "M=-M\n"
            self.ostream.write(code)
            return
        
        if command.lower() == "not":
            code += "// Not sequence\n"
            #Acquire address
            code += "@SP\n"
            code += "A=M-1\n"
            #Invert memory
            code += "M=!M\n"
            self.ostream.write(code)
            return
        
        if command.lower() == "or":
            code += "// Or sequence\n"
            #Decrements the stack pointer and grabs the first operond
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "M=0\n"
            #Decrements the stack pointer and grabs the second operond
            code += "@SP\n"
            code += "AM=M-1\n"
            #Performs logical or
            code += "M=D|M\n"
            #Increments the stack pointer
            code += "@SP\n"
            code += "AM=M+1\n"
            self.ostream.write(code)
            return
            
        if command.lower() == "and":
            code += "// And sequence\n"
            #Decrements the stack pointer and grabs the first operond
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "M=0\n"
            #Decremembers the stack pointer and grabs the second operond
            code += "@SP\n"
            code += "AM=M-1\n"
            #Performs the logical and
            code += "M=M&D\n"
            #Increments the stack pointer
            code += "@SP\n"
            code += "AM=M+1\n"
            self.ostream.write(code)
            return
        
        if command.lower() == "gt":
            code += "// Gt sequence\n"
            #Gets the second operond into D
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            #Clears the stack memory
            code += "M=0\n"
            #Gets the first operond
            code += "@SP\n"
            code += "AM=M-1\n"
            #Subtracts the second operond from the first
            code += "D=M-D\n"
            #Clears the stack memory
            code += "M=0\n"
            #Checks to see if D is greater than 0
            code += "@TRUE" + str(self.i) + "\n"
            code += "D;JGT \n"

            code += "@SP\n"
            code += "A = M\n"
            code += "M = M + 1\n"

            code += "(TRUE" + str(self.i) +")\n"
            code += "@SP\n"
            code += "A = M\n"
            code += "M = M - 1\n"
            code += "@SP\n"
            code += "M = M + 1\n"

            self.i += 1
            self.ostream.write(code)
            return
            
            
        if command.lower() == "eq":
            code += "// Eq sequence\n"
            #Gets the second operond into D
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            #Clears the stack memory
            code += "M=0\n"
            #Gets the first operond
            code += "@SP\n"
            code += "AM=M-1\n"
            #Subtracts the second operond from the first
            code += "D=D-M\n"
            #Clears the stack memory
            code += "M=0\n"
            #Checks to see if D is equal to 0
            code += "@TRUE" + str(self.i) + "\n"
            code += "D;JEQ \n"

            code += "@SP\n"
            code += "A = M\n"
            code += "M = M + 1\n"

            code += "(TRUE" + str(self.i) +")\n"
            code += "@SP\n"
            code += "A = M\n"
            code += "M = M - 1\n"
            code += "@SP\n"
            code += "M = M + 1\n"

            self.i += 1
            self.ostream.write(code)
            return
        
        if command.lower() == "lt":
            code += "// Lt sequence\n"
            #Gets the second operond into D
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            #Clears the stack memory
            code += "M=0\n"
            #Gets the first operond
            code += "@SP\n"
            code += "AM=M-1\n"
            #Subtracts the second operond from the first
            code += "D=M-D\n"
            #Clears the stack memory
            code += "M=0\n"
            #Checks to see if D is less than 0
            code += "@TRUE" + str(self.i) + "\n"
            code += "D;JLT \n"

            code += "@SP\n"
            code += "A = M\n"
            code += "M = M + 1\n"

            code += "(TRUE" + str(self.i) +")\n"
            code += "@SP\n"
            code += "A = M\n"
            code += "M = M - 1\n"
            code += "@SP\n"
            code += "M = M + 1\n"

            self.i += 1
            self.ostream.write(code)
            return
        
    def writePushPop(self, command, segment, index):
        code = ""
        if command.lower() == "c_push":
            code += "// push sequence\n"
            code += "@SP\n"
            code += "D = M\n"
            code += "M = M+1\n"
            code += "@R5\n"
            code += "M = D\n"

            if segment.lower() == "constant":
                code += "@" + index + "\n"
                code += "D = A\n"

            code += "@R5\n"
            code += "A = M\n"
            code += "M = D\n"
        if command.lower() == "c_pop":
            code += "// pop sequence\n"
            code += "@SP\n"
            code += "M = M-1\n"
            code += "A = M\n"
            code += "D = M\n"
            code += "M = 0\n"

            if segment.lower() == "":
               code += "ERROR"
 
        self.ostream.write(code)
        return
