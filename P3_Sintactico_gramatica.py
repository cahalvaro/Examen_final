#EXAMEN FINAL 
#PREGUNTA 3. CODIGO PARA LA GRAMATICA (ANALIZADOR SINTACTICO)

class Simbolo:
    def __init__(self, lexema, token):
        self.lexema = lexema
        self.token = token

def verificar_sintaxis(tabla_simbolos):
    index = 0
    resultado = directorio(tabla_simbolos, index)
    return resultado == len(tabla_simbolos)

def directorio(tabla_simbolos, index):
    if index + 1 >= len(tabla_simbolos) or tabla_simbolos[index].token != "dir" or tabla_simbolos[index + 1].token != "sig":
        print("Error: Asignación inválida")
        return -1
    index += 2
    while index + 1 < len(tabla_simbolos) and tabla_simbolos[index].token == "dir" and tabla_simbolos[index + 1].token == "sig":
        index += 2
    
    if index < len(tabla_simbolos) and tabla_simbolos[index].token == "dir":
        index +=1
        if index + 1 < len(tabla_simbolos) and tabla_simbolos[index].token=="punto":
            index+=1
            if index <len(tabla_simbolos) and tabla_simbolos[index].token=="extension":
                return index + 1
            else:
                print("Error: Asignación inválida")
                return -1
        else:
            print("Error: Asignación inválida")
            return -1
    else:
        print("Error: Asignación inválida")
        return -1

if __name__ == "__main__":
    tabla_simbolos = [
        Simbolo("home", "dir"),
        Simbolo("/", "sig"),
        Simbolo("user", "dir"),
        Simbolo("/", "sig"),
        Simbolo("Documents", "dir"),
        Simbolo("/", "sig"),
        Simbolo("compi", "dir"),
        Simbolo(".", "punto"),
        Simbolo("txt", "extension")
    ]

    resultado = verificar_sintaxis(tabla_simbolos)
    if resultado:
        print("No existen errores sintácticos")
    else:
        print("Se encontraron errores")