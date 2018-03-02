# -*- coding:utf-8 -*-
__author__ = 'jql'

import os,sys
# sys.path.append("..")
from tmp.People import *
# import tmp.People

def test():
    dictTest=dict()
    dictTest["aa"]="sdjf"

    setTest=set()
    setTest.add("sljdf")
    print(setTest)

def main():
    myPeople=People("jing")
    myPeople.printInfo()
    # print(sys.path)

def justTest():
    print("jsldjflsjdfsljflsdjfljsdlf")

if __name__ == "__main__":
    print("main")
    # print "sdljf"
    main()







