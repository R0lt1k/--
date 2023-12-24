def min_money_to_take(N, costs):

    costs.sort(reverse=True)

    total_cost = costs[0] + costs[1]
    
    return total_cost

N = int(input())
costs = list(map(int, input().split()))

result = min_money_to_take(N, costs)

print(result)
