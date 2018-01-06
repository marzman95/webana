import queue

candidateQueue = queue.Queue() # create fifo queue candidateQueue
resultSet = queue.PriorityQueue(q) # create priority queue resultSet

for level in range(1 , d): # loop
    beam = queue.PriorityQueue(w) # create priority queue beam
    while (canditateQueue.empty() != True): # while fifo queue is not empty
        seed = candidateQueue.get() #get first element and set seed to that element
        setv = #some function n (refinement-operator n(seed), so probably some optimization, see 4.1)
        #above one is quite vague, in psuede it says set = n(seed)
        for desc in setv: # for all desc( what is desc) in setv
            quality = #some function y (quality measure)
            # in psuedo above says: quality = y(desc)

            if (): #something, in psuede satisfiesall constraints
                #if in psuedo (desc.satisfiesall(c)) so if desc satisfies al constraints

                resultSet.put(desc.quality()) # set desc.qualityin in result i do not know what i means, but probably because i do not understand desc
                beam.put(desc.quality()) # set desc.quality in beam
    while (beam.empty() != True): # if beam is not empty
        candidateQueue.put(beam.get())
        # in psuedo beam.get_front_element() so not sure if fifo or the highest number like in priority
return resultSet


# Exhaustive/brute-force: just solve for every n
# Greede: solve for the best possible next item, which seems best now
# Beam search: combines those two, beam search solves for multiple best next items
#   and is in the middle between greedy and brute-force. It only searches for
#   next multiple promising branches, and skipping the rest (but not all such as greedy does)
def beamsearch(w, d)

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
    return result;
