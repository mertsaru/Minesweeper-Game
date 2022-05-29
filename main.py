from tkinter import *
import settings
import utils
from Cell import Cell

#interface
root = Tk()
root.title('Minesweeper')
root.configure(bg='black') #background color
root.geometry('{}x{}'.format(settings.width,settings.height)) #Width x Height
root.resizable(False, False) # not to resize height and width

#For Title
top_frame = Frame(
    root,
    bg='black',
    width= settings.width,
    height= utils.height_perc(25),
)
top_frame.place(x=0,
                y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text = 'Minesweeper Game',
    font = ('',48)
)

game_title.place(
    x= utils.width_perc(25),y=0
)

#For Cell count
left_frame = Frame(
    root,
    bg='black',
    width= utils.width_perc(25),
    height= utils.height_perc(25)
)
left_frame.place(x=0,
                 y=utils.height_perc(25))

#For Mine count
left_frame2 = Frame(
    root,
    bg='black',
    width= utils.width_perc(25),
    height= utils.height_perc(25)
)
left_frame2.place(x=0,
                 y=utils.height_perc(50))

#For Game
center_frame= Frame(
    root,
    bg='black',
    width=utils.width_perc(75),
    height=utils.height_perc(75)
)
center_frame.place(x=utils.width_perc(25),
                   y=utils.height_perc(25))

#Creating buttons
for i in range(settings.Grid_size):
    for j in range(settings.Grid_size):
        c = Cell(i,j)
        c.create_button_obj(center_frame)
        c.cell_button_obj.grid(
            column=i,
            row=j
        )

Cell.randomize_mines()

Cell.cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0,y=0)

Cell.mine_count_label(left_frame2)
Cell.mine_count_label_obj.place(x=0 ,y=0)

#Run
root.mainloop()