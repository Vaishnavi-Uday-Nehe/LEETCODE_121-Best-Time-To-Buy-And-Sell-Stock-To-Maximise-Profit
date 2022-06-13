import math
def stock(arr):
    max_profit = 0
    curr_index = arr[0]

    for i in range(0,size):

        curr_index = min(curr_index,arr[i])
        profit = arr[i] - curr_index
        max_profit = max(max_profit,profit)
        i+=1

    return max_profit

arr = [5,2,6,1,4]
size = len(arr)
print(stock(arr))
