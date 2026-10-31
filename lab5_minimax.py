import math
scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))
scores += [0] * (2**treeDepth - len(scores))
def minimax(currentDepth, nodeIndex, isMaxTurn):
    if currentDepth == treeDepth:
        return scores[nodeIndex]
    if isMaxTurn:
        return max(
            minimax(currentDepth + 1, nodeIndex * 2, False),
            minimax(currentDepth + 1, nodeIndex *2 + 1, False)
        )
    return min(
        minimax(currentDepth + 1, nodeIndex * 2, True),
        minimax(currentDepth + 1, nodeIndex * 2 + 1, True)
        )
print("optimal value:", minimax(0, 0, True))

