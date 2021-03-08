commandsList = ['+', '-', 'x', '/', '÷']

"""Contains all logic for calculator functionality"""


def divide(a, b):
    """
    Divides a by b
    :param a: first number for operation
    :type a: float
    :param b: second number for operation
    :type b: float
    :return: answer
    :rtype: str
    """
    answer = str(a / b)

    return answer


def multiply(a, b):
    """
    Multiplies a by b
    :param a: first number for operation
    :type a: float
    :param b: second number for operation
    :type b: float
    :return: answer
    :rtype: str
    """
    answer = str(a * b)

    return answer


def add(a, b):
    """
    Adds a to b
    :param a: first number for operation
    :type a: float
    :param b: second number for operation
    :type b: float
    :return: answer
    :rtype: str
    """
    answer = str(a + b)

    return answer


def subtract(a, b):
    """
    Subtracts b from a
    :param a: first number for operation
    :type a: float
    :param b: second number for operation
    :type b: float
    :return: answer
    :rtype: str
    """
    answer = str(a - b)

    return answer


def changeInt(answer):
    """
    Checks if answer is a whole number represented as a float e.g 19 > 19.0. Removes .0 after check - allows the program
    to keep answer as string instead of changing type
    :param answer: result from performed operation
    :type answer: str
    :return: answer
    :rtype: str
    """
    if answer[-2:] == ".0":
        answer = answer[:-2]

    return answer


def numberParser(request):
    """
    Finds both numbers in request and adds them to a list so they can be assigned to variables
    :param request: command from user - parsed from main.py
    :type request: str
    :return: a, b
    :rtype: float
    """

    l = []
    for t in request.split():
        try:
            l.append(float(t))
        except ValueError:
            pass
    a = l[0]
    b = l[1]

    return a, b


def start(request):
    """
    Determines which function should be performed based on whether any char in request matches commandsList
    :param request: command from user - parsed from main.py
    :type request: str
    :return: output
    :rtype: str
    """
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
