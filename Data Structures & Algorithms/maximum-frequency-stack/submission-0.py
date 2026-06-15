class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = {}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] = self.stack.count(val)
        
        

    def pop(self) -> int:
        max_freq = max(self.freq.values())

        for i in range(len(self.stack)-1, -1, -1):
            if self.freq[self.stack[i]] == max_freq:
                val = self.stack.pop(i)

                self.freq[val] -= 1
                if self.freq[val] == 0:
                    del self.freq[val]

                return val


   
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()