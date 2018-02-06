#!/usr/bin/env python
# -*- coding:utf8 -*-
import numpy as np
def load_mnist():
    trainData = []
    with open("./mnist/train-data-1") as infile:
        for line in infile.readlines():
            line = line.strip()
            trainData.append([float(s) for s in line.split('\t')])
    with open("./mnist/train-data-2") as infile:
        for line in infile.readlines():
            line = line.strip()
            trainData.append([float(s) for s in line.split('\t')])
    return np.array(trainData)

