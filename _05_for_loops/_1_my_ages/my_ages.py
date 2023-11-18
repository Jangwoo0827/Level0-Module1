from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    age = simpledialog.askinteger(title="All Ages",prompt="how old are you")
    for i in range(age):
        print(i+1)
