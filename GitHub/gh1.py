from github import Github
import os

token = input("Please provide the valid Token: ")
auth  = Github(token)
user  = auth.get_user("pa1kumardevops")

#Listing the Repos
for repos in user.get_repos():
    print (f"Repositories: {repos}")