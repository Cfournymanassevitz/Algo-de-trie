T = [3,5,0,4,5,8,7,2,6,1]
print(T)
def tri_bubble_sort(T):
    passage = 0
    permutation = True
    while permutation == True :
        permutation = False
        for i in range(0,len(T)-1):
            if T[i] > T[i+1]:
                permutation = True
                T[i], T[i+1] = T[i+1], T[i]
        passage = passage + 1
    return T
print(tri_bubble_sort(T))

def swap(idxi,idxj):
    temp = T[idxi]
    T[idxi] = T[idxj]
    T[idxj] = temp

