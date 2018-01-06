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
