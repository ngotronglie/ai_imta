# def custom_print(a):
#     print(a)

# custom_print("hello")
# custom_print("world")


# def welcome(name):
#     print("hello " + name)


# a = input("enter your name: ")

# welcome(a)






# def add (a, b):
#     return a + b 

# # print(add(5, 3))



# def multiple_return():
#     return 5+6 , 8+8

# # trả về 2 giá trị mà các ngôn ngữ khác không có

# print(multiple_return())

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)  

# p = Person("John", 30)



# def myfunc():
#     x = 300
#     print(x)

# myfunc()

# if(True):
#     print("Tooi la ai ")
# else :
#     print("toi bi sai a")
    
# # defining and using function

# def what_is_x():
#     print()

# x = 10
# what_is_x()



# def what_is_y():
#     y = 20 
#     print(y)

# y= 10 
# what_is_y()



# # ________________________________________________________________________________


# def calculate_total(price, quantity, discount=0):
#     """
#     Calculate the total price of items with an optional discount.

#     :param price: Price of a single item.
#     :param quantity: Number of items.
#     :param discount: Discount percentage (default is 0).
#     :return: The total price after applying the discount.
#     """
#     total = price * quantity
#     discounted_total = total - (total * discount / 100)
#     return discounted_total


# # Test cases
# print("discount = 10% : ", calculate_total(50, 20, 10))
# print("discount = 20% : ", calculate_total(50, 20, 20))
# print("discount = 0%  : ", calculate_total(50, 20, 0))
# print("discount = default value : ", calculate_total(50, 20))




# #  *args 

# def sequence_argments(*args):
#     print(args)

# sequence_argments(1, 2, 3, 4, 5)
# sequence_argments(5,6,"you are to good")


# # *01. args

# # Nếu dấu "*" được dùng khi gọi hàm, thì được hiểu là tách các giá trị trong list chia cho các tham số trong hàm.
# # Các giá trị sẽ được giải theo đúng thứ tự trong hàm đã định nghĩa.


# # Anonymous function

# func1 = lambda x: x**2
# def func2(x):
#     return x**2

# def plust_square(x, func1):

#     x = x + func1(x)
#     print("x: " , x)


# plust_square(5, func1)
# plust_square(5, func2)


# 1 : yield vs return 

def function1(x):
    return x
def function2(x):
    yield x 

print(function1(5))
print(function2(5))

