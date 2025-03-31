from fastapi import FastAPI, File, UploadFile, Form
import requests
import pandas as pd
import zipfile
import io
import os
import subprocess
import platform
import shutil
from vs_code_helper import install_vs_code
import re
import subprocess
import sys
import shutil
import os
from uv_request import send_request_and_get_json, extract_url_and_params
from Readme_generator import generate_markdown
from questions import is_github_pages_question, is_sentiment_analysis, is_wikipedia_question, is_chennai_min_latitude_question, is_hn_text_editor_question, is_github_melbourne_newest_user_question
from questions import is_student_biology_marks_question, is_pdf_to_markdown_conversion_question, is_total_margin_question
#from github_username import deploy_github_pages
from token_test import is_tokenization_test
from min_lat import get_min_latitude
from latest_post import get_latest_text_editor_post
from melbourne_user import get_newest_melbourne_user
from pdf_scrapper import extract_biology_marks
from pdf_to_markdown import pdf_to_markdown
from total_margin import calculate_total_margin

# Initialize FastAPI
app = FastAPI()

# AI Proxy Token (Replace with your actual token)
API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjI0ZjEwMDAxNDJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.sSlOzQLb470znA-0nX4aTe8e8chsa-YeGCsEIXHZvUA"
API_URL = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"

HEADERS = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json',
}

# Predefined answers database
ANSWER_DB = {
    "What is 2+2?": "4",
    "Who is the founder of IIT Madras?": "Government of India with German collaboration",
}


# Function to check if the user is asking about VS Code

def is_http_request_question(question: str) -> bool:
    http_keywords = ["uv run", "httpie", "https request", "httpbin"]
    return any(keyword in question.lower() for keyword in http_keywords)
def extract_url_and_params(question):
    # Extract URL
    url_match = re.search(r"https://[^\s]+", question)
    url = url_match.group(0) if url_match else None

    # Extract parameters
    param_match = re.search(r"email set to (\S+)", question)
    email = param_match.group(1) if param_match else None

    return url, {"email": email} if email else {}

def send_request_and_get_json(question):
    url, params = extract_url_and_params(question)
    if not url:
        return {"error": "URL not found in question"}

    response = requests.get(url, params=params)
    return response.json()
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
# Function to get LLM response
def get_llm_answer(question: str, context: str = "") -> str:
    try:
        messages = [
            {"role": "system", "content": "You are an AI assistant. Answer coding and data processing questions."}
        ]

        if context:
            messages.append({"role": "user", "content": f"Here is some data:\n{context}"})

        messages.append({"role": "user", "content": question})

        payload = {"model": "gpt-4o-mini", "messages": messages}
        response = requests.post(API_URL, json=payload, headers=HEADERS)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Error: {response.status_code}, {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"

from fastapi import FastAPI, File, UploadFile, Form, Depends
from typing import Optional

app = FastAPI()

@app.post("/api/")
async def get_answer(
    question: str = Form(...), 
    file: Optional[UploadFile] = File(None)  # Ensure `File(None)` is used
):
    #if file:
        # Handle file processing here
        #contents = await file.read()
        #return {"question": question, "file_size": len(contents)}

    
    if is_vscode_question(question):
        return {"vscode_status": install_vs_code()}  # Use VS Code helper function
    if is_http_request_question(question):
        json_output = send_request_and_get_json(question)
        return {"answer": json_output}
    if "Write documentation in Markdown" in question:
        return {"markdown": generate_markdown()}
    #if is_github_pages_question(question):
        #github_pages_url = deploy_github_pages()  # Call function from github_username.py
        #return {"github_pages_url": github_pages_url}
    if is_sentiment_analysis(question):
        return {
            "code": """import httpx

# OpenAI API endpoint
url = "https://api.openai.com/v1/chat/completions"

# Dummy API key (replace with a real key in production)
api_key = "sk-dummyapikey1234567890"

# Headers including Authorization
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# The request payload
payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": "Analyze the sentiment of the given text. The sentiment must be categorized as GOOD, BAD, or NEUTRAL."},
        {"role": "user", "content": "DevTools listening on ws://127.0.0.1:51150/devtools/browser/3d99b4b4-4f52-45a3-b6e3-7e9eff0156f5\n[3104:24400:0330/225411.666:ERROR:command_buffer_proxy_impl.cc(325)] GPU state invalid after WaitForGetOffsetInRange.\nTraceback (most recent call last):\n  File 'c:\\Users\\sneha\\OneDrive\\Documents\\Desktop\\TDS solver\\colab.py', line 22, in <module>\n    new_notebook_button.click()\n  File 'C:\\Users\\sneha\\OneDrive\\Documents\\Desktop\\TDS solver\\venv\\Lib\\site-packages\\selenium\\webdriver\\remote\\webelement.py', line 119, in click\n    self._execute(Command.CLICK_ELEMENT)\n  File 'C:\\Users\\sneha\\OneDrive\\Documents\\Desktop\\TDS solver\\venv\\Lib\\site-packages\\selenium\\webdriver\\remote\\webelement.py', line 572, in _execute\n    return self._parent.execute(command, params)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File 'C:\\Users\\sneha\\OneDrive\\Documents\\Desktop\\TDS solver\\venv\\Lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py', line 429, in execute\n    self.error_handler.check_response(response)\n  File 'C:\\Users\\sneha\\OneDrive\\Documents\\Desktop\\TDS solver\\venv\\Lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py', line 232, in check_response\n    raise exception_class(message, screen, stacktrace)\nselenium.common.exceptions.ElementNotInteractableException: Message: element not interactable"}
    ],
    "temperature": 0
}

# Send the request
response = httpx.post(url, json=payload, headers=headers)
response.raise_for_status()

# Parse response
result = response.json()
print(result)"""
        }
    if is_tokenization_test(question):
        return {"ans": "33"}

    if question in ANSWER_DB:
        return {"answer": ANSWER_DB[question]}
    if is_wikipedia_question(question):
        return {"link": "http://127.0.0.1:8001/api/outline"}
    if is_chennai_min_latitude_question(question):
        
        min_lat=get_min_latitude("Chennai","India")
        return {"min_lat":min_lat}
    if is_hn_text_editor_question(question):
       
        return {get_latest_text_editor_post()}
    if is_github_melbourne_newest_user_question(question):
         #print("Question matched")
         return {get_newest_melbourne_user()}
    if is_student_biology_marks_question(question):
        #print("question matched")
        marks=extract_biology_marks(file)
        return int(marks)
    if is_pdf_to_markdown_conversion_question(question):
        #print("question matched")
        return {pdf_to_markdown(file)}
    if is_total_margin_question(question):
        print("question matched")
        return int(calculate_total_margin(file))
    llm_answer = get_llm_answer(question)
    return {"answer": llm_answer}