#Import Module
from github import Github
import os

#Authentication
token = input("Please provide the valid Token: ")
auth  = Github(token)

#Get the details of Authenticated User
user = auth.get_user()
print (f"Username: {user.login}")
print (f"Public Repos: {user.public_repos}")
print (f"Followers: {user.followers}")
# print (f"Repositories: {user.get_repos}")
