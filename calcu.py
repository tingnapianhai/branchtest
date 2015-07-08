# -*- coding: utf-8 -*-
import numpy
import csv

'''
wo...
strnum = raw_input("Enter the data number: ")

    print datalist[i]
'''

def ave(dlist):
    '''average of list'''
    return numpy.average(dlist)

def variance(dlist):
    '''variance of the list'''
    return numpy.var(dlist)

def std(dlist):
    '''standard deviation'''
    return numpy.std(dlist)

def getCsvData(path = 'data/data.csv'):
    with open(path,'rb') as file:
        contents = csv.reader(file)
        matrix = list()
        for row in contents: # 'for' should be inside 'with'
            matrix.append(row)
        return matrix

def anaData(matrix):
    datalist = list()
    for i in range(len(matrix)):
        datalist.insert(i,float(matrix[i][0]))
    return datalist

dlist = getCsvData('data/data.csv')
datalist = anaData(dlist)
print "(1) length is: " + str(len(datalist))
print "(2) average is: " + str(ave(datalist))
print "(3) variance is: " + str(variance(datalist))
print "(4) standard deviation is: " + str(std(datalist))
str1 = raw_input("Press Enter to close")
