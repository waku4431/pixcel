import cv2  #OpenCVのインポート
import numpy as np  #numpyのインポート
from PIL import Image
from io import BytesIO 

fname="7.png" #開く画像ファイル名
threshold=127 #二値化閾値

img_color= cv2.imread(fname) #画像を読み出しオブジェクトimg_colorに代入
img_gray = cv2.imread(fname,cv2.IMREAD_GRAYSCALE) #画像をグレースケールで読み出しオブジェクトimg_grayに代入
img_blur = cv2.blur(img_gray,(9,9)) #img_grayを平均化領域9x9で平均化処理しimg_blurに代入

ret, img_binary= cv2.threshold(img_blur, threshold, 255, cv2.THRESH_BINARY) #オブジェクトimg_blurを閾値threshold(127)で二値化しimg_binaryに代入

pixel_number = np.size(img_binary) #全ピクセル数をpixel_numberに代入
pixel_sum = np.sum(img_binary) #全ピクセルの輝度の合計をpixel_sumに代入
white_pixel_number = pixel_sum/255 #白いピクセルの数を計算しwhite_pixel_numberに代入
black_pixel_number = pixel_number - white_pixel_number #黒いピクセルの数を計算しwhite_pixel_numberに代入
print("全ピクセル数",pixel_number) #全ピクセル数を表示
print("輝度の合計値",pixel_sum) #輝度の合計値を表示
print("白いピクセルの数",white_pixel_number) #白いピクセルの数を表示
print("黒いピクセルの数",black_pixel_number) #黒いピクセルの数を表示

cv2.imshow("binary",img_binary) #別ウィンドウを開き(ウィンドウ名 "contours")オブジェクトimg_colorを表示

cv2.waitKey(0) #キー入力待ち
cv2.destroyAllWindows() #ウインドウを閉じる