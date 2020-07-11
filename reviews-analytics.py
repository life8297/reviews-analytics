data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(len(data)) # 結果為100萬筆留言
print(data[0])
print('--------------------')
print(data[1])