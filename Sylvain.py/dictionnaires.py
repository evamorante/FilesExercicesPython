#on peut créer des dictionnaires avec des valeurs attribuées à des éléments d'une liste, soit on le créé en direct à la main avec les accolades
fishes = {'raie mantra':1, 'truite':13, 'ombre':2, 'saumon':4}
print(fishes)
#souvent on presente de la sorte ci-après
fishes = {'raie mantra':1, 
          'truite':13, 
          'ombre':2, 
          'saumon':4}
print(fishes)
#on peut créer avec la méthode suivante, qui donnera le même résultat
fishes["raie mantra"]=1
fishes["truite"]=13
fishes["ombre"]=2
fishes["saumon"]=4
print(fishes)
# 'raie mantra':1,
# 'truite':13, etccc.....sont des paires de clés, pour faire des manipulations (accéder, afficher, ajouter, enlever, etc) 
#  sur les éléments des dictionnaires on "invoque" les clés-string et non pas des positions comme pour les listes, 
#  et non pas sur les clés-valeurs, à mettre entre crochets
fishes["truite"] #fonctionne pas ici, cmd oui
print(["truite"]) #pas la bonne stratégie - ces 2 lignes de code - n'affichera que le string "truite" - solution ci-dessous
print(fishes["truite"])
#in pour rechercher la valeur ne marche pas, utiliser fishes.values() - .values étant une méthode du dictionnaire
print(13 in fishes.values())
#pour rechercher le type - comme pour les listes
print(type(fishes))
#ne pas oublier la fonction dir sur n'importe quel objet qui permet d'avoir toutes les méthodes, fonctions, instructions
print(dir("truite"))