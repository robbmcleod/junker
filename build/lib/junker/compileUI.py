# -*- coding: utf-8 -*-
"""
Compilation script for any Qt UI files generated by Qt designer


Created on Tues Feb 18 2014

@author: Robert A. McLeod
"""
import os, os.path, glob, re
####################### BUILDING PYSIDE FROM GIT
#http://pyside.readthedocs.org/en/latest/building/linux.html
#######################
#from PySide import QtUiTools, QtCore
#import pysideuic

my_path = os.path.dirname(__file__)


uiList = glob.glob( "*.ui" )
for ui in uiList:
#    file = QtCore.QFile( ui)
#    file.open(QtCore.QFile.ReadOnly)
#    loader.load(file)
#    file.close()
    uiFront, _ = os.path.splitext( ui )
    os.system( "pyside-uic " + ui + " -o " + uiFront + ".py" )

#import PyQt4.uic as qu
#
#my_path = os.path.dirname(__file__)
#
#qu.compileUiDir( my_path )


# Below is various buy fixes so that PySide is compatible with both Python 2.7 and 3.4
uiList = glob.glob( "Ui*.py" )


# Absolute_imports
for uiFilename in uiList:
    uiFH = open( uiFilename, 'r' )

    uiLines = uiFH.readlines()
    uiFH.close()
    for J, uiLine in enumerate(uiLines):
        if "from MplCanvas import MplCanvas" in  uiLine:
            uiLines[J] = "from .MplCanvas import MplCanvas\n"
        if "from ViewWidget import ViewWidget" in  uiLine:
            uiLines[J] = "from .ViewWidget import ViewWidget\n"
    uiFH = open( uiFilename, 'w' )
    uiFH.writelines( uiLines )
    uiFH.close()
    
    pass


# Unicode Strings
# I had thought that not using unicode strings in python 2.7 wouldn't align properly with dicts
# using unicode keys.
# This doesn't actually appear to be a problem, python 2.7 to 3.4
#regex_unicode = re.compile( '\".*?\"' )
#def toUnicode( match ):
#
#    unicode_repr = "u" + match.group()
#    print( "In: %s |||| Out: %s" %( match.group(), unicode_repr ) )
#    return unicode_repr
#    
#for uiFilename in uiList:
#    uiFH = open( uiFilename, 'r' )
#    uiText = uiFH.read()
#    uiFH.close()
#    
#    # Unicode_strings
#    newText = regex_unicode.sub( toUnicode, uiText )
#    uiFH = open( uiFilename, 'w' )
#    uiFH.writelines( newText )
#    uiFH.close()