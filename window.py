from Tkinter import *

#Placeholder function until I learn how to save in perhaps HTML format
#Prints all entries to console
#GOAL: Make a function that outputs all entries and saves them to HTML format
<<<<<<< HEAD
def print_entries():
=======
def printEntries():
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81
    for i in range(len(entries)):
        print(entries[i].get())

#Generic function used to create empty column/row of any size
#Seems extremely cumbersome and doesn't output properly all the time
#GOAL: Figure out a better way to create space between different sections
<<<<<<< HEAD
def empty_section(master, x, y, length, height):
=======
def emptySection(master, x, y, length, height):
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81
    empty = Label(master, text='  ')
    empty.grid(column=x, 
               row=y, 
               columnspan=length, 
               rowspan=height)

#Creates all of the basic information for the character
#Not sure if I like the formatting the way it is currently
#GOAL: Add more characteristics
#GOAL: Change formattting to make it prettier
<<<<<<< HEAD
def set_basic(master):
    BASIC_WIDTH = 16
    BASIC_ROW = 1; BASIC_COL = 0; BASIC_SPAN = 6

    basicSectionLabel = Label(master, text='Basic Character Information')
    basicSectionLabel.grid(row=BASIC_ROW, 
                            column=BASIC_COL, 
                            columnspan=100)

    for value in range(len(base)):
        basicLabel = Label(master, text=base[value])

        basic = Entry(master)
        basic.config(width=BASIC_WIDTH)

        if(value != 0):
            basicLabel.grid(row=BASIC_ROW+1, 
                            column=value*(BASIC_WIDTH/2)+2*value, 
                            columnspan=4)
            basic.grid(row=BASIC_ROW+1, 
                       column=value*(BASIC_WIDTH/2)+BASIC_SPAN+2*(value-1), 
                       columnspan=BASIC_SPAN)
        else:
            basicLabel.grid(row=BASIC_ROW+1, 
                            column=value*(BASIC_WIDTH/2), 
                            columnspan=4)
            basic.grid(row=BASIC_ROW+1, 
                       column=value*(BASIC_WIDTH/2)+5, 
                       columnspan=BASIC_SPAN)
=======
def setBasic(master):
    basic_width = 16
    basic_row = 1; basic_col = 0; basic_span = 6

    base_section_label = Label(master, text='Basic Character Information')
    base_section_label.grid(row=basic_row, 
                            column=basic_col, 
                            columnspan=100)

    for value in range(len(base)):
        base_label = Label(master, text=base[value])

        basic = Entry(master)
        basic.config(width=basic_width)

        if(value != 0):
            base_label.grid(row=basic_row+1, 
                            column=value*(basic_width/2)+2*value, 
                            columnspan=4)
            basic.grid(row=basic_row+1, 
                       column=value*(basic_width/2)+basic_span+2*(value-1), 
                       columnspan=basic_span)
        else:
            base_label.grid(row=basic_row+1, 
                            column=value*(basic_width/2), 
                            columnspan=4)
            basic.grid(row=basic_row+1, 
                       column=value*(basic_width/2)+5, 
                       columnspan=basic_span)
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81

        entries[value] = basic

#Creates stat labels and input grid
#May need more entry() modules
#Formatting seems off
#GOAL: Label each entry column
#GOAL: Make the formatting look better
<<<<<<< HEAD
def set_stats(master):
    STAT_ROW = 4; STAT_COL = 0; STAT_WIDTH = 3

    statSectionLabel = Label(master, text='Statistics')
    statSectionLabel.grid(row=STAT_ROW, 
                            column=STAT_COL, 
=======
def setStats(master):
    stat_row = 4; stat_col = 0; stat_width = 3

    stat_section_label = Label(master, text='Statistics')
    stat_section_label.grid(row=stat_row, 
                            column=stat_col, 
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81
                            columnspan=9)

    for value in range(len(stats)):
        stat_label = Label(master, text=stats[value])
<<<<<<< HEAD
        stat_label.grid(row=STAT_ROW+value+1, 
=======
        stat_label.grid(row=stat_row+value+1, 
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81
                        column=0, 
                        columnspan=4)

        orig = Entry(master)
<<<<<<< HEAD
        orig.config(width=STAT_WIDTH)
        orig.grid(row=STAT_ROW+value+1, 
                  column=STAT_COL+5)

        mod = Entry(master)
        mod.config(width=STAT_WIDTH)
        mod.grid(row=STAT_ROW+value+1, 
                 column=STAT_COL+6)

        bonus = Entry(master)
        bonus.config(width=STAT_WIDTH)
        bonus.grid(row=STAT_ROW+value+1, 
                   column=STAT_COL+7)
=======
        orig.config(width=stat_width)
        orig.grid(row=stat_row+value+1, 
                  column=stat_col+5)

        mod = Entry(master)
        mod.config(width=stat_width)
        mod.grid(row=stat_row+value+1, 
                 column=stat_col+6)

        bonus = Entry(master)
        bonus.config(width=stat_width)
        bonus.grid(row=stat_row+value+1, 
                   column=stat_col+7)
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81

        entries[value + len(base)] = mod

#Creates resistance labels and input grid
#entry()'s are too spaced out
#GOAL: Fix spacing errors
#GOAL: Label each column
<<<<<<< HEAD
def set_resist(master):
    RESIST_ROW = 4; RESIST_COL = 9; RESIST_WIDTH = 3

    resistSectionLabel = Label(master, text='Resistances')
    resistSectionLabel.grid(row=RESIST_ROW, 
                              column=RESIST_COL, 
                              columnspan=7)

    for value in range(len(resist)):
        resistLabel = Label(master, text=resist[value])
        resistLabel.grid(row=RESIST_ROW+value+1, 
                          column=RESIST_COL, 
                          columnspan=4)

        orig = Entry(master)
        orig.config(width=RESIST_WIDTH)
        orig.grid(row=RESIST_ROW+value+1, 
                  column=RESIST_COL+4)

        mod = Entry(master)
        mod.config(width=RESIST_WIDTH)
        mod.grid(row=RESIST_ROW+value+1, 
                 column=RESIST_COL+5)

        total = Entry(master)
        total.config(width=RESIST_WIDTH)
        total.grid(row=RESIST_ROW+value+1, 
                   column=RESIST_COL+6)
=======
def setResist(master):
    resist_row = 4; resist_col = 9; resist_width = 3

    resist_section_label = Label(master, text='Resistances')
    resist_section_label.grid(row=resist_row, 
                              column=resist_col, 
                              columnspan=7)

    for value in range(len(resist)):
        resist_label = Label(master, text=resist[value])
        resist_label.grid(row=resist_row+value+1, 
                          column=resist_col, 
                          columnspan=4)

        orig = Entry(master)
        orig.config(width=resist_width)
        orig.grid(row=resist_row+value+1, 
                  column=resist_col+4)

        mod = Entry(master)
        mod.config(width=resist_width)
        mod.grid(row=resist_row+value+1, 
                 column=resist_col+5)

        total = Entry(master)
        total.config(width=resist_width)
        total.grid(row=resist_row+value+1, 
                   column=resist_col+6)
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81

    entries[value + len(base) + len(stats)] = total

#Combines all character modules into one winow
#This function will probably change a lot
#May want to make this a class
#GOAL: Just make this better.
<<<<<<< HEAD
def make_app(master):
=======
def makeApp(master):
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81
    global base, stats, resist, entries

    base = ('Name', 'Race', 'Class', 'Age', 'Weight')
    stats = ('Strenth', 'Dexterity', 'Constitution', 
             'Intelligence', 'Wisdom', 'Charisma')
    resist = ('Fortitude', 'Reflex', 'Willpower')

    entries = {}

<<<<<<< HEAD
    set_basic(master)
    set_stats(master)
    set_resist(master)

    empty_section(master, 8, 3, 1, 7)
    empty_section(master, 0, 3, 100, 1)

    updateButton = Button(master, text='Update', command=print_entries)
=======
    setBasic(master)
    setStats(master)
    setResist(master)

    emptySection(master, 8, 3, 1, 7)
    emptySection(master, 0, 3, 100, 1)

    updateButton = Button(master, text='Update', command=printEntries)
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81
    updateButton.grid(row=12, 
                      column=60, 
                      sticky=SE)

#Need to make this better
root = Tk()
<<<<<<< HEAD
make_app(root)
=======
makeApp(root)
>>>>>>> eef8f9fc6c0ca2eb1df65e5ec172a5dedcd15e81

root.mainloop()
