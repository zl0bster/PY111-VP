def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    pairs = 0
    for character in brackets_row:
        if character == '(':
            pairs += 1
        if character == ')':
            pairs -= 1
        if pairs < 0:
            return False
    if pairs == 0:
        return True
    return False
