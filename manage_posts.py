
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
from datetime import datetime
import shutil
import re

class PostManager(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("JinB&B 貼文管理系統")
        self.geometry("900x850")
        
        # 設定路徑
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.posts_js_path = os.path.join(self.base_dir, "js", "posts_data.js")
        self.template_path = os.path.join(self.base_dir, "post", "template.html")
        self.img_dir = os.path.join(self.base_dir, "img")
        
        self.init_ui()
        
    def init_ui(self):
        # 主框架
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 標題
        ttk.Label(main_frame, text="新增貼文", font=("Arial", 20, "bold")).pack(pady=(0, 20))
        
        # 表單區域
        form_frame = ttk.LabelFrame(main_frame, text="文章資訊", padding="10")
        form_frame.pack(fill=tk.BOTH, expand=True)
        
        # 文章標題
        ttk.Label(form_frame, text="文章標題:").grid(row=0, column=0, sticky="w", pady=5)
        self.title_entry = ttk.Entry(form_frame, width=50)
        self.title_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        
        # 日期
        ttk.Label(form_frame, text="發布日期 (YYYY/MM/DD):").grid(row=1, column=0, sticky="w", pady=5)
        self.date_entry = ttk.Entry(form_frame, width=20)
        self.date_entry.insert(0, datetime.now().strftime("%Y/%m/%d"))
        self.date_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        # 標籤
        ttk.Label(form_frame, text="標籤 (用逗號分隔):").grid(row=2, column=0, sticky="w", pady=5)
        self.tags_entry = ttk.Entry(form_frame, width=50)
        self.tags_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        # 圖片
        ttk.Label(form_frame, text="封面圖片:").grid(row=3, column=0, sticky="w", pady=5)
        img_frame = ttk.Frame(form_frame)
        img_frame.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        
        self.img_path_var = tk.StringVar()
        ttk.Entry(img_frame, textvariable=self.img_path_var, width=40).pack(side=tk.LEFT)
        ttk.Button(img_frame, text="選擇圖片", command=self.select_image).pack(side=tk.LEFT, padx=5)
        
        # 簡介
        ttk.Label(form_frame, text="文章簡介 (顯示在列表):").grid(row=4, column=0, sticky="nw", pady=5)
        self.desc_text = tk.Text(form_frame, height=3, width=50)
        self.desc_text.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
        
        # 內容
        ttk.Label(form_frame, text="文章內文 (HTML):").grid(row=5, column=0, sticky="nw", pady=5)
        self.content_text = tk.Text(form_frame, height=10, width=50)
        self.content_text.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
        
        # 智能格式選項
        self.smart_format_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(form_frame, text="啟用智能格式轉換 (支援 Markdown 語法: #標題, -列表, **粗體**, 自動連結)", 
                       variable=self.smart_format_var).grid(row=6, column=1, sticky="w", padx=5)
        
        # 底部按鈕
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)
        
        ttk.Button(btn_frame, text="建立貼文", command=self.create_post, width=20).pack(side=tk.RIGHT)
        
        # 設定權重
        form_frame.columnconfigure(1, weight=1)

    def select_image(self):
        filename = filedialog.askopenfilename(
            title="選擇圖片",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if filename:
            self.img_path_var.set(filename)

    def create_post(self):
        # 獲取資料
        title = self.title_entry.get().strip()
        date_str = self.date_entry.get().strip()
        tags_str = self.tags_entry.get().strip()
        img_source = self.img_path_var.get().strip()
        description = self.desc_text.get("1.0", tk.END).strip()
        content = self.content_text.get("1.0", tk.END).strip()
        
        if not all([title, date_str, img_source, description]):
            messagebox.showerror("錯誤", "請填寫所有必要欄位")
            return
            
        try:
            # 1. 處理圖片
            # 如果圖片不在 img 目錄下，複製過去
            img_filename = os.path.basename(img_source)
            target_img_path = os.path.join(self.img_dir, img_filename)
            
            if os.path.abspath(img_source) != os.path.abspath(target_img_path):
                shutil.copy2(img_source, target_img_path)
            
            # 相對於根目錄的路徑
            rel_img_path = f"img/{img_filename}"
            
            # 2. 生成 ID 和 檔案名稱
            date_obj = datetime.strptime(date_str, "%Y/%m/%d")
            safe_title = "".join([c if c.isalnum() else "-" for c in title])[:20] 
            # 簡單的 slug 化，只保留字母數字，其他轉 -
            
            post_id = f"{date_obj.year}-{date_obj.month}-{date_obj.day}-{safe_title}"
            filename = f"{post_id}.html"
            filepath = os.path.join(self.base_dir, "post", filename)
            
            # 3. 讀取並填寫模板
            with open(self.template_path, "r", encoding="utf-8") as f:
                template = f.read()
            
            tags_list = [t.strip() for t in tags_str.split(",") if t.strip()]
            
            # 替換變數
            html_content = template.replace("{{TITLE}}", title)
            html_content = html_content.replace("{{DATE}}", date_str)
            html_content = html_content.replace("{{DESCRIPTION}}", description)
            html_content = html_content.replace("{{IMAGE}}", rel_img_path)
            html_content = html_content.replace("{{FILENAME}}", filename)
            html_content = html_content.replace("{{TAGS}}", ",".join(tags_list))
            html_content = html_content.replace("{{TAGS_RAW}}", ",".join(tags_list))
            
            # 處理內容格式
            if self.smart_format_var.get():
                formatted_content = self.convert_smart_text(content)
            else:
                # 簡單將換行轉為 <p>
                formatted_content = ""
                for para in content.split('\n'):
                    if para.strip():
                        formatted_content += f'<p class="content-paragraph">{para.strip()}</p>\n'
            
            html_content = html_content.replace("{{CONTENT}}", formatted_content)
            
            # 寫入 HTML 檔案
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html_content)
                
                
            # 4. 更新 posts_data.js
            self.update_js_database({
                "id": post_id,
                "title": title,
                "date": date_str,
                "link": f"post/{filename}",
                "image": rel_img_path,
                "description": description,
                "tags": tags_list
            })

            # 5. 更新 sitemap.xml
            self.update_sitemap(f"post/{filename}", date_str)
            
            messagebox.showinfo("成功", f"貼文已建立！\n檔案: {filename}\nSitemap 已更新")
            
            # 清空表單
            self.title_entry.delete(0, tk.END)
            self.desc_text.delete("1.0", tk.END)
            self.content_text.delete("1.0", tk.END)
            
        except Exception as e:
            messagebox.showerror("錯誤", f"發生錯誤: {str(e)}")

    def update_sitemap(self, rel_path, date_str):
        try:
            sitemap_path = os.path.join(self.base_dir, "sitemap.xml")
            if not os.path.exists(sitemap_path):
                return
            
            # 轉換日期格式 YYYY/MM/DD -> YYYY-MM-DD
            iso_date = date_str.replace("/", "-")
            
            with open(sitemap_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 尋找插入點 (</urlset> 之前)
            insert_pos = content.rfind("</urlset>")
            if insert_pos == -1:
                return
                
            new_url_entry = f"""
<url>
  <loc>https://jinbnb.com/{rel_path}</loc>
  <lastmod>{iso_date}</lastmod>
  <priority>0.80</priority>
</url>
"""
            new_content = content[:insert_pos] + new_url_entry + content[insert_pos:]
            
            with open(sitemap_path, "w", encoding="utf-8") as f:
                f.write(new_content)
                
        except Exception as e:
            print(f"Sitemap update failed: {e}")


    def update_js_database(self, new_post):
        try:
            with open(self.posts_js_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 尋找陣列開始的位置
            start_idx = content.find("[")
            if start_idx == -1:
                raise Exception("找不到陣列起始位置")
                
            # 在陣列開頭插入新資料
            # 我們不解析整個 JS，而是字串操作以保持註解等
            
            # 格式化新物件
            current_json_str = json.dumps(new_post, ensure_ascii=False, indent=4)
            # 移除前後大括號的縮排，手動調整
            current_json_str = "    " + current_json_str.replace("\n", "\n    ") + ","
            
            # 插入
            new_content = content[:start_idx+1] + "\n" + current_json_str + content[start_idx+1:]
            
            with open(self.posts_js_path, "w", encoding="utf-8") as f:
                f.write(new_content)
                
        except Exception as e:
            raise Exception(f"更新 JS 資料庫失敗: {str(e)}")

    def convert_smart_text(self, text):
        """
        將一般文字智能轉換為 HTML
        支援:
        - 自動分段 (雙換行)
        - 列表 (- 或 * 開頭)
        - 標題 (# 開頭)
        - 粗體 (**文字**)
        - 連結 (自動偵測 URL)
        """
        html_parts = []
        
        # 預先處理: 轉換粗體
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        
        # 此處不直接轉 URL 為 a tag，避免破壞後續的 HTML 結構偵測
        # 我們在段落處理時再轉 URL
        
        blocks = text.split('\n\n')
        
        for block in blocks:
            block = block.strip()
            if not block:
                continue
                
            lines = block.split('\n')
            
            # 檢查是否為列表
            if all(line.strip().startswith(('-', '*')) for line in lines):
                html_parts.append('<ul class="content-list">')
                for line in lines:
                    # 移除開頭的符號
                    item_text = re.sub(r'^[\-\*]\s+', '', line.strip())
                    item_text = self.linkify(item_text)
                    html_parts.append(f'  <li>{item_text}</li>')
                html_parts.append('</ul>')
                
            # 檢查是否為標題 (只支援 # H3)
            elif lines[0].startswith('#'):
                header_text = lines[0].lstrip('#').strip()
                html_parts.append(f'<h3 class="content-header">{header_text}</h3>')
                # 如果標題塊有多行，剩下的當作普通段落
                if len(lines) > 1:
                    para_text = '<br>'.join(lines[1:])
                    para_text = self.linkify(para_text)
                    html_parts.append(f'<p class="content-paragraph">{para_text}</p>')
                    
            # 普通段落
            else:
                # 處理塊內的換行
                para_text = '<br>'.join(lines)
                para_text = self.linkify(para_text)
                html_parts.append(f'<p class="content-paragraph">{para_text}</p>')
                
        return '\n'.join(html_parts)

    def linkify(self, text):
        # 簡單的 URL 偵測 regex
        url_pattern = r'(https?://[^\s<]+)'
        return re.sub(url_pattern, r'<a href="\1" target="_blank" class="content-link">\1</a>', text)

if __name__ == "__main__":
    app = PostManager()
    app.mainloop()
