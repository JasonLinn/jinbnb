#!/usr/bin/env python3
"""
圖片壓縮和剪裁工具
支援壓縮圖片品質和剪裁圖片（維持原比例）
具有處理紀錄功能，避免重複處理
"""

import os
import json
import hashlib
import shutil
from PIL import Image, ExifTags
import argparse
from datetime import datetime
from typing import Dict, Tuple, Optional

class ImageProcessor:
    def __init__(self, record_file: str = "processed_images.json"):
        self.record_file = record_file
        self.processed_images = self.load_records()
        self.backup_dir = "backup"
    
    def load_records(self) -> Dict:
        """載入處理紀錄"""
        if os.path.exists(self.record_file):
            try:
                with open(self.record_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_records(self):
        """儲存處理紀錄"""
        with open(self.record_file, 'w', encoding='utf-8') as f:
            json.dump(self.processed_images, f, indent=2, ensure_ascii=False)
    
    def get_file_hash(self, file_path: str) -> str:
        """計算檔案的 MD5 雜湊值"""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def create_backup(self, file_path: str) -> str:
        """建立檔案備份"""
        if not os.path.exists(file_path):
            return None
        
        # 建立備份目錄
        os.makedirs(self.backup_dir, exist_ok=True)
        
        # 產生備份檔案名稱（加上時間戳記）
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"{name}_{timestamp}{ext}"
        backup_path = os.path.join(self.backup_dir, backup_filename)
        
        # 複製原檔案到備份目錄
        shutil.copy2(file_path, backup_path)
        print(f"已備份原檔案: {backup_path}")
        
        return backup_path
    
    def correct_image_orientation(self, image: Image.Image) -> Image.Image:
        """修正圖片方向（根據 EXIF 資訊）"""
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            
            exif = image._getexif()
            if exif is not None:
                orientation_value = exif.get(orientation)
                if orientation_value == 3:
                    image = image.rotate(180, expand=True)
                elif orientation_value == 6:
                    image = image.rotate(270, expand=True)
                elif orientation_value == 8:
                    image = image.rotate(90, expand=True)
        except:
            pass
        return image
    
    def compress_image(self, input_path: str, output_path: str, quality: int = 85) -> bool:
        """壓縮圖片"""
        try:
            with Image.open(input_path) as img:
                # 修正圖片方向
                img = self.correct_image_orientation(img)
                
                # 如果是 PNG 且有透明度，保持 RGBA 模式
                if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                    # 如果輸出格式是 JPEG，需要轉換為 RGB
                    if output_path.lower().endswith('.jpg') or output_path.lower().endswith('.jpeg'):
                        # 創建白色背景
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                        img = background
                else:
                    # 確保是 RGB 模式
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                
                # 保存壓縮後的圖片
                img.save(output_path, quality=quality, optimize=True)
                
            return True
        except Exception as e:
            print(f"壓縮圖片時發生錯誤: {e}")
            return False
    
    def crop_image(self, input_path: str, output_path: str, target_size: Tuple[int, int]) -> bool:
        """縮放圖片到指定尺寸範圍內（維持原比例）"""
        try:
            with Image.open(input_path) as img:
                # 修正圖片方向
                img = self.correct_image_orientation(img)
                
                # 計算縮放比例（維持原比例）
                original_width, original_height = img.size
                target_width, target_height = target_size
                
                # 計算比例
                ratio_w = target_width / original_width
                ratio_h = target_height / original_height
                
                # 選擇較小的比例以確保完全在目標尺寸範圍內
                ratio = min(ratio_w, ratio_h)
                
                # 只有在需要縮小時才調整尺寸
                if ratio < 1:
                    # 計算調整後的尺寸
                    new_width = int(original_width * ratio)
                    new_height = int(original_height * ratio)
                    
                    # 調整圖片大小
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # 確保是 RGB 模式
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # 保存縮放後的圖片
                img.save(output_path, quality=85, optimize=True)
                
            return True
        except Exception as e:
            print(f"縮放圖片時發生錯誤: {e}")
            return False
    
    def process_image(self, input_path: str, output_path: str = None, 
                     quality: int = 85, crop_size: Tuple[int, int] = None, 
                     force: bool = False) -> bool:
        """處理圖片（壓縮和/或剪裁）"""
        if not os.path.exists(input_path):
            print(f"檔案不存在: {input_path}")
            return False
        
        # 跳過所有 PNG 檔案
        if input_path.lower().endswith('.png'):
            print(f"跳過 PNG 檔案: {input_path}")
            return True
        
        # 計算檔案雜湊值
        file_hash = self.get_file_hash(input_path)
        
        # 產生處理設定的雜湊值
        settings = {
            'quality': quality,
            'crop_size': crop_size,
            'output_path': output_path or input_path
        }
        settings_str = json.dumps(settings, sort_keys=True)
        settings_hash = hashlib.md5(settings_str.encode()).hexdigest()
        
        # 檢查是否已處理過
        record_key = f"{file_hash}_{settings_hash}"
        if not force and record_key in self.processed_images:
            print(f"圖片已處理過，跳過: {input_path}")
            return True
        
        # 設定輸出路徑
        if output_path is None:
            output_path = input_path
        
        # 如果是覆蓋原檔案，先建立備份
        if output_path == input_path:
            self.create_backup(input_path)
        
        # 確保輸出目錄存在
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        success = True
        
        # 如果需要縮放
        if crop_size:
            print(f"正在縮放圖片: {input_path} -> {output_path}")
            success = self.crop_image(input_path, output_path, crop_size)
        else:
            # 只壓縮
            print(f"正在壓縮圖片: {input_path} -> {output_path}")
            success = self.compress_image(input_path, output_path, quality)
        
        # 記錄處理結果
        if success:
            self.processed_images[record_key] = {
                'input_path': input_path,
                'output_path': output_path,
                'quality': quality,
                'crop_size': crop_size,
                'processed_time': datetime.now().isoformat(),
                'file_hash': file_hash
            }
            self.save_records()
            print(f"處理完成: {input_path}")
        else:
            print(f"處理失敗: {input_path}")
        
        return success
    
    def batch_process(self, directory: str, output_dir: str = None, 
                     quality: int = 85, crop_size: Tuple[int, int] = None, 
                     force: bool = False):
        """批次處理目錄中的圖片"""
        if not os.path.exists(directory):
            print(f"目錄不存在: {directory}")
            return
        
        # 支援的圖片格式
        supported_formats = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'}
        
        processed_count = 0
        skipped_count = 0
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in supported_formats):
                    input_path = os.path.join(root, file)
                    
                    if output_dir:
                        # 計算相對路徑
                        rel_path = os.path.relpath(input_path, directory)
                        output_path = os.path.join(output_dir, rel_path)
                    else:
                        output_path = input_path
                    
                    if self.process_image(input_path, output_path, quality, crop_size, force):
                        processed_count += 1
                    else:
                        skipped_count += 1
        
        print(f"\\n批次處理完成: 處理 {processed_count} 張圖片，跳過 {skipped_count} 張")

def main():
    parser = argparse.ArgumentParser(description='圖片壓縮和剪裁工具')
    parser.add_argument('input', help='輸入檔案或目錄路徑')
    parser.add_argument('-o', '--output', help='輸出檔案或目錄路徑')
    parser.add_argument('-q', '--quality', type=int, default=85, help='壓縮品質 (1-100，預設: 85)')
    parser.add_argument('-c', '--crop', help='剪裁尺寸，格式: WIDTHxHEIGHT (例如: 800x600)')
    parser.add_argument('-f', '--force', action='store_true', help='強制重新處理已處理過的圖片')
    parser.add_argument('-r', '--record', default='processed_images.json', help='處理紀錄檔案路徑')
    
    args = parser.parse_args()
    
    # 解析剪裁尺寸
    crop_size = None
    if args.crop:
        try:
            width, height = map(int, args.crop.split('x'))
            crop_size = (width, height)
        except:
            print("錯誤：剪裁尺寸格式不正確，應為 WIDTHxHEIGHT")
            return
    
    # 驗證品質參數
    if not (1 <= args.quality <= 100):
        print("錯誤：品質參數應在 1-100 之間")
        return
    
    # 建立處理器
    processor = ImageProcessor(args.record)
    
    # 判斷是檔案還是目錄
    if os.path.isfile(args.input):
        # 處理單一檔案
        processor.process_image(args.input, args.output, args.quality, crop_size, args.force)
    elif os.path.isdir(args.input):
        # 批次處理目錄
        processor.batch_process(args.input, args.output, args.quality, crop_size, args.force)
    else:
        print(f"錯誤：路徑不存在 - {args.input}")

if __name__ == "__main__":
    main()