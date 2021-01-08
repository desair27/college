from github import Github
import matplotlib.pyplot as plt
import numpy as np


# import json
def access_github_repo():
    github = Github()
    username = github.get_user("esjmb")
    list1 = []
    list2 = []
    for repository in username.get_repos():
        print("repository name = " + repository.name)
        print(repository.get_commits().totalCount)
        list1.append(repository.name + "" + "")
        list2.append(repository.get_commits().totalCount)

    ypos = np.arange(len(list1))
    plt.xticks(ypos, list1)
    plt.ylabel("number of commits")
    plt.title("Commits per repository")
    plt.bar(ypos,list2)
    plt.show()


if __name__ == '__main__':
    access_github_repo()
    #plt.plot([w,x,y,z], [1, 4, 2, 3])  # Matplotlib plot.
    #plt.show()
