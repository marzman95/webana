import networkx as nx
import csv
import os
import json
import statistics
from random import randint as rd
from networkx import number_of_nodes
from networkx import edges
os.chdir("C:\\Users\\s147356\\Documents\\University\\Year 4\\quartile 2\\web analytics\\assignment 4\\wd")
# load the edge list and create a directed Graph
fh = open("hamster.edgelist", 'rb')
G = nx.read_edgelist(fh,create_using=nx.DiGraph())
fh.close()

rand = rd(1, number_of_nodes(G))
stringrand = str(rand)
print(stringrand)

print(G.edges(stringrand))
#for run in G.edges(stringrand):
      #  print (run)
print(len(G.edges(stringrand)))
randTwo = rd(1, len(G.edges(stringrand)))

counter = 1
for run in G.edges(stringrand):
        if (counter == randTwo):

                print (run)
                print (run[1])
                print (run[0])
                G.remove_edge(run[0],run[1])
                break
        counter = counter +1
newTest = True


'''
# calculate PageRank directly use
# the function from NetworkX
# more details about this function
# can be found 
# https://networkx.github.io/documentation/latest/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html
pr = nx.pagerank(G, alpha=0.85)
# the return value pr is dict in Python
# in whici the keys are the node indices 
# and the values are corresponding PagRank values
#print(pr)
if(newTest):
        with open(os.getcwd()+"/results/result2.txt", 'w') as file:
            file.write(json.dumps(pr))

avg = float(1)/ float(2426)
f = str(avg)
print("average: "+f)
isavg = 0
underavg = 0
aboveavg = 0
minv=1
maxv=0
work = 0;
for key, value in pr.items():
        #print(key, 'corresponds to', value)
        g = str(value)
        a = str(key)+": "+g
        #print(a)
        work = work + value
        if (value < avg):
                underavg = underavg+1
                if (minv > value):
                        minv = value
        elif ( value == avg):
                isavg = isavg+1
        else:
                aboveavg = aboveavg+1
                if (maxv < value):
                        maxv = value

b = str(work)
c = str(isavg)
d = str(underavg)
e = str(aboveavg)
h = str(minv)
i = str(maxv)
print("total: "+b)
print("isavg: "+c)
print("underavg: "+d)
print("aboveavg: "+e)
print("minimum: "+h)
print("maximum: "+i)

onemin = -1
onemax = -1
items = []
for k, l in pr.items():
        items.append(l)
        if(l == minv):
                onemin = onemin +1
        elif(l == maxv):
                onemax = onemax+1

m = str(onemin)
n = str(onemax)
print("oneminimum: "+m)
print("onemaximum: "+n)
o = str(statistics.median(items))
p = str(statistics.median_low(items))
q = str(statistics.median_high(items))
#r = str(statistics.harmonic_median(items))
s = str(statistics.median_grouped(items))
t = str(statistics.mode(items))
u = str(statistics.pstdev(items))
v = str(statistics.pvariance(items))
w = str(statistics.stdev(items))
x = str(statistics.variance(items))
y= str(statistics.StatisticsError(items))

print("median: "+o)
print("low median: "+p)
print("high median: "+q)
#print("harmonic median: "+r) does not work
print("grouped median: "+s)
print("mode: "+t)
print("pstdev: "+u)
print("pvariance: "+v)
print("stdev: "+w)
print("variance: "+x)
#print("error: "+y) too much data, only if actually test

'''
