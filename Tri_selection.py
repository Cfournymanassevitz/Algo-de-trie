T = [3,5,0,4,5,8,7,2,6,1]
print(T)
def swap(idxi,idxj):
    temp = T[idxi]
    T[idxi] = T[idxj]
    T[idxj] = temp
def tri_selection(T):
    nb = len(T)
    for i in range(0,nb):
        min = i
        for j in range(i+1,nb):
            if T[j] < T[min]:
                min = j
        swap(i,min)
        print(T)
    return (T)

print(tri_selection(T))

