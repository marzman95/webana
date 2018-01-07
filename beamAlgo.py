import queue
import numpy as np
import pandas as pd
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

filename = 'datas\clicking_data'
c_data = pd.read_csv(filename, header=0, sep="\t") #clicking_data

filename2 = 'datas\meta_data'
m_data = pd.read_csv(filename2, header=0, sep="\t", encoding = "ISO-8859-1") #meta_data

filename3 = 'datas\experiment_details_5'
e_data = pd.read_csv(filename3, header=0) #experiment_details_5

isnumeric = []

selm = m_data.iloc[:,[1,2,3,4,5,6,7,8,12,13,15,16,17,18,19,20,21,22,24,25,26,27,29]]

merge = pd.merge(selm, e_data, on='user_id', suffixes=('_s', '_e'))

merge3 = pd.merge(merge, c_data, left_on='user_id', right_on='user_session', suffixes=('_s', '_c'))

selt = merge3.iloc[:,[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]]


numerictracker = 1
for column in selt:
    if is_string_dtype(selt[column]):
        print(column, "is string")
    else:
        if is_numeric_dtype(selt[column]):
            print(column, "is numeric")
            isnumeric[numerictracker] = column
            numerictracker = numerictracker+1
            print("min:", selt[column].min())
            print("max:", selt[column].max())
    print("")



def beamsearch(w, d, bins)

candidateQueue = queue.Queue() # create fifo queue candidateQueue
resultSet = queue.PriorityQueue(q) # create priority queue resultSet

for level in range(1 , d): # loop
    beam = queue.PriorityQueue(w) # create priority queue beam
    while (canditateQueue.empty() != True): # while fifo queue is not empty
        seed = candidateQueue.get() #get first element and set seed to that element
        #TODO: n(seed) generates set of candidate descriptions for the next level, by discretization
        #   Descritization: devide the domain (1 to n) of values of attribute a
        #   over b <= N bins (N #rows). Per level choose a b, depending on the number of N rows.
        for num in isnumeric:
            if (isnumeric[num] == seed):
    
                minv = df['colname'].min()       # set min
                maxv = df['colname'].max()       # set max
                dif = (minv - maxv) / bins
                setv = []
                for i in range(1, dif):
                    minv = minv+dif
                    setv[i] = minv
            else for # each different answer make a bin        
        # Wikipedia: discretization is the process of transferring continuous functions, models, variables, and equations into discrete counterparts
        #TODO: do we have numeric descriptions/attributes?
        #setv = some function n
        #above one is quite vague, in psuede it says set = n(seed)
        for desc in setv: # for all desc( what is desc) in setv
            quality = #some function y (quality measure)
            # in psuedo above says: quality = y(desc)
            # check all bins for (eenduidigheid) hoeveel informatie geeft een bepaalde bin
            # if not numeric  just check how usefull every group is

            if (): #something, in psuede satisfiesall constraints
                #if in psuedo (desc.satisfiesall(c)) so if desc satisfies al constraints

                #TODO: see slide 3A-15: "A quality measure for Subgroup Discovery summarizes the
                #       interestingness of a confusion matrix into a single number." Met Yale-Q?
                resultSet.put(desc.quality()) # set desc.qualityin in result i do not know what i means, but probably because i do not understand desc
                beam.put(desc.quality()) # set desc.quality in beam
    while (beam.empty() != True): # if beam is not empty
        candidateQueue.put(beam.get())
        # in psuedo beam.get_front_element() so not sure if fifo or the highest number like in priority
return resultSet

#TODO: old steps
# Exhaustive/brute-force: just solve for every n
# Greede: solve for the best possible next item, which seems best now
# Beam search: combines those two, beam search solves for multiple best next items
#   and is in the middle between greedy and brute-force. It only searches for
#   next multiple promising branches, and skipping the rest (but not all such as greedy does)

#   Do beamsearch
#   @param w: integer that defines a search width
#   @param d: integer that defines a search depth
#   @param bins: integer that defines the number of bins (as described by the HWA)
#   @returns set of q subgroups, a sultion with a top-q subgroup discovery task

def beamsearch(w, d, bins)

    # 1:        Generate all patterns consisting of one condition on one attribute.
    #               Evaluate them with [phi]; save the w best as the beam.
    # 2 (i+2):  Generate new candidate patterns by refining patterns from the
    #           i^th level beam. A pattern is refined into many new candidates,
    #           by conjoining each possible single condition on a single attribute.
    #               Evaluate all i+1 candidates with [phi]; save the w best as the beam.
    #   Terminate after the d^th level.

    # Create subgroups based on one attribute, such as age (increasing); a type (married=yes/no); etc.
    # With a specific subgroup (seed), such as age, evaluate the other attributes (age & married; age & not married)
    #   Repeat for the other seeds

    # Attributes: country/timezone, url/page, browser, device, language, os, referring_page, event (click/view)
    # Use equal-width binding since we need a w


    return result;
