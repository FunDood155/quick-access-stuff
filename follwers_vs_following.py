import re
x=["followers.txt","following.txt"]
y=["clean_followers.txt","clean_following.txt"]
def makeitperfect(i):
    
    with open(x[i], "r", encoding="utf-8") as f:
        lines = f.readlines()

    usernames = []

    for line in lines:
        line = line.strip()
        
        # Instagram username pattern
        if re.fullmatch(r"[a-z0-9._]{1,30}", line):
            usernames.append(line)

    # Remove duplicates (optional)
    usernames = list(set(usernames))

    # Save cleaned usernames
    with open(y[i], "w", encoding="utf-8") as f:
        for user in usernames:
            f.write(user + "\n")

    print("Total valid usernames of :",y[i], len(usernames))
    return(usernames)
    #print(usernames)
f1=makeitperfect(0)
f2=makeitperfect(1)
z=[]
for i in f2:
    if i not in f1:
        z.append(i)
print("to unfollow...")
for i in z:
    print(i)