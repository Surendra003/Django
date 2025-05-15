class Sum:
    def __init__(self):
        self.array = [4, 5, 1, 8, 3]
        self.target = 7
    def twoSum(self):
        dict={}
        for i in range(len(self.array)):
            diff=self.target-self.array[i]
            if diff in dict:
                return f"{[i,dict[diff]]}"
            else:
                dict[self.array[i]]=i
obj=Sum()
print(obj.twoSum())