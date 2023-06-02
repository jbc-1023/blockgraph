import random
import csv
import string

# Generate random name
def generate_random_name(type):
    if type == "first":
        names = [
            "Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia",
            "Harper", "Evelyn", "Landon", "Mason", "Lucas", "Logan", "Oliver", "Elijah", "Aiden", "James",
            "Benjamin", "Lucy", "Grace", "Claire", "Henry", "Alexander", "Daniel", "Samuel", "Joseph", "William",
            "Michael", "Emily", "Abigail", "Elizabeth", "Ella", "Victoria", "Sofia", "Avery", "Mila", "Scarlett",
            "Hannah", "Samantha", "Jacob", "Mason", "Ethan", "Emily", "Daniel", "Matthew", "Emma", "David", "Andrew",
            "Joseph", "Jackson", "Anthony", "Joshua", "Christopher", "Madison", "Sophia", "Ashley", "Sarah", "Alyssa",
            "Taylor", "Brianna", "Jessica", "Olivia", "Evelyn", "Gabriel", "Samuel", "Victoria", "Aiden", "Alexis",
            "Grace", "Lily", "Hailey", "Nathan", "Tyler", "Brandon", "Ava", "Chloe", "Alexa", "Zoe", "Julia", "Lauren"
        ]

    elif type == "last":
        names = [
            "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
            "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
            "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
            "Walker", "Young", "Hall", "Allen", "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson",
            "Turner", "Parker", "Collins", "Bell", "Murphy", "Cook", "Bennett", "Bailey", "Howard", "Rogers",
            "Cooper", "Gray", "Price", "Wood", "Kelly", "Barnes", "Powell", "Young", "Cruz", "Russell",
            "Hughes", "Peterson", "Carter", "Sanders", "Brooks", "Perry", "Long", "Foster", "Reed", "Morris",
            "Bryant", "Warren", "Reyes", "Jenkins", "Coleman", "Sullivan", "Ward", "Fisher", "Jordan", "Reynolds"
        ]
    random_name = random.choice(names)
    return random_name

# Generate random 2-digit number
def generate_random_number():
    return random.randint(20, 50)

# Generate random state
def generate_random_usa_state():
    # List of states
    states = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
        "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
        "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
        "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
        "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
    ]
    random_state = random.choice(states)
    return random_state


def loop_write(loops, out_file):
    # Title
    csv_title = ["First Name", "LastName", "Age", "State"]

    # Write the CSV row to a file
    with open(out_file, 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_title)
        for i in range(loops):
            # Generate the CSV row
            first_name = generate_random_name("first")
            last_name = generate_random_name("last")
            age = generate_random_number()
            state = generate_random_usa_state()
            writer.writerow([first_name, last_name, age, state])
            percentage = round((i/loops * 100.0), 2)
            print(f"{percentage}% {first_name}, {last_name}, {age}, {state}")

# Simulate the population of USA
loop_write(loops=1000000, out_file="data/large-csv.csv")

