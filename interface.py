import tkinter as tk
import detect as detect

def iniciarDeteccao():
    window.destroy()
    detect.reconhecimento_facial_tempo_real()

# Create the main window
window = tk.Tk()

# Set the window size and position
window.geometry("800x600")

# Create a button to start the recognition
start_button = tk.Button(window, text="INICIAR RECONHECIMENTO", command=iniciarDeteccao)

# Place the button at the middle vertically and horizontally
start_button.pack(anchor=tk.CENTER, expand=True)

# Run the main event loop
window.mainloop()
