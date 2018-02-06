#!/usr/bin/env python
# -*- coding:utf8 -*-
import numpy as np

def load_mnist(mnist_dir):
    trainData = []
    with open(mnist_dir + "/train-data-1") as infile:
        for line in infile.readlines():
            line = line.strip()
            trainData.append([float(s) for s in line.split('\t')])
    with open(mnist_dir + "/train-data-2") as infile:
        for line in infile.readlines():
            line = line.strip()
            trainData.append([float(s) for s in line.split('\t')])

    trainLabel = []
    with open(mnist_dir + "/train-label") as infile:
        for line in infile.readlines():
            line = line.strip()
            trainLabel.append([float(s) for s in line.split('\t')])

    testData = []
    with open(mnist_dir + "/test-data") as infile:
        for line in infile.readlines():
            line = line.strip()
            testData.append([float(s) for s in line.split('\t')])

    testLabel = []
    with open(mnist_dir + "/test-label") as infile:
        for line in infile.readlines():
            line = line.strip()
            testLabel.append([float(s) for s in line.split('\t')])

    return {"train-data": np.array(trainData),
            "train-label": np.array(trainLabel),
            "test-data": np.array(testData),
            "test-label": np.array(testLabel)}

def load_iris(iris_dir):
    data = []
    with open(iris_dir + "/data") as infile:
        for line in infile.readlines():
            line = line.strip()
            data.append([float(s) for s in line.split('\t')])
    label = []
    with open(iris_dir + "/target") as infile:
        for line in infile.readlines():
            line = line.strip()
            label.append([float(s) for s in line.split('\t')])
    return {"data":np.array(data),"label":np.array(label)}

def load_leukemia(leukemia_dir):
    data = []
    with open(leukemia_dir + "/data") as infile:
        for line in infile.readlines():
            line = line.strip()
            data.append([float(s) for s in line.split('\t')])
    label = []
    with open(leukemia_dir + "/target") as infile:
        for line in infile.readlines():
            line = line.strip()
            label.append([float(s) for s in line.split('\t')])
    return {"data":np.array(data),"label":np.array(label)}


