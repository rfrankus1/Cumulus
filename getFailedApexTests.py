'''
Created on May 1, 2017

@author: rfrankus
'''
import pandas as pd
import numpy as np
import time
import sys, getopt
import json
from pandas.io.json import json_normalize
import os.path

inputfile = "apexTestResult-SteelBricks-04-30-17.csv"
resultfile = "result.csv"

def setCliParameters():
    # Get CLI arguments
    try:
        # Parse CLI arguments
        opts, args = getopt.getopt(sys.argv[1:], 'hi:r:', ['help','inputfile','resultfile'])
    except getopt.GetoptError:
        print 'compareApexResults.py -i <inputfile> -r <resultfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
                print 'compareApexResults.py -i <inputfile> -r <resultfile>'
                sys.exit()
        elif opt in ("-i", "--inputfile"):
                global inputfile
                inputfile = arg
        elif opt in ("-r", "--resultfile"):
                global resultfile
                resultfile = arg

# Add Stylesheet to table
def ApplyGenericCSS(InputFile, CSSFile):

    with open(CSSFile,'r') as f:    
        newlines = []
    
        for line in f.readlines():
            newlines.append(line)
        
        f.close()
    
    newlines.append(InputFile.replace('class="dataframe"','class="GenericTable"'))   

    for line in newlines:
        print line 

# Get command line parameters        
setCliParameters()

try:
    if os.path.exists(inputfile):
        df1=pd.read_csv(inputfile)
    else:
        print 'Input File not found'
        sys.exit(1)
    
    # Filter rows that have failed on SDB or Oracle
    df1 = df1[(df1.Outcome == 'Fail')]
    #print "Filtered Joined Input Size:",df3.shape
    
    # Get subset of columns
    df2 = df1[['JobDate','ClassName','MethodName','Outcome','Message','StackTrace']]
    # Set is_copy = false to avoid warning
    df2.is_copy = False
    print "Export File Size:",df2.shape
    pd.set_option('display.max_colwidth', -1)
    # Export result as CSV
    df2.to_csv(resultfile, encoding='utf-8')
    # Marker for Jenkins to parse out content
    print 'start-here\n'
    # Create HTML table 
    htmlTable = df2.to_html();
    # Add stylesheet, doesn't work on Gmail right now
    ApplyGenericCSS(htmlTable,"table.css")
    # Marker for Jenkins to parse out content
    print 'end-here\n' 
    
except OSError as err:
    print("OS error: {0}".format(err))