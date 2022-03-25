import requests


class Val():
    """
    Класс, создающий словарь валют. Из файла берутся строки с валютой, но в конечный словарь
    попадают только два значения - код валюты и курс ('Value'). Остальные данные не используются за ненадобностью
    Для получения курса валюты необходимо использовать элемент словаря, например rate['USD'].
    Данный класс наследуется классом Money, чтобы один раз создать словать и работать с ним дальше.
    """
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    rate = {}
    for valute_name in data['Valute']:
        rate[valute_name] = data['Valute'][valute_name]['Value']


class Money(Val):
    def __init__(self, value: float, valute="RUR"):
        self.value = value
        self.valute = valute

    def convert_to_usd(self):
        """
        Конвертирование любой валюты в USD
        :return: валюта сконвертированная в USD, значение выдается с округлением до 2-х знаков после запятой
        """
        if self.valute == "RUR":
            """
            Если валюта RUR, то просто разделим на курс USD
            """
            return Money(round(self.value / self.rate["USD"], 2), "USD")
        else:
            """
            А если валюта другая, то сначала переведем в RUR, а потом в USD
            """
            return Money(round(self.value * self.rate[self.valute] / self.rate["USD"], 2), "USD")

    def convert_to_valute(self, valute):
        """
        Конвертирование любой валюты в любую.
        :param valute: буквенное значение валюты RUR, USD, EUR и т.д.
        :return: валюта сконвертированная, значение выдается с округлением до 2-х знаков после запятой
        """
        if self.valute == valute:  # если указаны одинаковые начальная и конечная валюты, то вернуть исходное значение
            result = self.value
        elif self.valute == "RUR":  # если исходная валюта RUR, то разделить ее на нужный курс
            result = self.value / self.rate[valute]
        elif valute == "RUR":  # если конечноая валюта RUR, то умножим ее на нужный курс
            result = self.value * self.rate[self.valute]
        else:  # если исходная и конечная валюты не RUR, то сначала переведем в RUR, а потом куда нужно.
            result = (self.value * self.rate[self.valute]) / self.rate[valute]
        return Money(round(result, 2), valute)

    def __add__(self, other):
        return Money(self.value + (other if isinstance(other, (float, int)) else other.value))

    def __sub__(self, other):
        return Money(self.value - (other if isinstance(other, (float, int)) else other.value))

    def __mul__(self, other):
        return Money(self.value * other)

    def __truediv__(self, other):
        return Money(self.value / other)

    def __eq__(self, other):
        if self.value == (other if isinstance(other, (float, int)) else other.value):
            return True
        return False

    def __ne__(self, other):
        if self.value != (other if isinstance(other, (float, int)) else other.value):
            return True
        return False

    def __gt__(self, other):
        if self.value > (other if isinstance(other, (float, int)) else other.value):
            return True
        return False

    def __lt__(self, other):
        if self.value < (other if isinstance(other, (float, int)) else other.value):
            return True
        return False

    def __ge__(self, other):
        if self.value >= (other if isinstance(other, (float, int)) else other.value):
            return True
        return False

    def __le__(self, other):
        if self.value <= (other if isinstance(other, (float, int)) else other.value):
            return True
        return False

    def __str__(self):
        return f"{self.value:.2f} {self.valute}"


print("Операции с классами:\n")
m1 = Money(180.80)
print(f"Экземпляр класса m1: {m1}")
m2 = Money(260.60)
print(f"Экземпляр класса m2: {m2}\n")
m3 = m1 + m2
print(f"Сложение экземпляров класса. m3: {m1} + {m2} = {m3}")
x = 2.58
print(f"Сложение экземпляра класса и числа: {m1} + {x} = {m1 + x}\n")
m4 = m1 - m2
print(f"Вычитание экземпляров класса. m4: {m1} - {m2} = {m4}")
print(f"Вычитание числа из класса: {m2} - {x} = {m2 - x}\n")
m5 = m1 * x
print(f"Умножение экземпляра на число. m5: {m1} * {x} = {m1 * x}")
m6 = m2 / x
print(f"Деление экземпляра на число. m6: {m2} / {x} = {m2 / x}")
print("-------------------------------------------------------------------\n")
print("Функции сравнения двух экземпляров и экземпляра с числом:\n")
print(f"Равенство m1 и m2:", True if m1 == m2 else False)
print(f"Равенство m1 и 180.8:", True if m1 == 180.8 else False, "\n")
print(f"Неравенство m1 и m2:", True if m1 != m2 else False)
print(f"Неравенство m1 и 180.8:", True if m1 != 180.8 else False, "\n")
print(f"m1 > m2:", True if m1 > m2 else False)
print(f"m1 > 1.2", True if m1 > 1.2 else False, "\n")
print(f"m1 < m2:", True if m1 < m2 else False)
print(f"m1 < 1.2", True if m1 < 1.2 else False, "\n")
print(f"m1 >= m2:", True if m1 >= m2 else False)
print(f"m1 >= 1.2", True if m1 >= 1.2 else False, "\n")
print(f"m1 <= m2:", True if m1 <= m2 else False)
print(f"m1 <= 1.2", True if m1 <= 1.2 else False)
print("-------------------------------------------------------------------\n")
print(f"Конвертация курсов\n")
print(f"Курс USD: {Money.rate['USD']}")
print(f"Курс EUR: {Money.rate['EUR']}\n")
m7 = m1.convert_to_usd()
print(f"{m1} -> {m7}")
m8 = m2.convert_to_usd()
print(f"{m2} -> {m8}")
m9 = Money(1, "EUR")
m10 = m9.convert_to_usd()
print(f"{m9} -> {m10}")
m11 = m9.convert_to_valute("RUR")
print(f"{m9} -> {m11}")
m12 = m9.convert_to_valute("GBP")
print(f"{m9} -> {m12}")
m13 = m1.convert_to_valute("RUR")
print(f"{m1} -> {m13}")
m14 = m1.convert_to_valute("EUR")
print(f"{m1} -> {m14}")
