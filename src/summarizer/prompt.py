def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
please provide a short summary of this website in markdown. \
If it includes news or announcements, then summarize these too.\n\n"
    user_prompt += website.text
    return user_prompt

from ..scraper.web import Website

ed = Website("https://edwarddonner.com")
print(ed.title)
print(ed.text)
print(user_prompt_for(ed))