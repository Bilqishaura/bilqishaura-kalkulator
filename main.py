import tkinter as tk
import math

class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Multi Tema")
        self.root.geometry("380x520")
        self.root.resizable(False, False)

        self.tema_index = 0
        self.tema = [
            {"bg": "#fa5e5e", "btn": "#f2c8c8", "txt": "#000"},
            {"bg": "#dff1ff", "btn": "#6cbcff", "txt": "#000"},
            {"bg": "#ffe4f0", "btn": "#ff9ec6", "txt": "#000"},
            {"bg": "#1e1e2f", "btn": "#3b82f6", "txt": "#fff"}
        ]

        self.display = tk.Entry(root, font=("Segoe UI", 20), justify='right', highlightthickness=0, borderwidth=0)
        self.display.pack(fill='x', padx=0, pady=0, ipady=12)

        tombol_frame = tk.Frame(root)
        tombol_frame.pack(expand=True, fill='both', padx=0, pady=0)

        tombol = [
            ['C','⌫','%','÷'],
            ['7','8','9','×'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['.','0','^','='],
            ['√','ln','(',')'],
        ]

        for r, row in enumerate(tombol):
            for c, val in enumerate(row):
                btn = tk.Button(tombol_frame, text=val, font=("Segoe UI", 16), command=lambda v=val: self.klik(v), relief=tk.RAISED, bd=3)
                btn.grid(row=r, column=c, sticky='nsew', padx=0, pady=0, ipadx=5, ipady=8)

        for i in range(4):
            tombol_frame.columnconfigure(i, weight=1)
        for i in range(6):
            tombol_frame.rowconfigure(i, weight=1)

        # Tombol ganti tema di bawah
        tema_btn = tk.Button(root, text="GANTI TEMA 🎨", command=self.ganti_tema)
        tema_btn.pack(fill='x', padx=0, pady=0)

        self.ganti_tema()

    def klik(self, nilai):
        try:
            if nilai == "C":
                self.display.delete(0, tk.END)
            elif nilai == "⌫":
                current = self.display.get()
                self.display.delete(0, tk.END)
                self.display.insert(0, current[:-1])
            elif nilai == "=":
                eksp = self.display.get()
                eksp = eksp.replace('×', '*').replace('÷', '/').replace('^', '**')
                hasil = eval(eksp)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, hasil)
            elif nilai == "√":
                hasil = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, hasil)
            elif nilai == "ln":
                hasil = math.log(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, hasil)
            else:
                self.display.insert(tk.END, nilai)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def ganti_tema(self):
        t = self.tema[self.tema_index]
        self.root.configure(bg=t['bg'])
        self.display.configure(bg=t['bg'], fg=t['txt'])
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for btn in widget.winfo_children():
                    btn.configure(bg=t['btn'], fg=t['txt'])
        self.tema_index = (self.tema_index + 1) % len(self.tema)

if __name__ == '__main__':
    root = tk.Tk()
    app = Kalkulator(root)
    root.mainloop()
