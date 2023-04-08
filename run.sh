#!/bin/bash
pip install -r requirements.txt
pip install -r lava/requirements.txt

python3 setup.py

source .env

(
  cd lava
  python3 main.py
) & (
  cd lavalink
  ../java/jdk/bin/java -jar Lavalink.jar
)
