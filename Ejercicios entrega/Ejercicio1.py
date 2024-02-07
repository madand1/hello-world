#Ejercicio1 
pelicula={
		"title": "Nyckeln till frihet",
		"year": "1994",
		"genres": [
			"Crime",
			"Drama"
		],
		"ratings": [8, 8, 6, 10, 2, 3, 4, 5, 4, 9, 3, 9, 6, 10, 4, 8, 10, 1, 2, 8, 1, 9, 5, 4, 4, 2, 4, 6, 9, 10],
		"duration": "PT142M",
		"releaseDate": "1995-03-03",
		"originalTitle": "The Shawshank Redemption",
		"storyline": "Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way of dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most notably a wise long-term inmate named Red.                Written by\nJ-S-Golden",
		"actors": [
			"Tim Robbins",
			"Morgan Freeman",
			"Bob Gunton"
		],
		"posterurl": ""
	}

'''
Y realiza un programa que muestre las siguientes informaciones:

Muestra el nombre y el año de la película
Muestra los actores que trabajan en la película.
Muestra la puntuación media de la película

'''
#Soluciones
# Muestra el nombre y el año de la película
print(f"Nombre de la película: {pelicula['title']}")
print(f"Año de lanzamiento: {pelicula['year']}\n")

# Muestra los actores que trabajan en la película
print("Actores:")
for actor in pelicula['actors']:
    print(f"- {actor}")
print()

# Calcula y muestra la puntuación media de la película
puntuaciones = pelicula['ratings']
puntuacion_media = sum(puntuaciones) / len(puntuaciones)
print(f"Puntuación media: {puntuacion_media:.2f}")
