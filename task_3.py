world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
#Добавим новый ключ и значение в словарь
world_champions[2022] = 'Аргентина'
#Напечатаем словарь в формате key - value
for key in world_champions.keys():
    print(str(key) +' - '+ world_champions[key])

country = 'Италия'
#Ищем Италию среди values и устанавливаем условия вывода
if country in world_champions.values():
    print(country + ' становилась чемпионом мира по футболу в 21 веке!')
else:
    print(country + ' не выигрывала чемпионат мира по футболу в 21 веке.')
