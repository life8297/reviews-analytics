# 分析留言數量
import time
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print('檔案讀取完了,共', len(data), '筆資料') # 結果為100萬筆留言
print(data[0])

start = time.time()
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 # 已有字典內容計數+ 1
		else :
			wc[word] = 1 # 新增新的key進字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end = time.time()
print(len(wc))
print('讀取共花費:', int(end - start), '秒')

while True:
	search = input('請輸入查詢內容(輸入q離開):')
	if search == 'q':
		break
	elif search in wc:
		print(search, '出現過', wc[search], '次')
	else:
		print('此內容不存在，請重新查詢')
print('感謝使用本查詢')