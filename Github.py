from github import Github

def access_github_repo():
    github = Github()
    username = github.get_user("seyekt")
    for repository in username.get_repos():
        print("repository name = " + repository.name)




if __name__ == '__main__':
    access_github_repo()
