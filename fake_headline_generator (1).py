import random

subjects = {
    "politician": [
        "Mamata Banerjee",
        "Narendra Modi",
        "Nirmala Sitharaman",
        "Rahul Gandhi",
        "Arvind Kejriwal"
    ],

    "cricketer": [
        "Virat Kohli",
        "MS Dhoni",
        "Rohit Sharma",
        "Hardik Pandya",
        "Jasprit Bumrah"
    ],

    "bollywood": [
        "Shah Rukh Khan",
        "Salman Khan",
        "Deepika Padukone",
        "Ranbir Kapoor",
        "Alia Bhatt"
    ]
}

actions = [
    "dances with",
    "eats",
    "celebrates with",
    "orders",
    "launches",
    "declares war on",
    "cancels"
]

places_or_things = [
    "at India Gate",
    "in a Howrah local train",
    "inside Parliament",
    "at the Ganga ghat",
    "during an IPL match",
    "a plate of momo",
    "at a secret party"
]

print("Welcome to the Fake News Headline Generator!")

while True:

    print("\nChoose a topic for the fake headline:")
    print("Politician")
    print("Cricketer")
    print("Bollywood")

    choice = input("Enter your choice: ").strip().lower()

    if choice == "politician":
        category = "politician"
    elif choice == "cricketer":
        category = "cricketer"
    elif choice == "bollywood":
        category = "bollywood"
    else:
        print("Invalid choice. Please try again.")
        continue

    subject = random.choice(subjects[category])
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f"\nBREAKING NEWS: {subject} {action} {place}"
    print(headline)

    again = input("\nDo you want another headline? (yes/no): ").strip().lower()

    if again == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day!")