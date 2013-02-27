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
    for value in range(len(basic)):
        basicLabel = Label(master, text=basic[value])
        base = Entry(master)
        base.config(width=BASIC_ENTRY_WIDTH)
        
        if value <= 4:
            basicLabel.grid(row=BASIC_ENTRY_LABEL_ROW,
                            column=BASIC_ENTRY_LABEL_COL+value*
                                   (BASIC_ENTRY_LABEL_SPAN+BASIC_ENTRY_SPAN),
                            columnspan=BASIC_ENTRY_LABEL_SPAN)
            base.grid(row=BASIC_ENTRY_ROW,
                       column=BASIC_ENTRY_COL+value*
                              (BASIC_ENTRY_LABEL_SPAN+BASIC_ENTRY_SPAN),
                       columnspan=BASIC_ENTRY_SPAN)
        else:
            basicLabel.grid(row=BASIC_ENTRY_LABEL_ROW+1,
                            column=BASIC_ENTRY_LABEL_COL+(value-5)*
                                   (BASIC_ENTRY_LABEL_SPAN+BASIC_ENTRY_SPAN),
                            columnspan=BASIC_ENTRY_LABEL_SPAN)
            base.grid(row=BASIC_ENTRY_ROW+1,
                       column=BASIC_ENTRY_COL+(value-5)*
                              (BASIC_ENTRY_LABEL_SPAN+BASIC_ENTRY_SPAN),
                       columnspan=BASIC_ENTRY_SPAN)

        entries[value] = base

#Creates stat labels and input grid
def set_stats(master):
    STAT_SECTION_LABEL_ROW      = 4
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

        entries[value + len(basic)] = total

#Creates resistance labels and input grid
def set_resist(master):
    RESIST_SECTION_LABEL_ROW    = 4
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

        entries[value + len(basic) + len(stats)] = total

def set_AC(master):
    AC_SECTION_LABEL_ROW    = 9
    AC_SECTION_LABEL_COL    = 6
    AC_SECTION_LABEL_SPAN   = 4
    AC_COL_LABEL_ROW        = AC_SECTION_LABEL_ROW + 1
    AC_COL_LABEL_COL        = AC_SECTION_LABEL_COL
    AC_COL_LABEL_SPAN       = 1
    AC_ENTRY_ROW            = AC_COL_LABEL_ROW + 1
    AC_ENTRY_COL            = AC_COL_LABEL_COL
    AC_ENTRY_WIDTH          = 4
    AC_ENTRY_SPAN           = 1
    
    ACSectionLabel = Label(master, text='Armor Class')
    ACSectionLabel.grid(row=AC_SECTION_LABEL_ROW,
                        column=AC_SECTION_LABEL_COL,
                        columnspan=AC_SECTION_LABEL_SPAN)
    
    for label in range(len(ac)):
        nextLabel = Label(master, text=ac[label])
        nextLabel.grid(row=AC_COL_LABEL_ROW,
                       column=AC_COL_LABEL_COL+label,
                       columnspan=AC_COL_LABEL_SPAN)
        
        base = Entry(master)
        base.config(width=AC_ENTRY_WIDTH)
        base.grid(row=AC_ENTRY_ROW,
                  column=AC_ENTRY_COL+label)
        
        entries[label + len(basic) + len(stats) + len(ac)] = base
    
#Combines all character modules into one winow
def make_app(master):
    global basic, stats, resist, ac, entries

    basic   = ('Name', 'Race', 'Class', 'Age', 'Weight',
                'Alignment', 'Sex', 'Eyes', 'Hair', 'Height')
    stats   = ('Strenth', 'Dexterity', 'Constitution', 
               'Intelligence', 'Wisdom', 'Charisma')
    resist  = ('Fortitude', 'Reflex', 'Willpower')
    ac      = ('Base', 'FF', 'Touch')
    entries = {}

    set_basic(master)
    set_stats(master)
    set_resist(master)
    set_AC(master)

    updateButton = Button(master, text='Update', command=print_entries)
    updateButton.grid(row=12, 
                      column=60, 
                      sticky=SE)

#Need to make this better
root = Tk()
make_app(root)

root.mainloop()
