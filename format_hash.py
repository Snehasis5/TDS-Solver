import subprocess
import hashlib

# Hardcoded file path
file_path = r"C:\Users\sneha\Downloads\README (4).md"

def format_and_hash_readme(file_path):
    """Formats the given file using Prettier and computes its SHA-256 hash."""
    try:
        # Run Prettier and capture output
        result = subprocess.run(
            ["npx", "-y", "prettier@3.4.2", file_path],
            capture_output=True,
            text=True,
            check=True
        )

        # Compute SHA-256 hash of formatted content
        sha256_hash = hashlib.sha256(result.stdout.encode()).hexdigest()
        print(f"{sha256_hash}  -")

    except subprocess.CalledProcessError as e:
        print("Error running Prettier:", e)
        exit(1)

# Run the function with the hardcoded file path
format_and_hash_readme(file_path)
