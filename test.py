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
