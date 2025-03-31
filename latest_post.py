import feedparser

def get_latest_text_editor_post():
    url = "https://hnrss.org/newest?q=Text+Editor&points=56"
    feed = feedparser.parse(url)
    
    if feed.entries:
        latest_post = feed.entries[0]
        return latest_post.link
    else:
        return "No matching post found."