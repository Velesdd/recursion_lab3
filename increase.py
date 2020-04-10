

class Increase:
    list_of_num = []
    returnable_list = []

    def func_increase(self, first, last):
        if first < last:
            Increase.list_of_num.append(first)
            return self.func_increase(first + 1, last)
        else:
            Increase.list_of_num.append(last)
            Increase.returnable_list = Increase.list_of_num
            Increase.list_of_num = []
            return Increase.returnable_list
