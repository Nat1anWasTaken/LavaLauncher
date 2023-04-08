#!/bin/bash
python3 -m pip install -r requirements.txt

python3 setup.py

python3 -m pip install -r lava/requirements.txt

(
  export TOKEN=$(sed -n 's/^DTOKEN=//p' .env)
  export SPOTIFY_CLIENT_ID=$(sed -n 's/^SPOTIFY_CLIENT_ID=//p' .env)
  export SPOTIFY_CLIENT_SECRET=$(sed -n 's/^SPOTIFY_CLIENT_SECRET=//p' .env)

  cd lava
  python3 main.py
) & (
  cd lavalink
  ../java/jdk/bin/java -jar Lavalink.jar
)
