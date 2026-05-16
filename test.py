<<<<<<< HEAD
def validar_correo_simple(correo):
    """Validación básica de formato de correo electrónico."""
    if not correo or "@" not in correo:
        return False
    
    nombre, dominio = correo.split("@", 1)
    
    if not nombre or not dominio:
        return False
    
    if "." not in dominio:
        return False
    
    # Verificar que el dominio termina con una extensión válida
    extensiones = (".com", ".org", ".net", ".edu", ".es")
    if not dominio.endswith(extensiones):
        return False
    
    return True

# Ejemplos
correos = ["usuario@ejemplo.com", "usuario@dominio", "usuario@ejemplo.org", 
           "@ejemplo.com", "usuario@.com", "usuario@ejemplo.xyz"]

for correo in correos:
    resultado = "válido" if validar_correo_simple(correo) else "inválido"
    print(f"{correo}: {resultado}")
=======
correo = "usuario@ejemplo.com"

# Extraer nombre de usuario y dominio
nombre, dominio = correo.split("@")
if(dominio):

    print(f"Usuario: {nombre}")  # Usuario: usuario
    print(f"Dominio: {dominio}")  # Dominio: ejemplo.com

# Verificar si el dominio es válido
if dominio.endswith(".com") or dominio.endswith(".org"):
    print("Dominio válido")

# Censurar parte de una dirección de correo
correo_censurado = nombre[:3] + "***@" + dominio
print(correo_censurado)  # usu***@ejemplo.com
>>>>>>> a17e74c17f82f507d7e8bae4bbd376564dbbfbd4
