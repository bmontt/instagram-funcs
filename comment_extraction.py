import instaloader
import re
from collections import Counter
from tqdm import tqdm

# Initialize Instaloader
L = instaloader.Instaloader()

# Login
USER = ...
PASSWORD = ...
L.login(USER, PASSWORD)

# Load a post
POST_URL = 'https://www.instagram.com/p/ENTER POST KEY HERE/'
post = instaloader.Post.from_shortcode(L.context, POST_URL.split('/')[-2])

# Extract comments
comments = [comment.text for comment in tqdm(post.get_comments(), desc="Extracting comments", unit=" comments")]

# Function to extract tagged usernames from a comment
def extract_usernames(comment):
    return set(re.findall(r'@([A-Za-z0-9_.]+)', comment))

# Collect all tagged usernames with a progress bar
all_usernames = []
for comment in tqdm(comments, desc="Processing comments", unit=" comments"):
    all_usernames.extend(extract_usernames(comment))

# Count the occurrences of each username
username_counts = Counter(all_usernames)

# Get the top 3 most tagged usernames
top_usernames = username_counts.most_common(5)

# Print the results
for username, count in top_usernames:
    print(f'{username}: {count} times')