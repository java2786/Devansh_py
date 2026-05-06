"""
Student:
    roll: 1001
    name: Ramesh
    subjects: Math: 75, Science: 83, English: 67
    contacts: 90909090, ramesh@mail.com
    address: dark building, pune, 76543
    
Student:
    roll: 1251
    name: Mahesh
    subjects: Math: 86, Science: 72, English: 71
    contacts: 87687656, mahesh@mail.com
    address: evenue society, bangalore, 98743
    
Topper -> Mahesh (Percentage)
"""


# students = list, array, set, dictionary, tuple

students = {
    1001: {
        "roll": 1001,
        "name": "Ramesh",
        "subjects": {"math": 75, "english": 67, "science": 83},
        # "semester": (67, 72),
        "contacts": [90909090, "ramesh@mail.com"],
        "address": "dark building, pune, 76543"
    },
    1251: {
        "roll": 1251,
        "name": "Mahesh",
        "subjects": {"science": 42, "math": 46, "english": 71},
        "contacts": [87687656, "mahesh@mail.com"],
        "address": "evenue society, bangalore, 98743"
    }
}

topScore = 0
topScorer = None

# std = students[1251]
# print(f"Name: {std['name']}")
# print(f"Roll: {std['roll']}")
# print(f"Math\tEnglish\tScience")
# print("-------------------------")
# subjects = std["subjects"]
# print(f"{subjects['math']}\t{subjects['english']}\t{subjects['science']}")
# std['total'] = subjects['math'] + subjects['english'] + subjects['science']
# print("-------------------------")
# print(f"\t\tTotal score: {std['total']}")


for roll in students:
    std = students[roll]
    print(f"Name: {std['name']}")
    print(f"Roll: {std['roll']}")
    print(f"Math\tEnglish\tScience")
    print("-------------------------")
    subjects = std["subjects"]
    print(f"{subjects['math']}\t{subjects['english']}\t{subjects['science']}")
    std['total'] = subjects['math'] + subjects['english'] + subjects['science']
    print("-------------------------")
    print(f"\t\tTotal score: {std['total']}\n\n")

    if(std['total']>topScore):
        topScore = std['total']
        topScorer = std['name']

print(f"Top Scorer: {topScorer}")