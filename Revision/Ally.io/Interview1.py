#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumLearning' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY iv
#  2. INTEGER_ARRAY articles
#  3. INTEGER p
#

def maximumLearning(iv, articles, p):
    # Write your code here
    """ 
    Use dynamic programing
    weight and capacity concept
    """
    articles = [i * 2 for i in articles]
    matrix = [[[0,0] for col in range(len(iv) + 1)] for row in range(len(articles) + 1)]

    # After getting matrix initialized
    maxScoreAuthorCanGet = -float('inf')
    for articleIDX in range(1, len(matrix)):
        for ivIDx in range(1, len(matrix[0])):
            curArticalPage = articles[articleIDX - 1]
            curIVScore = iv[ivIDx - 1]
            
            maxIdx = None
            maxIvScore = -float('inf')
            maxPage = None
            for i in range(ivIDx):
                iPage, iScore = matrix[articleIDX - 1][i]
                newCurPages = iPage + curArticalPage    
                newCurScore = iScore + curIVScore
                if newCurPages > p:
                    continue
                if newCurScore > maxIvScore:
                    maxIvScore = newCurScore
                    maxPage = newCurPages
                    maxIdx = i
            
            matrix[articleIDX][ivIDx] = [maxPage, maxIvScore]
            maxScoreAuthorCanGet = max(maxScoreAuthorCanGet, maxIvScore)
            
    return maxScoreAuthorCanGet
    
    
print(maximumLearning([3,2,2], [3,2,2], 9))