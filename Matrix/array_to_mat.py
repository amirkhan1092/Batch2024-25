# input matrix as an array 

'''
4 3
10 25 3 4 5 61 7 8 9 10 1 22
'''
def disp_mat(ls):
    for i in ls:
        print(*i, sep='\t')

r, c = map(int, input().split())
raw_lst = list(map(int, input().split()))
M = []
count = 0
if r * c == len(raw_lst):
    tmp = []
    for i in raw_lst:
        tmp.append(i)
        count += 1
        if count == c:
            M.append(tmp)
            tmp = []
            count = 0       
disp_mat(M)

