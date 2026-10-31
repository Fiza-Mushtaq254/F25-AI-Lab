
scores = [3, 5, 2, 9, 0, 0, 0, 7]
treeDepth = 3
count = 0
def minimax(currentDepth, nodeIndex, isMaxTurn):
    global count
    if currentDepth == treeDepth:
        count +=1
        return scores[nodeIndex]
    if isMaxTurn:
        return max(
            minimax(currentDepth + 1, nodeIndex * 2, False),
            minimax(currentDepth + 1, nodeIndex * 2 + 1, False)
            )
    else:
        return min(
            minimax(currentDepth + 1, nodeIndex * 2, True),
            minimax(currentDepth + 1, nodeIndex *2 + 1, True)
            )
minimaxvalue = minimax(0, 0, True)
print("Minimax Value:", minimaxvalue)
print("Minimax Leaf Evaluation:", count)
count = 0
def alpha_beta(currentDepth, nodeIndex, isMaxTurn, alpha, beta):
    global count
    if currentDepth == treeDepth:
        count += 1
        return scores[nodeIndex]
    if isMaxTurn:
        best = float("-inf")
        for i in range(2):
            value = alpha_beta(
                currentDepth + 1,
                nodeIndex * 2 + i,
                False,
                alpha,
                beta
               )
            best = max(best, value)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best
    else:
        best = float("inf")
        for i in range(2):
            value = alpha_beta(
                currentDepth + 1,
                nodeIndex * 2 + i,
                True,
                alpha,
                beta
                )
            best = min(best, value)
            beta =min(beta, best)
            if alpha >= beta:
                break
        return best
alphaBetaValue = alpha_beta(
        0, 0, True,
        float("-inf"),
        float("inf")
        )
print("Alpha-Beta Value:", alphaBetaValue)
print("Alpha-Beta Leaf Evaluation:", count)





