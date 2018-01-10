import networkx as nx
import csv
import os
import json
import statistics
import itertools
from random import randint as rd
from networkx import number_of_nodes
from networkx import number_of_edges
from networkx import edges
os.chdir("C:\\Users\\s147356\\Documents\\University\\Year 4\\quartile 2\\web analytics\\assignment 4\\wd")
# load the edge list and create a directed Graph
fh = open("hamster.edgelist", 'rb')
G = nx.read_edgelist(fh,create_using=nx.DiGraph())
Ginit = G
Gtest = G
GtestTwo = G
fh.close()
extTest = False
manualtest = True
if(G != Ginit):
        Ginit = G
elif (G != Gtest):
        Gtest = G
elif (G != GtestTwo):
        GtestTwo = G

#for dyna in G.edges():
     #   Gtest.remove_edge(dyna[0], dyna[1])
      #  for do in Gtest.edges():
                


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


 



#calculations function
def doCalc(G, counter, results):
        pr = nx.pagerank(G, alpha=0.85)
        avg = float(1)/ float(number_of_nodes(G))
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

        onemin = 0
        onemax = 0
        items = []
        for k, l in pr.items():
                items.append(l)
                if(l == minv):
                        onemin = onemin +1
                elif(l == maxv):
                        onemax = onemax+1

        m = str(onemin)
        n = str(onemax)
        b = str(work)
        c = str(isavg)
        d = str(underavg)
        e = str(aboveavg)
        h = str(minv)
        i = str(maxv)
        f = str(avg)
        o = str(statistics.median(items))
        p = str(statistics.median_low(items))
        q = str(statistics.median_high(items))
        s = str(statistics.median_grouped(items))
        t = str(statistics.mode(items))
        u = str(statistics.pstdev(items))
        v = str(statistics.pvariance(items))
        w = str(statistics.stdev(items))
        x = str(statistics.variance(items))
        y= str(statistics.StatisticsError(items))
        if(os.stat(os.getcwd()+"/results/testResults"+str(counter)+".txt").st_size >= 5000000):
                results.close()
                counter= counter +1
                results = open(os.getcwd()+"/results/testResults"+str(counter)+".txt", 'w')
                print(counter)
        results.write('\n')
        results.write('testdata \n')
        results.write(json.dumps(pr)+'\n')
        results.write("average: "+f+'\n')
        results.write("total: "+b+'\n')
        results.write("isavg: "+c+'\n')
        results.write("underavg: "+d+'\n')
        results.write("aboveavg: "+e+'\n')
        results.write("minimum: "+h+'\n')
        results.write("maximum: "+i+'\n')
        results.write("nrminimum: "+m+'\n')
        results.write("nrmaximum: "+n+'\n')
        results.write("median: "+o+'\n')
        results.write("low median: "+p+'\n')
        results.write("high median: "+q+'\n')
        results.write("grouped median: "+s+'\n')
        results.write("mode: "+t+'\n')
        results.write("pstdev: "+u+'\n')
        results.write("pvariance: "+v+'\n')
        results.write("stdev: "+w+'\n')
        results.write("variance: "+x+'\n')
        results.write("error: "+y+'\n') # too much data, only if actually test
        print("succes writing to test "+str(counter) +" result")
        return counter, results


### function to find all possible edge matches
def findMatches(G, counter, results):
        counter = 0
        for L in range(1, number_of_edges(G)+1):
                text = str(counter)
                loc = os.getcwd()+"/results/comb"+text+".txt"
                comb = open(os.getcwd()+"/results/comb"+text+".txt", 'w')
                for subset in itertools.combinations(G.edges(),L):
                        comb.write(str(subset)+'\n')
                        if(os.stat(os.getcwd()+"/results/comb"+text+".txt").st_size >= 500000):
                                comb.close()
                                info = delEdge(G, loc, counter, results)
                                counter = info[0]
                                results = info[1]
                                comb = open(os.getcwd()+"/results/comb"+text+".txt", 'w')
                                
                comb.close()
                info = delEdge(G, loc, counter, results)
                counter = info[0]
                results = info[1]
        return counter, results




### function to delete edges from graph
def delEdge(G, loc, counter, results):
        comb = open(loc, 'r')
        for line in comb:
                if (len(line.split()) > 1):
                        wordOne = line.split()[0]
                        wordOne = wordOne[3:]
                        wordOne = wordOne[:-2]
                        wordTwo = line.split()[1]
                        wordTwo = wordTwo[:-4]
                        wordTwo = wordTwo[1:]
                        print("word 1: "+ wordOne)
                        print("word 2: "+ wordTwo)
                        G.remove_edge(wordOne, wordTwo)
                        info = doCalc(G, counter, results)
                        counter = info[0]
                        results = info[1]
                        print("succes")
                        
        comb.close()
        return counter, results
                


                
### new test recursively check all needed data
'''
G = nx.read_edgelist(fh,create_using=nx.DiGraph())
Ginit = nx.read_edgelist(fh,create_using=nx.DiGraph())
Gtest = nx.read_edgelist(fh,create_using=nx.DiGraph())
GtestTwo = nx.read_edgelist(fh,create_using=nx.DiGraph())
pr = nx.pagerank(G, alpha=0.85)
'''
if extTest:
        counter = 0
        results = open(os.getcwd()+"/results/testResults"+str(counter)+".txt", 'w')
        
        findMatches(G, counter, results)
        results.close()
        '''
        print("starting loop")
        counter = 1
        while (True):
                print('in while')
                print(Gtest[str(counter)][1])
               # if():
        results = open(os.getcwd()+"/results/testresults.txt", 'w')
        print("loop")
        for dyna in G.edges():
                Gtest.remove_edge(dyna[0], dyna[1])
                doCalc(Gtest, results, str(dyna), '')
                for do in G.edges():
                        if(dyna != do):
                                Gtest.remove_edge(do[0], do[1])
                                doCalc(Gtest, results, str(dyna), str(do))
                        #Gtest.add_edge(do[0], do[1])
                #Gtest.add_edge(dyna[0], dyna[1])
                Gtest = G
        results.close()
        '''
def mandelete(G, n, singles):
        counter = 0
        results = open(os.getcwd()+"/results/testResults"+str(counter)+".txt", 'w')
        while(n >= 0):
                #print(n)
                #print("number of nodes: "+str(number_of_nodes(G)))
                rand = rd(1, number_of_nodes(G))
                stringrand = str(rand)
                #print(G.edges(stringrand))
                #print(len(G.edges(stringrand)))
                while (len(G.edges(stringrand)) < 1):
                        rand = rd(1, number_of_nodes(G))
                        stringrand = str(rand)
                #print(stringrand)

              #  print(G.edges(stringrand))
                #for run in G.edges(stringrand):
                #  print (run)
                #print(len(G.edges(stringrand)))
                if( len(G.edges(stringrand))-1 >  0):
                        randTwo = rd(0, len(G.edges(stringrand))-1)
                else:
                        randTwo = 0
                inc = 0
                for run in G.edges(stringrand):
                        if (inc == randTwo):
                                G.remove_edge(run[0],run[1])
                                
                                
                                if (singles):
                                        info = doCalc(G, counter ,results )
                                        counter = info[0]
                                        results = info[1]
                                        G.add_edge(run[0],run[1])
                                        
                                break
                        inc = inc +1
               # print(n)
                n = n-1
        info = doCalc(G, counter ,results )
        counter = info[0]
        results = info[1]
        results.close()

def mandelnode(G, n, singles):
        counter = 0
        results = open(os.getcwd()+"/results/testResults"+str(counter)+".txt", 'w')
        while(n >= 0):
                
                found = False
                while not found:
                        rand = rd(1, 2426)
                        stringrand = str(rand)
                        for node in G.nodes():
                                if(node == stringrand):
                                        G.remove_node(stringrand)
                                        found = True
                                        break;

                if (singles):
                        info = doCalc(G, counter ,results )
                        counter = info[0]
                        results = info[1]
                        G = Ginit
                
               
               # print(n)
                n = n-1
        info = doCalc(G, counter ,results )
        counter = info[0]
        results = info[1]
        results.close()

def statdeledge(G, stat, singles, n):
        counter = 0
        results = open(os.getcwd()+"/results/testResults"+str(counter)+".txt", 'w')
        minv = min(stat)
        maxv = max(stat)
        minlist = []
        maxlist = []
        min1list = []
        min2list = []
        min3list = []
        betweenlist = []
        for num in range (0,len(stat)):
                if(stat[num] == minv):
                        minlist.append(num)
                elif stat[num] == maxv:
                        maxlist.append(num)
                elif stat[num] == minv+1:
                        min1list.append(num)
                elif stat[num] == minv+2:
                        min2list.append(num)
                elif stat[num] == minv+3:
                        min3list.append(num)
                elif stat[num] > minv+2 & stat[num] < maxv:
                        betweenlist.append(num)
                        
        
        while(n >= 0):
                if len(minlist)-1  == 1: 
                        minlist = min1list
                        min1list = min2list
                        min2list = min3list
                        min3list = betweenlist
                if len(minlist)-1 > 1:
                        rand = rd(1, len(minlist)-1)
                else:
                        rand = 1
                dele = minlist[rand]
                minlist.pop(rand)
                G.remove_node(str(dele));
                if(singles):
                        info = doCalc(G, counter ,results )
                        counter = info[0]
                        results = info[1]
                        G=Ginit
                n = n-1
        info = doCalc(G, counter ,results )
        counter = info[0]
        results = info[1]
        results.close()
        
if (manualtest):
        #mandelete(G, 10000, False)
        #mandelnode(G, 2000, False)
        outdegreelist = []
        for num in range (0, number_of_nodes(G)-1):
                outdegreelist.append(len(G.edges(str(num))))
        statdeledge(G, outdegreelist, False, 2000)
