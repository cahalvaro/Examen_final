#EXAMEN FINAL 
#PREGUNTA 1. AUTOMATA FINITO

from enum import Enum

class Estados(Enum):
    Q0 = 0
    Q1 = 1
    Q2 = 2
    Q3 = 3

def es_identificador(source):
    estado_actual = Estados.Q0
    for c in source:
        if estado_actual == Estados.Q0:
            if c == 'm':
                estado_actual = Estados.Q1
            elif c == 'h':
                estado_actual = Estados.Q2
            else:
                return False
        elif estado_actual == Estados.Q1:
            if c == 'a':
                estado_actual = Estados.Q2
            elif c == 'h':
                estado_actual = Estados.Q3
            else:
                return False
        elif estado_actual == Estados.Q2:
            if c == 'm':
                estado_actual = Estados.Q1
            else:
                return False
        elif estado_actual == Estados.Q3:
            if c == 'a':
                estado_actual = Estados.Q3
            else:
                return False
    return estado_actual in (Estados.Q3, Estados.Q2)

if __name__ == "__main__":
    source = "hmamamha"
    if es_identificador(source):
        print("Identificador válido")
    else:
        print("Identificador no válido")