# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:02:35 2016

@author: Administrator
"""

#coding=utf-8
from numpy import *
#创建一个带有所有单词的列表
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)
    
def setOfWords2Vec(vocabList, inputSet):
    retVocabList = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            retVocabList[vocabList.index(word)] = 1
        else:
            print 'word ',word ,'not in dict'
    return retVocabList

#另一种模型    
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def trainNB0(trainMatrix,trainCatergory):
    numTrainDoc = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCatergory)/float(numTrainDoc)
    #防止多个概率的成绩当中的一个为0
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDoc):
        if trainCatergory[i] == 1:
            p1Num +=trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num +=trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)#处于精度的考虑，否则很可能到限归零
    p0Vect = log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive
    
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)    #element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    return p0,p1
    #if p1 > p0:
        #return 1
    #else: 
        #return 0

#************主程序***************************************************************
#训练语料
listOPosts=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
#语料的标签                 
listClasses = [0,1,0,1,0,1]    #1 is abusive, 0 not
#词表生成
myVocabList = createVocabList(listOPosts)
#生成文本向量
trainMat=[]
for postinDoc in listOPosts:
    trainMat.append(setOfWords2Vec(myVocabList, postinDoc))#主要是生成文本向量，布尔权重
#训练
p0V,p1V,pAb = trainNB0(array(trainMat),array(listClasses))
#测试文本向量化
testEntry =[['love', 'my', 'dalmation'],['stupid', 'garbage']]
testMat=[]
for temp in testEntry:
    testMat.append(setOfWords2Vec(myVocabList, temp))
thisDocs=array(testMat)
#测试
i=0
for thisDoc in thisDocs:
    p0,p1=classifyNB(thisDoc,p0V,p1V,pAb)
    if p0>p1:
       print testEntry[i],'classified as: ',0,p0,p1
       print '************************************'
       i+=1
    else:
       print testEntry[i],'classified as: ',1,p0,p1 
       print '************************************'
       i+=1
           







#if p0>p1:
    #print testEntry,'classified as: ',0,p0,p1
#else:
    #print testEntry,'classified as: ',1,p0,p1
      

#testEntry = ['stupid', 'garbage']
#thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
#p0,p1=classifyNB(thisDoc,p0V,p1V,pAb)
#if p0>p1:
    #print testEntry,'classified as: ',0,p0,p1
#else:
    #print testEntry,'classified as: ',1,p0,p1


