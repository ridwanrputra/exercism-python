import itertools


class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")[::-1]

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isnumeric():
            return False

        return (
            sum(
                map(
                    lambda x: x if x < 10 else x - 9,
                    [   int(elm) * 2 if idx % 2 != 0 else int(elm)
                        for idx, elm in enumerate(self.card_num)
                    ],
                )
            ) % 10 == 0
        )
