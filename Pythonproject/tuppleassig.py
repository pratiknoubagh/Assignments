#ans1:
color=("red","blue","green","yellow","black","white")
print("The second color is",color[1])

#ans2:
#modify=color.append("grey")
# Message displayed-AttributeError: 'tuple' object has no attribute 'append' because a tuple is immutable .

#ans3:
print("The colors in tupples are:")
for colname in color:
    print(colname)