import numpy as np
import random
dim = input("Enter dimension : ")
n = input("size of data : ")
print(n)
#print(type(n))
 
data = np.random.rand(int(n),int(dim))
 
print("Input data is : ")
for i in range(int(n)):
    print(data[i])
def distance(inp, c, ngroups, dim):
    dif = np.zeros((ngroups, dim))
    for i in range(ngroups):
        dif[i] = inp - c[i]
    dif = np.square(dif)
    sc = np.sum(dif, axis =1)
    rt=np.sqrt(sc)
    return rt
 
 
nn = int(n) #size of data
indexset = set(np.arange(nn))
print(indexset)
ngroups = int(input("no of groups : "))
groupsize = int(nn/ngroups)
groups = []
C = np.zeros((ngroups, int(dim)))
for i in range(ngroups):
    s = set(random.sample(indexset,groupsize))
    groups.append(s)
    for e in s:
        print(e)
        C[i] += data[e]
    C[i] = C[i]/groupsize
    print(C[i])        
    indexset -= s
 
input_pattern = data = np.random.rand(1,int(dim)) 
dist = distance(input_pattern, C, ngroups, int(dim))
gamma = 0.7
max = -10000
i = 0
maxi = -1
score = np.zeros((ngroups,1))
for d in dist :
    if(gamma*d > 1):
        score[i] = 0
    else :
        score[i] = 1 - gamma*d
    if(score[i]>max):
        max = score[i]
        maxi = i
    i += 1
print("input pattern matches to prototype number : ")
print(maxi+1)
