class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.lenght = 0  
        self.array = [None] * self.capacity 

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n  
            
    def pushback(self, n: int) -> None:
        if self.lenght == self.capacity: 
            self.resize()
        self.array[self.lenght] = n  
        self.lenght += 1

    def popback(self) -> int:
        self.lenght -= 1
        return self.array[self.lenght]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        newArray = [0] * self.capacity 
        for i in range(self.lenght): 
            newArray[i] = self.array[i]
        self.array = newArray

    def getSize(self) -> int:
        return self.lenght
    
    def getCapacity(self) -> int:
        return self.capacity 