def decorator_function(function_to_be_excecuated):
    def decorator_wrapper(*args, **kwargs):
        # before 
        print("Hi")

        function_to_be_excecuated(*args, **kwargs)

        # after
        print("Bye")
    return decorator_wrapper


@decorator_function  # decorating the "hello()" function
def hello(name):
    print(f"Hello! {name}")

# decorator_function(hello)(input("Name: "))
name = input("Name: ")
hello(name)