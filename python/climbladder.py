import math
import os
import random
import re
import sys

def binarysearch(scores, element, start, end):
    rank = 0
    #print start, end, (start + ((end - start) / 2)), element, scores
    print start, end, (start + ((end - start) / 2)), element

    if start <= end:
        mid = start + ((end - start) / 2)
        if scores[mid] == element:
            rank = mid + 1
        elif element < scores[mid]:
            print "bottom half"
            if end < mid+1:
                print "end < mid+1"
                rank = start + 2
                return rank
            rank = binarysearch(scores, element, mid+1, end)
        elif element > scores[mid]:
            print "top half"
            if mid-1 < start:
                print "mid-1 < start"
                rank = start + 1
                return rank
            rank = binarysearch(scores, element, start, mid-1)
    else:
        print "rank = -1"
        rank = end
    return rank

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores = list(dict.fromkeys(scores))
    scores.sort(reverse=True)
    maxscore = scores[0]
    minscore = scores[len(scores)-1]
    lastrank = len(scores)
    midrank = lastrank/2
    ranks = []
    for j in range(0, len(alice)):
        rank = 0
        if alice[j] >= maxscore:
            rank = 1
        elif alice[j] < minscore:
            rank = lastrank + 1
        elif alice[j] == minscore:
            rank = lastrank
        else:
            rank = binarysearch(scores, alice[j], 0, lastrank-1)
        print rank
        ranks.append(rank)
    return ranks


fh = open("files/romeo.txt")

count = 0
results = []
for line in fh:
    #print line
    if count == 0:
        scores_count = int(line)
    if count == 1:
        scores = map(int, line.rstrip().split())
    if count == 2:
        alice_count = int(line)
    if count == 3:
        alice = map(int, line.rstrip().split())
    count = count + 1
result = climbingLeaderboard(scores, alice)
print results
