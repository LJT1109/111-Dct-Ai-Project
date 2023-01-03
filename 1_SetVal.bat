@echo off
set /p var=ValPersent(ex:0.1):
echo %var%

python SetVal.py %var%
echo "Press 2.convert yolo format On App4Ai"
pause
echo "Press 3.prepare txt On App4Ai"
pause
echo "Press 4.train On App4Ai"
pause