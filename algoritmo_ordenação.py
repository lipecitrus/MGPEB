from collections import deque

modulos = [
    {"nome": "Habitacao", "pouso": 2, "massa": 18000, "criticidade": 10, "hora": 10,
     "combustivel": 30, "cond_atmosferica": 9, "area_pouso": True, "integridade": 95},

    {"nome": "Energia", "pouso": 1, "massa": 12000, "criticidade": 10, "hora": 8,
     "combustivel": 60, "cond_atmosferica": 8, "area_pouso": True, "integridade": 70},

    {"nome": "Medico", "pouso": 3, "massa": 5000, "criticidade": 9, "hora": 12,
     "combustivel": 40, "cond_atmosferica": 7, "area_pouso": True, "integridade": 85},

    {"nome": "Logistica", "pouso": 4, "massa": 15000, "criticidade": 8, "hora": 14,
     "combustivel": 50, "cond_atmosferica": 6, "area_pouso": True, "integridade": 80},

    {"nome": "Pesquisa", "pouso": 5, "massa": 7000, "criticidade": 7, "hora": 16,
     "combustivel": 50, "cond_atmosferica": 7, "area_pouso": True, "integridade": 88}
]

def bublle_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j]['pouso'] > lista[j + 1]['pouso']:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

print(bublle_sort(modulos))
