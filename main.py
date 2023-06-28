import tkinter as tk

x1 = 480
y1 = 330
x2 = 600
y2 = 460
arr = []

class Set:
    
    i = 0
    def __init__(self, num):
        self.num = num
    
    def generate_set(self,num):
        
        if Set.i == 0:
            print(arr)
            Set.i+=1

        for i in range(num+1):
            arr.append(i)
            i+=1 
            print(arr)
        
    
    def generate_shapes(self, canvas, num ):
        # Draw a small square on the canvas
        canvas.create_rectangle(x1, y1, x2, y2, outline='black')

    def generate_square(self, num):
        root = tk.Tk()


        canvas = tk.Canvas(root, width=1000, height=1000)
        canvas.pack()

        # Call generate_shapes and pass the canvas object
        self.generate_shapes(canvas, num)

        root.mainloop()

p1 = Set(2)
p1.generate_set(2)
p1.generate_square(2)





import tkinter as tk

# Size of the squares
size = 50

class Set:
    def _init_(self, num):
        self.num = num

    def generate_shapes(self, canvas, num):
        # Draw a large square
        canvas.create_rectangle(size, size, size * (num + 1), size * (num + 1), outline='black')
        # For each number in the set, draw a smaller square inside the larger square
        for i in range(1, num + 1):
            canvas.create_rectangle(i * size, size, (i + 1) * size, 2 * size, outline='black')

    def generate_square(self):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=1000, height=1000)
        canvas.pack()

        # Call generate_shapes and pass the canvas object
        self.generate_shapes(canvas, self.num)

        root.mainloop()

# Create a set representing the number 2
p1 = Set(2)
p1.generate_square()