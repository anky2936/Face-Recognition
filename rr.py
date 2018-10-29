import tkinter
from tkinter import messagebox
# hide main window
window = tkinter.Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
if():
    messagebox.showinfo("Information","Access Granted")
else:
    messagebox.showerror("Information","Access Denied")

window.quit()
