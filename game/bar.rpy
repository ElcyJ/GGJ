style the_bar:
    keyboard_focus True



screen bar :
     bar :
        bar_vertical True
        #value VariableValue('var',100)
        value AnimatedValue(value=0.0, range=100, delay=2.0, old_value=100)

        range 100
        xysize(50,500)
        xalign 0.05
        yalign 0.1



$ count = 0
while count < 40:
    $ varaa += 1
    $ counting += 1
    pause 0.01
#value StaticValue(barvariable, 100)
