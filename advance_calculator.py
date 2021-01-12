import re
print("here is solution for your problem")
print("eneter exit to close your calculator")
previous =0
run=True
def maths():
    global run
    global previous
    equation =""
    if previous ==0:
        equation=input("enter your equation:")
    else:
        equation=input(str(previous))
    if equation=='exit':
        print("process finished")
        run=False
    else:
        equation = re.sub('[a-zA-Z,.:;()""?]','',equation)
        if previous ==0:
            previous=eval(equation)
        else:
            previous =eval(str(previous)+equation)
while run:
    maths()