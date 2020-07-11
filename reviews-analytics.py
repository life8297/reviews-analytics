# 分析留言數量
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print('檔案讀取完了,共', len(data), '筆資料') # 結果為100萬筆留言

# 分析平均留言長度
sum_len = 0
for d in data:
	sum_len += len(d)
print('總平均留言長度為:', int(sum_len / len(data)))

# 篩選內容較短之留言
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('留言長度小於100字母長的有', len(new), '筆')

# 篩選內含good之留言
good_reviews = []
for d in data:
	if "good" in d:
		good_reviews.append(d)
print('留言中有提到good的留言有', len(good_reviews), '筆')

# 篩選內含good之留言-清單快寫法
good = [d for d in data if 'good' in d]
print('留言中有提到good的留言有', len(good), '筆')