#!/usr/bin/env python
#-*- coding: utf-8 -*-
import csv

DataList = []

with open('dataset/n100m5_1.dat', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        for item in row:
            DataList.append(item.rstrip().split(   ))

print(DataList)
nbValeurs = DataList[0][0]
nbContraintes = DataList[0][1]
