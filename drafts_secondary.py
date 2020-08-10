class Ranger:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current

nums = Ranger(1,10)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))





