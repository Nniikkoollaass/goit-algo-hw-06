from collections import UserDict
from dataclasses import dataclass

@dataclass
class Field:
    value: str

@dataclass
class Name(Field):
    # реалізація класу
	value: str

@dataclass
class Phone(Field):
    # реалізація класу
    def __init__(self, number: int):
        if len(number) == 10 \
            and str(number).isdigit():
            self.value = number

@dataclass
class Record:
    name = Name
    def __init__(self, name: int):
        self.name = name
        self.phones = []
    # реалізація класу
    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"
    # додавання телефону
    def add_phone(self, phone: str):
        if phone.isdigit():
            self.phones.append(Phone(phone))
            return "Phone added.\n"
        else:
            return "Please use digits to add a phone number."
    # видалення телефону
    def remove_phone(self, phone: Phone):
        if type(phone)==Phone:
            self.phones.remove(phone)
            return "Phone deleted.\n"
        else:
            return "Please use Phone object to remove phone number."
    # редагування телефону
    def edit_phone(self, old_phone_number: str, new_phone_number: str):
        if old_phone_number.isdigit() and new_phone_number.isdigit():
            index_of_phone_record = self.phones.index(Phone(old_phone_number))
            self.phones[index_of_phone_record] = Phone(new_phone_number)
            return "Phone changed.\n"
        else:
            return "Please use two digits to edit phone number."
    # пошук телефона
    def find_phone(self, phone: str):
        if phone.isdigit():
            if Phone(phone) in self.phones:
                return phone
            else:
                return f"The phone {phone} is not found."
        else:
            return "Please use digits to find phone number."

@dataclass
class AddressBook(UserDict):
    data = {}
    # реалізація класу
    # додавання нового контакту
    def add_record(self, record: Record):
        if type(record)==Record:
            self.data[record.name] = record
            return "Record added.\n"
        else:
            return "Please use Record object to add the record."
    # видалення контакту за ім'ям
    def delete(self, name: str):
        if name.isalpha():
            self.data.pop(name)
            return "Record deleted.\n"
        else:
            return "Please use srting name to delete the record."
        # пошук контакту
    def find(self, name: str) -> Record:
        if name.isalpha():
            if self.data.get(name) is not None:
                return self.data.get(name)
            else:
                print(f"Record witn name {name} is not found.")
        else:
            return "Please use string name to find the record."

###############################################################
# ПЕРЕВІРКА РОБОТИ ЛОГІКИ
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
print(john_record)
print("1------------------------------------------")
john_record.add_phone("5555555555")
print(john_record)
print("2------------------------------------------")
# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
print(john_record)
print("3------------------------------------------")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print("------------------------------------------")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

print("33------------------------------------------")
print(john_record)
print(jane_record)
# Видалення запису Jane
book.delete("Jane")

print("44------------------------------------------")
for name, record in book.data.items():
    print(record)

# видалення номера у записі
print("55------------------------------------------")
john_record.remove_phone(Phone("1112223333"))
print(john_record)
