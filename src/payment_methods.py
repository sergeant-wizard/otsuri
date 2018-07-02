possibilities_150 = [
    {
        100: 1, 50: 1, 'odds': 4/5 * 1/2
    }, {
        100: 2, 50: 0, 'odds': 3/5 * 1/2
    }, {
        500: 1, 100:0, 50: 1, 'odds': 1/2 * 1/5 * 1/2
    }, {
        500: 1, 100:0, 50: 0, 'odds': 1/2 * 2/5 * 1/2
    }, {
        1000: 1, 500:0, 100:0, 50: 1, 'odds': 4/5 * 1/2 * 1/5 * 1/2
    }, {
        1000: 1, 500:0, 100:0, 50: 0, 'odds': 4/5 * 1/2 * 2/5 * 1/2
    }, {
        5000: 1, 1000: 0, 500:0, 100:0, 50: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5 * 1/2
    }, {
        5000: 1, 1000: 0, 500:0, 100:0, 50: 0, 'odds': 1/2 * 1/5 * 1/2 * 2/5 * 1/2
    }, {
        10000: 1, 5000: 0, 1000: 0, 500:0, 100:0, 50: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5 * 1/2
    }, {
        10000: 1, 5000: 0, 1000: 0, 500:0, 100:0, 50: 0, 'odds': 1/2 * 1/5 * 1/2 * 2/5 * 1/2
    }
]
assert sum([p['odds'] for p in possibilities_150]) == 1

possibilities_300 = [
    {
        100: 3, 'odds': 2/5
    }, {
        500: 1, 'odds': 3/5 * 1/2
    }, {
        1000: 1, 'odds': 4/5 * 3/5 * 1/2
    }, {
        5000: 1, 'odds': 1/2 * 1/5 * 3/5 * 1/2
    }, {
        10000: 1, 'odds': 1/2 * 1/5 * 3/5 * 1/2
    }
]
assert sum([p['odds'] for p in possibilities_300]) == 1


possibilities_100 = [
    {
        100: 1, 'odds': 4/5
    }, {
        500: 1, 'odds': 1/2 * 1/5
    }, {
        1000: 1, 'odds': 4/5 * 1/2 * 1/5
    }, {
        5000: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5
    }, {
        10000: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5
    }
]
assert sum([p['odds'] for p in possibilities_100]) == 1



possibilities_50 = [
    {
        50: 1, 'odds': 1/2
    }, {
        100: 1, 'odds': 4/5 * 1/2
    }, {
        500: 1, 'odds': 1/2 * 1/5 * 1/2
    }, {
        1000: 1, 'odds': 4/5 * 1/2 * 1/5 * 1/2
    }, {
        5000: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5 * 1/2
    }, {
        10000: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5 * 1/2
    }
]
assert sum([p['odds'] for p in possibilities_50]) == 1

possibilities_10 = [
    {
        10: 1, 'odds': 4/5,
    }, {
        50: 1, 'odds': 1/2 * 1/5,
    }, {
        100: 1, 'odds': 4/5 * 1/2 * 1/5,
    }, {
        500: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5,
    }, {
        1000: 1, 'odds': 4/5 * 1/2 * 1/5 * 1/2 * 1/5,
    }, {
        5000: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5 * 1/2 * 1/5,
    }, {
        10000: 1, 'odds': 1/2 * 1/5 * 1/2 * 1/5 * 1/2 * 1/5,
    }
]
assert sum([p['odds'] for p in possibilities_10]) == 1

payment_methods = {
    10: possibilities_10,
    50: possibilities_50,
    100: possibilities_100,
    150: possibilities_150,
    300: possibilities_300,
}