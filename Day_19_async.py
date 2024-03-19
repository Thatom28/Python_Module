import asyncio


async def hello_world():  # when you marks they can pass this method and  pass and run others
    print("started 🌍")  # this will be presented immediately
    await asyncio.sleep(
        1
    )  # sleep | async function # determines the time to amount to wait
    print("Hello, Sanlam🌍")  # it will be printed 1 second after the above print


# how to run the async function with
# asyncio.run(hello_world())

# Task 1 countdown
# 3 2 1 Happy new year


async def new_year():  # type = coroutine
    print("3")
    await asyncio.sleep(1)
    print("2")
    await asyncio.sleep(1)
    print("1")
    await asyncio.sleep(1)
    print("HAPPY NEW YEAR🎊")


# asyncio.run(new_year())


# ---------------------------------------------------------------------
# Task 2 create a function by making your code dry
async def new_year2(time):
    while time > 0:
        print(time)
        await asyncio.sleep(1)
        time -= 1
    else:
        print("HAPPY NEW YEAR🎊")


# asyncio.run(new_year2(3))


# ------------------------------------------------------------------------
# Task 3: without the loop reuse
async def new_year3(time):
    if time > 0:
        print(time)
        await asyncio.sleep(1)
        await new_year3(time - 1)
    else:
        print("HAPPY NEW YEAR🎊")


# asyncio.run(new_year3(3))


async def count_and_sleep(num):
    print(num)
    await asyncio.sleep(1)  # sleep -> inbuilt async function


async def countdown():
    await count_and_sleep(3)
    await count_and_sleep(2)
    await count_and_sleep(1)
    await count_and_sleep("HAPPY NEW YEAR🎊")


# every async function returns a coroutie
# asyncio.run(countdown())  # type = coroutine

# UNDERSTANDING THE BEHIND THE SCENE
# -Event loop: the code runs in a call stack
# - when the line is called in is tranferred to the call stack, and once it is executed it will be removed from the stack
# - LIFO- last in first out | after the line is executed it is removed from the call stack
# WHEN DOES A SACK HAPPEN?
# - when you have a function that call another function
# - a line gets popped out of a stack when a function is done and returned


# To overflow the stack : using recussion, a function calling itself
def add(x):
    return x + 1


def sum(a, b):
    c = sum(a) + sum(
        b
    )  # second in the call stack (add(3)) on top the return froom the add function NB after return the line is removed from the call stack
    return c


# sum(3, 5)  # fist in the call stack (it will be at the bottom)


# schedule -> after 2 seconds execute this code when the call stack is empty
# The event loop pushed to the stack when the call stack is empty and
# - benefitial because you can run other code


async def background_task():
    print("Start backgroud task")
    await asyncio.sleep(3)


async def main():
    await background_task()
    # waiting for the backgound to execute before executing these lines
    print("Main function says - Hi")


# asyncio.run(main())
# ---------------------------------------------------------------------------------------------


# improving to make it asynchonous
async def background_task():
    print("Start backgroud task")
    await asyncio.sleep(3)
    print("Success")  # it will not print anything because the main is already executed


async def main():
    # request to schedule the task below
    # moved to the pause area
    task = asyncio.create_task(background_task())  # execute concurrently
    # await background_task()
    # executing these lines because background is paused
    print("Main function says - Hi")
    print("Main function says - Hi")
    print("Main function says - Hi")
    # waits for the backgroudtask to be completed, therefore it will execute all the methods of background
    await task


# asyncio.run(main())

# ------------------------------------------------------------------------------------------------------------


async def cooking_eggs():
    print("Eggs cooking🍳")
    await asyncio.sleep(3)
    print("Eggs cooked✅")


async def make_coffee():
    print("coffee brewing☕")
    await asyncio.sleep(2)
    print("Coffee done✅")


async def main():
    task1 = asyncio.create_task(cooking_eggs())
    task2 = asyncio.create_task(make_coffee())
    # await background_task()
    # waiting for the backgound to execute before executing these lines
    print("Bread toasting 1🍞")
    print("Bread toasting 2🍞")
    print("Bread toasting 3🍞")
    # only waits for the time on task1
    await task2


# asyncio.run(main())
# ---------------------------------------------------------------------------------------------


# when you dont know how long the methods take and making sure that all tasks are executed
# THE OLD WAY
async def cooking_eggs():
    print("Eggs cooking🍳")
    await asyncio.sleep(3)
    print("Eggs cooked✅")


async def make_coffee():
    print("coffee brewing☕")
    await asyncio.sleep(2)
    print("Coffee done✅")


async def main():
    task1 = asyncio.create_task(cooking_eggs())
    task2 = asyncio.create_task(make_coffee())
    # await background_task()
    # waiting for the backgound to execute before executing these lines
    print("Bread toasting 1🍞")
    print("Bread toasting 2🍞")
    print("Bread toasting 3🍞")
    # wait until both fuctions are completed (the longest one compltes) | set of tasks
    await asyncio.wait({task1, task2})


# asyncio.run(main())


# -----------------------------------------------------------------------------------------------
# when you dont know how long the methods take and making sure that all tasks are executed
# THE NEW WAY
async def cooking_eggs():
    print("Eggs cooking🍳")
    await asyncio.sleep(3)
    print("Eggs cooked✅")


async def make_coffee():
    print("coffee brewing☕")
    await asyncio.sleep(2)
    print("Coffee done✅")


async def make_cereal():
    print("Cereal brewing🥣")
    await asyncio.sleep(2)
    print("Cereal done✅")


async def main():
    # the event loop (.create_task): manage thinds on your call stack
    task1 = asyncio.create_task(cooking_eggs())
    task2 = asyncio.create_task(make_coffee())
    task3 = asyncio.create_task(make_cereal())
    all_tasks = [task1, task2, task3]
    # await background_task()

    print("Bread toasting 1🍞")
    print("Bread toasting 2🍞")
    print("Bread toasting 3🍞")
    # Can be used with unpacking operaror (*)
    # await asyncio.gather(task1, task2, task3)
    await asyncio.gather(*all_tasks)


# asyncio.run(main())


# -------------------------------------------------------------------------
# SIMPLIFYING FUTHER
async def cooking_eggs():
    print("Egg cooking 🥚")
    await asyncio.sleep(3)
    print("Eggs cooked ✅")
    return f"Data - Eggs 🥚"


async def make_coffee():
    print("Coffee brewing ☕")
    await asyncio.sleep(2)
    print("Coffee done ✅")
    return f"Data - Coffee ☕"


async def make_cereal():
    print("Making Cereal bowl 🧃")
    await asyncio.sleep(7)
    print("Cereal done ✅")
    return f"Data - Cereal 🧃"


async def main():
    # Request to event loop to schedule
    # schedule happenes here when create_task is written
    all_tasks = [
        asyncio.create_task(cooking_eggs()),
        asyncio.create_task(make_coffee()),
        asyncio.create_task(make_cereal()),
    ]
    print("Bread Toast 1")
    print("Bread Toast 2")
    print("Bread Toast 3")
    print("Bread Toast 4")
    # the other tasks will be executed in the mean time because the call stack is empty during the sleep
    # and because tasks are already scheduled
    print("Sleep started")
    await asyncio.sleep(6)
    print("sleep ended")

    #  Wait till the longest one completes
    # await asyncio.gather(all_tasks[0], all_tasks[1],  all_tasks[2])
    # Order of data == Order given in create_task
    data = await asyncio.gather(*all_tasks)
    print(data)


asyncio.run(main())


# -------------------------------------------------------------------------
# SIMPLIFYING FUTHER
async def cooking_eggs():
    print("Egg cooking 🥚")
    await asyncio.sleep(3)
    print("Eggs cooked ✅")
    return f"Data - Eggs 🥚"


async def make_coffee():
    print("Coffee brewing ☕")
    await asyncio.sleep(2)
    print("Coffee done ✅")
    return f"Data - Coffee ☕"


# returns coroutines
async def make_cereal():
    print("Making Cereal bowl 🧃")
    await asyncio.sleep(5)
    print("Cereal done ✅")
    return f"Data - Cereal 🧃"


async def main():
    # Request to event loop to schedule
    # no scheduling, schedules at the gather call
    all_coroutines = [
        cooking_eggs(),
        make_coffee(),
        make_cereal(),
    ]

    # Waiting for the background_task
    print("Bread Toast 1")
    print("Bread Toast 2")
    print("Bread Toast 3")
    print("Bread Toast 4")

    # this will make the tasks wait 6 seconds before the scheduling happens
    # therefore every async task will be paused until sleep ends
    print("Sleep started")
    await asyncio.sleep(6)
    print("sleep ended")

    #  Wait till the longest one completes
    # await asyncio.gather(all_tasks[0], all_tasks[1],  all_tasks[2])
    # Order of data == Order given in create_task
    # only schedule here
    data = await asyncio.gather(*all_coroutines)
    # you can only print what you returned
    print(data)


# asyncio.run(main())
