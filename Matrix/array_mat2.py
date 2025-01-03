# Array to matrix 


'''
3 3
2 3 4 5 6 7 8 9 0
'''

r, c = list(map(int, input().split()))
raw_list = list(map(int, input().split()))

M = []
tmp = []
count = 0
for i in raw_list:
    tmp.append(i)
    count += 1
    if count == c:
        M.append(tmp)
        tmp=[]
        count = 0

for i in M:
    print(*i, sep='\t')
  

    