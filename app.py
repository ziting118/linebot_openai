a9a13a3b7e79f9f56ff66e289c46621a7df40967
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

words_dict = {
    "飯": "滷肉飯",
    "麵": "擔仔麵",
    "日式料理": "拉麵",
    "水餃": "鮮蝦水餃",
    "速食": "漢堡",
    "韓式料理": "韓式拌飯",
    "健康餐食": "雞胸肉健身餐",
    "不知道": "小火鍋",
    "豐盛一點": "牛排",
    "簡單吃":"便利商店"
}

# 使用者想吃的食物類型


Q = input("今天想吃甚麼類型的食物？").lower()
if Q == 'quit':
    break
A=words_dict[Q]
print("答案:",A )
