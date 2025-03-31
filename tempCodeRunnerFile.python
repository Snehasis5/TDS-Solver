import re
def is_vscode_question(question: str) -> bool:
    vscode_keywords = [
        r"\binstall vs code\b",
        r"\bsetup vs code\b",
        r"\bcheck vs code\b",
        r"\bvs code status\b",
        r"\bcode -s\b",
        r"\bVisual Studio Code\b"
    ]
    
    question = question.lower()
    return any(re.search(keyword, question) for keyword in vscode_keywords)
query = "Install and run Visual Studio Code. In your Terminal (or Command Prompt), type code -s and press Enter. Copy and paste the entire output below. What is the output of code -s?"
print(is_vscode_question(query))  # ✅ Expected output: True
