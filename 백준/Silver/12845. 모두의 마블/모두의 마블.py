n = int(input())
li = list(map(int, input().split()))
print(sum(li) - max(li) + max(li)*(len(li)-1))