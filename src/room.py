import textwrap
# Implement a class to hold room information. This should have name and
# description attributes.

wrapper = textwrap.TextWrapper(width=50)


class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, 
                 w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def desc(self):
        wrapper = textwrap.TextWrapper(width=70)
        desc = wrapper.fill(text=self.description)
        return f"{desc}"

    def __str__(self):
        return f"{self.name}:\n{Room.desc(self)}"
