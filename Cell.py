from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all=[]
    cell_count = settings.Cell_number - settings.Mine_number
    mine_count = settings.Mine_number
    cell_count_label_obj=None
    mine_count_label_obj=None
    def __init__(self,x,y,is_mine=False):
        self.is_mine= is_mine
        self.is_opened = False
        self.is_flaged = False
        self.cell_button_obj= None
        self.x = x
        self.y = y

        # adding created cell to all list
        Cell.all.append(self)

    def create_button_obj(self,location):
        button = Button(
            location,
            width=12,
            height=4,
        )
        button.bind('<Button-1>', self.left_click_actions )
        button.bind('<Button-3>', self.right_click_actions)
        self.cell_button_obj = button

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_lenght == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()


    def right_click_actions(self, event):
        if not self.is_flaged and not self.is_opened:
            self.cell_button_obj.configure(
                bg='Orange'
                )
            self.is_flaged = True
            Cell.mine_count -= 1
        elif self.is_flaged:
            self.cell_button_obj.configure(bg='SystemButtonFace')
            self.is_flaged = False
            Cell.mine_count += 1
        Cell.mine_count_label_obj.configure(text='Remaining Mines: {}'.format(Cell.mine_count))


    @staticmethod
    def cell_count_label(location):
        lbl = Label(
            location,
            text='Remaining Cells: {}'.format(Cell.cell_count),
            width=20,
            height=6,
            bg='black',
            fg='white',
            font=("", 15)
        )
        Cell.cell_count_label_obj = lbl


    @staticmethod
    def mine_count_label(location):
        lbl = Label(
            location,
            text='Remaining Mines: {}'.format(Cell.mine_count),
            width=20,
            height=6,
            bg='black',
            fg='white',
            font=("", 15)
        )
        Cell.mine_count_label_obj = lbl


    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell


    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y - 0),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x - 0, self.y - 1),
            self.get_cell_by_axis(self.x - 0, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 0),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]

        #taking surrounding cells list also for corner cells
        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def surrounded_cells_mines_lenght(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter


    def show_mine(self):
        self.cell_button_obj.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'You hit a mine', 'Game Over',0)
        Cell.mine_count -= 1

        #Lose condition
        Cell.mine_count_label_obj.configure(text='Remaining Mines: {}'.format(Cell.mine_count))
        sys.exit()


    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button_obj.configure(text=self.surrounded_cells_mines_lenght)
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(text='Remaining Cells: {}'.format(Cell.cell_count))
            self.is_opened=True

        #Not to flag an opened cell
        if self.is_flaged:
            self.cell_button_obj.configure(bg = 'SystemButtonFace')

        #Win condition
        if Cell.cell_count == 0:
            ctypes.windll.user32.MessageBoxW(0,'You won!!','Congratulations', 0)
            sys.exit()


    @staticmethod
    def randomize_mines():
        mines = random.sample(
            Cell.all,settings.Mine_number
            )
        for mine in mines:
            mine.is_mine = True
