# -------------------------------
# GitHub Repository Creation Tool
# -------------------------------

# 📦 Importing Required Modules
import os
from github import Github

# 📝 Get the Repository Name from User
Repo_Name = input("Please provide the name for the new GitHub repository: ")

# 🔐 Get the GitHub Personal Access Token from User
token = input("Please provide your GitHub Personal Access Token: ")

# ✅ Authenticate the User with GitHub API
auth = Github(token)
user = auth.get_user()

# 🛠️ Create the Repository with the Given Name
repo = user.create_repo(Repo_Name)

# ✅ Confirm Successful Creation
print(f"✅ The repository '{Repo_Name}' has been successfully created on GitHub.")



























# #GitHub Repo Creation

# #Modules Import
# import os
# from github import Github

# #Defining the Repo Name
# Repo_Name = input("Please provide the Repo Name: ")

# #Authentication for Github
# token = input("Please provide the Token: ")

# #User Authenticate
# auth = Github(token)
# user = auth.get_user()

# #Repo Creation

# repo = user.create_repo(Repo_Name)
# print (f"The Repository {Repo_Name} is successfully created")

