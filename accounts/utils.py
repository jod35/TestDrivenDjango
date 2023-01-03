from libgravatar import Gravatar

def create_avatar(email_address):
    g = Gravatar(email_address)

    return g.get_image(default="https://static.thenounproject.com/png/574704-200.png")
    