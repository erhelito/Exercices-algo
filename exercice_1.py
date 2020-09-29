# exercice sur les programmes de calculs :
# saisir A
# affecter à B la valeur 5
# affecter à C la valeur A X B
# affecter à A la caleur C + 4
# afficher A, B, C


print("Ce programme permet execute les actions suivantes : \n")
print("- Vous choississez un nombre de départ, qui est affecté à \"A\"")
print("- La valeur 5 est affectée à B")
print("- Il est affecté à C la valeur de A X B")
print("- Il est affecté à A la valeur de C + 4")
print("- On affiche A, B, C\n")

A = input("Choississez un nombre de départ. \n")
A = int(A)
B = 5
C = A*B
A = C+4

print("A =", A, "B=", B, "C=", C)
