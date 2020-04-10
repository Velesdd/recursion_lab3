class MaximumOfList:
    max_number = 0
    returnable_max = 0

    def find_max(self, list_of_num, num_index):
        if num_index:
            if list_of_num[num_index]>MaximumOfList.max_number:
                MaximumOfList.max_number=list_of_num[num_index]
            return self.find_max(list_of_num,num_index-1)
        else:
            MaximumOfList.returnable_max=MaximumOfList.max_number
            MaximumOfList.max_number=0
            return MaximumOfList.returnable_max
