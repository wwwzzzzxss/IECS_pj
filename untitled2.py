import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. 讀取資料 (跳過第二行英文標頭)
df = pd.read_csv('B_lvr_land_A.csv', skiprows=[1])

# 2. 篩選西屯區並選擇特徵
data = df[df['鄉鎮市區'] == '西屯區']
features = ['土地移轉總面積平方公尺', '建物移轉總面積平方公尺', '建物現況格局-房', '建物現況格局-廳', '建物現況格局-衛']
target = '總價元'

# 3. 清理資料 (移除包含空值的資料列)
ml_data = data[features + [target]].dropna()
X = ml_data[features]
y = ml_data[target]

# 4. 拆分訓練集與測試集 (80% 訓練, 20% 測試)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. 訓練線性回歸模型
model = LinearRegression()
model.fit(X_train, y_train)

# 6. 輸出結果
print(f"模型準確度 (R^2 Score): {model.score(X_test, y_test):.4f}")
print("各項因素對房價的影響力 (係數):")
for feat, coef in zip(features, model.coef_):
    print(f"{feat}: {coef:,.0f}")