import os
import sys

def process_user_data(n, a, e):
    
    if a < 18:
        return "Error: El usuario es menor de edad"
    else:
        if e == "":
            return "Error: Falta el correo electrónico"
        else:
            try:
                if n == "admin":
                    return "Error: No se puede registrar al administrador"
                else:
                    # print("Usuario registrado correctamente")
                    return f"Éxito: {n} registrada correctamente"
            except Exception:
                return "Error: Algo salió mal en el sistema"