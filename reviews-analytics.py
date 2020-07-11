data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print('檔案讀取完了,共', len(data), '筆資料') # 結果為100萬筆留言
sum_len = 0
for d in data:
	sum_len += len(d)
print('總平均留言長度為:', int(sum_len / len(data)))
