@echo off
python -m pip install -r requirements.txt

python setup.py

python -m pip install -r lava/requirements.txt

start /b cmd /c "( cd lava && python main.py )"

start /b cmd /c "( cd lavalink && ..\java\jdk\bin\java -jar Lavalink.jar )"