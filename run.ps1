python -m pip install -r requirements.txt

python setup.py

python -m pip install -r lava/requirements.txt

Start-Process -FilePath powershell -ArgumentList "-NoLogo -NoExit -Command cd lava; python main.py"

Start-Process -FilePath powershell -ArgumentList "-NoLogo -NoExit -Command cd lavalink; ..\java\jdk\bin\java -jar Lavalink.jar"