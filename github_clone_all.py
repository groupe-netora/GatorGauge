# github-clone-all.py
# Dan Wallach <dwallach@rice.edu>

import requests
import sys
import os
import subprocess
import time

# TODO: make keywords a list of keywords to search for in the name of the
# github repositories


def get_repositories(githubProject, keywords, githubToken, outDir):
    #
    # local goodies (for my cron job)
    #
    from datetime import datetime
    from pytz import timezone

    print("")
    print(">>>>>>>>>>>>>>")
    print(
        ">>>>>>>>>>>>>> Running github-clone-all: " +
        datetime.now(
            timezone("US/Eastern")).strftime('%Y-%m-%d %H:%M:%S %Z%z'))
    print(">>>>>>>>>>>>>>")
    print("")

    requestHeaders = {
        "User-Agent": "GitHubCloneAll/1.0",
        "Authorization": "token " + githubToken,
    }

    allReposList = []

    pageNumber = 1
    sys.stdout.write('Getting repo list from Github')

    while True:
        sys.stdout.write('.')
        sys.stdout.flush()
        reposPage = requests.get(
            'https://api.github.com/orgs/' +
            githubProject +
            '/repos?page=' +
            str(pageNumber),
            headers=requestHeaders)
        pageNumber = pageNumber + 1

        if reposPage.status_code != 200:
            print("Failed to load repos from GitHub: " + str(reposPage.content))
            return

        reposPageJson = reposPage.json()

        if len(reposPageJson) == 0:
            print(" Done.")
            break

        allReposList = allReposList + reposPage.json()

    # Each repo in the list has the following fields that we care about:
    #
    # clone_url: starts with https, suitable for checking out from the command-line
    #     (e.g., 'https://github.com/RiceComp215/comp215-week01-intro-2017-dwallach.git')
    #
    # ssh_url: starts with git@github.com (e.g., 'git@github.com:RiceComp215/comp215-week01-intro-2017-dwallach.git')
    #
    # name: the name of the repo itself (e.g., 'comp215-week01-intro-2017-dwallach')
    #
    # full_name: the project and repo (e.g.,
    # 'RiceComp215/comp215-week01-intro-2017-dwallach')

    filteredRepoList = [
        x for x in allReposList if all(key in x['name'] for key in keywords)] # attempt to check for all keywords in name
    print(str(len(filteredRepoList)) +
          " of " +
          str(len(allReposList)) +
          " repos start with " +
          str(keywords))
    time.sleep(2)
    # before we start getting any repos, we need a directory to get them
    if outDir != ".":
        try:
            os.makedirs(outDir)
        except OSError:
            # directory probably already exists
            print(
                "Directory '" +
                str(outDir) +
                "' already exists, please wait while directory is deleted\n")
            # deletes outDir folder if it already exists
            command = 'rm -r -f ./' + str(outDir)
            os.system(command)
            os.makedirs(outDir)
        os.chdir(outDir)

    # specific clone instructions here:
    # https://github.com/blog/1270-easier-builds-and-deployments-using-git-over-https-and-oauth
    repoNum = 1
    for repo in filteredRepoList:
        cloneUrl = 'https://' + \
            str(githubToken) + '@github.com/' + str(repo['full_name']) + '.git'

        # Steps to take, per docs above:
        #
        # mkdir foo
        # cd foo
        # git init
        # git pull https://<token>@github.com/username/bar.git

        # if repositories are not placed in seperate folder
        # each one must be deleted before it can be redownloaded
        if os.path.isdir(repo['name']):
            command = 'rm -r -f ' + repo['name']
            os.system(command)
        os.mkdir(repo['name'])
        os.chdir(repo['name'])
        subprocess.call(["git", "init"])
        print(">>>>>>>>>>>>>>")
        print(">>>>>>>>>>>>>> Downloading repository number " +
              str(repoNum) + " of " + str(len(filteredRepoList)) + " repositories")
        print(">>>>>>>>>>>>>>")
        subprocess.call(["git", "pull", cloneUrl])
        os.chdir('..')
        repoNum += 1

    #
    # leftover from an earlier emergency: if you want to make a repo be private, here's the code to do it
    #
    #         response = requests.patch('https://api.github.com/repos' + githubProject + '/' + name,
    #                                   headers = requestHeaders, json={ "private": True })
    #
