# 圖片壓縮和剪裁工具

這是一個功能強大的圖片處理工具，支援圖片壓縮、剪裁（維持原比例）和處理紀錄功能。

## 功能特色

- **圖片壓縮**：支援調整 JPEG 品質（1-100）
- **智能剪裁**：剪裁圖片時維持原比例，避免變形
- **處理紀錄**：記錄已處理的圖片，避免重複處理
- **批次處理**：支援整個目錄的批次處理
- **方向修正**：自動根據 EXIF 資訊修正圖片方向
- **格式支援**：支援 JPG、PNG、BMP、GIF、TIFF 等格式

## 安裝

```bash
pip install -r requirements.txt
```

## 使用方式

### 基本用法

```bash
# 壓縮單張圖片（品質 85）
python image_processor.py image.jpg

# 指定輸出檔案和品質
python image_processor.py image.jpg -o compressed_image.jpg -q 70

# 剪裁圖片為 800x600（維持原比例）
python image_processor.py image.jpg -c 800x600

# 同時壓縮和剪裁
python image_processor.py image.jpg -o output.jpg -q 80 -c 1920x1080
```

### 批次處理

```bash
# 批次處理整個目錄
python image_processor.py img/

# 批次處理並輸出到指定目錄
python image_processor.py img/ -o compressed_img/

# 批次壓縮和剪裁
python image_processor.py img/ -o processed_img/ -q 75 -c 1200x800
```

### 進階選項

```bash
# 強制重新處理已處理過的圖片
python image_processor.py img/ -f

# 指定處理紀錄檔案
python image_processor.py img/ -r my_records.json
```

## 參數說明

- `input`: 輸入檔案或目錄路徑
- `-o, --output`: 輸出檔案或目錄路徑
- `-q, --quality`: 壓縮品質 (1-100，預設: 85)
- `-c, --crop`: 剪裁尺寸，格式: WIDTHxHEIGHT
- `-f, --force`: 強制重新處理已處理過的圖片
- `-r, --record`: 處理紀錄檔案路徑 (預設: processed_images.json)

## 處理紀錄

程式會自動記錄已處理的圖片資訊，包括：
- 檔案雜湊值
- 處理參數
- 處理時間
- 輸入/輸出路徑

這樣可以避免重複處理相同的圖片和設定。

## 注意事項

1. 剪裁功能會維持原圖片比例，採用置中剪裁方式
2. 程式會自動根據 EXIF 資訊修正圖片方向
3. PNG 圖片如果有透明度，轉換為 JPEG 時會使用白色背景
4. 處理紀錄檔案為 JSON 格式，可以手動編輯或刪除

## 範例

假設你有一個包含多張圖片的 `img` 目錄，想要：
- 壓縮品質設為 80
- 剪裁為 1200x800 尺寸
- 輸出到 `optimized` 目錄

```bash
python image_processor.py img/ -o optimized/ -q 80 -c 1200x800
```

這樣就會批次處理所有圖片，並且下次執行時會跳過已處理的圖片。