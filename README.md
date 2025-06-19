#Final-Project-Report-for-YZU-113-2-EEB215A-by1120422胡祐禎

##Folder Structure
train_plates/
│
├── positive/                          # 正樣本
├── negative/                          # 負樣本
├── output/                            # Haar模型輸出（例如 cascade.xml）
├── info.lst                           # 正樣本描述檔
├── bg.txt                             # 負樣本描述檔
└── trans.py                           # 訓練 hear cascade的程式
車牌偵測/
│
├── License_Plate_Detection/           # 車牌辨識程式
├── car_example1.jpg                   # 辨識圖片1
├── car_example2.jpg                   # 辨識圖片2
├── car_example3.jpg                   # 辨識圖片3
├── car_example4.jpg                   # 辨識圖片4
├── no_car.jpg                         # 辨識圖片5
└── 測試結果/                           #裡面有兩個資料夾，一個為使用opencv提供的模型去運行車牌辨識程式後的結果截圖、一個為使用我自己所訓練的模型去運行車牌辨識程式後的結果截圖



##如何安裝與執行
