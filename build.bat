@echo off
for /f %%i in ('python -c "import site; print(site.getsitepackages()[0])"') do set PYTHON_ROOT="%%i"
pyinstaller ^
 --clean ^
 --exclude-module tkinter ^
 --add-data %PYTHON_ROOT%\Lib\site-packages\pymunk\chipmunk.dll;. ^
 --add-data %PYTHON_ROOT%\src\arcade\arcade\soloud\soloud_*.dll;arcade\soloud ^
 --add-data %PYTHON_ROOT%\src\arcade\arcade\resources;arcade\resources ^
 --add-data "./data;data" ^
 -n cast_away_robot ^
 -c ^
 -d all ^
 run_game.py

pause