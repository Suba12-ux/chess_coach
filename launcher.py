import tkinter as tk
import tkinter, Frame_update
import shell

class Chess_face:
	def __init__(self):

		self.tk = tk.Tk()
		self.tk.configure(bg='#5C151F')
		self.tk.title("Твой помошник <3")
		self.tk.geometry("%dx%d" % (400, 200))
		self.data = ''

		self.frame1 = tkinter.Frame(self.tk, bg="#8B3E48", bd=5, width=195, height=50) # bg="#8B3E48"
		self.frame1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, pady=5, padx=5)

		self.frame1_1 = tkinter.Frame(self.frame1, bg="#000000", bd=5, width=195, height=50) # bg="#000000"
		self.frame1_1.pack(side=tkinter.TOP, fill=tkinter.BOTH, pady=2, padx=2)

		self.frame2 = tkinter.Frame(self.tk, bg="#8B3E48", bd=5, width=195, height=50) # bg="#8B3E48"
		self.frame2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, pady=5, padx=5)

		self.frame2_1 = tkinter.Frame(self.frame2, bg="#000000", bd=5, width=195, height=50) # bg="#000000"
		self.frame2_1.pack(side=tkinter.TOP, fill=tkinter.BOTH, pady=2, padx=2)

		# Обозначения полей фрейм 1
		self.url = tk.Label(self.frame1_1, text='url-адрес:', font=("Arial", 10), fg="#000000", bg="#928F41").grid(row=0, column=0, pady=2, padx=2) # bg="#928F41"
		self.url_entry = tk.Entry(self.frame1_1, bg="#928F41")
		self.url_entry.grid(row=0, column=1, pady=2, padx=2) # bg="#928F41"
		tkinter.Button(self.frame1_1, text='подсказка', font=("Arial", 10), fg="#000000", bg="#C58991", command=lambda: self.start_bild() ).grid(row=1, pady=2, padx=2)

		self.tk.mainloop()

	def start_bild(self):

		self.data = shell.Chess_hint(self.url_entry.get()).viewing_branch()
		self.text1 = tk.Label(self.frame2_1, text='лучший ход', font=("Arial", 10), fg="#000000", bg="#928F41").grid(row=0, column=0, pady=2, padx=2, ) # bg="#928F41"
		self.text2 = tk.Label(self.frame2_1, text=self.data, font=("Arial", 10), fg="#000000", bg="#928F41").grid(row=2, column=0, pady=2, padx=2, ) # bg="#928F41"
Chess_face()