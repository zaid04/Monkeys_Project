from utils import check_hexacolor
class Monkey:
    """A monkey."""
    def __init__(self,fur_color,size,weight,species=''):
        if not check_hexacolor(fur_color):
            raise KeyError("Invalid hexadecimal color code")
        self.fur_color=fur_color
        self.size=size
        self.weight=weight
        self.species=species
    def __str__(self):
        print(f"Monkey ({self.species}), {self.weight}kg, {self.size}cm, fur: {self.fur}")
    def __repr__(self):
        print(f"Monkey ({self.species}), {self.weight}kg, {self.size}cm, fur: {self.fur}")
    def compute_bmi(self):
        return self.weight/self.size**2
