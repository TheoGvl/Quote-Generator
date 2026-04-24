import flet as ft
import requests

def main(page: ft.Page):
    # --- Window Settings ---
    page.title = "Zen Wisdom"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 450
    page.window.height = 300
    page.window.always_on_top = True  # Keeps the widget floating above other windows
    page.padding = 40
    
    # Center everything perfectly in the window
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#121212"

    # --- UI Elements ---
    # We start with a placeholder greeting
    initial_text = ft.Text(
        "Breathe in. Press the star for wisdom.",
        size=20,
        italic=True,
        weight=ft.FontWeight.W_300,
        color="white70",
        text_align=ft.TextAlign.CENTER,
        # The key is crucial for AnimatedSwitcher to know when content changes
        key="initial_greeting" 
    )

    # The AnimatedSwitcher wraps our text to provide the smooth fade effect
    quote_display = ft.AnimatedSwitcher(
        content=initial_text,
        transition=ft.AnimatedSwitcherTransition.FADE,
        duration=800, # 800 milliseconds for a slow, relaxing fade
        reverse_duration=800,
        switch_in_curve=ft.AnimationCurve.EASE_IN_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN_OUT
    )

    # --- API Logic ---
    def fetch_advice(e=None):
        # Briefly fade to a "thinking" state
        quote_display.content = ft.Text(
            "Seeking clarity...",
            size=18,
            italic=True,
            color="white30",
            text_align=ft.TextAlign.CENTER,
            key="loading_state"
        )
        page.update()

        try:
            # Fetching from the free AdviceSlip API
            response = requests.get("https://api.adviceslip.com/advice")
            response.raise_for_status()
            data = response.json()
            new_advice = data["slip"]["advice"]
            
            # Update the text inside the AnimatedSwitcher.
            # Using the actual quote as the 'key' forces the fade animation to trigger.
            quote_display.content = ft.Text(
                f'"{new_advice}"',
                size=24,
                italic=True,
                weight=ft.FontWeight.W_400,
                color="white",
                text_align=ft.TextAlign.CENTER,
                key=new_advice 
            )
        except Exception:
            # Minimalist error handling
            quote_display.content = ft.Text(
                "Silence is also an answer. (Network Error)",
                size=18,
                color="#FF5555",
                text_align=ft.TextAlign.CENTER,
                key="error_state"
            )
        
        page.update()

    # --- Controls ---
    # The bulletproof custom button using a star emoji
    action_button = ft.Container(
        content=ft.Text("New Quote", size=30),
        on_click=fetch_advice,
        padding=10,
        border_radius=50,
        ink=True, # Provides a ripple effect when clicked
        tooltip="Draw a new piece of advice",
        alignment=ft.Alignment(0, 0)
    )

    # --- Build Page ---
    page.add(
        quote_display,
        ft.Container(height=30), # Clean spacing
        action_button
    )

if hasattr(ft, 'run'):
    ft.run(main)
else:
    ft.app(target=main)