my_favorite_songs = ["La Corida", "Viens, je t'emmène", "L'aigle noir", "Les copains d'abord"]
my_favorite_songs.sort()
print(my_favorite_songs)

print(my_favorite_songs[0])
print(my_favorite_songs[1])
print(my_favorite_songs[2])
print(my_favorite_songs[3]) 

#my_favorite_songs = ["La Corida", "Viens, je t'emmène", "L'aigle noir", "Les copains d'abord"] 
#PAS BESOIN DE REECRIRE LE 1ER STATEMENT
my_favorite_songs.append("Ella")
print(my_favorite_songs)

number_songs = len(my_favorite_songs)
message = "There are " + str(number_songs) +" favorite songs in my playlist"
print(message)

my_favorite_songs.pop(2)
print(my_favorite_songs)

print((my_favorite_songs))
 #7.Display the lenght of the array. ????
 # let's check the nico's walkthrough 
print(len(my_favorite_songs))

