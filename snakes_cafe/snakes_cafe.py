

print('**************************************')
print('** Welcome to the Snakes Cafe! **')
print('** Please see our menu below. **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************\n')


print('Appetizers')
print('----------')

appetizers = ['Wings', 'Cookies', 'Spring Rolls']

for app in appetizers:
    print(app)

print('\nEntrees')
print('----------')

entrees = ['Salmon', 'Steak', 'Meat Tornado']

for ent in entrees:
    print(ent)

print('\nDesserts')
print('----------')

desserts = ['Ice Cream', 'Cake', 'Pie']

for des in desserts:
    print(des)

print('\nDrinks')
print('----------')

drinks = ['Coffee', 'Tea', 'Unicorn Tears']

for drink in drinks:
    print(drink)

print('\n***********************************')
print('** What would you like to order? **')
print('***********************************')

ordered = []

ordering = True

while ordering == True:
    order = str(input())
    if order == 'quit':
        ordering = False
    else:
        ordered.append(order)
        count_on = str(ordered.count(order))
        print('** ' + count_on + ' order of ' +
              order + ' have been added to your meal **')
