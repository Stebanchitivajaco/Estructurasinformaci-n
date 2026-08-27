from nodo import Nodo


class ListaAdopcion:
    """Lista doblemente enlazada que gestiona los animales disponibles."""

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.total = 0

    def rescatar_animal(self, id_animal, nombre, especie, edad):
        nuevo = Nodo(id_animal, nombre, especie, edad)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.total += 1
        print(f"[Rescatado] {nombre} ({especie}) ingresó al sistema.")

    def buscar_por_id(self, id_animal):
        actual = self.cabeza
        while actual is not None:
            if actual.id_animal == id_animal:
                return actual
            actual = actual.siguiente
        return None

    def evaluar_adoptante(self, id_animal, aprobado):
        nodo = self.buscar_por_id(id_animal)
        if nodo is None:
            print(f"No se encontró un animal con id {id_animal}.")
            return

        nodo.estado = "en_evaluacion"
        if aprobado:
            nodo.estado = "adoptado"
            self._retirar_nodo(nodo)
            print(f"[Adoptado] {nodo.nombre} fue adoptado y salió del sistema.")
        else:
            nodo.estado = "en_espera"
            print(f"[No aprobado] {nodo.nombre} vuelve a la lista de espera.")

    def _retirar_nodo(self, nodo):
        if nodo.anterior is not None:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.cabeza = nodo.siguiente

        if nodo.siguiente is not None:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.cola = nodo.anterior

        nodo.anterior = None
        nodo.siguiente = None
        self.total -= 1

    def listar_desde_mas_antiguo(self):
        print("\n--- Más antiguo primero ---")
        actual = self.cabeza
        while actual is not None:
            print(f"ID {actual.id_animal} | {actual.nombre} | {actual.especie} | "
                  f"{actual.edad} años | {actual.estado}")
            actual = actual.siguiente

    def listar_desde_mas_reciente(self):
        print("\n--- Más reciente primero ---")
        actual = self.cola
        while actual is not None:
            print(f"ID {actual.id_animal} | {actual.nombre} | {actual.especie} | "
                  f"{actual.edad} años | {actual.estado}")
            actual = actual.anterior

    def contar_disponibles(self):
        return self.total