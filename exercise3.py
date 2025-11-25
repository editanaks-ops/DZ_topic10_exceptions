class NegativeNumberError(Exception):
    def __init__(self, value, message="Число не должно быть отрицательным"):
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.message}. Получено значение: {self.value}"


def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    print(f"Число положительное: {number}")
    return True


# --- Проверка ---
print("Тест 1: отрицательное число")
try:
    check_positive_number(-10)
except NegativeNumberError as e:
    print("Поймано исключение:", e)

print("\nТест 2: положительное число")
check_positive_number(15)
