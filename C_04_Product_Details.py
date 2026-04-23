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

def not_blank(question):
    """checks that user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response

        print("sorry this cant be blank. please try again. \n")

#main routine goes here

#loop for testing
while True:
    product_name = not_blank("product name: ")
    quantity_made = num_checker(question= "Quantity being made:", num_type= "integer")
    print(f"you are making {quantity_made} of {product_name}")
    print()