import re

def is_number(s):
    if re.match("^\d+?\.\d+?$", s) is None:
        return s.isdigit()
    return True

cook_book = {}
with open('files/recipes.txt') as f:
    for i, l in enumerate(f):
        strip_line = l.strip()
        if i == 0 or receipt_name == False:
            receipt_name = strip_line
        elif strip_line == "":
            receipt_name = False

        if "|" in strip_line:
            ingredient = strip_line.split(' | ')
            cook_book[receipt_name].append({'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]})
        elif strip_line != "" and not is_number(strip_line):
            cook_book[strip_line] = []

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in shop_list:
                shop_list[ingredient['ingredient_name']]['quantity'] = shop_list[ingredient['ingredient_name']]['quantity'] + ingredient['quantity'] * person_count
            else:
                shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
    return shop_list

print(get_shop_list_by_dishes(['Обитатель утёсов', 'Фаттро', 'Татуинский закат'], 3))