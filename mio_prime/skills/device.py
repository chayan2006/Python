import os
import subprocess
import platform

import webbrowser

class DeviceSkills:
    def __init__(self):
        self.os_type = platform.system()
        self.web_apps = {
            "linkedin": "https://www.linkedin.com",
            "linkdin": "https://www.linkedin.com", # Alias
            "youtube": "https://www.youtube.com",
            "you": "https://www.youtube.com", # Alias
            "tube": "https://www.youtube.com", # Alias
            "google": "https://www.google.com",
            "github": "https://github.com",
            "gmail": "https://mail.google.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "twitter": "https://twitter.com",
            "x": "https://twitter.com",
            "reddit": "https://www.reddit.com",
            "chatgpt": "https://chat.openai.com",
            "whatsapp": "https://web.whatsapp.com"
        }

    def open_app(self, app_name):
        """
        Attempts to open an application or website.
        """
        app_lower = app_name.lower().strip()
        
        # 1. Check Web Apps
        if app_lower in self.web_apps:
            url = self.web_apps[app_lower]
            try:
                # On Windows, os.startfile is more reliable for default browser
                if self.os_type == "Windows":
                    os.startfile(url)
                else:
                    webbrowser.open(url)
                return True
            except Exception as e:
                print(f"Error opening web app: {e}")
                return False

        # 2. Try Native App
        try:
            if self.os_type == "Windows":
                subprocess.Popen(f"start {app_name}", shell=True)
                return True
            elif self.os_type == "Darwin": # macOS
                subprocess.Popen(["open", "-a", app_name])
                return True
            elif self.os_type == "Linux":
                # Check if we are on Android (via simple environment check or platform)
                if "ANDROID_ARGUMENT" in os.environ:
                    print("App launching not yet supported on Android directly.")
                    return False
                subprocess.Popen([app_name])
                return True
        except Exception as e:
            print(f"Error opening app: {e}")
            return False
        return False
