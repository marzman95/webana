def beamsearch(w, d)
    # Exhaustive/brute-force: just solve for every n
    # Greede: solve for the best possible next item, which seems best now
    # Beam search: combines those two, beam search solves for multiple best next items
    #   and is in the middle between greedy and brute-force. It only searches for
    #   next multiple promising branches, and skipping the rest (but not all such as greedy does)
    return result;
