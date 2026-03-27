from producto import *

#Lista de productos
storage = []

def menu(): #Dictionaries are passed as parameters to functions to avoid the use of global variables
    running = True #variable with boolean value
    while running:

        print("\n===== ORDER SYSTEM =====")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        option = input("Choose an option: ")

        if option == "1":
            agg_product = add_product(storage)
            print(agg_product)

        elif option == "2":
            show_product = show_storage(storage)

        elif option == "3":
            search_storage = search_product(storage)
            print(search_storage)

        elif option == "4":
            update_storage = upd_product(storage)
            print(update_storage)

        elif option == "5":
            delete_storage = delete_product(storage)

        elif option == "6":
            storage_stats = show_stats(storage)

        elif option == "7":
            save_file(storage)

        elif option == "8":
            load_file(storage)

        elif option == "9":
            print("Exiting...")
            running = False
        
        else:
            print("Invalid option")

