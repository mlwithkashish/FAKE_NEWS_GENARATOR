# Fake News Channel Generator
import random
import time
from datetime import datetime

# categories with subjects
categories = {
    "sports": [
        "Virat Kohli",
        "MS Dhoni",
        "Rohit Sharma",
        "A Local Cricket Umpire",
        "An IPL Cheerleader"
    ],
    "bollywood": [
        "Shahrukh Khan",
        "Salman Khan",
        "Deepika Padukone",
        "A Struggling Actor",
        "A Mumbai Cat"
    ],
    "politics": [
        "Prime Minister Modi",
        "Nirmala Sitharaman",
        "Rahul Gandhi",
        "An Angry MP",
        "A Rickshaw Driver from Delhi"
    ],
    "animals": [
        "A Group of Monkeys",
        "A Street Dog",
        "A Dancing Elephant",
        "A Lazy Panda",
        "A Parrot from Old Delhi"
    ]
}

# actions
actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
    "argues with",
    "steals"
]

# places or things
places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate",
    "on Instagram Live",
    "at a wedding ceremony"
]

print(" Welcome to the LIVE Fake News Channel ")
print("Categories: sports | bollywood | politics | animals")

# ask category
category = input("\nChoose a category (or press Enter for random): ").strip().lower()

# ask headline limit
try:
    limit = int(input("How many headlines do you want? (0 for unlimited): "))
except ValueError:
    limit = 0

print("\n Starting live news ticker.............\n")

# save session header in file
with open("fake_news.txt", "a", encoding="utf-8") as f:
    f.write("\n=== New Fake News Session: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n")

try:
    count = 0
    while True:
        # pick subject
        if category in categories:
            subject = random.choice(categories[category])
        else:
            subject = random.choice(random.choice(list(categories.values())))

        action = random.choice(actions)
        place_or_thing = random.choice(places_or_things)

        # timestamp + headline
        timestamp = datetime.now().strftime("%H:%M:%S")
        headline = f"[{timestamp}] BREAKING NEWS: {subject} {action} {place_or_thing}!!!!"

        print(headline)

        # save to file
        with open("fake_news.txt", "a", encoding="utf-8") as f:
            f.write(headline + "\n")

        count += 1
        if limit > 0 and count >= limit:
            break

        time.sleep(3)

except KeyboardInterrupt:
    print("\n FINAL NEWS: Fake News Channel signs off for today! ")
