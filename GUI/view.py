import tkinter as tk
import threading

from tkinter import messagebox
from report_generators.generate_team_report import create_team_report
from report_generators.generate_player_report import create_player_report
from report_generators.generate_full_report import create_full_report


def render_team_report():
    """render the team report"""
    try:
        create_team_report()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")


def render_player_report():
    """render the player report"""
    try:
        create_player_report()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")


def render_full_report():
    """render a full report"""
    try:
        create_full_report()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate report: {e}")

#
# # GUI
#


def setup_gui():
    # Create main window
    window = tk.Tk()
    window.title("NRL Reports Generator")
    window.geometry("350x200")  # W x H

    # button for generating the TEAM report
    btn_team_report = tk.Button(window, text="Generate Team Report",
                                command=lambda: threading.Thread(target=render_team_report).start())
    btn_team_report.pack(pady=10)  # Add vertical padding

    # button to generate PLAYER report
    btn_player_report = tk.Button(
        window, text="Generate Player Report",
        command=lambda: threading.Thread(target=render_player_report).start())
    btn_player_report.pack(pady=10)  # Add vertical padding

    # button to generate FULL report
    btn_full_report = tk.Button(
        window, text="Generate Full Report",
        command=lambda: threading.Thread(target=render_full_report).start())
    btn_full_report.pack(pady=10)  # Add vertical padding

    # button to exit the application
    btn_exit = tk.Button(window, text="Close Tool", command=window.quit)
    btn_exit.pack(pady=10)

    # Start the GUI event loop
    window.mainloop()
