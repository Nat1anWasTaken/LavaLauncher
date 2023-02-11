import shutil
from os import getenv, listdir, path, mkdir, rename
from os.path import isdir

import jdk
import requests
from git import Repo, NoSuchPathError


def main():
    repo = clone_lava()

    update_lava(repo)

    setup_lava()

    get_java()

    get_lavalink()


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

    print("Lava cloned successfully!")

    return repo


def update_lava(repo: Repo):
    print("Updating Lava...")

    remote = repo.remote("origin")

    remote.pull()

    print("Lava updated successfully!")


def setup_lava():
    print("Setting up Lava...")

    shutil.copyfile("default_configs/lavalink.json", "lava/configs/lavalink.json")

    shutil.copyfile("default_configs/icons.json", "lava/configs/icons.json")

    print("Lava setup successfully!")


def get_java():
    print("Installing JDK...")

    if not isdir("./java"):
        try:
            jdk.install("17", path="./java", jre=True)
        except StopIteration:
            pass

    for directory in listdir('./java'):
        if directory.startswith('jdk'):
            rename(f"./java/{directory}", f"./java/jdk")
            break

    print("JDK installed successfully!")


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

    shutil.copyfile("default_configs/application.yml", "lavalink/application.yml")

    print("Lavalink installed successfully!")


if __name__ == "__main__":
    main()
