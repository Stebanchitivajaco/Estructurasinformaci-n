from lista_adopcion import ListaAdopcion

sistema = ListaAdopcion()

sistema.rescatar_animal(1, "Luna", "Perro", 2)
sistema.rescatar_animal(2, "Michi", "Gato", 1)
sistema.rescatar_animal(3, "Rocky", "Perro", 4)
sistema.rescatar_animal(4, "Nala", "Gato", 3)

sistema.listar_desde_mas_antiguo()
sistema.listar_desde_mas_reciente()
print(f"\nTotal disponibles: {sistema.contar_disponibles()}")

sistema.evaluar_adoptante(2, aprobado=True)
sistema.evaluar_adoptante(3, aprobado=False)

sistema.listar_desde_mas_antiguo()
print(f"\nTotal disponibles: {sistema.contar_disponibles()}")
