# YOUR CODE HERE
def get_input(n):
    lst1 = [int(input())for _ in range(n)]
    lst2 = [int(input())for _ in range(n)]
    
    update_list = [lst1[i]+lst2[i] for i in range(n)]
    return update_list
def min_max(result):
    return (min(result),max(result))
result = get_input(int(input()))
min_maxupdate = min_max(result)
print(f"{result}\n{min_maxupdate}")
