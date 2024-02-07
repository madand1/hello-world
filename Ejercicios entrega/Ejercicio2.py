#Ejercicio2
peliculas=[
	{
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
	},
	{
		"title": "Gudfadern",
		"year": "1972",
		"genres": [
			"Crime",
			"Drama"
		],
		"ratings": [6, 10, 4, 10, 1, 3, 7, 2, 3, 3, 3, 4, 2, 5, 6, 9, 10, 8, 7, 4, 8, 9, 9, 10, 4, 6, 2, 9, 7, 7],
		"duration": "PT175M",
		"releaseDate": "1972-09-27",
		"originalTitle": "The Godfather",
		"storyline": "When the aging head of a famous crime family decides to transfer his position to one of his subalterns, a series of unfortunate events start happening to the family, and a war begins between all the well-known families leading to insolence, deportation, murder and revenge, and ends with the favorable successor being finally chosen.                Written by\nJ. S. Golden",
		"actors": [
			"Marlon Brando",
			"Al Pacino",
			"James Caan"
		],
		"posterurl": ""
	},
	{
		"title": "Gudfadern del II",
		"year": "1974",
		"genres": [
			"Crime",
			"Drama"
		],
		"ratings": [2, 5, 1, 1, 8, 4, 2, 3, 10, 10, 4, 9, 8, 9, 7, 6, 6, 9, 9, 4, 1, 8, 4, 5, 7, 7, 7, 1, 10, 6],
		"duration": "PT202M",
		"releaseDate": "1975-07-28",
		"originalTitle": "The Godfather: Part II",
		"storyline": "The continuing saga of the Corleone crime family tells the story of a young Vito Corleone growing up in Sicily and in 1910s New York; and follows Michael Corleone in the 1950s as he attempts to expand the family business into Las Vegas, Hollywood and Cuba.                Written by\nKeith Loh <loh@sfu.ca>",
		"actors": [
			"Al Pacino",
			"Robert De Niro",
			"Robert Duvall"
		],
		"posterurl": ""
	},
	{
		"title": "The Dark Knight",
		"year": "2008",
		"genres": [
			"Action",
			"Crime",
			"Drama"
		],
		"ratings": [3, 6, 4, 1, 6, 10, 6, 3, 5, 9, 1, 3, 1, 7, 8, 10, 6, 2, 8, 6, 7, 1, 4, 3, 8, 3, 10, 8, 10, 4],
		"duration": "PT152M",
		"releaseDate": "2008-07-25",
		"originalTitle": "",
		"storyline": "Set within a year after the events of Batman Begins, Batman, Lieutenant James Gordon, and new district attorney Harvey Dent successfully begin to round up the criminals that plague Gotham City until a mysterious and sadistic criminal mastermind known only as the Joker appears in Gotham, creating a new wave of chaos. Batman's struggle against the Joker becomes deeply personal, forcing him to \"confront everything he believes\" and improve his technology to stop him. A love triangle develops between Bruce Wayne, Dent and Rachel Dawes.                Written by\nLeon Lombardi",
		"actors": [
			"Christian Bale",
			"Heath Ledger",
			"Aaron Eckhart"
		],
		"posterurl": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2MwUndetermined error: ._V1_SY500_CR0,0,333,500_AL_.jpg"
	},
	{
		"title": "Schindler's List",
		"year": "1993",
		"genres": [
			"Biography",
			"Drama",
			"History"
		],
		"ratings": [2, 6, 7, 8, 8, 6, 2, 4, 6, 2, 3, 3, 5, 9, 5, 10, 9, 5, 5, 2, 10, 4, 8, 7, 4, 10, 2, 10, 4, 10],
		"duration": "PT195M",
		"releaseDate": "1994-03-04",
		"originalTitle": "",
		"storyline": "Oskar Schindler is a vainglorious and greedy German businessman who becomes an unlikely humanitarian amid the barbaric German Nazi reign when he feels compelled to turn his factory into a refuge for Jews. Based on the true story of Oskar Schindler who managed to save about 1100 Jews from being gassed at the Auschwitz concentration camp, it is a testament to the good in all of us.                Written by\nHarald Mayr <marvin@bike.augusta.de>",
		"actors": [
			"Liam Neeson",
			"Ralph Fiennes",
			"Ben Kingsley"
		],
		"posterurl": ""

        	}]

'''
Muestra el nombre y el argumento de cada película.
Muestra el nombre y los actores de cada pélicula
Pide por teclado un genero y muestra el nombre de las péliculas de ese genero.
Pide un año por teclado y muestra todas las péliculas anteriores a ese año.
'''
# Muestra el nombre y el argunmento de la película

# Muestra el nombre y el argumento de cada película.
print("Nombre y Argumento de cada película:")
for pelicula in peliculas:
    print(f"Nombre: {pelicula['title']}")
    print(f"Argumento: {pelicula['storyline']}")
    print("\n")

# Muestra el nombre y los actores de cada película.
print("Nombre y Actores de cada película:")
for pelicula in peliculas:
    print(f"Nombre: {pelicula['title']}")
    print(f"Actores: {', '.join(pelicula['actors'])}")
    print("\n")

# Pide por teclado un género y muestra el nombre de las películas de ese género.
genero_buscar = input("Introduce un género: ")
print(f"Películas del género {genero_buscar}:")
for pelicula in peliculas:
    if genero_buscar.lower() in pelicula['genres']:
        print(pelicula['title'])
print("\n")

# Pide por teclado un año y muestra todas las películas anteriores a ese año.
anno_buscar = int(input("Introduce un año: "))
print(f"Películas anteriores a {anno_buscar}:")
for pelicula in peliculas:
    if int(pelicula['year']) < anno_buscar:
        print(pelicula['title'])
