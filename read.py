# 讀取留言檔
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:	# because read one line each time
		data.append(line)
		count += 1	# 快寫法
		if count % 1000 == 0:
			print(len(data))	# print current progess
print(len(data))

#print(data)  # too much
print(data[0])
print('---------------------')
print(data[1])