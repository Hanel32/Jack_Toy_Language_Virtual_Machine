# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:10:18 2017

@author: Carson Hanel
"""
import sys 
from Parser     import Parser
from CodeWriter import CodeWriter

class Main():
    
    #call file reader with command line argument
    #match per-line output with dictionary
    #create assembly per-line output
    def __init__(self, filename):
        self.parser   = Parser(filename)
        self.writer   = CodeWriter(filename)
        self.Main()        
        
    def Main(self):
        while(self.parser.hasMoreCommands()):
            self.parser.advance()
            if self.parser.commandType() == "C_ARITHMETIC":
                command = self.parser.currcmd
                command = command.split()
                self.writer.writeArithmetic(command[0])
            else:
                command = self.parser.commandType()
                segment = self.parser.arg1()
                index   = self.parser.arg2()
                self.writer.writePushPop(command, segment, index)

Main(sys.argv[1])
