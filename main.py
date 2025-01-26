
try:
    start = input("Welcome at our program. Let's find the best car for you "
              "To start, type 'start' ").lower()
    if start != "start":
        raise ValueError("To start the program, you have to write 'start'")
except:
    print("Error")


engine_on = False
if start == "start":
    engine_on = True

# while engine_on is True:

    cars = {
        "Dodge RAM": [],
        "Aston Martin DB12": [],
        "Toyota Supra": [],

    }

def question1():
    answer1 = input("Do you like tanks? Type 'yes' or 'no' ").lower()
    if answer1 == "yes":
        cars["Dodge RAM"].append(1)

def question2():
    answer2 = input("Do you like to drift? Type 'yes' or 'no' ").lower()
    if answer2 == "yes":
        cars["Toyota Supra"].append(2)

def question3():
    answer3 = input("Is your surname 'Bond'? Type 'yes' or 'no' ").lower()
    if answer3 == "yes":
        cars["Aston Martin DB12"].append(3)

class Engine():
    def __init__(self, answer1, answer2, answer3):
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3

def count(dodge,supra,db12):
    dodge = Engine(answer1="yes",answer2="no",answer3="no")
    supra = Engine(answer1="no",answer2="yes",answer3="no")
    db12 = Engine(answer1="no",answer2="no",answer3="yes")

count(dodge=question1(),supra=question2(),db12=question3())

answer_dodge = "The best car for you is a Dodge RAM, nice!"
answer_supra = "The best car for you is a Toyota Supra, well done!"
answer_db12 = "Great choice, Mr./Mrs. Bond"

def answer(answer_dodge,answer_supra,answer_db12):
    if cars["Dodge RAM"] == [1] and cars["Toyota Supra"] == [] and cars["Aston Martin DB12"] == []:
        print(answer_dodge)
    elif cars["Toyota Supra"] == [2] and cars["Dodge RAM"] == [] and cars["Aston Martin DB12"] == []:
        print(answer_supra)
    elif cars["Aston Martin DB12"] == [3] and cars["Dodge RAM"] == [] and cars["Toyota Supra"] == []:
        print(answer_db12)


""" ----------- new class ------------- """

answer(answer_dodge,answer_supra,answer_db12)
check = [cars.values()]
ev = cars["Aston Martin DB12"] + cars["Dodge RAM"] + cars["Toyota Supra"]
# print(ev)
# print(len(ev))
if len(ev) < 2:
    pass
else:
    print("In that case, we need to ask another question.")
    answer4 = input("Do you prefer speed, size or old school? ").lower()
    if answer4 == "speed":
        cars["Aston Martin DB12"].append(1)
        if len(cars["Aston Martin DB12"]) >= 2:
            print(f"Aston Martin is for you. {answer_db12}")
    elif answer4 == "size":
        cars["Dodge RAM"].append(1)
        if len(cars["Dodge RAM"]) >= 2:
            print(answer_dodge)
    elif answer4 == "old school":
        cars["Toyota Supra"].append(1)
        if len(cars["Toyota Supra"]) >= 2:
            print(answer_supra)

# print(ev)
# print(len(ev))

""" -------------- new class -------------- """

if len(cars["Aston Martin DB12"] and cars["Dodge RAM"] and cars["Toyota Supra"]) == 1:
    pass
else:    
    print("Okay, now last question")
    answer5 = input("Do you prefer luxury, safety or fun? ").lower()
    if answer5 == "luxury":
        cars["Aston Martin DB12"].append(1)
        if len(cars["Aston Martin DB12"]) >= 2:
            print(f"Aston Martin DB12 is for you. {answer_db12}")
    elif answer5 == "safety":
        cars["Dodge RAM"].append(1)
        if len(cars["Dodge RAM"]) >= 2:
            print(answer_dodge)
    elif answer5 == "fun":
        cars["Toyota Supra"].append(1)
        if len(cars["Toyota Supra"]) >= 2:
            print(answer_supra)


""" ------------ naw class "another" with charts from matplotlib and pandas ---------- """



""" ------------- new class comparing with compared information about cars ------------- """
