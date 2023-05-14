@echo off

call "%~dp0.venv\Scripts\activate.bat"

python "%~dp0main.py" input/angry:output/angry input/disgust:output/disgust input/fear:output/fear input/happy:output/happy input/neutral:output/neutral input/sad:output/sad input/surprise:output/surprise

pause
deactivate
