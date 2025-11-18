from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)     
        self.phones = []           

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone):
        target = self.find_phone(phone)
        if target:
            self.phones.remove(target)
        else:
            raise ValueError("Phone not found")

    def edit_phone(self, old_phone, new_phone):
        old_obj = self.find_phone(old_phone)
        if not old_obj:
            raise ValueError("Old phone not found")

        new_obj = Phone(new_phone)        
        old_obj.value = new_obj.value    

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

# Видалення запису Jane
book.delete("Jane")

"""
Вивід:
Contact name: John, phones: 1234567890; 5555555555
Contact name: Jane, phones: 9876543210
Contact name: John, phones: 1112223333; 5555555555
John: 5555555555
"""