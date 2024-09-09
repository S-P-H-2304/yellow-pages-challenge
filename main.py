# Tu código aquí

menu_on = True

while menu_on:
    print("Presiona 1 para ver el directorio de usuarios")
    print("Presiona 2 para agregar un usuario nuevo")
    print("Presiona 3 para modificar un usuario existente en el directorio")
    print("Presiona 4 para eliminar un usuario del directorio")
    print("Presiona 5 para salir de este menú")

    user_input = int(input())

    if user_input == 1:
        from data import people
        for key, value in people.items():
            print(f"El número de {key} es {value}")
        break
    elif user_input == 2:
        new_user = input("Ingresa el nombre del usuario a modificar: ")
        new_numb = input("Ingresa el número correspondiente al nuevo usuario: ")
        people[new_user] = new_numb
        break
    elif user_input == 3:
        mod_user = input("Ingresa el nombre de usuario a modificar: ")
        if people.get(mod_user):
            print("Presiona ")


    