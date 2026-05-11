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
