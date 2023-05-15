n = int(input())
li = list(map(int, input().split()))
print(sum(li) + max(li)*(n-2))