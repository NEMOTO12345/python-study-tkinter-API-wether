#都市の一週間の天気を調べるアプリ
import json
import re
import requests
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext


root = tk.Tk()
root.title("天気アプリ")
root.minsize(400,300)



#画面上のテキストを設定1
static1 = tk.Label(text="今週の天気")
static1.pack()

#セレクトボックス(コンボボックス)を作る
combo = ttk.Combobox(root, state='readonly')
# セレクトボックスの選択値を設定
city_data = {'釧路': 304, '旭川': 302, '札幌': 306, '青森': 308, '秋田': 309, '仙台': 312, '新潟': 323, '金沢': 325,
'東京': 319, '宇都宮': 316, '長野': 322, '名古屋': 329, ' 大阪': 331, '高松': 341, '松江': 337, '広島': 338, '高知': 344, '福岡': 346, '鹿児島': 352, '那覇': 353,
'石垣': 356}
# city_data_reverse = {v:k for k,v in city_data.items()}
city = []
for k,v in city_data.items():
    city.append(k)
# print(city)
combo["values"] = ([x for x in city])

# デフォルトの値をA(index=0)に設定　"タイトル", "著者", "出版社", "説明"
combo.current(0)
# コンボボックスの配置
combo.pack()

result = tkinter.scrolledtext.ScrolledText(width = 30,height=10)

def get_resutlt(event):
    combo_get = combo.get()
    result.delete("1.0", tk.END)
    url = f"https://api.aoikujira.com/tenki/week.php?fmt=json&city={city_data[combo_get]}"
    data = requests.get(url)

    today_data = []
    n = 0
    json_data = json.loads(data.text)
    for k,v in json_data.items():
        if n == 0:
            today_data.append(v)
            #k:mkdata v:319
            n += 1
            #mkdataは一回のみ
        else:
            for line in v:
            #k:319のデータvをlineに入れる。
                for k2,v2 in line.items():
                #k2:data v2:22日（月）
                    if k2 == 'date':
                        result.insert(tk.END,f"{v2}\n")
                    elif k2 == 'forecast':
                        result.insert(tk.END,f"天気予報：{v2.replace('曇','☁').replace('晴','☀').replace('雨','☂')}\n")
                    elif k2 == 'mintemp':
                        result.insert(tk.END,f"最低気温：{v2}度\n")
                    elif k2 == 'maxtemp':
                        result.insert(tk.END,f"最高気温：{v2}度\n")


# "date"	日付
# "forecast"	天気予報
# "mintemp"	最低気温
# "maxtemp"	最高気温
# "pop"	降水確率
btn = tk.Button(text="検索")
btn.bind("<1>", get_resutlt)
btn.pack()



result.pack()

root.mainloop()