import tkinter as tk
from tkinter import messagebox

# Conversion Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Main Function to Convert Temperature
def convert_temperature():
    print("Convert button clicked!")  # Confirm the button click
    try:
        # Get the input value from the entry field
        temp_str = entry_temp.get()
        print(f"Entered temperature (as string): {temp_str}")

        # Try converting the input to a float
        temp = float(temp_str)
        print(f"Converted temperature (as float): {temp}")

        # Get the selected unit
        unit = unit_var.get()
        print(f"Selected unit: {unit}")

        # Perform conversion based on the selected unit
        if unit == 'Celsius':
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            result.set(f"{temp:.2f}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")
            print(f"Result: {temp:.2f}°C = {fahrenheit:.2f}°F = {kelvin:.2f}K")
        elif unit == 'Fahrenheit':
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            result.set(f"{temp:.2f}°F = {celsius:.2f}°C = {kelvin:.2f}K")
            print(f"Result: {temp:.2f}°F = {celsius:.2f}°C = {kelvin:.2f}K")
        elif unit == 'Kelvin':
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            result.set(f"{temp:.2f}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
            print(f"Result: {temp:.2f}K = {celsius:.2f}°C = {fahrenheit:.2f}°F")
        else:
            messagebox.showerror("Error", "Please select a valid unit")
    except ValueError as e:
        # Error if the input is not a valid number
        print(f"Error: Invalid input value for temperature. {e}")
        messagebox.showerror("Invalid Input", "Please enter a valid temperature value.")

# Set up the main application window
app = tk.Tk()
app.title("Temperature Converter")
app.geometry("400x250")  # Increased height to accommodate results

# Input field for temperature
label_temp = tk.Label(app, text="Enter Temperature:")
label_temp.pack(pady=10)
entry_temp = tk.Entry(app, width=10)
entry_temp.pack(pady=5)

# Dropdown menu for temperature units
unit_var = tk.StringVar(app)
unit_var.set("Celsius")  # Default unit
units_menu = tk.OptionMenu(app, unit_var, "Celsius", "Fahrenheit", "Kelvin")
label_unit = tk.Label(app, text="Select Unit:")
label_unit.pack(pady=10)
units_menu.pack(pady=5)

# Button to trigger conversion
convert_button = tk.Button(app, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

# Result display label
result = tk.StringVar()
label_result = tk.Label(app, textvariable=result, font=("Arial", 14))
label_result.pack(pady=20)  # Added more padding for clarity

# Start the application
app.mainloop()
