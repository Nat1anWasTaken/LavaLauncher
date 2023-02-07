from os import getenv, listdir, path, mkdir, environ
from os.path import isdir

import jdk
import subprocess as sp
import sys
import requests
from git import Repo, NoSuchPathError


def main():

    set_environment_variable()
    print("成功!")

    repo = clone_lava()
    print("成功!")

    update_lava(repo)
    print("成功!")

    java = get_java()
    print("成功!")

    get_lavalink()
    print("成功!")

    print("腳本已執行完畢! 正在自動啟動")
    print("正在自動安裝所需的依賴")
    sp.check_call([sys.executable, "-m", "pip", "install", "-r", "./lava/requirements.txt"])
    print("成功!")
    p = sp.Popen(['python','main.py'],cwd="./lava/",shell=True,stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE) #有問題的
    



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

        with open("./lava/__init__.py","w") as f:
            f.write("from .main import *")

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

def set_environment_variable():
    token = input("請輸入你的機器人Token")
    client_id = input("請輸入你的 Spotify Client ID #獲取方式詳見https://developer.spotify.com/ ")
    client_secret = input("請輸入你的 Spotify Client Secret #獲取方式詳見https://developer.spotify.com/" )
    redirect_uri = input("請輸入你的 Spotify Redirect URI #獲取方式詳見https://developer.spotify.com/ ")
    print("正在儲存環境變數...")
    environ["TOKEN"] = token
    environ["SPOTIFY_CLIENT_ID"] = client_id
    environ["SPOTIFY_CLIENT_SECRET"] = client_secret
    environ["SPOTIPY_REDIRECT_URI"] = redirect_uri



if __name__ == "__main__":
    main()
