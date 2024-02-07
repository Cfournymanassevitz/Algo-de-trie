list = [3,5,0,4,5,8,7,2,6,1]
print(list)
def shell_sort(list):
    espacements = []
    longueur = len(list)
    e = 0
    while e < longueur:
        e = (3 * e + 1)
        espacements.append(e)

    for e in espacements:
        for i in range(longueur):
            valeur = list[i]
            j = i
            while j > e - 1 and list[j - e] > valeur:
                list[j] = list[j - e]
                j = j - e
            list[j] = valeur

    return list

print (shell_sort(list))