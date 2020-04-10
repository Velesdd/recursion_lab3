from unittest import TestCase
from Fibonacci import Fibonacci
from maximum import MaximumOfList
from increase import Increase

class FibonacciTestCase(TestCase):

    def setUp(self):
        self.fibonacci = Fibonacci()
        self.fibonacci_test_data =[
            [20, 6765], [82, 61305790721611591], [44, 701408733],
            [32, 2178309], [100, 354224848179261915075],
            [132, 1725375039079340637797070384],
            [172, 394810887814999156320699623170776339]]

    def test_fibonacci_test_data(self):
        for num, expected_num in self.fibonacci_test_data:
            actual_num = self.fibonacci.find_fibonacci(num)
            self.assertEqual(actual_num, expected_num)


class MaximumTestCase(TestCase):

    def setUp(self):
        self.maximum = MaximumOfList()
        self.maximum_test_data = [
            [[23,43,-5,567,-345,3,-954,0,2,5,3,5],11,567],
            [[4628,8472,-23848,0,74,278,374,33332],7,33332],
            [[242,214,15525,-42,224,-42,-45667,7742,7744,225,2556,543,15525.1],12,15525.1]]

    def test_maximum_test_data(self):
        for list_of_num,num_index,expected_max in self.maximum_test_data:
            actual_max = self.maximum.find_max(list_of_num,num_index)
            self.assertEqual(actual_max,expected_max)


class IncreaseTestCase(TestCase):

    def setUp(self):
        self.increase = Increase()
        self.increase_test_data = [
            [-10,2,[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2]],
            [10,17,[10,11,12,13,14,15,16,17]],
            [-99,-88,[-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88]]]

    def test_increase_test_data(self):
        for first, last, expected_list in self.increase_test_data:
            actual_list = self.increase.func_increase(first,last)
            self.assertEqual(actual_list,expected_list)


