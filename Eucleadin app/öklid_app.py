import tkinter as tk
from tkinter import messagebox
import math

# Öklidyen mesafe fonksiyonu
def euclidean(x1, y1, x2, y2):
    x3 = (x1 - x2) ** 2
    y3 = (y1 - y2) ** 2
    distance = math.sqrt(x3 + y3)
    return distance

# Hesapla butonuna basıldığında yapılacak işlem
def calculate_distance():
    try:
        x1 = float(entry_x1.get())
        y1 = float(entry_y1.get())
        x2 = float(entry_x2.get())
        y2 = float(entry_y2.get())
        
        # Mesafeyi hesapla
        result = euclidean(x1, y1, x2, y2)
        messagebox.showinfo("Sonuç", f"İki nokta arasındaki mesafe: {result}")
    
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayılar girin!")

# Tkinter arayüzünü oluşturma
root = tk.Tk()
root.title("Öklidyen Mesafe Hesaplama Paneli")

# Giriş alanları
label_x1 = tk.Label(root, text="x1:")
label_x1.grid(row=0, column=0)
entry_x1 = tk.Entry(root)
entry_x1.grid(row=0, column=1)

label_y1 = tk.Label(root, text="y1:")
label_y1.grid(row=1, column=0)
entry_y1 = tk.Entry(root)
entry_y1.grid(row=1, column=1)

label_x2 = tk.Label(root, text="x2:")
label_x2.grid(row=2, column=0)
entry_x2 = tk.Entry(root)
entry_x2.grid(row=2, column=1)

label_y2 = tk.Label(root, text="y2:")
label_y2.grid(row=3, column=0)
entry_y2 = tk.Entry(root)
entry_y2.grid(row=3, column=1)

# Hesapla düğmesi
button_calculate = tk.Button(root, text="Hesapla", command=calculate_distance)
button_calculate.grid(row=4, column=0, columnspan=2)

# Paneli başlat
root.mainloop()