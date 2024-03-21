k = input('Item: ').lower()

#dictionary
fruit = {
    'apple':'130','avocado':'50','banana':'110','cantaloupe':'50','grapefruit':'60',
    'grapes':'90','honeydew melon':'50','pineapple':'50','plums':'70','strawberries':'50',
    'kiwifruit':'90','lemon':'15','lime':'20','nectarine':'60','peach':'60',
    'pear':'100','sweet cherries':'100','tanmgerine':'50','watermelon':'80','orange':'80'
}

if k in fruit:
    print(f'Calories: {fruit[k]}')