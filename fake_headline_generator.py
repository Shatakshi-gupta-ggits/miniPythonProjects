#1- import random module
import random 

#2 - create subjects
subjects = [
    "Sharukh khan",
    "Virat Kohli",
    "Nirmala Sitaraman",
    "A mumbai Cat",
    "Prime minister Modi ji",
    "Auto Rickshaw driver from Delhi",
    "Group of Monkeys"
]

actions = [
    "Launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at red fort",
    "in Mumbai Local Train",
    "a plate of Samosa",
    "inside parliament",
    "during IPL Match", 
    "at India Gate"   
]

#3 Start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    
    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n" + headline)
    
    user_input = input("\n Do you want another Headline? (yes/no)").strip().lower()
    if user_input == "no":
        break
    
#print goodbye message
print("\nThanks for using the Fake News Headline Generator.Have a fun day")
