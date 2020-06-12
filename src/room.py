# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name= name
        self.description= description
        self.n_to= None
        self.s_to= None
        self.e_to= None
        self.w_to= None
        self.items = []

    def __str__(self):
        output = f"You are currently at {self.name} \nWhere: {self.description} \nItems:{self.items}"
        

        if self.n_to:
            output += f'To the north [n] is: ' + self.n_to.name + '\n'
        if self.s_to:
            output += f'To the south [s] is: ' + self.s_to.name + '\n'
        if self.e_to:
            output += f'To the east [e] is: ' + self.e_to.name + '\n'
        if self.w_to:
            output += f'To the west [w] is: ' + self.w_to.name + '\n'
        
        return output