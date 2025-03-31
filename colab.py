from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Open Google Colab
    driver.get("https://colab.research.google.com/")

    # Wait for the "File" menu
    wait = WebDriverWait(driver, 15)
    file_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='File']")))
    file_menu.click()
    print("File menu clicked.")

    # Step 2: Click "New notebook in Drive"
    new_notebook = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'New notebook in Drive')]")))
    new_notebook.click()
    print("New notebook in Drive clicked.")

    # Step 3: Wait for notebook interface to load
    time.sleep(10)  # Ensure full load

    # Step 4: Select the first code cell
    first_cell = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "CodeMirror")))
    first_cell.click()

    # Step 5: Enter Python script
    colab_code = """import hashlib
import requests
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
creds = GoogleCredentials.get_application_default()
token = creds.get_access_token().access_token
response = requests.get(
  "https://www.googleapis.com/oauth2/v1/userinfo",
  params={"alt": "json"},
  headers={"Authorization": f"Bearer {token}"}
)
email = response.json()["email"]
print(hashlib.sha256(f"{email} {creds.token_expiry.year}".encode()).hexdigest()[-5:])"""

    first_cell.send_keys(colab_code)

    # Step 6: Run the cell (Shift + Enter)
    first_cell.send_keys(Keys.SHIFT, Keys.ENTER)

    # Step 7: Wait for execution to complete
    time.sleep(15)

    # Step 8: Extract the output
    output_elements = driver.find_elements(By.CLASS_NAME, "output")

    if output_elements:
        result = output_elements[-1].text
        print("Result:", result)
    else:
        print("No output found.")

finally:
    # Close the browser
    driver.quit()
