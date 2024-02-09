tableau = [3,5,0,4,5,8,7,2,6,1,25,33,11,17,18]
print(tableau)


def fusion(gauche, droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche != len(gauche)-1 and index_droite != len(droite)-1:
        if gauche[index_gauche] < droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1

    return resultat + [gauche[index_gauche]] + [droite[index_droite]]


def tri_fusion(tableau):
    if len(tableau) <= 1:
        return tableau
    milieu = len(tableau) // 2
    return fusion( tri_fusion(tableau[:milieu]), tri_fusion(tableau[milieu:]))

print(tri_fusion(tableau))