digits = "9876543210"

#создаём рекурсивную функцию для поиска выражения, которое равно 200
def find_expression(index, expression):
    #проверяем если индекс будет равен длинне цифр, то проверяем выражение на равенство 200
    if index == len(digits):
        if eval(expression) == 200:
            print(expression + "=200")
            return True
        return False

    #рекурсивнно проверяем и пытаемсядобавить текущую цифру к выражению без знака, с плюсом и с минусом
    if find_expression(index + 1, expression + digits[index]):
        return True

    if find_expression(index + 1, expression + "+" + digits[index]):
        return True

    if find_expression(index + 1, expression + "-" + digits[index]):
        return True

    return False

#запускаем функцию с начальным индексом 1 и первым символом строки digits
find_expression(1, digits[0])