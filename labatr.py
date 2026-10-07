from functools import reduce

warehouse = [
    {
        "name": "Ноутбук",
        "category": "Електроніка",
        "quantity": 10,
        "price": 25000
    },
    {
        "name": "Мишка",
        "category": "Електроніка",
        "quantity": 35,
        "price": 600
    },
    {
        "name": "Клавіатура",
        "category": "Електроніка",
        "quantity": 20,
        "price": 1200
    },
    {
        "name": "Стілець",
        "category": "Меблі",
        "quantity": 15,
        "price": 3500
    },
    {
        "name": "Стіл",
        "category": "Меблі",
        "quantity": 8,
        "price": 6000
    }
]


def show_products():
    if not warehouse:
        print("Склад порожній.")
        return

    print("\n=== Товари на складі ===")

    for i, product in enumerate(warehouse):
        print(
            f"{i}: {product['name']} | "
            f"Категорія: {product['category']} | "
            f"Кількість: {product['quantity']} | "
            f"Ціна: {product['price']} грн"
        )


def add_product():
    name = input("Введіть назву товару: ")
    category = input("Введіть категорію: ")

    try:
        price = float(input("Введіть ціну: "))
        quantity = int(input("Введіть кількість: "))

        if price < 0 or quantity < 0:
            print("Ціна та кількість не можуть бути від'ємними.")
            return

        product = {
            "name": name,
            "category": category,
            "quantity": quantity,
            "price": price
        }

        warehouse.append(product)

        print("Товар успішно додано.")

    except ValueError:
        print("Помилка! Введіть правильні числові значення.")


def delete_product():
    show_products()

    try:
        index = int(input("Введіть номер товару для видалення: "))

        if 0 <= index < len(warehouse):
            removed = warehouse.pop(index)
            print(f"Товар '{removed['name']}' видалено.")
        else:
            print("Неправильний номер товару.")

    except ValueError:
        print("Введіть ціле число.")


def update_product():
    show_products()

    try:
        index = int(input("Введіть номер товару для оновлення: "))

        if 0 <= index < len(warehouse):

            product = warehouse[index]

            print("Залиште поле порожнім, якщо змінювати його не потрібно.")

            name = input(f"Назва [{product['name']}]: ")
            category = input(f"Категорія [{product['category']}]: ")
            price = input(f"Ціна [{product['price']}]: ")
            quantity = input(f"Кількість [{product['quantity']}]: ")

            if name:
                product["name"] = name

            if category:
                product["category"] = category

            if price:
                product["price"] = float(price)

            if quantity:
                product["quantity"] = int(quantity)

            print("Інформацію оновлено.")

        else:
            print("Неправильний номер товару.")

    except ValueError:
        print("Помилка введення даних.")


def search_product():
    name = input("Введіть назву товару для пошуку: ").lower()

    results = list(
        filter(
            lambda product: name in product["name"].lower(),
            warehouse
        )
    )

    if results:
        print("\n=== Результати пошуку ===")

        for product in results:
            print(
                f"{product['name']} | "
                f"{product['category']} | "
                f"{product['quantity']} шт. | "
                f"{product['price']} грн"
            )
    else:
        print("Товар не знайдено.")


def filter_by_category():
    category = input("Введіть категорію: ").lower()

    results = list(
        filter(
            lambda product: product["category"].lower() == category,
            warehouse
        )
    )

    if results:
        print("\n=== Товари категорії ===")

        for product in results:
            print(
                f"{product['name']} | "
                f"{product['quantity']} шт. | "
                f"{product['price']} грн"
            )
    else:
        print("Товарів цієї категорії немає.")


def total_value():
    values = map(
        lambda product: product["price"] * product["quantity"],
        warehouse
    )

    total = reduce(lambda x, y: x + y, values, 0)

    print(f"\nЗагальна вартість товарів на складі: {total:.2f} грн")


def sort_by_price():
    sorted_products = sorted(
        warehouse,
        key=lambda product: product["price"]
    )

    print("\n=== Товари за ціною ===")

    for product in sorted_products:
        print(
            f"{product['name']} | "
            f"{product['price']} грн | "
            f"{product['quantity']} шт."
        )


def sort_by_quantity():
    sorted_products = sorted(
        warehouse,
        key=lambda product: product["quantity"],
        reverse=True
    )

    print("\n=== Товари за кількістю ===")

    for product in sorted_products:
        print(
            f"{product['name']} | "
            f"{product['quantity']} шт."
        )


def average_price():
    if not warehouse:
        print("Склад порожній.")
        return

    prices = list(
        map(lambda product: product["price"], warehouse)
    )

    average = sum(prices) / len(prices)

    print(f"\nСередня ціна товару: {average:.2f} грн")


def min_max_quantity():
    if not warehouse:
        print("Склад порожній.")
        return

    min_product = min(
        warehouse,
        key=lambda product: product["quantity"]
    )

    max_product = max(
        warehouse,
        key=lambda product: product["quantity"]
    )

    print(
        f"\nНайменша кількість: "
        f"{min_product['name']} — {min_product['quantity']} шт."
    )

    print(
        f"Найбільша кількість: "
        f"{max_product['name']} — {max_product['quantity']} шт."
    )


def main():
    while True:
        print("\n===== УПРАВЛІННЯ СКЛАДОМ =====")
        print("1. Показати всі товари")
        print("2. Додати товар")
        print("3. Видалити товар")
        print("4. Оновити інформацію про товар")
        print("5. Знайти товар")
        print("6. Фільтрувати за категорією")
        print("7. Обчислити загальну вартість")
        print("8. Сортувати за ціною")
        print("9. Сортувати за кількістю")
        print("10. Обчислити середню ціну")
        print("11. Знайти мінімальну та максимальну кількість")
        print("0. Вийти")

        choice = input("\nОберіть опцію: ")

        if choice == "1":
            show_products()

        elif choice == "2":
            add_product()

        elif choice == "3":
            delete_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            search_product()

        elif choice == "6":
            filter_by_category()

        elif choice == "7":
            total_value()

        elif choice == "8":
            sort_by_price()

        elif choice == "9":
            sort_by_quantity()

        elif choice == "10":
            average_price()

        elif choice == "11":
            min_max_quantity()

        elif choice == "0":
            print("Програму завершено.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()