def convert_to_int(value):
    try:
        result = int(value)
        print(f"Успешное преобразование: {result}")
        return result

    except ValueError:
        print("Ошибка: невозможно преобразовать значение в целое число.")

    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

    finally:
        print("Попытка преобразования завершена.")


# --- Проверка ---
print("Тест 1: корректная строка")
convert_to_int("123")

print("\nТест 2: некорректная строка")
convert_to_int("abc")

print("\nТест 3: другой тип данных (список)")
convert_to_int([1, 2, 3])
