#!/bin/bash
python3 -m pip install -r requirements.txt

python3 setup.py

python3 -m pip install -r lava/requirements.txt

(
  cd lava
  python3 main.py
) & (
  cd lavalink
  ../java/jdk/bin/java -jar Lavalink.jar
)
