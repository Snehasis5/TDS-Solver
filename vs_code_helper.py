import subprocess
import sys
import shutil
import os

def install_vs_code():
    # Check if VS Code is installed
    if shutil.which("code") is None:
        print("VS Code is not installed. Installing now...")
        
        if sys.platform.startswith("win"):  # Windows installation
            subprocess.run(["winget", "install", "--id", "Microsoft.VisualStudioCode"], check=True)
        elif sys.platform.startswith("darwin"):  # macOS installation
            subprocess.run(["brew", "install", "--cask", "visual-studio-code"], check=True)
        elif sys.platform.startswith("linux"):  # Linux installation
            subprocess.run(["sudo", "apt", "install", "-y", "code"], check=True)
        else:
            raise Exception("Unsupported operating system.")
    else:
        print("VS Code is already installed.")
    
    # Check if 'code' command works, try using full path if needed
    try:
        result = subprocess.run(["code", "-s"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except FileNotFoundError:
        print("VS Code CLI is not found. Trying with full path...")

        # Windows specific: Locate VS Code manually
        possible_paths = [
            r"C:\Program Files\Microsoft VS Code\bin\code.cmd",
            r"C:\Users\{}\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd".format(os.getenv("USERNAME"))
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                result = subprocess.run([path, "-s"], capture_output=True, text=True, check=True)
                return result.stdout.strip()

        return "VS Code CLI is not available. Try adding it to PATH manually."

if __name__ == "__main__":
    output = install_vs_code()
    print( output)
