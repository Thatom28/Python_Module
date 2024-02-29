## Currying
- Reduced a function with many arguments  to a chain of functions that takes one argument each.
-  If a function has many arguments, the function is changed into a function that takes only one argument and it returns a function and takes the second argument, and it returns a function until the parameters that a function can take are complete.
-  it changes a function that takes in multiples arguments into a chain consisting of multiple functions that take a single argument.
-  
## Partial funtion
- Used to reduce the number of arguments a function takes to simplify  the function. Creates a new function using the function with many arguments.
- i.e. def marks (n1, n2, n3):
- you can use the partial function to curry the function.
- marks1 = partial(marks, n1=10)   -the first parameter is the name of the fuvtion we are deriving from, in this case when we call the fuction, we will only need to pass two argumnets to the function, since n1 is already prefixed.
- marks2 = partial(marks1, n2=45, n3=60)
- return(marks2)
- When you call marks3 function, python calls marks1 function then go to the marks function.