

class User:
    def __init__(self) -> None:
        self.is_logged_in = False

def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

def is_authenticated_decorator(function):
    def wrapper_function(*args):
        if args[0].is_logged_in == True:
            function()
    return wrapper_function

new_user = User("edward")
new_user.is_logged_in = True
create_blog_post(new_user)