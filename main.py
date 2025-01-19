def greet_people(**kwargs):
    for name, greeting in kwargs.items():
        print(f"{greeting}, {name}!")

if __name__ == "__main__":
    greet_people(Alice="Hello", Bob="Hi", Charlie="Greetings")
