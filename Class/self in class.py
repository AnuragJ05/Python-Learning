class Car():
    def __init__(self,model,color):
        self.model=model
        self.color=color
    def show(self):
        print("Model is",self.model)
        print("color is",self.color)
audi= Car("audi all","blue")
ferari= Car("ferari all","green")
audi.show()
ferari.show()
    
