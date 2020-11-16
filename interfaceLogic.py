from tkinter import filedialog
from tkinter import *
import itertools
import tkinter as tk
from pandastable import Table
import matplotlib.pyplot as plt
from tkinter import messagebox


def open_file():

    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"),))

    '''save chosen file path'''
    chosen_file = open("chosen_file.txt", "w")
    chosen_file.write(root.filename)
    chosen_file.close()
    root.destroy()
    return root.filename


def read_file(file_path):
    try:
        with open(file_path) as opened_file:
            '''converts string format to the list'''
            converted_file_list = [(line.strip()).split(',') for line in opened_file]

            '''removes headline'''
            converted_file_list.pop(0)
            '''converts list with str to the list with numbers'''
            final_list = []
            for number in range(len(converted_file_list)):
                main_list_element = converted_file_list[number]
                for sub_list_element in range(1, len(main_list_element)):
                    main_list_element[sub_list_element] = float(main_list_element[sub_list_element])
                final_list.append(main_list_element)
        return final_list
    except FileNotFoundError:
        return 'FileNotFoundError'
    except ValueError:
        return 'ValueError'
    except IndexError:
        return 'IndexError'


def data_analyst(final_list):

    try:
        '''period dates'''
        start_data = final_list[0]
        start_data_correct = start_data[0]

        end_data = final_list[-1]
        end_data_correct = end_data[0]

        '''increase or decrease'''
        opening_rate = final_list[0]
        opening_rate_correct = opening_rate[1]

        closing_rate = final_list[-1]
        closing_rate_correct = closing_rate[4]

        increase_decrease = closing_rate_correct - opening_rate_correct

        '''max and min value'''
        max_mini_correct = []
        for number in range(len(final_list)):
            max_min = final_list[number]
            max_min_list = max_min[1:-1]
            max_mini_correct.append(max_min_list)
            max_mini_correct_list = (list(itertools.chain.from_iterable(max_mini_correct)))

        maximum_price = max(max_mini_correct_list)
        minimum_price = min(max_mini_correct_list)
        return f'{start_data_correct} / {end_data_correct}', increase_decrease, opening_rate_correct, closing_rate_correct, maximum_price, minimum_price
    except IndexError:
        return 'IndexError'
    except TypeError:
        return 'TypeError'


def open_path():

    try:
        chosen_file = open("chosen_file.txt")
        path = chosen_file.read()
        chosen_file.close()
        if path == '':
            return 'FileNotFoundError'
        else:
            return path
    except FileNotFoundError:
        return 'FileNotFoundError'


def closing_price():

    path = open_path()

    '''check if file with path exist'''
    if path == 'FileNotFoundError':
        return 'FileNotFoundError'
    else:
        data = read_file(path)[-1]
        price = data[4]
        return price


def data_to_charts(choice):

    path = open_path()

    '''check if file with path exist'''
    if path == 'FileNotFoundError':
        error_box('Please upload data first.')
        return

    data = read_file(path)

    date_list = []
    for element in data:
        date_list.append(element[0])

    opening_prices = []
    for element in data:
        opening_prices.append(element[1])

    closing_prices = []
    for element in data:
        closing_prices.append(element[4])

    daily_change_list = []
    number = len(opening_prices)
    flag = number
    for element in closing_prices:
        daily_change = element - opening_prices[number - flag]
        flag -= 1
        daily_change_list.append(round(daily_change, 2))

    volume = []
    for element in data:
        volume.append(element[5])

    if choice == 'OP':
        choice2 = message_box()
        if choice2 == 'N':
            create_chart(date_list, opening_prices, 'Opening prices PLN', 'DAILY OPENING PRICES', 'Opening Prices')
        if choice2 == 'Y':
            create_combine_chart(date_list, opening_prices, closing_prices,'Opening prices and closing PLN',
                                 'DAILY OPENING & CLOSING PRICES', 'Opening prices', 'Closing prices')

    if choice == 'DC':
        create_chart(date_list, daily_change_list, 'Daily changes PLN', 'DAILY VALUE CHANGES', 'Daily change')

    if choice == 'CP':
        choice2 = message_box()
        if choice2 == 'N':
            create_chart(date_list, closing_prices, 'Closing prices PLN', 'DAILY CLOSING PRICES', 'Closing prices')
        if choice2 == 'Y':
            create_combine_chart(date_list, opening_prices, closing_prices, 'Opening prices and closing PLN',
                                 'DAILY OPENING & CLOSING PRICES', 'Opening prices', 'Closing prices')

    if choice == 'DV':
        create_chart(date_list, volume, 'Volume', 'DAILY STOCK VOLUME', 'Volume')


def create_chart(list1, list2, y_name, chart_name, ax_name):

    x = list1
    y = list2
    plt.plot(x, y, linewidth=1)
    plt.legend([ax_name])
    plt.grid(True)
    plt.xlabel('X - DATE')
    plt.ylabel(f'Y - {y_name}')
    plt.title(chart_name)
    plt.show()


def create_combine_chart(list1, list2, list4, y_name, chart_name, ax_name, ay_name):
    x = list1
    y = list2
    x1 = list1
    y1 = list4

    plt.plot(x, y, label=ax_name, linewidth=1)
    plt.plot(x1, y1, label=ay_name, linewidth=1)
    plt.legend()
    plt.grid(True)
    plt.xlabel('X - DATE')
    plt.ylabel(f'Y - {y_name}')
    plt.title(chart_name)
    plt.show()


def show_data_table():

    path = open_path()
    if path == 'FileNotFoundError':
        error_box('Please upload data first.')
        return
    root = tk.Tk()
    root.title('STOCK ANALYST')

    frame = tk.Frame(root)
    frame.pack(fill='both', expand=True)
    datatable = Table(frame, showtoolbar=True, showstatusbar=True)
    datatable.show()

    '''shows data in the table'''
    datatable.importCSV(filename=path, dialog=False)
    root.mainloop()


def message_box():
    root = tk.Tk()
    root.withdraw()
    canvas1 = tk.Canvas(root, width=300, height=300)
    canvas1.pack()
    MsgBox = tk.messagebox.askquestion('Chart Choice',
                                       'Would you like to combine opening and closing prices into one chart?',
                                       icon='question')
    if MsgBox == 'yes':
        root.destroy()
        return 'Y'
    if MsgBox == 'no':
        root.destroy()
        return 'N'


def error_box(text):
    root = tk.Tk()
    root.withdraw()
    canvas1 = tk.Canvas(root, width=300, height=300)
    canvas1.pack()
    tk.messagebox.showerror('Error', f'{text}', icon='error')
    root.destroy()


if __name__ == '__main__':
    open_file()