import tkinter as tk
from tkinter import messagebox
import threading
from teams.generate_team_report import create_team_report
from players.generate_player_report import create_player_report
from generate_full_report import create_full_report


def render_team_report():
    try:
        create_team_report()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")


def render_player_report():
    try:
        create_player_report()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")


def render_full_report():
    try:
        create_full_report()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")


def setup_gui():
    # Create the main window
    window = tk.Tk()
    window.title("NRL Reports Generator")
    window.geometry("350x200")  # Width x Height

    # Create a button for generating the full report
    btn_generate_team_report = tk.Button(window, text="Generate Team Report",
                                         command=lambda: threading.Thread(target=render_team_report).start())
    btn_generate_team_report.pack(pady=10)  # Add some vertical padding

    # button to generate player report
    btn_generate_player_report = tk.Button(
        window, text="Generate Player Report",
        command=lambda: threading.Thread(target=render_player_report).start())
    btn_generate_player_report.pack(pady=10)  # Add some vertical padding

    # button to generate player report
    btn_generate_full_report = tk.Button(
        window, text="Generate Full Report",
        command=lambda: threading.Thread(target=render_full_report).start())
    btn_generate_full_report.pack(pady=10)  # Add some vertical padding

    # Create a button to exit the application
    btn_exit = tk.Button(window, text="Exit", command=window.quit)
    btn_exit.pack(pady=10)

    # Start the GUI event loop
    window.mainloop()


# if __name__ == "__main__":
#     setup_gui()
