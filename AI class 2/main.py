import re
import random
from colorama import Fore, init

init(autoreset=True)

destination = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

def normalize_input(text):
    return re.sub(r"\s+", "", text.strip().lower())

def recommend():
    print(Fore.CYAN + "Travelbot: Beaches, mountains, or cities?")
    preference = normalize_input(input(Fore.YELLOW + "You: "))

    if preference in destination:
        suggestion = random.choice(destination[preference])
        print(Fore.GREEN + f"Travelbot: How about {suggestion}?")
        print(Fore.CYAN + "Travelbot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"Travelbot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "Travelbot: Let's try another one.")
            recommend()
        else:
            print(Fore.RED + "Travelbot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "Travelbot: Sorry, I don't have destinations for that type.")
    
    show_help()

def packing_tips():
    print(Fore.CYAN + "Travelbot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "Travelbot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"Travelbot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def tell_jokes():
    joke = random.choice(jokes)
    print(Fore.YELLOW + f"Travelbot: {joke}")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell jokes (say 'joke')")
    print(Fore.CYAN + "- Type 'exit' or 'bye' to end.\n")

def chats():
    print(Fore.CYAN + "Hello! I'm Travelbot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_jokes()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "Travelbot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "Travelbot: Could you rephrase that?")

if __name__ == "__main__":
    chats()
