import tkinter as tk

def start_recognition():
    # Add your code here to start the recognition process
    pass

# Create the main window
window = tk.Tk()

# Set the window size and position
window.geometry("800x600")

# Create a button to start the recognition
start_button = tk.Button(window, text="INICIAR RECONHECIMENTO", command=start_recognition)

# Place the button at the middle vertically and horizontally
start_button.pack(anchor=tk.CENTER, expand=True)

# Run the main event loop
window.mainloop()