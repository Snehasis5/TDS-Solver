import pdfplumber
import subprocess
import os
import markdownify

def pdf_to_markdown(file):
    try:
        # Read content from the uploaded PDF file
        pdf_content = file.file.read()

        # Save to a temporary file
        with open("temp_pdf.pdf", "wb") as temp_pdf:
            temp_pdf.write(pdf_content)

        # Extract text from PDF
        with pdfplumber.open("temp_pdf.pdf") as pdf:
            text = "\n\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

        if not text.strip():
            raise ValueError("No text extracted from the PDF.")

        # Convert to Markdown
        md_content = markdownify.markdownify(text, heading_style="ATX")

        # Save raw Markdown to a temporary file
        temp_md_path = "temp_output.md"
        with open(temp_md_path, "w", encoding="utf-8") as md_file:
            md_file.write(md_content)

        # Log the command for debugging
        print("Running Prettier command...")
        print(f"Command: npx prettier --write {temp_md_path}")

        # Ensure Prettier is available and format with Prettier
        result = subprocess.run(["npx", "prettier", "--write", temp_md_path], check=True, capture_output=True)
        print(f"Prettier output: {result.stdout.decode()}")
        print(f"Prettier errors: {result.stderr.decode()}")

        # Read and return the formatted Markdown content
        with open(temp_md_path, "r", encoding="utf-8") as md_file:
            formatted_md_content = md_file.read()

        # Clean up temporary files
        os.remove("temp_pdf.pdf")
        os.remove(temp_md_path)

        return formatted_md_content

    except Exception as e:
        return f"An error occurred: {e}"

# Example usage (FastAPI route handler example):
# Assuming `file` is a FastAPI `UploadFile` object
# result = pdf_to_markdown(file)
