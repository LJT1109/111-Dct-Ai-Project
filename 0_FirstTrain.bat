@echo off
set /p var=PleaseEnterCountofTrainImage:
echo %var%
python RandomFIrstTrain.py 
python RandomTrain.py %var%
echo "Press 1.annotation voc xml On App4Ai"
pause