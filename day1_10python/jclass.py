class Animals():
    def __init__(self,color,weight):
        self.color = color
        self.weight = weight
    def resources(self):
        print("The color is ",self.color)
        print("The weight is ",self.weight)

Tiger = Animals("brown",200)
Tiger.resources()
Monkey = Animals("black",100)
Monkey.resources()

'''
The color is  brown
The weight is  200
The color is  black
The weight is  100
'''