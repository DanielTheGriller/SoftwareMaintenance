# Software Maintenance
# Week 1 Assignment 1a
# Daniel Linna
# 0509355
# 19.1.2020
###################################################################
import unittest
import fibonacci

class TestFibonacci(unittest.TestCase):
    
    def test_output(self):
        fibonacci.fib(2,1)
        reader = open("result.txt", "r", encoding="UTF-8")
        result = reader.readline()
        self.assertEqual(result, "2\n")
        result = reader.read()
        self.assertEqual(result, "3\n")
        reader.close()
    
    def test_input(self):
        result = fibonacci.fib(10,2)
        self.assertEqual(result,0) 

    def test_falseinput(self):
        data = [":", 0, -1, "1", " "]
        for i in range(0,len(data)):
            fibonacci.fib(data[i],data[i])


        
if __name__ == '__main__':
    unittest.main()
