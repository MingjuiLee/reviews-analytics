# 讀取留言檔 read reviews
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

# filtering
new = []
for d in data:	# data list 中一筆一筆review叫出來 d: string, data: list
	if len(d) < 100:
		new.append(d)	# 篩選完成
print('There are total %d reviews with length less than 100' %len(new))
print(new[0])	# print first review after filtering
print(new[0])	# print second review after filtering