def validate_user_input(data):
    # Проверяем, что data — словарь
    if not isinstance(data, dict):
        raise TypeError("Ожидается словарь с данными пользователя.")

    # Проверяем наличие ключа name
    if "name" not in data:
        raise ValueError("Отсутствует ключ 'name'.")
    if not isinstance(data["name"], str):
        raise ValueError("Значение по ключу 'name' должно быть строкой.")

    # Проверяем наличие и корректность ключа age
    if "age" not in data:
        raise ValueError("Отсутствует ключ 'age'.")

    try:
        age = data["age"]
        if not (isinstance(age, int) and age > 0):
            raise ValueError("Возраст должен быть положительным целым числом.")
    except Exception as e:
        raise ValueError("Ошибка при проверке возраста.") from e

    print("Данные корректны:", data)
    return True


# --- Проверка ---
print("Тест 1: корректные данные")
validate_user_input({"name": "Alice", "age": 30})

print("\nТест 2: отсутствует name")
try:
    validate_user_input({"age": 20})
except Exception as e:
    print("Поймано исключение:", e)

print("\nТест 3: некорректный возраст")
try:
    validate_user_input({"name": "Bob", "age": -5})
except Exception as e:
    print("Поймано исключение:", e)

print("\nТест 4: некорректный тип входных данных")
try:
    validate_user_input("not a dict")
except Exception as e:
    print("Поймано исключение:", e)
