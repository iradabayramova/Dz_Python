import json
import os

def load_contacts():
    if os.path.exists('contacts.json'):
        with open('contacts.json', 'r') as file:
            return json.load(file)
    else:
        return {}

def save_contacts(contacts):
    try:
        with open('contacts.json', 'w', encoding='utf-8') as file:
            json.dump(contacts, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Ошибка при сохранении контактов:", e)
def add_contact(contacts, name, phone):
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Контакт '{name}' успешно добавлен.")

def remove_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Контакт '{name}' успешно удален.")
    else:
        print(f"Контакт '{name}' не найден.")

def view_contacts(contacts):
    if contacts:
        print("Список контактов:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Справочник пуст.")

def search_contact(contacts, name):
    name = name.strip()  # Удаляем лишние пробелы по краям введенного имени

    if name in contacts:
        print(f"Контакт '{name}': {contacts[name]}")
    else:
        print(f"Контакт '{name}' не найден.")

def modify_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        save_contacts(contacts)
        print(f"Контакт '{name}' успешно изменен.")
    else:
        print(f"Контакт '{name}' не найден.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Поиск контакта")
        print("5. Изменить контакт")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            view_contacts(contacts)
        elif choice == '2':
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            add_contact(contacts, name, phone)
        elif choice == '3':
            name = input("Введите имя для удаления: ")
            remove_contact(contacts, name)
        elif choice == '4':
            name = input("Введите имя для поиска: ")
            search_contact(contacts, name)
        elif choice == '5':
            name = input("Введите имя для изменения: ")
            new_phone = input("Введите новый номер телефона: ")
            modify_contact(contacts, name, new_phone)
        elif choice == '6':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()