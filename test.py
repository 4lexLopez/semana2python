import random

def generar_usuarios(usuarios: int):
    nombres = ["p", "l", "k", "j", "h", "f", "g", "d", "s", "a"]
    personas = []
    for i in range(usuarios):
        persona = {'id': i + 1, 'nombre': random.choice(nombres), 'edad': random.randint(18, 65), 'puntuacion': round(random.uniform(0.0, 10.0,),1)}
        personas.append(persona)
    return personas

print(generar_usuarios(2))
