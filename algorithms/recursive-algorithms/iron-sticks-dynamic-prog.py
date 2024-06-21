def getBestCut(stick_length, prices, memo):
    if stick_length == 0:
        return 0
    if memo[stick_length] != -1:
        return memo[stick_length]
    best_value = 0
    for i in range(1, stick_length+1):
        value = prices[i] + getBestCut(stick_length-i, prices, memo)
        if value > best_value:
            best_value = value

    memo[stick_length] = best_value
    return best_value


stick_length = 6    
prices = [0, 1, 5, 8, 9, 10, 17, 17, 24, 30]
memo = [-1 for i in range(stick_length+1)]

print(getBestCut(stick_length, prices, memo))
