# exercice sur les programmes de calculs :
# saisir le prix de départ A
# saisir le pourcentage de remise P
# affecter au montant de la remise R la valeur A*P/100
# afficher R


print("Ce programme permet de calculer la remise d'un produit en indiquant le prix initial et le pourcentage de réduction./n")
print("Pour faire cela, il execute les actions suivantes : ")
print("- Vous choississez un prix, qui sera affecté à A")
print("- Vous choississez un pourcentage de remise, qui sera affecté à P")
print("- Il est affecté à R le montant de la reemise, soit A*P/100\n")

A = input("Choississez le prix initial.\n")
A = int(A)
P = input("Choississez le pourcentage de réduction.\n")
P = int(P)
R = A*P/100
R = int(R)
print("Lorsque l'on applique une réduction de ", P, "% à un prix initial de ", A, "€, la remise est de ", R, "€.")