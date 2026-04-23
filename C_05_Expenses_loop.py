def not_blank(question):
    """checks that user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response

        print("sorry this cant be blank. please try again. \n")

def num_checker(question, num_type="float"):
            """checks that the response is a float / integer more than zero"""

            if num_type == "float":
                error = "Please enter a number more than 0."

            else:
                error = "Please enter an integer more than 0."

            while True:
                try:

                    if num_type == "float":
                        response = float(input(question))
                    else:
                        response = int(input(question))

                    if response > 0:
                        return response
                    else:
                        print(error)

                except ValueError:
                    print(error)

def get_expenses (exp_type):
    """gets variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # lists for panda
    all_items = []

    #expenses dictionary

    #loop to get expenses
    while True:
        item_name = not_blank("item name: ")

        #check users enter at least one variable expense
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("oops you didn't enter anything  "
                  "you need at least one item.")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

    #return all items for now so we can check loop.
    return all_items


# main routine stars here

# print("getting variable costs")
# variable_expenses = get_expenses("variable")
# num_variable =len(variable_expenses)
# print(f"you entered {num_variable} items")
# print()

print("getting fixed costs")
fixed_expenses = get_expenses("fixed")
num_fixed = len(fixed_expenses)
print(f"you entered {num_fixed} items.")