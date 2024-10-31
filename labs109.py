def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

def is_ascending(items):
    if len(items) == 0 or len(items) == 1:
        return True
    bool_check_list = []
    for x in range(len(items) - 1):
        if (items[x+1] - items[x]) >= 1:
            bool_check_list.append(True)
        else:
            bool_check_list.append(False)
    if False in bool_check_list:
        return False
    else:
        return True
