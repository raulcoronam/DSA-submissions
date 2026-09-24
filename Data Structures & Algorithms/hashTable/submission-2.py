class HashTable:

    class Pair: 
        def __init__(self, key, value):
            self.key = key
            self.value = value 
        
    TOMBSTONE = Pair(None, None)

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0 
        self.map = [None] * capacity 

    def insert(self, key: int, value: int) -> None:
        
        index = key % self.capacity 

        while True: 

            if self.map[index] is None:
                self.map[index] = self.Pair(key, value) 
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return

            elif self.map[index].key == key: 
                self.map[index].value = value
                return

            index = (index + 1) % self.capacity 

    def get(self, key: int) -> int:
        
        index = key % self.capacity 

        while True: 

            if self.map[index] is None: 
                return -1

            elif self.map[index].key == key: 
                return self.map[index].value  
            
            index = (index + 1) % self.capacity 

    def remove(self, key: int) -> bool:

        index = key % self.capacity

        while True: 
        
            if self.map[index] is None:
                return False 

            elif self.map[index].key == key: 
                self.map[index] = self.TOMBSTONE
                self.size -= 1
                return True 
            
            index = (index + 1) % self.capacity 

    def getSize(self) -> int:
        
        return self.size
    
    def getCapacity(self) -> int:

        return self.capacity 

    def resize(self) -> None:
        self.size = 0
        self.capacity = self.capacity * 2
        oldMap = self.map  
        self.map = [None] * self.capacity 
        for pair in oldMap: 
            if pair is not None and pair is not self.TOMBSTONE:
                self.insert(pair.key, pair.value)


