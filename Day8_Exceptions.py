#this allws the rest of the file to run
try:
     result= 10/ 0
except ZeroDivisionError: #when error occurs
     print('you cannot divide by zero')
else: #if there is no error
     print('you division was successful')
finally: #always run whether error found or not
    #useful for closing objects and clean up resources
    print('operation complete')
print('hello')