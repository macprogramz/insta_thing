#Lists the posts, likes and followers of an instagram account

#Ideas to make better:
# See which users like which posts, and display a list of what % of posts they like, ranked
# need to have a map? of usernames and likes
# Add some error handling for no username, private account, errors etc.

# Setup
# Use instaloader module - https://instaloader.github.io/as-module.html
import instaloader

# Initialise
version = "2.5"
testing = True

print("Macs Insta Thing")
print("----------------")
print("Version : ", version)

# Prompts

if testing == True:
    instagramUsername = "nelsonhockey93"
    #instagramUsername = "maclarensmith_hockey12"
    #instagramUsername = "boston___smith"

else:
    username = input("Please enter your Instagram Username: ")
    password = input("Please enter your Instagram Password: ")
    instagramUsername = input("Please enter the Instragram Username: ")

# Connect to Instagram

instagram = instaloader.Instaloader()

# Get Profile
profile = instaloader.Profile.from_username(instagram.context, instagramUsername)

## Improvement - Add error handling here if username, password or account error
print("Got Instagram Profile: ", profile.full_name)
print("Account has ", profile.followers, " followers.")
print("Account has ", profile.mediacount, "posts." )
if profile.is_private == True:
    print("Account is private")
else:
    ## Improvement - Try loging in for private accounts?
    print("Account is public")
print("")

#Some functions to make things easier
def printPostDetails(post):
    #Prints the details of the post
    if testing == True:
        print("In printPostDetails()")
    print("Got Instagram Post: ", post.caption[:20])
    print("Post date: ", post.date_local)
    print("Post has ", post.likes, " likes")
    print("Post has ", post.comments, "comments")
    print("")

def printFollowerDetails(like):
    #Prints the list of follower usernames
    if testing == True:
        print("In printFollowerDetails()")
    print("")
    for thislike in like:
        print("Liked by user: ", thislike.username)

def printCommentDetails(comment):
    #Prints a list of commenter usernames
    if testing == True:
        print("In printCommentDetails()")
    print("")
    for thiscomment in comment:
        print ("Comment by user: ", thiscomment.owner.username)

#Go over each post
for thispost in profile.get_posts():
    printPostDetails(thispost)
    #Only print follower likes if there are likes
    if thispost.likes != 0:
        printFollowerDetails(thispost.get_likes())
    #Only print follower comments if there are comments
    if thispost.comments != 0:
        printCommentDetails(thispost.get_comments())

#End
print ("Finished")






