import re

def clean_text(text):
    """
    Cleans raw scraped webpage text by removing HTML tags, URLs, 
    special characters, and excessive whitespace.
    """
    text = re.sub(r'<[^>]*?>', '', text)
    
    text = re.sub(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|'
        r'(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
        '', 
        text
    )
    text = re.sub(r'[^a-zA-Z0-9.,!? ]', '', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = text.strip()
    return text
