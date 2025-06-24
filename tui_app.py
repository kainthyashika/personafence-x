# tui_app.py
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Header, Footer, Static, Button
from modules import fingerprint, detect, chatbot, report
import os

class PersonaDashboard(App):

    CSS_PATH = "style.css"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static("🛡️ PersonaFence - TUI Dashboard", classes="title")
        yield Vertical(
            Button("📌 Create Behavioral Fingerprint", id="fingerprint"),
            Button("🕵️ Analyze Suspicious Message(s)", id="analyze"),
            Button("🤖 Start AI ChatBot", id="chat"),
            Button("🧾 Generate PDF Report", id="report"),
            Button("❌ Exit", id="exit"),
            classes="menu"
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        choice = event.button.id

        if choice == "fingerprint":
            folder = input("Enter sample folder: ")
            user = input("Enter user name: ")
            fingerprint.create_profile(folder, user)

        elif choice == "analyze":
            path = input("File/Folder to check: ")
            user = input("Profile to compare: ")
            if os.path.isdir(path):
                results = detect.analyze_folder(path, user)
                for r in results:
                    print(f"{r['file']} - Score: {r['score']}%, Verdict: {r['verdict']}")
            else:
                r = detect.analyze_message(path, user)
                if isinstance(r, dict):
                    print(f"{r['file']} - Score: {r['score']}%, Verdict: {r['verdict']}")
                else:
                    print(r)

        elif choice == "chat":
            user = input("Enter profile name: ")
            chatbot.start_chat(user)

        elif choice == "report":
            user = input("Profile name: ")
            message_file = input("Suspicious message file: ")
            score = float(input("Score: "))
            verdict = input("Verdict: ")
            output = input("Output file name: ") or "report.pdf"
            report.generate_pdf(output_path=output, user=user, score=score, verdict=verdict, message_file=message_file)

        elif choice == "exit":
            self.exit()

if __name__ == "__main__":
    PersonaDashboard().run()
