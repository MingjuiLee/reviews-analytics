# 讀取留言檔
data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:	# because read one line each time
		data.append(line)
		count += 1	# 快寫法
		if count % 1000 == 0:
			print(len(data))	# print current progess
print('File reading is completed, total %d data' %(len(data)))

sum_len = 0
for d in data:	# d is a string
	sum_len += len(d)	# count len for all d
	#print(sum_len)
print('Average length for reviews is %f' %(sum_len / len(data)))