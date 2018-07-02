items = [
    {
        'name': 'yakisoba',
        'quantity': 238,
        'unit_price': 300,
        'class': 'taiyo',
    }, {
        'name': 'kakigoori',
        'quantity': 200,
        'unit_price': 150,
        'class': 'hoshi',
    }, {
        'name': 'nomimono',
        'quantity': 182,
        'unit_price': 100,
        'class': 'hoshi',
    }, {
        'name': 'ramune',
        'quantity': 100,
        'unit_price': 100,
        'class': 'niji',
    }, {
        'name': 'onigiri',
        'quantity': 30,
        'unit_price': 300,
        'class': 'niji',
    }, {
        'name': 'kyoshutu',
        'quantity': 30,
        'unit_price': 10,
        'class': 'tsuki',
    }, {
        'name': 'yoyo',
        'quantity': 100,
        'unit_price': 50,
        'class': 'issai',
    }, {
        'name': 'mascot',
        'quantity': 250,
        'unit_price': 50,
        'class': 'issai',
    }, {
        'name': 'cookie',
        'quantity': 40,
        'unit_price': 150,
        'class': 'sensei',
    }, {
        'name': 'miso_oden',
        'quantity': 288,
        'unit_price': 50,
        'class': 'sensei',
    }
]

for item in items:
    for coin in coins:
        item[coin] = 0
    payment_method = payment_methods[item['unit_price']]
    for pm in payment_method:
        change = change_for(item['unit_price'], pm)
        for coin in change.keys():
            # np(1-p) = 0.25n, we use 1 sigma
            item[coin] += change[coin] * pm['odds'] * item['quantity'] * 0.25

pd_items = pandas.DataFrame(items)
by_class = pd_items.groupby('class').sum()
total = by_class.aggregate(sum)
sum([coin * total[coin] for coin in coins])
