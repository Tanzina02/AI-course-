import math

def minimax(depth, index, is_max, scores, max_depth):
    if depth == max_depth:
        return scores[index]
    if is_max:
        
        left = minimax(depth+1, index*2, False, scores, max_depth)
        right = minimax(depth+1, index*2+1, False, scores, max_depth)
        return max(left,right)
      
    else:
        
        left = minimax(depth+1, index*2, True, scores, max_depth)
        right = minimax(depth+1, index*2+1, True, scores, max_depth)
        return min(left,right)
        

n = int(input("Number of leaf nodes: "))
scores = [int(x) for x in input().split()]

if len(scores) != n:
    print("Number of scores must match leaf nodes")
else:
    max_depth = int(math.log2(n))
    best = minimax(0, 0, True, scores, max_depth)
    print("Leaf nodes:", scores)
    print("Optimal value (Minimax result):", best)
