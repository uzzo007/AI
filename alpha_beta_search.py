def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Base case: when we reach the maximum depth
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        maxEval = float('-inf')
        for i in range(2):
            eval = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return maxEval
    else:
        minEval = float('inf')
        for i in range(2):
            eval = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return minEval

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    optimal_value = minimax(0, 0, True, values, float('-inf'), float('inf'))
    print("The optimal value is:", optimal_value)
