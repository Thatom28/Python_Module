# Iterables -> __iter__can be looped : List| dictionary
# minimum requement to be a Iterable is to have __iter__
# -> iterables have add, count, append, pop, remove
# eager -> always finish
# -----when to use____
# They dont know where you are in the loop


# Iterator -> __next__ you can only loop one time
# minimum reqiremnet to be a iterator it needs to have __next__
# -. do not have add,remove, count methods
# they are Iterable because it has both __next__ and __iter__
# Lazy, stops until next is called
# -----when to use____
# it knows the current value and the next value also

# nums = [5, 10, 20]
# print(dir(nums))  # returns methods avaliable for the list icluding the dunter methods

# nums_iter = nums.__iter__()  # converted into an iterator | iterable -> itrabable
# print(nums_iter)  # <list_iterator object at 0x00000217BC9F5E40>

# # 2
# nums_iter = iter(nums)  # converted into an iterator
# print(nums_iter)  # <list_iterator object at 0x00000217BC9F5E40>
# print(dir(nums))  # will not have the add,remove, count methods

# # CONCLISION: ALL ITERATORS ARE ITERABLES BUT NOT THE OTHER WAY AROUND, _
# # because they both have __next_ and __iter__
# # print(next(nums_iter))
# # print(next(nums_iter))  #Stopiteration error if at the end of list
# # n = 0
# # while n <= nums_iter:
# #     print(next(n))

# while True:
#     try:
#         print(next(nums_iter))
#     except StopIteration:
#         print("done")
#         break

#     # using for loop
#     for nu in nums_iter:
#         print(nu)

# # ---------RAnge--------
# # it hold the start value, the last value and the skips
# # range(0, 100_000, 1)  ?With list all these values will be stored in memory
# # | Iterator only remeber sone value | saves memory


class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # because it is an iterator already

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1  # the current value is changing because it


for n in MyRange(1, 5):nums
    print(n)


# # -----Generators -clean returns an Iterator
# # ------Generators use Yeild -> iterator
# def infinite_integers():
#     n = 0
#     while True:
#         yield n  # return & pause, the next line is not called unit the next is called again
#         n += 1


def fib(limit):
    num1 = 0
    num2 = 1
    while num1 < limit:
        yield num1
        num3 = num1 + num2
        num1 = num2
        num2 = num3


for num in fib(10):
    print(num)

# calling
# integers = infinite_integers()
# print(next(integers))  # 0 it stops
# print(next(integers))  # 1
# print(next(integers))  # 2

# if __name__ == '__main__'
