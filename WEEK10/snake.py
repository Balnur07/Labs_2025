import psycopg2
import csv
from config import load_config

# Подключение к базе данных PostgreSQL
def insert_or_update_user(name, phone_number):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
                count = cur.fetchone()[0]

                if count > 0:
                    # Обновление существующего контакта
                    cur.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s", (phone_number, name))
                    print(f"Контакт {name} обновлен.")
                else:
                    # Вставка нового контакта
                    cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone_number))
                    print(f"Контакт {name} добавлен.")

                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

# Загрузка и вставка данных из CSV файла
def insert_from_csv(filename):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, newline='') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        name, phone = row
                        # Проверка корректности номера телефона
                        if not phone.isdigit() or len(phone) != 10:
                            print(f"Некорректный номер телефона: {phone} для контакта {name}")
                            continue

                        # Проверка, существует ли контакт с таким именем
                        cur.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
                        count = cur.fetchone()[0]

                        if count > 0:
                            # Если контакт существует, обновляем его номер телефона
                            cur.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s", (phone, name))
                        else:
                            # Если контакт не существует, вставляем новый контакт
                            cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone))

                conn.commit()
                print("CSV загрузка завершена.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

# Запрос данных (по имени, телефону или всех записей)
def collecting_info_by_pattern(pattern):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Использование оператора LIKE для поиска подстроки
                cur.execute("SELECT user_id, name, phone_number FROM phonebook WHERE name LIKE %s OR phone_number LIKE %s ORDER BY user_id", 
                            ('%' + pattern + '%', '%' + pattern + '%'))
                rows = cur.fetchall()
                print("Количество найденных записей: ", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

# Обновление данных (имени или номера телефона)
def update_data():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                target = input("Update by (name/phone): ")
                if target == "name":
                    old_name = input("Old name: ")
                    new_name = input("New name: ")
                    cur.execute("UPDATE phonebook SET first_name = %s WHERE first_name = %s", (new_name, old_name))
                elif target == "phone":
                    old_phone = input("Old phone: ")
                    new_phone = input("New phone: ")
                    cur.execute("UPDATE phonebook SET phone_number = %s WHERE phone_number = %s", (new_phone, old_phone))
                conn.commit()
                print("Updated.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

# Удаление данных по имени
def delete_user_by_name(name):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
                conn.commit()
                print(f"Контакт с именем {name} успешно удален.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

# Удаление данных по номеру телефона
def delete_user_by_phone(phone_number):
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone_number,))
                conn.commit()
                print(f"Контакт с номером {phone_number} успешно удален.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

# Главное меню
def menu():
    while True:
        print("\n1. Insert from console\n2. Insert from CSV\n3. Update\n4. Query\n5. Delete\n6. Exit")
        choice = input("Choose: ")
        if choice == '1':
            name = input("Enter first name: ")
            phone_number = input("Enter phone number: ")
            insert_or_update_user(name, phone_number)
        elif choice == '2':
            insert_from_csv("contacts.csv")  # Убедись, что файл contacts.csv лежит в той же папке
        elif choice == '3':
            update_data()
        elif choice == '4':
            pattern = input("Enter pattern (part of name or phone): ")
            collecting_info_by_pattern(pattern)
        elif choice == '5':
            delete_type = input("Delete by:\n1 - Name\n2 - Phone\nChoose type: ")
            if delete_type == "1":
                name = input("Enter name to delete: ")
                delete_user_by_name(name)
            elif delete_type == "2":
                phone_number = input("Enter phone number to delete: ")
                delete_user_by_phone(phone_number)
        elif choice == '6':
            break

# Запуск программы
if __name__ == '__main__':
    menu()
