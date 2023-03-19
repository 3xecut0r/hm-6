import re

contacts = {}

def hello():
    print("How can I help you?")

def show_all():
    for key, value in contacts.items():
        print(f"{key}: {value}")
    l = len(key)
    print(f"List contain <{l}> contacts")
        
def change(name, phone):
    contacts.update({name:phone})
        
def add(name, phone):
    contacts.update({name:phone})
    print(f"I add contact for <{name}> with phone <{phone}>")

def phone(name):
    for k,v in contacts.items():
        if name == k:
            print(v)

def input_error(func):
    def wrapper():
        try:
            return func()
        except KeyError:
            print("There is no contact with that name")
            return func()
        except ValueError:
            print("Number is incorrect")
            return func()
        except IndexError:
            print("Give me a name and phone please")
            return func()
        
    return wrapper
            
        
@input_error
def main():
    while True:
        command = input(">>> ").strip().lower()

        if "show all" in command:
            return show_all()
        
        elif "hello" in command:
            return hello()
        
        elif "add" in command:
            res = command[4:].strip().split()
            add(res[0], res[1])
            
        elif command == ".":
            break
        
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        
        elif "change" in command:
            res = command[7:].strip().split()
            change(res[0], res[1])
            
        elif "phone" in command:
            name = command[6:]
            phone(name)
            

if __name__ == "__main__":
    main()