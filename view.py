import tkinter as tk
from tkinter import messagebox
import threading
from main import create_word_document


def create_report():
    try:
        create_word_document()
        messagebox.showinfo("Success", "Report generated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")


def setup_gui():
    # Create the main window
    window = tk.Tk()
    window.title("NRL Reports Generator")
    window.geometry("350x150")  # Width x Height

    # Create a button for generating the full report
    btn_generate_report = tk.Button(window, text="Generate Full Report",
                                    command=lambda: threading.Thread(target=create_report).start())
    btn_generate_report.pack(pady=10)  # Add some vertical padding

    # Create a button to exit the application
    btn_exit = tk.Button(window, text="Exit", command=window.quit)
    btn_exit.pack(pady=10)

    # Start the GUI event loop
    window.mainloop()


if __name__ == "__main__":
    setup_gui()
