def checking_braces(s) -> bool:
    """
    Checks the correctness of the parenthesis sequence
    of round, square and curly brackets

    >>> checking_braces("((13[]({})[]))")
    True
    >>> checking_braces("(5+(2*6+7)-8)+[45}*{0}")
    False
    >>> checking_braces("((")
    False
    >>> checking_braces("([]{5*df}77)")
    True
    >>> checking_braces("9}")
    False

    """
    stack = []
    right = ""

    for brace in s:
        if brace not in "()[]{}":
            continue
        if brace in "([{":
            stack.append(brace)

        elif brace in ")]}":
            if len(stack) < 1:
                return False
            if stack[-1] == "(":
                right = ")"
            elif stack[-1] == "[":
                right = "]"
            elif stack[-1] == "{":
                right = "}"
            else:
                assert stack[-1] in "([{", "opening bracket expected " + str(stack[-1])

            if right != brace:
                return False

            stack.pop()

    return len(stack) < 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    # for silent testing, replace with doctest.testmod()
