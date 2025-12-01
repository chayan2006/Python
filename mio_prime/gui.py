import sys
import os

# Adjust path if running directly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import flet as ft
from mio_prime.core import MioAgent
from mio_prime import config

def main(page: ft.Page):
    page.title = config.SYSTEM_NAME
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_width = 400
    page.window_height = 800  # Mobile-like aspect ratio

    # Loading Screen
    loading_text = ft.Text("Initializing MIO PRIME...", color=ft.Colors.CYAN)
    page.add(ft.Column([ft.ProgressRing(), loading_text], alignment=ft.MainAxisAlignment.CENTER))
    page.update()

    try:
        agent = MioAgent()
    except Exception as e:
        page.add(ft.Text(f"Error: {e}", color=ft.Colors.RED))
        page.update()
        return

    page.clean()

    # --- UI Components ---

    # Chat Area
    chat_list = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    def add_message(text, sender="System"):
        color = ft.Colors.CYAN_ACCENT if sender == "MIO" else ft.Colors.WHITE
        alignment = ft.MainAxisAlignment.START if sender == "MIO" else ft.MainAxisAlignment.END
        
        chat_list.controls.append(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text(text, color=ft.Colors.BLACK if sender == "MIO" else ft.Colors.WHITE),
                        padding=10,
                        border_radius=10,
                        bgcolor=color if sender == "MIO" else ft.Colors.BLUE_GREY_900,
                        width=250, # Max width for bubbles
                    )
                ],
                alignment=alignment,
            )
        )
        page.update()

    # Input Area
    user_input = ft.TextField(
        hint_text="Type a command...",
        expand=True,
        border_color=ft.Colors.CYAN_400,
        on_submit=lambda e: send_command(e),
    )

    def send_command(e):
        text = user_input.value
        if not text:
            return
        
        user_input.value = ""
        add_message(text, config.OWNER_NAME)
        
        # Process via Agent
        if not agent.is_authenticated:
            if agent.auth.authenticate(text):
                agent.is_authenticated = True
                agent.logger.log("AUTH", "SUCCESS", "Via GUI")
                add_message(f"Welcome, Owner {config.OWNER_NAME}.", "MIO")
            else:
                add_message("Access denied.", "MIO")
        else:
            # Capture stdout/print from agent (mocking the interaction for GUI)
            # Since core.py prints to stdout, we need to adapt it or just handle logic here.
            # For this version, we'll replicate the core logic slightly or modify core to return strings.
            # Let's modify core.py to be more return-oriented in the future, 
            # but for now we will wrap the process_command logic.
            
            response_text = ""
            status = agent.process_command(text)
            
            # We need to fetch what the agent "said". 
            # Since process_command returns status, we can infer or fetch from memory.
            last_interaction = agent.memory.get_context()[-1] if agent.memory.get_context() else None
            if last_interaction and last_interaction['user'] == text:
                response_text = last_interaction['agent']
            else:
                response_text = "Command processed."

            add_message(response_text, "MIO")
            
            # Feedback Controls (Only show if it was a real command, not auth)
            if agent.last_query:
                feedback_row = ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.Icons.THUMB_UP,
                            icon_size=16,
                            tooltip="Correct",
                            on_click=lambda e: handle_feedback(True, agent.last_query)
                        ),
                        ft.IconButton(
                            icon=ft.Icons.THUMB_DOWN,
                            icon_size=16,
                            tooltip="Wrong",
                            on_click=lambda e: open_correction_dialog(agent.last_query)
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                )
                chat_list.controls.append(feedback_row)
            
            if status == "HALT":
                page.window_close()

        page.update()

    def handle_feedback(is_correct, query):
        if is_correct:
            snack = ft.SnackBar(ft.Text("Thanks! I've reinforced this knowledge."))
            page.overlay.append(snack)
            snack.open = True
            page.update()
        else:
            pass # Handled by dialog

    # Correction Dialog
    correction_input = ft.TextField(label="What should I have said?")
    
    def save_correction(e):
        query = correction_dialog.data # We store the query here
        new_answer = correction_input.value
        if new_answer:
            agent.knowledge_base.learn(query, new_answer)
            agent.logger.log("LEARNING", "CORRECTION", f"Updated answer for '{query}'")
            
            correction_dialog.open = False
            correction_input.value = ""
            
            snack = ft.SnackBar(ft.Text("Learned! I will remember this next time."))
            page.overlay.append(snack)
            snack.open = True
            page.update()

    correction_dialog = ft.AlertDialog(
        title=ft.Text("Teach MIO"),
        content=correction_input,
        actions=[
            ft.TextButton("Save", on_click=save_correction),
            ft.TextButton("Cancel", on_click=lambda e: close_dialog()),
        ],
    )

    def close_dialog():
        correction_dialog.open = False
        page.update()

    def open_correction_dialog(query):
        correction_dialog.data = query
        page.dialog = correction_dialog
        correction_dialog.open = True
        page.update()

    send_button = ft.IconButton(
        icon=ft.Icons.SEND_ROUNDED,
        icon_color=ft.Colors.CYAN_400,
        on_click=lambda e: send_command(e)
    )

    # Voice Auth / Enrollment Logic
    def trigger_voice_auth(e=None):
        # Run in thread to not block UI
        def _auth_thread():
            if not agent.auth.is_configured():
                # --- ENROLLMENT FLOW ---
                add_message("SYSTEM NOT CONFIGURED.", "System")
                add_message("Please speak your desired secret phrase to set up ownership.", "System")
                agent.auth.voice.speak("System not configured. Please speak your desired secret phrase to set up ownership.")
                page.update()
                
                phrase = agent.auth.voice.listen(timeout=10)
                
                if phrase:
                    agent.auth.set_voice_key(phrase)
                    add_message(f"Voice Key Saved: '{phrase}'", "System")
                    add_message("Ownership granted.", "System")
                    agent.auth.voice.speak("Voice key saved. Ownership granted.")
                    
                    agent.is_authenticated = True
                    agent.logger.log("AUTH", "ENROLLMENT", "New Key Set")
                    add_message(f"Welcome, Owner {config.OWNER_NAME}.", "MIO")
                    agent.auth.voice.speak(f"Welcome, Owner {config.OWNER_NAME}.")
                else:
                    add_message("Enrollment failed. Could not hear you.", "System")
                    agent.auth.voice.speak("Enrollment failed.")
            else:
                # --- AUTH FLOW ---
                add_message("Listening...", "System")
                page.update()
                
                success, phrase = agent.auth.authenticate_voice()
                if phrase:
                    add_message(f"Heard: {phrase}", "You")
                    if success:
                        agent.is_authenticated = True
                        agent.logger.log("AUTH", "SUCCESS", "Via Voice")
                        add_message(f"Welcome, Owner {config.OWNER_NAME}.", "MIO")
                        agent.auth.voice.speak(f"Welcome, Owner {config.OWNER_NAME}.")
                    else:
                        target = agent.auth.get_voice_key()
                        add_message(f"Access denied. (Expected: '{target}')", "MIO")
                        agent.auth.voice.speak("Access denied.")
                else:
                    add_message("Could not hear you.", "System")
            
            page.update()

        import threading
        threading.Thread(target=_auth_thread).start()

    voice_auth_btn = ft.IconButton(
        icon=ft.Icons.MIC,
        icon_color=ft.Colors.RED_ACCENT,
        tooltip="Voice Auth",
        on_click=trigger_voice_auth
    )

    input_row = ft.Row([voice_auth_btn, user_input, send_button])

    # Login Overlay (Simple visibility toggle for now, or just start with chat)
    # We'll start with a system message in the chat.
    add_message("SYSTEM ONLINE.", "MIO")

    # Layout
    page.add(
        ft.Column(
            [
                ft.Text("MIO PRIME", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN),
                ft.Divider(color=ft.Colors.CYAN_900),
                chat_list,
                ft.Divider(color=ft.Colors.CYAN_900),
                input_row,
            ],
            expand=True,
        )
    )
    
    # Auto-trigger voice auth on startup - DISABLED
    # trigger_voice_auth()

if __name__ == "__main__":
    ft.app(target=main)
