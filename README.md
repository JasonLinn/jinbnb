# JinB&B 網站管理工具文件

本文件說明專案中用於管理貼文與處理圖片的 Python 工具程式。

## 目錄

- [貼文管理系統 (manage_posts.py)](#貼文管理系統-manage_postspy)
- [圖片處理工具 (image_processor.py)](#圖片處理工具-image_processorpy)

---

## 貼文管理系統 (manage_posts.py)

這是一個圖形化介面 (GUI) 的應用程式，用於快速建立新的部落格貼文。它會自動處理檔案生成、圖片複製以及資料庫更新。

### 功能特色

- **圖形化介面**：使用 Tkinter 構建，無需操作複雜的 JSON 或 HTML。
- **自動化流程**：
  - 自動將選擇的圖片複製到 `img/` 目錄。
  - 根據標題與日期生成唯一的 Post ID 與對應的 HTML 檔案 (`post/YYYY-MM-DD-title.html`)。
  - 自動讀取 `post/template.html` 模板並填入內容。
  - 自動更新 `js/posts_data.js` 中的文章列表資料。
  - 自動更新 `sitemap.xml` 以利 SEO。

### 安裝需求

程式使用 Python 內建的 `tkinter`，通常無需額外安裝套件。確保環境中有 Python 3 即可。

### 使用方式

在專案根目錄下執行：

```bash
python manage_posts.py
```

### 操作說明

1. **啟動程式**：執行後會出現 "JinB&B 貼文管理系統" 視窗。
2. **填寫資訊**：
   - **文章標題**：輸入文章的主標題。
   - **發布日期**：預設為當天日期 (YYYY/MM/DD)。
   - **標籤**：輸入文章標籤，以逗號分隔 (例如：`宜蘭, 景點, 美食`)。
   - **封面圖片**：點擊 "選擇圖片" 按鈕選取圖片檔案。程式會自動將圖片複製到專案的 `img/` 資料夾中。
   - **文章簡介**：顯示在文章列表頁面的短文。
   - **文章內文 (HTML)**：文章的主要內容。
     - **智能格式轉換**：勾選「啟用智能格式轉換」後，支援 Markdown 風格語法：
       - **段落**：使用空白行分隔段落。
       - **標題**：行首使用 `#` 表示標題 (轉為 H3)。
       - **列表**：行首使用 `-` 或 `*` 表示列表項目。
       - **粗體**：使用 `**文字**` 表示粗體。
       - **連結**：自動偵測網址並轉換為超連結。
     - 若取消勾選，則僅將換行轉換為段落。亦可直接輸入 HTML 代碼。
3. **建立貼文**：點擊底部 "建立貼文" 按鈕。
   - 成功後會跳出提示視窗，顯示生成的檔案名稱。
   - 若有錯誤 (如欄位未填)，會跳出警告。

---

## 圖片處理工具 (image_processor.py)

這是一個功能強大的圖片處理工具，支援圖片壓縮、剪裁（維持原比例）和處理紀錄功能。

### 功能特色

- **圖片壓縮**：支援調整 JPEG 品質（1-100）
- **智能剪裁**：剪裁圖片時維持原比例，避免變形
- **處理紀錄**：記錄已處理的圖片，避免重複處理
- **批次處理**：支援整個目錄的批次處理
- **方向修正**：自動根據 EXIF 資訊修正圖片方向
- **格式支援**：支援 JPG、PNG、BMP、GIF、TIFF 等格式

### 安裝需求

```bash
pip install -r requirements.txt
```

### 使用方式

#### 基本用法

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

#### 批次處理

```bash
# 批次處理整個目錄
python image_processor.py img/

# 批次處理並輸出到指定目錄
python image_processor.py img/ -o compressed_img/

# 批次壓縮和剪裁
python image_processor.py img/ -o processed_img/ -q 75 -c 1200x800
```

#### 進階選項

```bash
# 強制重新處理已處理過的圖片
python image_processor.py img/ -f

# 指定處理紀錄檔案
python image_processor.py img/ -r my_records.json
```

### 參數說明

- `input`: 輸入檔案或目錄路徑
- `-o, --output`: 輸出檔案或目錄路徑
- `-q, --quality`: 壓縮品質 (1-100，預設: 85)
- `-c, --crop`: 剪裁尺寸，格式: WIDTHxHEIGHT
- `-f, --force`: 強制重新處理已處理過的圖片
- `-r, --record`: 處理紀錄檔案路徑 (預設: processed_images.json)

### 處理紀錄

程式會自動記錄已處理的圖片資訊 (檔案雜湊值、參數、時間等) 於 JSON 檔案中，避免重複處理。

### 注意事項

1. 剪裁功能會維持原圖片比例，採用置中剪裁方式。
2. 程式會自動根據 EXIF 資訊修正圖片方向。
3. PNG 圖片如果有透明度，轉換為 JPEG 時會使用白色背景。
