lang = input("What's the programming language you want to learn?")

match lang:
    case "Javascript":
        print("You can become a web developer")

    case "Python":
        print("You can become a data scientist")

    case "PHP":
        print("You can become a backend developer")

    case "Solidity":
        print("You can become a blockchain developer")

    case "Java":
        print("You can become a mobile app developer")

    case _:
        print("The language doesn't matter, what matters is solving problems")
