import sys
input = sys.stdin.readline

n, m = map(int, input().split())
po_dic = {}
for i in range(1, n+1):
    po = input().strip()
    po_dic[str(i)] = po
    po_dic[po] = i

for i in range(m):
    print(po_dic[input().strip()])