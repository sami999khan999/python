# **kwargs

# **kwargs is used in function definitions to allow the function to accept a variable number of keyword arguments. These keyword arguments are passed in the form of key-value pairs, and **kwargs collects them into a dictionary.


def info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


info(first_name="Sami", last_name="Khan")
