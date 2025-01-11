if __name__ != "__main__":

    # import relativo
    from ..gestion.crud import guardar

    # import abasoluto
    # from usuarios.gestion.crud import guardar

    def pagar_impuestos():
        print("pagando impuestos")
        guardar()

if __name__ == "__main__":
    print("Tareas de mantenimiento")
