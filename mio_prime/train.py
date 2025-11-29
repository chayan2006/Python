import os
import sys

# Adjust path if running directly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from mio_prime import config, learning

def train_from_logs():
    log_file = os.path.join(config.LOG_DIR, "activity.log")
    if not os.path.exists(log_file):
        print("No activity log found.")
        return

    kb = learning.KnowledgeBase()
    
    print("--- MIO PRIME TRAINING MODE ---")
    print("Scanning logs for unknown commands...")
    
    unknown_commands = set()
    
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            # Look for the specific marker we will add to core.py
            if "[SKILL] [MISSING]" in line:
                # Extract the command (assuming format: ... [MISSING] command)
                parts = line.split("[MISSING]")
                if len(parts) > 1:
                    cmd = parts[1].strip()
                    # Check if we already know it (maybe trained recently)
                    if not kb.get_response(cmd):
                        unknown_commands.add(cmd)

    if not unknown_commands:
        print("No new unknown commands found.")
        return

    print(f"Found {len(unknown_commands)} unknown commands.")
    
    for cmd in unknown_commands:
        print(f"\nCommand: '{cmd}'")
        action = input("What should I say? (Press Enter to skip): ").strip()
        if action:
            kb.learn(cmd, action)
            print("Learned.")
        else:
            print("Skipped.")

    print("\nTraining session complete.")

if __name__ == "__main__":
    train_from_logs()
