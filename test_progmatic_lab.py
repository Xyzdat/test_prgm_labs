digits = "9876543210"


def find_expression(index, expression):
    # Если обработали все цифры
    if index == len(digits):
        if eval(expression) == 200:
            print(expression + "=200")
            return True
        return False

    # Пробуем три варианта:
    # 1. ничего не ставить
    if find_expression(index + 1, expression + digits[index]):
        return True

    # 2. поставить '+'
    if find_expression(index + 1, expression + "+" + digits[index]):
        return True

    # 3. поставить '-'
    if find_expression(index + 1, expression + "-" + digits[index]):
        return True

    return False


find_expression(1, digits[0])