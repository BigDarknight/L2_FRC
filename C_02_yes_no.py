def yes_no(question):
    """checks user response to question is yes or no/y or n then returns yes or no"""
    while True:
        response = input(question).lower()
        #user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes (y) or no (n) \n")

#testing loop
while True:
    want_instructions = yes_no("do you want to read the instructions? ")
    print(f"you chose {want_instructions} \n")