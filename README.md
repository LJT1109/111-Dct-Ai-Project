# 111-Dct-Ai-Project\n
\n
測試影片\n
https://youtu.be/VovK4KxS4WU\n

操作流程\n
1.開啟app4ai，安裝yolov7\n
2.開啟yolov7
3.建立新Dataset
4.開啟Dataset資料夾
5.解壓縮下載的檔案
6.啟動python terminal 
7.cd 資料夾目錄
8.pip install -r requirement.txt
9.run 0_FirstTrain.bat
10.輸入50 -> 隨機取得圖片作為訓練資料
11.yolov7 選擇 1.annotation voc xml
12.標記要尋找的物品
13.run 1_SetVal.bat
14.輸入0.1 -> 取10%的訓練資料作為驗證集
15.調整label
16.yolov7 選擇 2.convert yolo format
17.yolov7 選擇 3.prepare txt
18.(6GB VRam) Batch Size->50
              Image Size->256
              Epochs -> 建議500次以上
19.yolov7 選擇 4.train
20.run 2_SetTest.bat
21.輸入200 -> 隨機200張圖片作為測試
22.yolov7 選擇 6.inference folder -> test/image
23.測試結果不好：
   run 3_ReTrain.bat
   正確資料按 Right Arrow，錯誤資料按 Left Arrow，回到上一筆案 Up Arrow
   完成後，資料會自動增加到 Train 資料集
   (run 1_SetVal.bat)
   回到 step 16
24.測試結果可接受：
   run 4_CreatArea.bat
   輸入地圖範圍
   yolov7 選擇 6.inference folder -> area
   run 5.Draw.bat
   得到結果
