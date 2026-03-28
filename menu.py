from product import *

#List of products
storage = []

def menu(): #Dictionaries are passed as parameters to functions to avoid the use of global variables
    running = True #variable with boolean value
    while running:

        print("\n===== ORDER SYSTEM =====")
        print("1. Add product")
        print("2. Show products")
        print("3. Search product")
        print("4. Update")
        print("5. Delete")
        print("6. Stats")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")

        option = input("Choose an option: ")

        if option == "1":
            agg_product = add_product(storage)
            print(agg_product)

        elif option == "2":
            show_storage(storage)

        elif option == "3":
            search_storage = search_product(storage)
            print(search_storage)

        elif option == "4":
            update_storage = upd_product(storage)
            print(update_storage)

        elif option == "5":
            delete_product(storage)

        elif option == "6":
            show_stats(storage)

        elif option == "7":
            save_file(storage)

        elif option == "8":
            load_file(storage)

        elif option == "9":
            print("Exiting...")
            running = False
        
        else:
            print("Invalid option")

