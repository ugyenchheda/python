from tkinter import *
root = Tk()
root.geometry('200x4000')
root.title('Ugyen Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'verdana 20 bold').pack()
Label(root, text = 'Click One :', font = 'arial 14 bold').place(x=40, y=80)

def my_madlibs():
    adjactive = input('Enter adjective : ')
    color = input('Enter a color name : ')
    thing = input('Enter a thing name :')
    place = input('Enter a place name : ')
    person= input('Enter a person name : ')
    adjactive1 = input('Enter a adjactive : ')
    insect= input('Enter a insect name : ')
    food = input('Enter a food name : ')
    verb = input('Enter a verb name : ')
    print('texts will be added here' +adjactive+ ' texts will be added here ' + color+ ' texts will be added here '+thing+ ' texts will be added here ' + place+ ' texts will be added here '+person+ ' texts will be added here '+adjactive1+ ' ' +insect +' .texts will be added here ' +food+ 'texts will be added here '+verb+ 'texts will be added here ' +verb+ '.')

def my_madlibs_2():
    name= input('Enter a name: ')
    place = input('Enter a place name: ')
    verb = input('Enter a verb in ing form: ')
    food = input('Enter a food name: ')
    animals= input('Enter a animal name : ')
    profession = input('Enter a profession name: ')
    cloth = input('Enter a piece of cloth name: ')
    things = input('Enter a thing name: ')
    print('text here ' + food + ', texts will be added here ' + name + ' texts will be added here' + place +'texts will be added here' + animals + ' texts will be added here' + profession + '. texts will be added here ' + things + ' texts will be added here ' + cloth + ' texts will be added here ' + verb + ' texts will be added here')

Button(root, text= 'The Photographer', font ='verdana 15', command= my_madlibs, bg = 'white').place(x=60, y=120)
Button(root, text= 'apple and apple', font ='verdana 15', command = my_madlibs_2 , bg = 'white').place(x=70, y=180)
root.mainloop()  
