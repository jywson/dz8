class PhoneBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                contacts = {}
                for line in file:
                    data = line.strip().split(':')
                    name = data[0]
                    number = data[1]
                    email = data[2] if len(data) > 2 else ""  # Добавляем проверку на наличие адреса электронной почты
                    contacts[name] = {'number': number, 'email': email}
                return contacts
        except FileNotFoundError:
            return {}


    def save_contacts(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for name, info in self.contacts.items():
                file.write(f"{name}:{info['number']}:{info['email']}\n")

    def display_contacts(self):
        if not self.contacts:
            print("Справочник пуст")
        else:
            print("Телефонный справочник:")
            for idx, (name, info) in enumerate(self.contacts.items(), start=1):
                print(f"{idx}. {name}: {info['number']} ({info['email']})")

    def add_contact(self, name, number, email):
        self.contacts[name] = {'number': number, 'email': email}
        self.save_contacts()
        print(f"Контакт {name} добавлен в справочник.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print("Контакт удален из справочника.")
        else:
            print("Контакт не найден.")

    def edit_contact(self, name, new_number, new_email):
        if name in self.contacts:
            self.contacts[name]['number'] = new_number
            self.contacts[name]['email'] = new_email
            self.save_contacts()
            print("Контакт отредактирован.")
        else:
            print("Контакт не найден.")

    def copy_contact_to_another_file(self, index, destination_filename):
        if 1 <= index <= len(self.contacts):
            contact_names = list(self.contacts.keys())
            contact_to_copy = self.contacts[contact_names[index - 1]]
            with open(destination_filename, 'a', encoding='utf-8') as destination_file:  # добавляем параметр encoding
                destination_file.write(f"{contact_names[index - 1]}:{contact_to_copy['number']}:{contact_to_copy['email']}\n")
            print("Контакт скопирован в другой файл.")
        else:
            print("Неверный номер контакта.")


def main():
    filename = "phonebook.txt"
    phonebook = PhoneBook(filename)

    while True:
        print("\nВыберите действие:")
        print("1. Показать контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Редактировать контакт")
        print("5. Скопировать контакт в другой файл")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            phonebook.display_contacts()
        elif choice == '2':
            name = input("Введите имя: ")
            number = input("Введите номер телефона: ")
            email = input("Введите адрес электронной почты: ")
            phonebook.add_contact(name, number, email)
        elif choice == '3':
            name = input("Введите имя контакта для удаления: ")
            phonebook.remove_contact(name)
        elif choice == '4':
            name = input("Введите имя контакта для редактирования: ")
            new_number = input("Введите новый номер телефона: ")
            new_email = input("Введите новый адрес электронной почты: ")
            phonebook.edit_contact(name, new_number, new_email)
        elif choice == '5':
            try:
                index = int(input("Введите номер контакта для копирования: "))
                destination_filename = input("Введите имя файла, в который нужно скопировать контакт: ")
                phonebook.copy_contact_to_another_file(index, destination_filename)
            except ValueError:
                print("Неверный ввод. Введите число.")
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()