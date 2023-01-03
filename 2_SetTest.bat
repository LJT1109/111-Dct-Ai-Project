@echo off
set /p var=TeatCount(ex:0.1):
echo %var%

python rawToTest.py %var%

echo "Press 6.inference folder On App4Ai"
pause