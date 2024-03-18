## UNDERSTANDING THE BEHIND THE SCENE
 -Event loop: the code runs in a call stack
 - when the line is called in is tranferred to the call stack, and once it is executed it will be removed from the stack
 - LIFO- last in first out | after the line is executed it is removed from the call stack
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