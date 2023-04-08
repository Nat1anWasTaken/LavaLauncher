pip install -r requirements.txt
pip install -r lava/requirements.txt

python setup.py

set /p envfile=<.env

(
  cd lava
  start cmd /k python main.py
) &

(
  cd lavalink
  start cmd /k java -jar Lavalink.jar
)