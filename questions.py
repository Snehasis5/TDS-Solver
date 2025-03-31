import re
# Function to check if the user is asking about GitHub Pages deployment
def is_github_pages_question(question: str) -> bool:
    return (
        "GitHub Pages" in question
        and "email address" in question
        and "https://" in question
    )

def is_sentiment_analysis(question: str) -> bool:
    # Define key patterns that must be present in the question
    patterns = [
        r"Write a Python program",  # Must request Python code
        r"httpx to send a POST request",  # Must involve `httpx` and a POST request
        r"OpenAI's API",  # Must be using OpenAI's API
        r"analyze the sentiment",  # Must be about sentiment analysis
        r"GOOD, BAD or NEUTRAL",  # Must categorize into these sentiment labels
        r"gpt-4o-mini",  # Must specify model
        r"Authorization header with dummy API key",  # Must mention API key usage
        r"system message asking the LLM",  # Must involve a system message
        r"DataSentinel Inc\.",  # Must mention DataSentinel Inc.
        r"response = httpx\.post\(",  # Must include an HTTP POST request with `httpx`
    ]

    # Check if all patterns exist in the question
    return all(re.search(pattern, question, re.IGNORECASE) for pattern in patterns)

def is_wikipedia_question(question: str) -> bool:
    """
    Checks if the given question is asking for a Wikipedia outline.

    Args:
        question (str): The input question.

    Returns:
        bool: True if the question is about Wikipedia, False otherwise.
    """
    question_lower = question.lower().strip()

    # Define patterns that indicate a Wikipedia outline request
    patterns = [
        r"\bwikipedia\b",  # Matches "wikipedia" as a full word
        r"\bwiki\b",  # Matches "wiki" as a full word
        r"wikipedia outline",  
        r"extract.*headings",  
        r"sections.*wikipedia",  
        r"wikipedia.*page.*headings",  
        r"fetch.*wikipedia.*page",  
        r"markdown.*outline.*wikipedia",
        r"api.*fetch.*wikipedia.*headings"
    ]

    return any(re.search(pattern, question_lower) for pattern in patterns)

def is_chennai_min_latitude_question(question: str) -> bool:
    """
    Checks if the given question is asking for latitude details of Chennai, India,
    using the Nominatim API.

    Args:
        question (str): The input question.

    Returns:
        bool: True if the question is about Chennai's latitude via Nominatim, False otherwise.
    """
    question_lower = question.lower().strip()

    # Define patterns that indicate a Nominatim API latitude request
    patterns = [
        r"\bnominatim\b.*\bapi\b",  # Matches "Nominatim API"
        r"\bbounding\s*box\b",  # Matches "bounding box"
        r"\bminimum\s+(?:latitude|lat)\b",  # Matches "minimum latitude" or "min lat"
        r"\bchennai\b",  # Matches "Chennai"
        r"\bindia\b",  # Matches "India"
        r"\burbanride\b",  # Matches "UrbanRide" (optional but included)
        r"\bextract.*latitude",  # Matches "extract latitude"
        r"\bfetch.*bounding\s*box",  # Matches "fetch bounding box"
        r"\bretrieve.*coordinates",  # Matches "retrieve coordinates"
        r"\bnominatim.*get.*bounding\s*box",  # Matches "Nominatim get bounding box"
        r"\bnominatim.*city.*coordinates",  # Matches "Nominatim city coordinates"
    ]

    return any(re.search(pattern, question_lower) for pattern in patterns)
def is_hn_text_editor_question(question: str) -> bool:
    """
    Checks if the given question is asking for the latest Hacker News post
    mentioning "Text Editor" with at least 56 points via HNRSS API.

    Args:
        question (str): The input question.

    Returns:
        bool: True if the question is about fetching the latest Text Editor post, False otherwise.
    """
    question_lower = question.lower().strip()
    
    # Define patterns that indicate a Hacker News RSS request for Text Editor posts
    patterns = [
        r"\bhnrss\b.*\bapi\b",  # Matches "HNRSS API"
        r"\bhacker\s*news\b",  # Matches "Hacker News"
        r"\btext\s*editor\b",  # Matches "Text Editor"
        r"\bminimum\s+(?:points|score)\b",  # Matches "minimum points" or "minimum score"
        r"\bfetch.*latest\b",  # Matches "fetch latest"
        r"\bextract.*link\b",  # Matches "extract link"
        r"\bretrieve.*hacker\s*news\b",  # Matches "retrieve Hacker News"
        r"\bsearch.*hnrss\b",  # Matches "search HNRSS"
    ]
    
    return any(re.search(pattern, question_lower) for pattern in patterns)
import re

def is_github_melbourne_newest_user_question(question: str) -> bool:
    """
    Checks if the given question is asking for the newest GitHub user from Melbourne
    with over 50 followers, using a liberal regex pattern match.

    Args:
        question (str): The input question.

    Returns:
        bool: True if the question is relevant, False otherwise.
    """
    question_lower = question.lower().strip()

    patterns = [
        r"github.*user",  # Mentions GitHub users
        r"newest.*github.*user",  # Looks for "newest GitHub user"
        r"latest.*github.*user",  # Looks for "latest GitHub user"
        r"melbourne.*github",  # Ensures the location "Melbourne" is mentioned
        r"over\s*50\s*followers",  # Ensures "over 50 followers" is included
        r"created_at",  # Refers to account creation date
        r"when.*created",  # Queries about creation date
        r"github.*profile.*created"  # Ensures it's about account creation
    ]

    return any(re.search(pattern, question_lower) for pattern in patterns)
import re

def is_student_biology_marks_question(question: str) -> bool:
    """
    Checks if the given question is asking for the total Biology marks of students 
    who scored 79 or more in English in groups 1-25.

    Args:
        question (str): The input question.

    Returns:
        bool: True if the question is relevant, False otherwise.
    """
    question_lower = question.lower().strip()

    patterns = [
        r"total.*biology.*marks",  # Ensures the question is about total Biology marks
        r"students.*scored.*79.*english",  # Looks for students scoring 79 or more in English
        r"groups?\s*1-25",  # Ensures the question specifies groups 1-25
        r"including.*both",  # Ensures inclusion of both ends of the range
        r"sum.*biology",  # Ensures it asks for the sum of Biology marks
        r"english.*>=?\s*79",  # Variation checking the score condition
        r"group.*between.*1.*25"  # Ensures filtering within group range
    ]

    return any(re.search(pattern, question_lower) for pattern in patterns)
def is_pdf_to_markdown_conversion_question(question: str) -> bool:
    """
    Checks if the given question is asking about converting PDF files to Markdown and formatting with Prettier.

    Args:
        question (str): The input question.

    Returns:
        bool: True if the question is relevant to PDF to Markdown conversion with Prettier formatting, False otherwise.
    """
    question_lower = question.lower().strip()

    patterns = [
        r"convert.*pdf.*markdown",  # Ensures the question is about converting PDF to Markdown
        r"extract.*content.*pdf",  # Looks for content extraction from PDF
        r"markdown.*format",  # Ensures the question involves formatting the content in Markdown
        r"prettier.*format",  # Ensures the use of Prettier for formatting
        r"prettier.*3\.4\.2",  # Ensures the specific version of Prettier is mentioned
        r"submit.*formatted.*markdown",  # Looks for submission of formatted Markdown
        r"markdown.*quality.*standardized",  # Ensures the question emphasizes quality and standardized formatting
        r"automation.*markdown.*conversion",  # Ensures the question mentions automation in the conversion process
        r"pdf.*markdown.*prettier"  # Looks for the combination of all concepts: PDF, Markdown, and Prettier
    ]

    return any(re.search(pattern, question_lower) for pattern in patterns)

def is_total_margin_question(question: str) -> bool:
    """
    Checks if the given question is asking for the total margin of Iota sales in the US before April 3, 2023.

    Args:
        question (str): The input question.

    Returns:
        bool: True if the question is relevant, False otherwise.
    """
    question_lower = question.lower().strip()

    # More liberal conditions that can be met
    must_have_patterns = [
        r"margin",  # Allows any mention of margin, not strictly "total margin"
        r"iota",  # Allows "Iota" anywhere in the question
        r"(before|up\s+to|until|by)\s*(apr?|\d{1,2})\s*3[\s,\.]*2023",  # More flexible date conditions
    ]
    
    # At least one way of mentioning US must be present
    us_patterns = [
        r"\bus\b", r"\bu\.s\.?\b", r"\busa\b", r"\bunited states\b"
    ]

    # Check if all must-have patterns are met
    if not any(re.search(pattern, question_lower) for pattern in must_have_patterns):
        return False

    # Check if at least one US-related pattern is present
    if not any(re.search(pattern, question_lower) for pattern in us_patterns):
        return False

    return True