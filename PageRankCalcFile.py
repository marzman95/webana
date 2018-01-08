import networkx as nx
import csv
import os
import json 
os.chdir("C:\\Users\\s147356\\Documents\\University\\Year 4\\quartile 2\\web analytics\\assignment 4\\wd")
# load the edge list and create a directed Graph
fh = open("hamster.edgelist", 'rb')
G = nx.read_edgelist(fh,create_using=nx.DiGraph())
fh.close()

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

with open(os.getcwd()+"/results/result.txt", 'w') as file:
    file.write(json.dumps(pr))

work = 0;
for key, value in pr.items():
        #print(key, 'corresponds to', value)
        a = str(key)+": "+str(value)
        #print(a)
        work = work + value
        print(work)
