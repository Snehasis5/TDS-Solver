import os
import subprocess

def deploy_github_pages():
    # Configuration
    GITHUB_USERNAME = "Snehasis5"  # Replace with your GitHub username
    REPO_NAME = "portfolio"  # Change as needed
    EMAIL = "24f1000142@ds.study.iitm.ac.in"
    GITHUB_PAGES_URL = f"https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/"

    # Create and move into the project directory
    os.makedirs(REPO_NAME, exist_ok=True)
    os.chdir(REPO_NAME)

    # Create index.html with obfuscated email
    html_content = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Portfolio</title>
    </head>
    <body>
        <h1>Welcome to My Portfolio</h1>
        <p>Contact me: <!--email_off-->{EMAIL}<!--/email_off--></p>
    </body>
    </html>
    """

    with open("index.html", "w") as f:
        f.write(html_content)

    # Initialize Git and create a new repository
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

    # Create GitHub repository (if not already created)
    try:
        subprocess.run(["gh", "repo", "create", REPO_NAME, "--public", "--source=.", "--remote=origin"], check=True)
    except subprocess.CalledProcessError:
        pass  # Repository might already exist, ignore error

    # Add remote origin manually if not set
    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"], check=True)

    # Push code
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

    # Enable GitHub Pages
    try:
        subprocess.run([
            "gh", "api", "-X", "PUT", 
            f"/repos/{GITHUB_USERNAME}/{REPO_NAME}/pages",
            "-f", "source[branch]=main", "-f", "source[path]=/"
        ], check=True)
    except subprocess.CalledProcessError:
        pass  # Ignore error if API request fails

    return GITHUB_PAGES_URL  # Return the GitHub Pages URL

# Call function and return URL
deploy_github_pages()
