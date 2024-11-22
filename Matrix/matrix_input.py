# Matrix from User 

'''
1-D Array (list)
3 5
2 3 4 5 6 
2 3 0 8 1
1 4 5 7 0
'''
def disp_mat(ls):
    for i in ls:
        print(*i, sep='\t')

# main Program 
# print(__name__)
if __name__ == '__main__':
    r, c = list(map(int, input().split()))
    M = []
    for i in range(r):
        ls=list(map(int, input().split()))
        M.append(ls)
    disp_mat(M)


