from turtle import *

speed(0)

def tree(size, levels, angle):
    if levels == 0: return
    
    forward(size)
    right(angle)

    tree(size*0.8, levels-1, angle)

    left(angle*2)

    tree(size*0.8, levels-1, angle)

    right(angle)
    backward(size)


left(90)
tree(70, 7, 30)


mainloop()





# from turtle import *

# def sierpinski(size, levels):

#     if levels == 0:
#         for _ in range(3):
#             forward(size)
#             left(120)
#     else:
#         sierpinski(size / 2, levels - 1)
#         forward(size / 2)
#         sierpinski(size / 2, levels - 1)
#         backward(size / 2)
#         left(60)
#         forward(size / 2)
#         right(60)
#         sierpinski(size / 2, levels - 1)
#         left(60)
#         backward(size / 2)
#         right(60)

# speed(0)
# sierpinski(160, 5)
# mainloop()