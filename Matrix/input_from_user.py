# Matrix Input From User at run time 
'''
2 3
1 2 3
4 5 8
3 3
1 2 3
4 5 8
1 2 3
'''

r1, c1 = list(map(int, input().split()))
M1 = []
for i in range(r1):
    lst = list(map(int, input().split()))
    M1.append(lst)
for i in M1:
    print(*i, sep='\t')

r2, c2 = list(map(int, input().split()))
M2 = []
for i in range(r2):
    lst = list(map(int, input().split()))
    M2.append(lst)
for i in M2:
    print(*i, sep='\t')
