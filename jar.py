class Jar:

    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.total = 0
    
    def __str__(self):
        return ("🍪" * self.total)
    
    def deposit(self, number):
        if self.total + number > self.capacity:
            raise ValueError("Cant add more cookies than capacity")
        self.total += number

    def withdraw(self, number):
        if number > self.total:
            raise ValueError("Not enough cookie to withdraw")
        self.total -= number
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity = 12):
        if capacity < 0:
            raise ValueError("Jar capacity too low")
        self._capacity = capacity

    @property
    def size(self):
        return self.total


def main():
    jar = Jar()
    jar.deposit(2)
    jar.deposit(3)
    print(jar)
    jar.withdraw(4)
    print(jar)
    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()    