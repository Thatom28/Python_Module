import datetime


# this allws the rest of the file to run
def math_divide(n1, n2):
    try:  # lets you test a block of code for errors
        result = n1 / n2
    except ZeroDivisionError:  # when error occurs
        print("you cannot divide by zero ❌")
    else:  # if there is no error
        print("you division was successful✅")
    finally:  # always run whether error found or not
        # useful for closing objects and clean up resources like closing files
        print("operation complete")


def calculate_age():
    try:
        age = input("Please tell me your year of birth: ")
        year = int(age)
        current_year = datetime.date.today().year
        # handling ogical errors
        if current_year <= 0:
            # stop futher execution
            raise ValueError("year cannot be negetive)")

        if current_year > 0:
            # stop futher execution
            raise ValueError("you are not from the future)")

        print(f"your age is {current_year - year}")
    except ValueError:
        print("you cannot calculate a string and int")
    else:
        print("Age calculated successfully")
    finally:
        print("calculation completed!")


# if __name__ == "__main__":
#     # math_divide(5, 6)
#     calculate_age()


def calculate_age1():
    try:
        age = input("Please tell me your year of birth: ")
        year = int(age)
        current_year = datetime.date.today().year
        # handling ogical errors
        if current_year <= 0:
            # stop futher execution
            raise ValueError("year cannot be negetive)")

        if current_year > 0:
            # stop futher execution
            raise ValueError("you are not from the future)")

        print(f"your age is {current_year - year}")
    except ValueError:
        print("you cannot calculate a string and int")
        # if you dont know the error you will get
    except Exception as err:  # make an aliase |
        print("this is catch all", err)


class NegetiveNumberError(Exception):
    # the value represent the value causing the error
    def __init__(self, value):
        self.value = value
        self.message = "negetive numbers not allowed"
        super().__init__(
            self.message
        )  # pass the self.message to the base class(exception)

    # Overides to create a custom string representation
    def __str__(self):
        return f"{self.value} -> {self.message}"

        # How to use the exeption

    def only_positive(self):
        try:
            x = -10
            if x < 0:
                raise NegetiveNumberError(x)
        # match the type of the erro
        except NegetiveNumberError as e:
            print(e)


if __name__ == "__main__":
    only_positive()
