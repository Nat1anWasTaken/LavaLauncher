#!/bin/bash
pip install -r requirements.txt

python3 setup.py

pip install -r lava/requirements.txt

source .env

(
  cd lava
  python3 main.py
) & (
  cd lavalink
  ../java/jdk/bin/java -jar Lavalink.jar
)
