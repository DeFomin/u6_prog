from tkinter import *
from tkinter import messagebox
from math import sqrt, pi


class Main(Frame):
	def __init__(self, root):
		super(Main, self).__init__(root)
		self.build()
	def build(self):
		self.formula = '0'
		self.lbl = Label(text=self.formula, font=('Arial', 32, 'bold'), bg='#f0f0f0', foreground='#000')
		self.lbl.place(x=10, y=50)


		buttons = [
            'C', 'DEL', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '+/-', '^2', '=']


		x = 10
		y = 140
		for btn in buttons:
			com = lambda f=btn: self.logicalc(f)
			Button(text=btn, bg='#e9e9e9', font=('Arial', 16), command=com).place(x=x, y=y, width=90, height=78)
			x += 92
			if x > 300:
				x = 10
				y += 80

	def logicalc(self, operation):
		if operation == 'C':
			self.formula = ''
		elif operation == 'DEL':
			self.formula = self.formula[0:-1]
		elif operation == '^2':
			self.formula = str((eval(self.formula)) ** 2)
		elif operation == '=':
			self.formula = str(eval(self.formula))
		elif operation == '+/-':
			self.formula = str(-eval(self.formula))
		else:
			if self.formula == '0':
				self.formula = ''
			self.formula += operation
		self.update()

	def update(self):
		if self.formula == '':
			self.formula = '0'
		self.lbl.configure(text=self.formula)

class Example(Frame):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		vr = 0
		self.pack(fill=BOTH, expand=1)
		canvas = Canvas(self)
		canvas.create_line(450, 0, 450, 1000)

		canvas.pack(fill=BOTH, expand=1)

class GUI():
	# global db
	def __init__(self, master):
		# super().__init__()
		self.master = master

		def validate(value, action):
			if action == '1':
				return value.isdigit()
			return True


		self.len = Label(master, text="Длина: ", font=('Arial', 11))
		self.len.place(relx=0.73, rely=0.15)
		self.var = StringVar()
		self.arg_1_ent = Entry(master, validate="all", textvariable=self.var, width=10)
		self.arg_1_ent['vcmd'] = (self.arg_1_ent.register(validate),'%P','%d')
		self.arg_1_ent.place(relx=0.825, rely=0.15, relwidth=0.1, relheight=0.05)

		self.len = Label(master, text="Высота: ", font=('Arial', 12))
		self.len.place(relx=0.73, rely=0.20)
		self.var_2 = StringVar()
		self.arg_2_ent = Entry(master, validate="all", textvariable=self.var_2, width=10)
		self.arg_2_ent['vcmd'] = (self.arg_2_ent.register(validate),'%P','%d')
		self.arg_2_ent.place(relx=0.825, rely=0.20, relwidth=0.1, relheight=0.05)

		self.l = Label(master, text="", font=('Arial', 14))
		self.l.place(relx=0.6, rely=0.45)

		# self.but = Button(master, text="OK")
		# self.but.place(relx=0.825, rely=0.4, relwidth=0.1, relheight=0.05)

#-------------------------------------------------------------------------
		# def test(event):
		# 	self.gt = self.var.get()
		# 	self.gt_2 = self.var_2.get()
		# 	self.l["text"] = str(int(self.gt)* int(self.gt_2))
		#
		# self.but.bind('<Button-1>', test())
#-------------------------------------------------------------------------

		def show_square():
			s = str(int(self.var.get()) * int(self.var_2.get())); self.l["text"]= "Площадь: " + str(int(self.var.get()) * int(self.var_2.get()))
			self.canvas = Canvas(width=427, height=533)
			self.canvas.create_rectangle(0, 0, self.var.get(), self.var_2.get(), fill='black')
			self.canvas.place(relx=0.01, rely=0.01)


		def show_perim():
			s = str(int(self.var.get())*2 + int(self.var_2.get())*2); self.l["text"]= "Периметр: " + str(int(self.var.get())*2 + int(self.var_2.get())*2)
			# window = Tk()
			# window.title('Прямоугольник')
			# _canvas = Canvas(window, width=100, height=400, bg='#f0f0f0')
			# a = int(s)
			# _canvas.create_rectangle(200 - a, 225 - a, 200 + a, 225 + a, fill='black')
			# _canvas.pack()
			# window.mainloop()
			self.canvas = Canvas(width=427, height=533)
			self.canvas.create_rectangle(0, 0, self.var.get(), self.var_2.get(), fill='black')
			self.canvas.place(relx=0.01, rely=0.01)


		def calc_active():
			self.square["state"] = "disabled"
			self.perim["state"] = "disabled"
			self.canvas = Canvas(width=427, height=533)
			self.canvas.create_rectangle(0, 0, 450, 1000, fill="#f0f0f0")
			self.canvas.place(relx=0, rely=0, relwidth=0.6, relheight=1)
			self.app = Main(master)
			# self.temp_1 = self.var.get(); self.temp_2 = self.var_2.get()
			self.arg_1_ent.delete(0, END)
			self.arg_2_ent.delete(0, END)

			# self.app.mainloop()




		def rectangle_active():
			self.square["state"] = "normal"
			self.perim["state"] = "normal"
			self.canvas = Canvas()
			self.canvas.create_rectangle(0, 0, 450, 1000, fill="#f0f0f0")
			self.canvas.place(relx=0, rely=0, relwidth=0.6, relheight=1)



		self.square = Checkbutton(master, text="Площадь",command=show_square)
		self.square.place(relx=0.825, rely=0.30)
		self.perim = Checkbutton(master, text="Периметр",command=show_perim)
		self.perim.place(relx=0.825, rely=0.34)


		self.calc = Radiobutton(master, text="Калькулятор", value=1, command=calc_active)
		self.calc.place(relx=0.6, rely=0.07)

		self.rectangle = Radiobutton(master, text="Прямоугольник", value=2, command=rectangle_active)
		self.rectangle.place(relx=0.8, rely=0.07)

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.place(relx=0.89, rely=0.91, relwidth=0.1, relheight=0.07)



if __name__ == '__main__':
	root = Tk()
	ex = Example()
	db = GUI(root)

	root['bg'] = '#f0f0f0'
	root.geometry('885x550+200+200')
	root.title('Calculator')
	root.resizable(False, False)

	root.mainloop()
