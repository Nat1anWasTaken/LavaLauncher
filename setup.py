from os import getenv, listdir, path, mkdir
from os.path import isdir

import jdk
import requests
from git import Repo, NoSuchPathError


def main():
    repo = clone_lava()

    update_lava(repo)

    java = get_java()

    get_lavalink()

    pass


def clone_lava() -> Repo:
    """
    Clones lava from the git repo
    :return: The repo
    """
    try:
        repo = Repo("./Lava")

    except NoSuchPathError:
        print("Cloning Lava...")

        repo = Repo.clone_from(
            getenv("git_repo", "https://github.com/Nat1anWasTaken/Lava.git"), "./lava", branch="master"
        )

    return repo


def update_lava(repo: Repo):
    print("Updating Lava...")

    remote = repo.remote("origin")

    remote.pull()


def get_java() -> str:
    print("Installing JDK...")

    if not isdir("./java"):
        try:
            jdk.install("17", path="./java", jre=True)
        except StopIteration:
            pass

    for directory in listdir('./java'):
        if directory.startswith('jdk'):
            return f"./java/{directory}/bin/java.exe"


def get_lavalink():
    print("Installing Lavalink...")

    if path.isfile("./lavalink/Lavalink.jar"):
        return

    if not path.isdir('./lavalink'):
        mkdir('./lavalink')

    data = requests.get("https://api.github.com/repos/freyacodes/Lavalink/releases/latest").json()

    jar = requests.get(data["assets"][0]["browser_download_url"])

    with open("./lavalink/Lavalink.jar", 'wb') as f:
        f.write(jar.content)


if __name__ == "__main__":
    main()
