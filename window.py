from Tkinter import *

#Placeholder function until I learn how to save in perhaps HTML format
#Prints all entries to console
#GOAL: Make a function that outputs all entries and saves them to HTML format
def print_entries():
    for i in range(len(entries)):
        print(entries[i].get())

#Generic function used to create empty column/row of any size
#Seems extremely cumbersome and doesn't output properly all the time
#Not currently in use
#GOAL: Figure out a better way to create space between different sections
def empty_section(master, x, y, length, height):
    empty = Label(master, text='1234')
    empty.grid(column=x, 
               row=y, 
               columnspan=length, 
               rowspan=height)

#Creates all of the basic information for the character
#Not sure if I like the formatting the way it is currently
#GOAL: Add more characteristics
#GOAL: Change formattting to make it prettier
def set_basic(master):
    BASIC_SECTION_LABEL_ROW     = 0
    BASIC_SECTION_LABEL_COL     = 0
    BASIC_SECTION_LABEL_SPAN    = 100
    BASIC_ENTRY_LABEL_ROW       = BASIC_SECTION_LABEL_ROW + 1
    BASIC_ENTRY_LABEL_COL       = 0
    BASIC_ENTRY_LABEL_SPAN      = 1
    BASIC_ENTRY_ROW             = BASIC_ENTRY_LABEL_ROW
    BASIC_ENTRY_COL             = BASIC_ENTRY_LABEL_COL + 1
    BASIC_ENTRY_WIDTH           = 16
    BASIC_ENTRY_SPAN            = 4

    basicSectionLabel = Label(master, text='Basic Character Information')
    basicSectionLabel.grid(row=BASIC_SECTION_LABEL_ROW, 
                           column=BASIC_SECTION_LABEL_COL, 
                           columnspan=BASIC_SECTION_LABEL_SPAN)
                           
    #Prints labels for each entry() it places
    for value in range(len(base)):
        basicLabel = Label(master, text=base[value])
        basicLabel.grid(row=BASIC_ENTRY_LABEL_ROW,
                        column=BASIC_ENTRY_LABEL_COL+value*
                               (BASIC_ENTRY_LABEL_SPAN+BASIC_ENTRY_SPAN),
                        columnspan=BASIC_ENTRY_LABEL_SPAN)
                        
        basic = Entry(master)
        basic.config(width=BASIC_ENTRY_WIDTH)
        basic.grid(row=BASIC_ENTRY_ROW,
                   column=BASIC_ENTRY_COL+value*
                          (BASIC_ENTRY_LABEL_SPAN+BASIC_ENTRY_SPAN),
                   columnspan=BASIC_ENTRY_SPAN)

        entries[value] = basic

#Creates stat labels and input grid
def set_stats(master):
    STAT_SECTION_LABEL_ROW      = 3
    STAT_SECTION_LABEL_COL      = 0
    STAT_SECTION_LABEL_SPAN     = 5
    STAT_ROW_LABEL_ROW          = STAT_SECTION_LABEL_ROW + 2
    STAT_ROW_LABEL_COL          = 0
    STAT_ROW_LABEL_SPAN         = 1
    STAT_COL_LABEL_ROW          = STAT_SECTION_LABEL_ROW + 1
    STAT_COL_LABEL_COL          = STAT_ROW_LABEL_COL + STAT_ROW_LABEL_SPAN-1
    STAT_ENTRY_ROW              = STAT_COL_LABEL_ROW + 1
    STAT_ENTRY_COL              = STAT_ROW_LABEL_SPAN
    STAT_ENTRY_WIDTH            = 4

    colLabels = (' ', 'Base', 'Mod', 'Total', 'Bonus')
    
    statSectionLabel = Label(master, text='Statistics')
    statSectionLabel.grid(row=STAT_SECTION_LABEL_ROW, 
                          column=STAT_SECTION_LABEL_COL, 
                          columnspan=STAT_SECTION_LABEL_SPAN)
                          
    #Prints stat column labels
    for label in range(len(colLabels)):
        nextLabel = Label(master, text=colLabels[label])
        nextLabel.grid(row=STAT_COL_LABEL_ROW,
                       column=STAT_COL_LABEL_COL+label)
    #Places stat row labels and place stat entries
    for value in range(len(stats)):
        statLabel = Label(master, text=stats[value])
        statLabel.grid(row=STAT_ROW_LABEL_ROW+value, 
                       column=STAT_ROW_LABEL_COL, 
                       columnspan=STAT_ROW_LABEL_SPAN)
        
        orig = Entry(master)
        orig.config(width=STAT_ENTRY_WIDTH)
        orig.grid(row=STAT_ENTRY_ROW+value, 
                  column=STAT_ENTRY_COL)
        mod = Entry(master)
        mod.config(width=STAT_ENTRY_WIDTH)
        mod.grid(row=STAT_ENTRY_ROW+value, 
                 column=STAT_ENTRY_COL+1)
        total = Entry(master)
        total.config(width=STAT_ENTRY_WIDTH)
        total.grid(row=STAT_ENTRY_ROW+value,
                   column=STAT_ENTRY_COL+2)
        bonus = Entry(master)
        bonus.config(width=STAT_ENTRY_WIDTH)
        bonus.grid(row=STAT_ENTRY_ROW+value, 
                   column=STAT_ENTRY_COL+3)

        entries[value + len(base)] = total

#Creates resistance labels and input grid
def set_resist(master):
    RESIST_SECTION_LABEL_ROW    = 3
    RESIST_SECTION_LABEL_COL    = 5
    RESIST_SECTION_LABEL_SPAN   = 4
    RESIST_COL_LABEL_ROW        = RESIST_SECTION_LABEL_ROW + 1
    RESIST_COL_LABEL_COL        = RESIST_SECTION_LABEL_COL
    RESIST_COL_LABEL_SPAN       = 1
    RESIST_ROW_LABEL_ROW        = RESIST_COL_LABEL_ROW + 1
    RESIST_ROW_LABEL_COL        = RESIST_SECTION_LABEL_COL
    RESIST_ROW_LABEL_SPAN       = 1
    RESIST_ENTRY_ROW            = RESIST_ROW_LABEL_ROW
    RESIST_ENTRY_COL            = RESIST_ROW_LABEL_COL + 1
    RESIST_ENTRY_WIDTH          = 4
    RESIST_ENTRY_SPAN           = 1

    colLabels = (' ', 'Base', 'Mod', 'Total')

    resistSectionLabel = Label(master, text='Resistances')
    resistSectionLabel.grid(row=RESIST_SECTION_LABEL_ROW, 
                            column=RESIST_SECTION_LABEL_COL, 
                            columnspan=RESIST_SECTION_LABEL_SPAN)
    
    #Prints resistance column labels                        
    for label in range(len(colLabels)):
        nextLabel = Label(master, text=colLabels[label])
        nextLabel.grid(row=RESIST_COL_LABEL_ROW,
                       column=RESIST_COL_LABEL_COL+label,
                       columnspan=RESIST_COL_LABEL_SPAN)
    #Print resistance row labels and place resistance entries
    for value in range(len(resist)):
        resistLabel = Label(master, text=resist[value])
        resistLabel.grid(row=RESIST_ROW_LABEL_ROW+value, 
                         column=RESIST_ROW_LABEL_COL, 
                         columnspan=RESIST_ROW_LABEL_SPAN)

        orig = Entry(master)
        orig.config(width=RESIST_ENTRY_WIDTH)
        orig.grid(row=RESIST_ENTRY_ROW+value, 
                  column=RESIST_ENTRY_COL)
        mod = Entry(master)
        mod.config(width=RESIST_ENTRY_WIDTH)
        mod.grid(row=RESIST_ENTRY_ROW+value, 
                 column=RESIST_ENTRY_COL+1)
        total = Entry(master)
        total.config(width=RESIST_ENTRY_WIDTH)
        total.grid(row=RESIST_ENTRY_ROW+value, 
                   column=RESIST_ENTRY_COL+2)

        entries[value + len(base) + len(stats)] = total

#Combines all character modules into one winow
#This function will probably change a lot
#May want to make this a class
#GOAL: Just make this better.
def make_app(master):
    global base, stats, resist, entries

    base    = ('Name', 'Race', 'Class', 'Age', 'Weight')
    stats   = ('Strenth', 'Dexterity', 'Constitution', 
               'Intelligence', 'Wisdom', 'Charisma')
    resist  = ('Fortitude', 'Reflex', 'Willpower')
    entries = {}

    set_basic(master)
    set_stats(master)
    set_resist(master)

    updateButton = Button(master, text='Update', command=print_entries)
    updateButton.grid(row=12, 
                      column=60, 
                      sticky=SE)

#Need to make this better
root = Tk()
make_app(root)

root.mainloop()
