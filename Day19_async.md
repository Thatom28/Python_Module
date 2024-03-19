## The role of event loop
- to manage execution of asyncronous functions and events
- to coordinate their operations without blocking he main thread
- Event loops allow python to hanldle multiple tasks concurrently therefore increasing persomance
- event loop is executed when the call stack is empty

## UNDERSTANDING THE BEHIND THE SCENE OF EVENT LOOP
 -Event loop: the code runs in a call stack
 - when the line is called in is tranferred to the call stack, and once it is executed it will be removed from the stack
 - LIFO- last in first out | after the line is executed it is removed from the call stack
 - ends when the function is completed or ruturn happens
 ## WHEN DOES A STACK HAPPEN?
 - when you have a function that call another function
 - a line gets popped out of a stack when a function is done and returned


## To overflow the stack : using recussion, a function calling itself
def add(x):
    return x +1

def sum(a,b):
    c = sum(a) + sum(b) #second in the call stack (add(3)) on top the return froom the add function NB after return the line is removed from the call stack
    return c

sum(3,5)  #fist in the call stack (it will be at the bottom)


## schedule -> after 2 seconds execute this code when the call stack is empty  
- The event loop pushed to the stack when the call stack is empty and
- benefitial because you can run other code-# executing all the requests at the same time

# type(cooking_eggs())  #corouting
# type(await cooking_eggs()) #string ->  eggs cooked (await opens the box and you get the values)
# gather takes in coroutines and puts them in a box again
# await gather -> takes the values out of the box