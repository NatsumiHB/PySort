import random


class Lines:
    def __init__(self, max_num, amount):
        self.max_num = max_num
        self.amount = amount
        self.already_sorted = 0

        self.values = []
        for i in range(amount):
            self.values.append(random.randint(1, max_num))

    def reset(self):
        self.__init__(self.max_num, self.amount)
