import sys
import os

# Adjust path if running directly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import flet as ft
from mio_prime.gui import main

if __name__ == "__main__":
    print("Launching MIO PRIME in your web browser...")
    # view=ft.AppView.WEB_BROWSER tells Flet to open in the default browser
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
