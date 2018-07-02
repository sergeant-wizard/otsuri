coins = [10000, 5000, 1000, 500, 100, 50, 10]
def change_for(price, payment):
    paid_sum = 0
    for coin in coins:
        if coin in payment.keys():
            paid_sum += coin * payment[coin]
    diff = paid_sum - price
    ret = {}
    for coin in coins:
        ret.update({
            coin: diff // coin
        })
        diff -= coin * (diff // coin)
    return ret


def test_change_for():
    assert change_for(650, {100:2, 500:1}) == {
        10: 0, 50: 1, 100: 0, 500: 0, 1000: 0, 5000: 0, 10000: 0
    }
    assert change_for(750, {1000:1}) == {
        10: 0, 50: 1, 100: 2, 500: 0, 1000: 0, 5000: 0, 10000: 0
    }
    assert change_for(25000, {10000:3}) == {
        10: 0, 50: 0, 100: 0, 500: 0, 1000: 0, 5000: 1, 10000: 0
    }
    assert change_for(150, {1000:1}) == {
        10: 0, 50: 1, 100: 3, 500: 1, 1000: 0, 5000: 0, 10000: 0
    }


if __name__ == '__main__':
    test_change_for()
