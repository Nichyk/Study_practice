# Custom exception
# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file

class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open("logs.txt", "a") as file:
            file.write(f"Error message: {msg}\n")


error = CustomException('Error3')


with open('logs.txt') as f:
    text = f.read()
    print(text)
