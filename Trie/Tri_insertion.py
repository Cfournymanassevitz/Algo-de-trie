T = [3,5,0,4,5,8,7,2,6,1]
print(T)
def tri_inertion(T):
    for i in range(0,len(T)):
        en_cour = T[i]
        j = i
        while j > 0 and T[j-1]> en_cour:
            T[j]= T[j-1]
            j = j-1

        T[j] = en_cour
    print(T)

print(tri_inertion(T))



#
# def swap(num1,num2):
#     temp = num1
#     num1 = num2
#     num2 = temp



