import pandas as pd

# --- 步驟 1：讀取檔案 ---
# 讀取我們剛剛清洗好的、包含 10740 筆資料的大檔案
print("正在讀取檔案...")
df = pd.read_csv('B_lvr_land_TGOS_ready.csv')

# --- 步驟 2：資料切片 (Slicing) ---
# .iloc 是 Pandas 用來「透過位置抓取資料」的語法
# [:10000] 代表抓取第 0 筆到第 9999 筆 (剛好 10,000 筆)
print("正在分割資料...")
df_part1 = df.iloc[:10000].copy()

# [10000:] 代表抓取第 10000 筆一路到最後一筆 (剩下的 740 筆)
df_part2 = df.iloc[10000:].copy()

# --- 步驟 3：重設流水號 (id) ---
# TGOS 的範本要求要有 id，為了保險起見，我們讓第二個檔案的 id 也從 1 開始算
df_part1['id'] = range(1, len(df_part1) + 1)
df_part2['id'] = range(1, len(df_part2) + 1)

# --- 步驟 4：匯出新檔案 ---
# index=False 代表不要把 Pandas 預設的左側索引值印出來
# encoding='utf-8-sig' 是關鍵！這樣存檔，用微軟 Excel 打開中文字才不會變亂碼
print("正在匯出檔案...")
df_part1.to_csv('B_lvr_land_TGOS_ready_part1.csv', index=False, encoding='utf-8-sig')
df_part2.to_csv('B_lvr_land_TGOS_ready_part2.csv', index=False, encoding='utf-8-sig')

print(f"處理完成！")
print(f"第一份檔案包含 {len(df_part1)} 筆資料")
print(f"第二份檔案包含 {len(df_part2)} 筆資料")