tableau = [3, 5, 0, 4, 5, 8, 7, 2, 6, 1]
print(tableau)
plus_petit = 0
plus_grand = 0


def tri_rapide(tableau):
    if not tableau:
        return []
    else:
        pivot = tableau[-1]
        plus_petit = [x for x in tableau if x < pivot]
        plus_grand = [x for x in tableau[:-1] if x >= pivot]
        return tri_rapide(plus_petit) + [pivot] + tri_rapide(plus_grand)


# print(tri_rapide(tableau))


def tri_rapide2(tableau, plus_petit, plus_grand):
    if plus_petit < plus_grand :
        pi = partitionner(tableau, plus_petit,plus_grand)
        tri_rapide2(tableau, plus_petit, pi-1)
        tri_rapide2(tableau, pi+1, plus_grand)
        return tableau


def partitionner(tableau, plus_petit, plus_grand):
    pivot = tableau[plus_grand]
    j = plus_petit-1
    for i in range(plus_petit, plus_grand):
        if tableau[i] <= pivot:
            j= j+1
            tableau[j], tableau[i] = tableau[i], tableau[j]

    tableau[j+1], tableau[plus_grand] = tableau[plus_grand], tableau[j+1]
    return j+1


def swap(idxi, idxj):
    temp = tableau[idxi]
    tableau[idxi] = tableau[idxj]
    tableau[idxj] = temp


print(tri_rapide2(tableau, 0, len(tableau)-1))
