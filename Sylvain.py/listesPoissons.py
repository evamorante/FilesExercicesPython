#pour attribuer plusieurs valeurs à une variables on utilise les listes (arrays) et puis on utilise diverses méthodes pour travailler dessus
fishes = ["raie manta", "poisson-perroquet", "poisson-trompette"]
print(fishes)

fishes = []
fishes.append("truite")
print(fishes)
fishes.append("pengasuis")
print(fishes)
fishes.append("ombre")
print(fishes)
#la recherche de type ne fonctionne pas dans VSCode mais bien dans le terminal ;)
type(fishes)
fishes
#idem là
fishes[0]
print(fishes) #donne un résultat sur cmd - mais pas ici, il faut donner l'instruction "print", comme ci-après
print(fishes[0])
#pour effacer instruction del ou méthode .pop
del fishes[0]
print(fishes)
fishes.append("truite")
print(fishes)
fishes.pop(1) #pour enlever ombre
print(fishes)
#len - longueur de la liste
print(len(fishes))
#in - recherche si un élément existe ou pas
print("raie mantra" in(fishes))
print("truite"in(fishes))

