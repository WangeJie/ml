#! /usr/bin/env python
# encoding:utf-8

import numpy as np

X_unlabeled_prime = np.arange(30).reshape(10, -1)
# print X_unlabeled_prime,'\n'

# y_unlebeled_prime = np.array([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])

# p=[1,3,4,5]
# n=[2,6,7,9]
# p.extend(n)
# p_n=p

# y_unlebeled_prime[[x for x in p]] = 1

# X_unlabeled_prime=np.delete(X_unlabeled_prime,p,axis=0)

# #print X_unlabeled_prime

# np.vstack((X_labeled, X_unlabeled[uidx, :]))


a = np.array([0.44143048, 0.44556381, 0.39276066, 0.55387896, 0.39276292, 0.68417014,
              0.68417014, 0.39545264, 0.40344773, 0.39762204, 0.52020917, 0.37765359])
print a

p=[]
idx=a.argsort()[-3:][::-1]
print idx
print type(idx)
p.extend(idx)
print p