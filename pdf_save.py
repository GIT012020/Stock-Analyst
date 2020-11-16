from fpdf import FPDF
from interfaceLogic import read_file, open_path, data_analyst
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from tkinter import *


def save_pdf():

    root = Tk()
    root.withdraw()
    root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("pdf files", "*.pdf"),))

    data = read_file(open_path())
    analysed_data = data_analyst(data)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)

    '''takes file name as document title'''
    title_list = root.filename.split('/')
    title = (title_list[-1])

    '''create page layout'''

    pdf.cell(200, 10, txt=f'{title}', ln=1, align='C')
    try:

        if analysed_data[1] < 0:
            pdf.cell(200, 10, txt=f'Period result: STOCK DECREASE', ln=2, align='L')
        if analysed_data[1] == 0:
            pdf.cell(200, 10, txt=f'Period result: NO STOCK CHANGE', ln=2, align='L')
        if analysed_data[1] < 0:
            pdf.cell(200, 10, txt=f'Period result: STOCK INCREASE', ln=2, align='L')

    except TypeError:
        root2 = tk.Tk()
        root2.withdraw()
        canvas1 = tk.Canvas(root, width=300, height=300)
        canvas1.pack()
        tk.messagebox.showerror('Error', 'Please load data first.', icon='error')
        root2.destroy()
        return

    pdf.cell(200, 10, txt=f'Period dates: {analysed_data[0]}', ln=2, align='L')
    pdf.cell(200, 10, txt=f'Maximum price in the given period: {analysed_data[4]}', ln=2, align='L')
    pdf.cell(200, 10, txt=f'Minimum price in the given period: {analysed_data[5]}', ln=2, align='L')
    pdf.cell(200, 10, txt=f'Starting Price in the given period: {analysed_data[2]}', ln=2, align='L')
    pdf.cell(200, 10, txt=f'End Price in the given period: {analysed_data[3]}', ln=2, align='L')
    pdf.cell(200, 10, txt=f'Price change in the given period: {analysed_data[1]}', ln=2, align='L')

    '''save pdf'''
    pdf.output(f'{root.filename}.pdf')
    root.destroy()

