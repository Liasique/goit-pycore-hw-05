
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        #if not args and command in ["add", "change", "phone"]:
        if command in ["add", "change"] and len(args) < 2:
            print("Enter the argument for the command")
            continue
        if command == "phone" and len(args) < 1:
            print("Enter the argument for the command")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()





#TERMNAL OUTPUT:
"""(base) ➜  goit-pycore-hw-05 git:(main) ✗ python3 task4/cli.py                                                                                 
Welcome to the assistant bot!
Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356
Enter a command: """



#Вимоги до завдання:

"""Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error.
Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо.
Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError, ValueError, IndexError. 
Коли відбувається виняток декоратор повинен повертати відповідну відповідь користувачеві. Виконання програми при цьому не припиняється."""#


#Рекомендації для виконання:

"""В якості прикладу додамо декоратор input_error для обробки помилки ValueError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner


Та обгорнемо декоратором функцію add_contact нашого бота, щоб ми почали обробляти помилку ValueError.

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."



#Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку винятків інших типів з відповідними повідомленнями.
"""


#Критерії оцінювання:
"""
Наявність декоратора input_error, який обробляє помилки введення користувача для всіх команд.
Обробка помилок типу KeyError, ValueError, IndexError у функціях за допомогою декоратора input_error.
Кожна функція для обробки команд має власний декоратор input_error, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.

"""
#Приклад використання:
"""python task4/cli.py"""
"""
При запуску скрипту діалог з ботом повинен бути схожим на цей.

Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356 
Enter a command:

"""





