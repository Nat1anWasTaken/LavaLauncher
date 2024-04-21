# LavaLauncher

適用於 Lava 的 One-Click to Run Script

你可以在 [這裡](https://github.com/Nat1anWasTaken/Lava) 找到 Lava 的主要 Repository

## ⚠️ 已棄用 ⚠️

此專案已在 2024/4/22 棄用，
目前 Lava 的主要架設方式已改為使用 **Docker** 或是 **Docker Compose**
請參考主要 Repository 的 [README.md](https://github.com/Nat1anWasTaken/Lava?tab=readme-ov-file#開始使用)

## 需求

- 基本英文 / 中文閱讀能力
- Python 3.10+
- [Git Bash](https://git-scm.com/)

註：這個腳本是設計在 Linux 中運行，在 Windows 中，你可以嘗試使用
[Windows Subsystem for Linux](https://learn.microsoft.com/zh-tw/windows/wsl/install)

## 如何使用

如何使用 LavaLauncher

### 創建 Discord 機器人

如果你已經有了一個 Discord 機器人，你可以跳過這個區段

1. 前往 [Discord Developer Portal](https://discord.com/developers) 並登入你的帳號，接著點擊 New Application

   ![developer-portal.png](img/discord/developer-portal.png)

2. 為你的機器人取名字 (這個名字將會顯示在 Discord 上)

   ![name-your-application.png](img/discord/name-your-application.png)

3. 到左方的 Bots，點擊 Reset Token 獲得 Token

   Token 會看起來像這樣：`MTA5ODYxNDI5NjExMzU3Nzk5NA.Ga7fZq.j9XXSVOWDdXJIlbZpOrkL7fsT4xB42zlHjB7Fg`
   請將這個字串儲存起來，我們稍後會使用到

   ![get-token.png](img/discord/get-token.png)

   > 註：這是私密資訊，請勿將它分享給任何人

4. 往下捲，開啟 Intents

   Lava 需要這些 Intent 才能夠運作，將三個 Intent 開啟後，請記得點擊 Save Changes

   ![enable-intents.png](img/discord/enable-intents.png)

5. 獲得機器人邀請連結

   請勾選 `bot` 和 `applications.commands`

   ![setup-scopes.png](img/discord/setup-scopes.png)

   並捲到下方，點擊 `Copy` 來複製邀請連結

   ![copy-invite-link.png](img/discord/copy-invite-link.png)

### 設置 Spotify

這是為了對 [Spotify](https://open.spotify.com/) 連結的支援，以及自動播放，
如果你不需要這些功能，你可以跳過這個區段

1. 前往 [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)，並登入你的 Spotify 帳號，接著 Create App

   ![create-spotify-app.png](img/spotify/create-spotify-app.png)

2. 填入表單，並點擊 Create App

   `App name`, `App description`, `Website` 可以隨意填寫，但 `Redirect URIs` 請填入 `http://localhost/`

   ![fill-in-forms.png](img/spotify/fill-in-forms.png)

3. 獲得 Client ID 和 Client Secrets

   進入 Settings

   ![get-into-settings.png](img/spotify/get-into-settings.png)

   點擊 View Client Secrets

   ![show-client-secrets.png](img/spotify/view-client-secrets.png)

   複製 Client ID 和 Client Secrets 並儲存，我們稍後會使用到

   ![copy-fields.png](img/spotify/copy-fields.png)

   > 註：這是私密資訊，請勿將它分享給任何人

### 開始設定 Lava

1. 下載 LavaLauncher

   你可以使用 `git clone` 或是直接下載 ZIP 檔

   ```bash
   git clone https://github.com/Nat1anWasTaken/LavaLauncher.git
   ```

2. 運行腳本
3. 
   ```bash
   python run.py
   ```

   > 如果你遇到了 Permission Error，請打開命令提示字元後輸入 `powershell Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

4. 輸入資料

   LavaLauncher 的第一次啟動可能需要一點時間，請耐心等待
   在啟動完成後，你會看到幾個彈出來的問題

   `[?] TOKEN:`
   請輸入你在上方 [創建機器人](#創建 Discord 機器人) 獲得的 TOKEN

   `[?] Do you want to enable Spotify support?`
   請輸入 `y` 或 `n` 來決定是否啟用 Spotify 支援

   `[?] SPOTIFY_CLIENT_ID:`, `[?] SPOTIFY_CLIENT_SECRET:`
   請輸入你在上方 [設置 Spotify](#設置 Spotify) 獲得的 Client ID 和 Client Secrets

   `[?] SPOTIFY_REDIRECT_URI:`
   請輸入 `http://localhost/`

   接著，LavaLauncher 會跳出一個連結，請點擊它並授權
   授權完成後，顯示 `http://localhost/ 拒絕連線` 是正常的，此時你應該將瀏覽器分頁的連結複製下來，並貼到 LavaLauncher 的輸入框中

5. 運行機器人

   LavaLauncher 會自動安裝所需的套件，並啟動機器人
   如果你看到 `Logged in as` 這行字，恭喜你，你已經成功啟動了 Lava

## 支援

需要協助？你可以前往 [A.C.G.M CITY](https://discord.gg/acgmcity) 詢問有關 Lava 的問題，
或是直接 [開啟一個 Issue](https://github.com/Nat1anWasTaken/LavaLauncher/issues)
