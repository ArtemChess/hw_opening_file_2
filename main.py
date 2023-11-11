cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}


def get_shop_list_by_dishes(dishes, person):
    shopping_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity_per_person = ingredient['quantity']
                measure = ingredient.get('measure', '')
                total_quantity = quantity_per_person * person
                if dish not in shopping_list:
                    shopping_list[dish] = {}
                shopping_list[dish][ingredient_name] = {'quantity': total_quantity, 'measure': measure}
    return shopping_list


selected_dishes = ['Омлет', 'Утка по-пекински', 'Запеченный картофель']
number_of_persons = 2
resulting_shopping_list = get_shop_list_by_dishes(selected_dishes, number_of_persons)

for dish, ingredients in resulting_shopping_list.items():
    print(f"\n{dish}:")
    for ingredient, details in ingredients.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")

def print_dish_info(dish_name, dish_data, file):
    file.write(dish_name + '\n')
    file.write(f'Ингредиентов: {len(dish_data)}\n')
    for ingredient in dish_data:
        file.write(f'{ingredient["ingredient_name"]}: "measure": {ingredient["measure"]}: "quantity": {ingredient["quantity"]}:\n')


with open('hw.txt', 'w') as file:
    for dish_name in cook_book:
        file.write('\n')
        if dish_name in cook_book:
            print_dish_info(dish_name, cook_book[dish_name], file)
        else:
            file.write(f'Ингредиентов для блюда "{dish_name}" нет в рецепте\n')
