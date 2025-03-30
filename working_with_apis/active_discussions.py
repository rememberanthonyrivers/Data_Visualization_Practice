import requests
import matplotlib.pyplot as plt

from operator import itemgetter

# Make the API call and store the response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("\nStatus Code:", r.status_code)

# Process the info for each submission
submission_ids = r.json()
submission_dicts = []

# Pick the top 30 stories
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    submission_r = requests.get(url)
    response_dict = submission_r.json()

    # Ensure 'title' exists in the response
    if 'title' in response_dict:
        # create a dictionay storing
        submission_dict = {
            'title': response_dict['title'],
            'link': f'http://news.ycombinator.com/item?id={submission_id}',
            'comments': response_dict.get('descendants', 0)
        }
        submission_dicts.append(submission_dict)

# Sort submissions by comment count
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Extract data for visualization
titles = [submission['title'] for submission in submission_dicts]
comment_counts = [submission['comments'] for submission in submission_dicts]
links = [submission['link'] for submission in submission_dicts]

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(titles, comment_counts, color='skyblue')
plt.xlabel("Number of Comments")
plt.ylabel("Discussion Titles")
plt.title("Most Active Discussions on Hacker News")

# Reverse the order so the most commented story is at the top
plt.gca().invert_yaxis()

# Add interactive links
for bar, link in zip(bars, links):
    bar.set_label(link)  # This does not make the bars clickable in matplotlib but helps with annotations

# Show the plot
plt.tight_layout()
plt.show()
