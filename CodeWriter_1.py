# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:01:53 2017

@author: Carson Hanel
@author: Max Loeffler
"""
from Parser.py import Parser

class CodeWriter():
    def __init__(self, filename):
        self.filename = filename.replace("vm", "asm")
        self.ostream  = io.open(self.filename, mode = 'w')
        self.i        = 0  
        
    def setFileName(self, filename):
        self.ostream.close()
        self.filename     = filename.replace("vm", "asm")
        self.ostream = open(self.filename, mode = 'w')
        
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
            code += "M=D+M"
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
            #Decrement the stack pointer
            code += "@SP\n"
            code += "AM=M-1\n"
            #Negate memory
            code += "M=-M\n"
            #Increments the stack pointer
            code += "@SP\n"
            code += "AM=M+1\n"
            self.ostream.write(code)
            return
        
        if command.lower() == "not":
            code += "// Not sequence\n"
            #Decrement the stack pointer
            code += "@SP\n"
            code += "AM=M-1\n"
            #Invert memory
            code += "M=!M\n"
            #Increments the stack pointer
            code += "@SP\n"
            code += "AM=M+1\n"
            self.ostream.write(code)
            return
        
        if command.lower() == "or":
            code += "// Or sequence\n"
            #Decrements the stack pointer and grabs the first operond
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
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
            #Checks to see if D is greater than 0 (true)
            code += "@TRUE" + self.i + "\n"
            code += "D;JGT\n"
            #If D isn't greater, sets SP's M to 0.
            code += "@SP\n"
            code += "A=M\n" #Replaces
            code += "M=0\n" #Above
            '''
            TODO:
            
            #Otherwise, in the true section:
            #  Should set return to (true), and increment SP.
            code += "(TRUE" + self.i + ")\n"
            code += "D=D-1\n"
            code += "D;JGT"
            code += "D=D+1"
            code += "@SP\n"
            code += "A=M\n"
            code += "M=D\n"
            '''
            #regardless, need to increment SP
            code += "@SP\n"
            code += "M=M+1\n"
            self.i += 1
            return code
            
        if command.lower() == "eq":
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
            '''
            TODO:
                
            #Checks to see if D is equal to 0 (true)
            code += "@TRUE" + self.i + "\n"
            code += "D;JEQ\n"
            code += "@SP\n"
            code += "A=M\n"
            code += "M=0\n"
            code += "(TRUE" + self.i +")\n"
            '''
            
            #regardless, need to increment SP
            code += "@SP\n"
            code += "M=M+1\n"
            self.i += 1
            return code
        
        if command.lower() == "lt":
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
            #Checks to see if D is less than 0 (true)
            code += "@TRUE" + self.i + "\n"
            code += "D;JLT\n"
            #If D isn't less, sets SP's M to 0.
            code += "@SP\n"
            code += "A=M\n" #Replaces
            code += "M=0\n" #Above
            '''
            TODO:
                
            #Checks to see if D is equal to 0 (true)
            code += "@TRUE" + self.i + "\n"
            code += "D;JEQ\n"
            code += "@SP\n"
            code += "A=M\n"
            code += "M=0\n"
            code += "(TRUE" + self.i +")\n"
            '''
            
            #regardless, need to increment SP
            code += "@SP\n"
            code += "M=M+1\n"
            self.i += 1
            return code
            
        
    def writePushPop(self, command, segment, index):
        
        
    def close(self):
        self.ostream.close()
