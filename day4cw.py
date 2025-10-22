fruit = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'broccoli', 'spinach'] 
beverages = ['water', 'juice', 'soda']

fruit.append('mango')
print(fruit)

vegetables.insert(2, 'ginger' )
print(vegetables)

beverages.pop()
print(beverages)

inventory = [fruit, vegetables, beverages]
print(inventory)

print(fruit[:2])

print(vegetables[-1])

length = [len(items) for items in fruit]
print(length)

if 'water' in beverages:
    print('water is present in beverages list ')
else:
    print('water is not present in beverages list')
    
tuple = (fruit[0], vegetables[0], beverages[0])
print(tuple)



