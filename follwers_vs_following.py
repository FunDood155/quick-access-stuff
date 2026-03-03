import re

with open("followers.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

usernames = []

for line in lines:
    line = line.strip()
    
    # Instagram username pattern
    if re.fullmatch(r"[a-zA-Z0-9._]{1,30}", line):
        usernames.append(line)

# Remove duplicates (optional)
usernames = list(set(usernames))

# Save cleaned usernames
with open("cleaned_usernames.txt", "w", encoding="utf-8") as f:
    for user in usernames:
        f.write(user + "\n")

print("Total valid usernames:", len(usernames))