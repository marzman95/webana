# Description of the algorithm and more
Keep in mind that is works like a greedy algorithm, but also looks for more possible results (more attributes or better probability). It continues based on the best probability found until now and tries to predict the next probabilities and if that is better, use that better one.

1. Setup (*lines __1-3__*)
2. Repeat until we have had every level
  1. Setup empty recursion-'path'
  2. Do as long as we have possible (good) new attributes (candidates) (*line __6__*):
    1. Subprocedure `n` (*line __8__*):
        1. For all attributes *a* add to result: *a* __is equal__ and *a* __is not equal__ to a value
    2. For every other description do (*line __9__*):
        1. Check quality
        2. Test conditions:
          - Yes: Those descriptions are good results, so add them to the resulting set with their quality
          and add to beam (other good candidates)
          - No: continue
      3. Take out the good attributes and add it to the candidates (*line __14-15__*)
