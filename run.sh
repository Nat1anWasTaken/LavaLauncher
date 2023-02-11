pip install -r lava/requirements.txt

set TOKEN=your_token_here
set SPOTIFY_CLIENT_ID=your_client_id_here
set SPOTIFY_CLIENT_SECRET=your_client_secret_here
set SPOTIFY_REDIRECT_URI=your_redirect_uri_here

(
  cd lava
  python3 main.py
) &
(
  cd lavalink
  ../java/jdk/bin/java.exe -jar Lavalink.jar
)
