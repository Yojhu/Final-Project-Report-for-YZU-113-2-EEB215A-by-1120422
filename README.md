# Final-Project-Report-for-YZU-113-2-EEB215A-by1120422胡祐禎

## Folder Structure

`train_plates`資料夾裡有
- `positive/`:正樣本
- `negative/`:負樣本
- `output/`  :Haar模型輸出（例如 cascade.xml）
- `info.lst` :正樣本描述檔
- `bg.txt`   :負樣本描述檔
- `trans.py` :訓練 hear cascade的程式
  
`車牌偵測/`資料夾裡有
- `License_Plate_Detection/`:車牌辨識程式
- `car_example1.jpg`        :辨識圖片1
- `car_example2.jpg`        :辨識圖片2
- `car_example3.jpg`        :辨識圖片3
- `car_example4.jpg`        :辨識圖片4
- `no_car.jpg`              :辨識圖片5
- `測試結果/`                :裡面有兩個資料夾，分別存放使用opencv提供的模型、我自己所訓練的模型去運行車牌辨識程式後結果的截圖

## Requirements
- Python 3
- OpenCV     （我是使用opencv3.4.2版本訓練模型）
- pytesseract
## 如何安裝
-直接下載`train_plates`、`車牌偵測/`這兩個資料夾
## 如何執行
- 如果要重新訓練，首先打開 `train_plates`中的`trans.py`將程式碼2到13行改至正確位置，就可以運行`trans.py`結果會放置在`output/`中
- 再打開 `車牌偵測/`中的`License_Plate_Detection/`將程式碼5、6行改至正確位置，就可以運行`License_Plate_Detection/`，圖片中車牌位置會被方框框著，車牌號碼辨識結果會output

