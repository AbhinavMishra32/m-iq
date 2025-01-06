class T:
    def __init__(self, x):
        self.data = x
    
    def __add__(self, other):
        return T(self.data + other.data)
    
    def __mul__(self, other):
        return T(self.data * other.data)
    

if __name__ == "__main__":
    a = T(3)
    b = T(4)
    c = a + b
    print(type(c))
    print(c.data)
    d = a * b
    print(d.data)