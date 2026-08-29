const digits = "9876543210";

//создаём функцию для поиска выражения, которое равно 200
function find_expression() {
    //перебираем все возможные комбинации знаков между цифрами
    for (let number = 0; number < 3 ** 9; number++) {
      //создаём переменную для хранения текущего числа и выражения
      let n = number;
      let expression = digits[0];

      //перебираем все цифры, начиная со второй, и добавляем к выражению соответствующий знак
      for (let i = 1; i < digits.length; i++) {
        //вычисляем остаток от деления на 3, чтобы определить, какой знак использовать
        const operator = n % 3;
        n = Math.floor(n / 3);

        //добавляем к выражению соответствующий знак и цифру в зависимости от значения переменной operator
        if (operator === 0) {
          expression += digits[i];
        } else if (operator === 1) {
          expression += "+" + digits[i];
        } else {
          expression += "-" + digits[i];
        }
      }

      //проверяем, равно ли выражение 200, и если да, то выводим его в консоль
      if (eval(expression) === 200) {
        console.log(expression + "=200");
      }
    }
}

//запускаем функцию
find_expression();