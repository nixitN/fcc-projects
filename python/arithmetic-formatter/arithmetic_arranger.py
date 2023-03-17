import re

def arithmetic_arranger(problems, solve = False):
    if(len(problems) > 5):
        return "Error: Too many problems."
    
    first_row = ""
    second_row = ""
    lines = ""
    summary = ""
    string = ""

    for problem in problems:
        if(re.search("[^\s0-9.+-]", problem)):
            if(re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        
        first_number = problem.split(" ")[0]
        operator = problem.split(" ")[1]
        second_number = problem.split(" ")[2]

        if(len(first_number) >= 5 or len(second_number) >= 5):
            return "Error: Numbers cannot be more than four digits."
        
        sum = ""
        if(operator == "+"):
            sum = str(int(first_number) + int(second_number))
        elif(operator == "-"):
            sum = str(int(first_number) - int(second_number))

        length = max(len(first_number), len(second_number)) + 2
        top = str(first_number).rjust(length)
        bottom = operator + str(second_number).rjust(length - 1)
        line = ""
        value = str(sum).rjust(length)
        for s in range(length):
            line += "-"

        if problem != problems[-1]:
            first_row += top + '    '
            second_row += bottom + '    '
            lines += line + '    '
            summary += value + '    '
        else:
            first_row += top
            second_row += bottom
            lines += line
            summary += value

    if solve:
        string = first_row + "\n" + second_row + "\n" + lines + "\n" + summary
    else:
        string = first_row + "\n" + second_row + "\n" + lines
    return string