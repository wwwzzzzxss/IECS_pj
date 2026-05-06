import pandas as pd
import re

# 1. 讀取臺中市實價登錄原始檔
df = pd.read_excel('B_lvr_land_A.csv.xlsx')

# 2. 移除第一列的英文標頭
if len(df) > 0 and 'The villages' in str(df.iloc[0].get('鄉鎮市區', '')):
    df = df.iloc[1:].copy()

# 3. 過濾掉純土地交易 (不包含'地號'的才保留)
df_houses = df[~df['土地位置建物門牌'].astype(str).str.contains('地號')].copy()

# 4. 定義地址清洗函數
def clean_address(addr):
    addr = str(addr)
    addr = addr.replace('等公共設施', '')
    if '，' in addr:
        addr = addr.split('，')[0]
        if '號' not in addr: 
            addr += '號'
    match = re.match(r'(.*?號)', addr)
    if match:
        addr = match.group(1)
    return addr

# 執行清洗
cleaned_addresses = df_houses['土地位置建物門牌'].apply(clean_address)

# 5. 建立 TGOS 專屬格式的 DataFrame (嚴格按照 Address.csv 範本)
tgos_df = pd.DataFrame({
    'id': range(1, len(cleaned_addresses) + 1),
    'Address': cleaned_addresses,
    'Response_Address': '',
    'Response_X': '',
    'Response_Y': ''
})

# 6. 匯出 CSV 檔案
output_filename = 'B_lvr_land_TGOS_ready.csv'
tgos_df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"處理完成！共轉換了 {len(tgos_df)} 筆地址。")
print(tgos_df.head(5))