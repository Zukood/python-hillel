class Record:
    def __init__(self, name, phone, last_name=None, date_of_birth=None):
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._date_of_birth = date_of_birth

    @property
    def name(self):
        return self._name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone(self):
        return self._phone

    @property
    def date_of_birth(self):
        return self._date_of_birth


class Directory:
    def __init__(self):
        self._records = []

    def add_record(self, record):
        self._records.append(record)

    def remove_record(self, record):
        if record not in self._records:
            print("Запись не найдена.")
        else:
            self._records.remove(record)

    def edit_record(self, record, new_name=None, new_last_name=None, new_phone=None, new_date_of_birth=None):
        if record not in self._records:
            print("Запись не найдена.")
        else:
            if new_name:
                record._name = new_name
            if new_last_name:
                record._last_name = new_last_name
            if new_phone:
                record._phone = new_phone
            if new_date_of_birth:
                record._date_of_birth = new_date_of_birth


class Interface:
    @staticmethod
    def read_name():
        name = input("Введите имя: ")
        return name

    @staticmethod
    def read_last_name():
        last_name = input("Введите фамилию: ")
        return last_name

    @staticmethod
    def read_phone():
        phone = input("Введите телефон: ")
        return phone

    @staticmethod
    def read_date_of_birth():
        date_of_birth = input("Введите дату рождения: ")
        return date_of_birth

    @staticmethod
    def print_record(record):
        print(f"Имя: {record.name}")
        print(f"Фамилия: {record.last_name}")
        print(f"Телефон: {record.phone}")
        print(f"Дата рождения: {record.date_of_birth}")


def main():
    directory = Directory()

    # Создание записей
    record1 = Record("Иван", "1234567890")
    record2 = Record("Петр", "9876543210", "Иванов", "01.01.1990")

    # Добавление записей в справочник
    directory.add_record(record1)
    directory.add_record(record2)

    # Вывод записей
    for record in directory._records:
        Interface.print_record(record)

    # Удаление записи
    directory.remove_record(record1)

    # Редактирование записи
    directory.edit_record(record2, new_name="Новое имя")

    # Вывод измененной записи
    Interface.print_record(record2)


if __name__ == "__main__":
    main()
