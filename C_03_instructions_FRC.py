def instructions():
    print(make_statement("instructions", "ℹ️"))

    print('''
    
    this program will ask you for ...
    -the name of the product you are selling
    -how many items you plan on selling
    -the costs for each component of the product
    (variable experiences)
    -whether or not you have fixed expenses 
    (if you have fixed expenses it will ask you what they are)
    -how much money you want to make (ie: your profit goal)
    
    it will also ask you how much the recommended sales price should be rounded to.
    
    the program outputs an itemized list of the variable and fixed expenses 
    (which includes the subtotals of these expenses)
    ''')

def make_statement(statement, decoration):
    """add decoration at the start and end of text"""
    return f"{decoration * 3} {statement} {decoration * 3} \n"

def string_check(question, valid_answers =('yes', 'no'),
                 num_letters=1):
    """checks that the user enters the full word
    or 'n' letter/s of a word fom a list of responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:
            if response == item:
                return item

            elif response == item[:num_letters]:
                return item

        print(f"please choose an option from {valid_answers}")


print(make_statement("fund raising calculator", "💰"))

want_instructions = string_check("do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()




