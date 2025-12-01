import sys
import os

# Add the parent directory to sys.path to allow importing mio_prime modules
# This is needed because we are running main.py from inside the package directory usually,
# or if we run it from outside, we need to make sure imports work.
# However, the cleanest way is to treat 'mio_prime' as a package.
# For this simple script, we'll just ensure we can import local modules.

# Adjust path if running directly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from mio_prime.core import MioAgent

def main():
    agent = MioAgent()
    try:
        agent.start_session()
        
        while True:
            command = input(f"{agent.auth.owner_name} >> ")
            status = agent.process_command(command)
            if status == "HALT":
                break
                
    except KeyboardInterrupt:
        print("\nForce shutdown initiated.")
    except Exception as e:
        print(f"Critical Error: {e}")

if __name__ == "__main__":
    main()
