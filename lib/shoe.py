#!/usr/bin/env python3

class Shoe:

    def __init__(self, product_brand, product_size):
        self.brand = product_brand
        self.size = product_size
        self.condition = "New after repair"
        
        
    def repair(self):
        self.condition = "New"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
            
    