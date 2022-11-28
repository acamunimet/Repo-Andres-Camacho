generos = {"Hombres":{"Deportes","Videojuegos","Corbatas","Sacos"}, "Mujeres":{"Maquillaje", "Accesorios", "Tacones", "Carteras"}}

print(generos)
print(generos.keys())
print(generos.values())
print(generos.items())
print(len(generos))
print("Hombres" in generos)
print(generos.get("hermafroditas", "No existe tal cosa"))