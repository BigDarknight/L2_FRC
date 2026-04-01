def make_statement(statement, decoration):
    """add decoration at the start and end of text"""
    return f"{decoration * 3} {statement} {decoration * 3} \n"


# Main routine goes here
print( make_statement("instructions", decoration= "ℹ️"))

