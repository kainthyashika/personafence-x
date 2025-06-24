# main.py
import os
from modules import fingerprint, detect, report, chatbot, ai_detector

def print_menu():
    print("\n🛡️ PersonaFence X – Impersonation Detection CLI\n")
    print("[1] Create Behavioral Fingerprint")
    print("[2] Analyze Suspicious Message(s)")
    print("[3] Start AI ChatBot")
    print("[4] Run AI-Generated Text Detector")
    print("[5] Generate PDF Report")
    print("[6] Exit")

def main():
    while True:
        print_menu()
        choice = input("\n👉 Enter your choice: ").strip()

        if choice == "1":
            folder = input("📁 Enter folder path of known messages: ").strip()
            user = input("👤 Enter user profile name: ").strip()
            fingerprint.create_profile(folder, user)

        elif choice == "2":
            path = input("📄 Enter file or folder path to analyze: ").strip()
            user = input("👤 Enter user profile name to compare: ").strip()
            if os.path.isdir(path):
                results = detect.analyze_folder(path, user)
                for r in results:
                    print(f"\n📁 File: {r['file']}")
                    print(f"📊 Score: {r['score']}%")
                    print(f"🔍 Verdict: {r['verdict']}")
                    if "ai_flag" in r:
                        print(f"🤖 AI-Written?: {r['ai_flag']}")
            else:
                result = detect.analyze_message(path, user)
                if isinstance(result, dict):
                    print(f"\n📄 File: {result['file']}")
                    print(f"📊 Score: {result['score']}%")
                    print(f"🔍 Verdict: {result['verdict']}")
                    if "ai_flag" in result:
                        print(f"🤖 AI-Written?: {result['ai_flag']}")
                else:
                    print(result)

        elif choice == "3":
            user = input("👤 Enter user profile for chat: ").strip()
            chatbot.start_chat(user)

        elif choice == "4":
            message = input("✉️ Enter suspicious message text: ").strip()
            result = ai_detector.detect_ai_text(message)
            print("\n🔍 Verdict:", result["verdict"])
            print("🤖 AI Probability:", result["ai_score"], "%")
            print("👤 Human Probability:", result["human_score"], "%")

        elif choice == "5":
            user = input("👤 Profile name: ").strip()
            message_file = input("📄 Suspicious message file path: ").strip()
            score = float(input("📊 Score (0–100): ").strip())
            verdict = input("🔍 Verdict (Genuine or Impersonation): ").strip()
            output = input("🧾 Output PDF file name (default: report.pdf): ").strip() or "report.pdf"
            report.generate_pdf(output_path=output, user=user, score=score, verdict=verdict, message_file=message_file)
            print(f"✅ Report saved as {output}")

        elif choice == "6":
            print("👋 Exiting PersonaFence X. Stay safe.")
            break

        else:
            print("❌ Invalid choice. Please try again.")

        input("\n🔁 Press Enter to return to menu...")

if __name__ == "__main__":
    main()
