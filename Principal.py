__author__ = 'Gisella Ineira Sanchez'

from MemoriaDinamica import *
Reposteria = ['Pastel de queso','Frappe', 'Flan', 'Donas', 'Capuchino']
precios = [20, 25, 15, 10, 20]


listas = MemoriaDinamica(Reposteria)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.agregarelementoarray('cheese cake')
listas.imprimirLista()
lista2 = MemoriaDinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(35)
lista2.imprimirLista()
