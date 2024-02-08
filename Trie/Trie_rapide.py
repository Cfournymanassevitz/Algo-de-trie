tableau = [3,5,0,4,5,8,7,2,6,1]
print(tableau)
def tri_rapide(tableau):
    if not tableau:
        return []
    else:
        pivot = tableau[-1]
        plus_petit = [x for x in tableau     if x <  pivot]
        plus_grand = [x for x in tableau[:-1] if x >= pivot]
        return tri_rapide(plus_petit) + [pivot] + tri_rapide(plus_grand)

print(tri_rapide(tableau))