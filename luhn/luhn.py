class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        def luhny_tune(num):
            return num * 2 - 9 if num * 2 >= 10 else num * 2

        def luhny_bin(pos, sum, chars):
            if not chars:
                return False if pos <= 1 else sum % 10 == 0
            head, *tail = chars
            if not head.isdigit():
                return False
            if pos % 2 == 0:
                return luhny_bin(pos + 1, sum + int(head), tail)
            else:
                return luhny_bin(pos + 1, sum + luhny_tune(int(head)), tail)
        return luhny_bin(0, 0, list(self.card_num[::-1]))


