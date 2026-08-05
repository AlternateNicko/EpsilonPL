import json

code = {
    # ALL OF THE FOLLOWING ERROR CODES FROM 1-70 ARE PRE EXISTING ERROR CODES
    # ERROR CODES ABOVE IT ARE UPDATED/ADDED ERRORS TO THE PROGRAMMING LANGUAGE
    # main important errors
    1: {
        "response": "SyntaxError: Instruction `{arg1}` is not a valid syntax",
        "error": "SyntaxError"
    },
    2: {
        "response": "ValueError: Give value is invalid",
        "error": "ValueError"
    },
    3: {
        "response": "TypeError: Invalid type for instruction `{arg1}`",
        "error": "TypeError"
    },
    4: {
        "response": "ZeroDivisionError: Cannot divide from 0",
        "error": "ZeroDivisionError"
    },
    5: {
        "response": "ModuleError: Module `{arg1}` is not found",
        "error": "ModuleError"
    },
    6: {
        "response": "SyntaxError: Given built in function `{arg1}` is not found",
        "error": "SyntaxError"
    },
    7: {
        "response": "MemoryError: Maximum memory is reached",
        "error": "MemoryError"
    },
    8: {
        "response": "SyntaxError: Built in method `{arg1}` is not found",
        "error": "SyntaxError"
    },
    9: {
        "response": "SyntaxError: No starting curly braces `{` at the start of an code block",
        "error": "SyntaxError"
    },
    10: {
        "response": "ParsingError: This is mostly Npp's source code fault and not a problem within your npp program",
        "error": "ParsingError"
    },
    # Errors from keywords
    11: {
        "response":  "TypeError: Expected value type of condition is `bool` but got `{arg1}`",
        "error": "TypeError"
    },
    12: {
        "response": "TypeError: Function `{arg1}` takes {arg2} amount of arguments, but {arg3} is given",
        "error": "TypeError"
    },
    13: {
        "response": "TypeError: Class method `{arg1}` takes {arg2} amount of arguments, but {arg3} is given",
        "error": "TypeError"
    },
    14: {
        "response": "IndexError: Length of `{arg1}` is `{arg2}` but `{arg3}` is out of range",
        "error": "IndexError"
    },
    15: {
        "response": "TypeError: Given variable `{arg1}` is not a list -> type `{arg2}`",
        "error": "TypeError"
    },
    16: {
        "response": "NameError: Inherited parent class `{arg1}` is not found in child class `{arg2}`",
        "error": "NameError"
    },
    17: {
        "response": "NameError: Method `{arg1}` is not found with in class `{arg2}",
        "error": "NameError"
    },
    18: {
        "response": "NameError: Name `{arg1}` is not a defined variable",
        "error": "NameError"
    },
    19: {
        "response": "SyntaxError: Syntax `break` is currently not inside a loop",
        "error": "SyntaxError"
    },
    20: {
        "response": "SyntaxError: Syntax `continue` is currently not inside a loop",
        "error": "SyntaxError"
    },
    21: {
        "response": "NameError: Name `{arg1}` is not a defined variable",
        "error": "NameError"
    },
    22: {
        "response": "SyntaxError: Invalid use case of `else if` syntax, no if-statement starting line",
        "error": "SyntaxError"
    },
    23: {
        "response": "SyntaxError: invalid else statement syntax use, no if and/or else if statement use before else",
        "error": "SyntaxError"
    },
    24: {
        "response": "NameError: Error name `{arg1}` is not an available error name",
        "error": "NameError"
    },
    25: {
        "response": "SyntaxError: Invalid catch syntax, no attempt statement was found before catch was parsed",
        "error": "SyntaxError"
    },
    26: {
        "response": 'SyntaxError: Invalid name for error `{arg1}`, given must end with a "Error" suffix',
        "error": "SyntaxError"
    },
    27: {
        "response": "SyntaxError: Invalid given arguments for `throw` keyword",
        "error": "SyntaxError"
    },
    28: {
        "response": "ModuleError: Cannot access directory `{arg1}`, it's not an available directory, perhaps try a different directory",
        "error": "ModuleError"
    },
    29: {
        "response": "ModuleError: Module `{arg1}` is not found",
        "error": "ModuleError"
    },
    30: {
        "response": "SyntaxError: Keyword `rename` requires `as` to split both library and renamed library name, but got `{arg1}`",
        "error": "SyntaxError"
    },
    31: {
        "response": "SyntaxError: Cannot convert `{arg1}` to `{arg2}` due to containing a special character",
        "error": "SyntaxError"
    },
    32: {
        "response": "NameError: Name `{arg1}` is not a variable",
        "error": "NameError"
    },
    33: {
        "response": "NameError: Name `{arg1}` is not a defined host variable",
        "error": "NameError"
    },
    34: {
        "response": "NameError: Name `{arg1}` is not defined with in `{arg2}` syncronization group",
        "error": "NameError"
    },
    35: {
        "response": "TypeError: No such file type named `{arg1}`",
        "error": "TypeError"
    },
    36: {
        "response": "ValueError: Name `{arg1}` contains a special character the function couldn't support",
        "error": "ValueError"
    },
    # Built In Functions
    37: {
        "response": "ValueError: Value `{arg1}` cannot be evaluated",
        "error": "ValueError"
    },
    38: {
        "response": "TypeError: Second given argument to sort() is not a boolean value",
        "error": "TypeError"
    },
    39: {
        "response": "TypeError: sort() expected 2 arguments, but got `{arg1}` arguments instead",
        "error": "TypeError"
    },
    40: {
        "response": "TypeError: sort() 1st given argument is not a list",
        "error": "TypeError"
    },
    41: {
        "response": "ValueError: Given value `{arg1}` is not a list",
        "error": "ValueError"
    },
    42: {
        "response": "TypeError: Expected arguments for dict() are `2` but got `{arg1}`",
        "error": "TypeError"
    },
    43: {
        "response": "TypeError: Both arguments must be at the same length",
        "error": "TypeError"
    },
    44: {
        "response": "ValueError: `{arg1}` is an invalid number system type",
        "error": "ValueError"
    },
    45: {
        "response": "SyntaxError: Invalid parameter for num() function",
        "error": "SyntaxError"
    },
    46: {
        "response": "ValueError: Cannot print out content `{arg1}`",
        "error": "ValueError"
    },
    47: {
        "response": "TypeError: range() 1st argument is not a interger",
        "error": "TypeError"
    },
    48: {
        "response": "TypeError: range() 2nd argument `{arg1}` is not an interger",
        "error": "TypeError"
    },
    49: {
        "response": "TypeError: range() 3rd argument `{arg1}` is not an interger",
        "error": "TypeError"
    },
    # Methods
    50: {
        "response": "ValueError: Can't push variable as it is not a list",
        "error": "ValueError"
    },
    51: {
        "response": "TypeError: Cannot evaluate expression `{arg1}`",
        "error": "TypeError",
    },
    52: {
        "response": "TypeError: Given variable or value type is not a set",
        "error": "TypeError"
    },
    53: {
        "response": "ValueError: The data type given of the variable `{arg1}` -> `{arg2}` is not a set",
        "error": "ValueError"
    },
    54: {
        "response": "SyntaxError: cap() method doesn't support any arguments",
        "error": "SyntaxError"
    },
    55: {
        "response": "TypeError: Given value `{arg1}` is not a string",
        "error": "TypeError"
    },
    56: {
        "response": "TypeError: low() method doesn't expext an argument, but `{arg1}` is given",
        "error": "TypeError"
    },
    57: {
        "response": "TypeError: as() method expected a string argument, not `{arg1}`",
        "error": "TypeError"
    },
    58: {
        "response": "ValueError: `{arg1}` can't be converted into `{arg2}`",
        "error": "ValueError"
    },
    59: {
        "response": "SyntaxError: Invalid expression of pop() method !-> `{arg1}`",
        "error": "SyntaxError"
    },
    60: {
        "response": "IndexError: pop() method index is out of range",
        "error": "IndexError"
    },
    61: {
        "response": "TypeError: `{arg1}` is not a list" ,
        "error": "TypeError"
    },
    # Calling Errors
    62: {
        "response": "NameError: Name `{arg1}` is not a defined class",
        "error": "NameError"
    },
    63: {
        "response": "NameError: Name `{arg1}` is not a defined function",
        "error": "NameError"
    },
    64: {
        "response": "NameError: Name `{arg1}` is not a defined class method for `{arg2}`",
        "error": "NameError"
    },
    65: {
        "response": "LocalBoundError: Function `{arg1}` cannot be access within the local function scope",
        "error": "LocalBoundError"
    },
    66: {
        "response": "TypeError: Given argument `{arg1}` can't be passed through to `{arg2}`",
        "error": "TypeError"
    },
    # Others
    67: {
        "response": "TypeError: `{arg1}` cannot be created without an ending `{arg2}` bracket/parenthesis",
        "error": "TypeError"
    },
    68: {
        "response": "SyntaxError: {arg1}",
        "error": "SyntaxError"
    },
    69: {
        "response": "TypeError: {arg1}",
        "error": "TypeError"
    },
    70: {
        "response": "ValueError: {arg1}",
        "error": "ValueError"
    },
    # Newly added, 70 and above
    71: {
        "response": "AccessError: Method `{arg1}` in class `{arg2}` is private and cannot be called from outside the class",
        "error": "AccessError"
    }
}

with open("errormd.json", "w") as file:
    json.dump(code, file)