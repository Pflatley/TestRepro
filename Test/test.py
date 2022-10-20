# @TODO: Your code here

Pet_Info = {
    "name": "Rover",
    "age": 5,
    "hobbies": [
        "Walk",
        "Fetch",
        "Sleep"
        ],
    "wake_ups": {
        "monday": 7,
        "saturday": 10
    }
    }

print(f"My pets name is {Pet_Info['name']} and he is {Pet_Info['age']} years old")

print(f"My pet has {len(Pet_Info['hobbies'])} hobbies")

print(f"My pet's favorite hobby is: {Pet_Info['hobbies'][0]}")

print(f"My pet wakes up at {Pet_Info['wake_ups']['monday']} on Mondays")