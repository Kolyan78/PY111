import a0_my_stack
def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    result = 0
    for i in brackets_row:
        if i == "(":
            result += 1
        elif i == ")":
            result -= 1
    if result == 0:
        return True
    return False

print(check_brackets("(()("))
print(check_brackets("(()))"))
print(check_brackets("(()))"))
print(check_brackets(")("))
print(check_brackets(")()("))