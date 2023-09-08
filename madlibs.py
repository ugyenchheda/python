from tkinter import *
root = Tk()
root.geometry('200x4000')
root.title('Ugyen Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click One :', font = 'arial 14 bold').place(x=40, y=80)

def my_madlibs():
  
    name= input('Enter a name: ')
    place = input('Enter a place name: ')
    verb = input('Enter a verb in ing form: ')
    food = input('Enter a food name: ')
    animals= input('Enter a animal name : ')
    profession = input('Enter a profession name: ')
    cloth = input('Enter a piece of cloth name: ')
    things = input('Enter a thing name: ')
    print('say ' + food + ', texts will be added here ' + name + ' texts will be added here' + place +'texts will be added here' + animals + ' texts will be added here' + profession + '. texts will be added here ' + things + ' texts will be added here ' + cloth + ' texts will be added here ' + verb + ' texts will be added here')
