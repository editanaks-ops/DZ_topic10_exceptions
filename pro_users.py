# ==== Пользовательские исключения ====

class UserAlreadyExistsError(Exception):
    """Ошибка: пользователь с таким именем уже существует."""
    def __init__(self, username):
        self.username = username
        super().__init__(f"Пользователь '{username}' уже существует.")


class UserNotFoundError(Exception):
    """Ошибка: пользователь с таким именем не найден."""
    def __init__(self, username):
        self.username = username
        super().__init__(f"Пользователь '{username}' не найден.")


# ==== Модель пользователя ====

class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}', age={self.age})"


# ==== Менеджер пользователей ====

class UserManager:
    def __init__(self):
        self.users = {}  # ключ — username, значение — объект User

    def add_user(self, user: User):
        if user.username in self.users:
            raise UserAlreadyExistsError(user.username)
        self.users[user.username] = user
        print(f"Пользователь добавлен: {user}")

    def remove_user(self, username: str):
        if username not in self.users:
            raise UserNotFoundError(username)
        del self.users[username]
        print(f"Пользователь '{username}' удалён.")

    def find_user(self, username: str) -> User:
        if username not in self.users:
            raise UserNotFoundError(username)
        return self.users[username]


# ==== Тестирование функционала ====

if __name__ == "__main__":
    manager = UserManager()

    print("\n=== Тест 1: добавление пользователей ===")
    try:
        manager.add_user(User("alice", "alice@mail.com", 30))
        manager.add_user(User("bob", "bob@mail.com", 25))
        manager.add_user(User("alice", "alice2@mail.com", 40))  # повторное имя
    except UserAlreadyExistsError as e:
        print("Ошибка:", e)

    print("\n=== Тест 2: удаление существующего и несуществующего пользователя ===")
    try:
        manager.remove_user("bob")
        manager.remove_user("charlie")  # такого нет
    except UserNotFoundError as e:
        print("Ошибка:", e)

    print("\n=== Тест 3: поиск пользователя ===")
    try:
        user = manager.find_user("alice")
        print("Найден:", user)

        manager.find_user("david")  # нет такого
    except UserNotFoundError as e:
        print("Ошибка:", e)
