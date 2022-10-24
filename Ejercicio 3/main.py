from hash import Hash
if __name__ == "__main__":
    unHash = Hash(10)
    
    unHash.insertar(1596523)
    unHash.insertar(215131)
    unHash.insertar(54832)
    unHash.insertar(54232)
    unHash.insertar(84152)
    unHash.insertar(123)
    unHash.insertar(1354)
    unHash.insertar(15575)

    
    print(unHash.buscar(1354))
    print(unHash.buscar(15575))