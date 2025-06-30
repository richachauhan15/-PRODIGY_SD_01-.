import tkinter as tk

def convert():
    try:
        t = float(entry.get())
        unit = var.get()

        if unit == "Celsius":
            f = (t * 9/5) + 32
            k = t + 273
            result.config(text=f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")

        elif unit == "Fahrenheit":
            c = (t - 32) * 5/9
            k = c + 273
            result.config(text=f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")

        elif unit == "Kelvin":
            c = t - 273
            f = (c * 9/5) + 32
            result.config(text=f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")

        else:
            result.config(text="Select a valid unit")

    except ValueError:
        result.config(text="Enter a valid number")

win = tk.Tk()
win.title("Temperature Converter")
win.geometry("350x250")

tk.Label(win, text="Enter Temperature:", font=("Times New Roman", 16)).pack(pady=5)
entry = tk.Entry(win, font=("Times New Roman", 16))
entry.pack()

var = tk.StringVar(value="Celsius")
tk.OptionMenu(win, var, "Celsius", "Fahrenheit", "Kelvin").pack(pady=5)

tk.Button(win, text="Convert", command=convert, font=("Times New Roman", 16)).pack(pady=10)

result = tk.Label(win, text="", font=("Times New Roman", 18, "bold"), fg="black")
result.pack(pady=10)

win.mainloop()
