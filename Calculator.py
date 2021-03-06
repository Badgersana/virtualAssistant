commandsList = ['+', '-', 'x', '/', '÷']


def divide(a, b):
    answer = str(a / b)

    return answer


def multiply(a, b):
    answer = str(a * b)

    return answer


def add(a, b):
    answer = str(a + b)

    return answer


def subtract(a, b):
    answer = str(a - b)

    return answer


# checks if whole number is represented as float instead of int, and removes '.0' from the end > 19.0 - 19
def changeInt(answer):
    if answer[-2:] == ".0":
        answer = answer[:-2]

    return answer

# finds the two numbers in calculation request and adds them to a list, to be assigned to variables
def numberParser(request):
    l = []
    for t in request.split():
        try:
            l.append(float(t))
        except ValueError:
            pass
    a = l[0]
    b = l[1]

    return a, b


# determines which command is in request and performs action based
def start(request):
    a, b = numberParser(request)

    # addition
    if commandsList[0] in request:
        output = add(a, b)

    # subtraction
    elif commandsList[1] in request:
        output = subtract(a, b)

    # multiplication
    elif commandsList[2] in request:
        output = multiply(a, b)

    # division
    elif commandsList[3] or commandsList[4] in request:
        output = divide(a, b)

    output = changeInt(output)

    return output
