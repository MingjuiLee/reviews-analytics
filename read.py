# 讀取留言檔 read reviews
import time
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

# filter review with 'good'
start_1 = time.time()
good = []
for d in data:
	if 'good' in d:	   # in 
		good.append(d)	# put this particular review in list
print("There are %d reviews that mention 'good'" %len(good))
print(good[0])
end_1 = time.time()
print("Basic version time: %f" %(end_1 - start_1))

# list comprehension, filtering with one line
start_2 = time.time()
good_2 = [d for d in data if 'good' in d]
end_2 = time.time()
print("Advanced version time: %f" %(end_2 - start_2))

# put a computation in front
bad = ['bad' in d for d in data]	 # 放一個運算 True or False 共1000000筆
print(bad[0:10])	# list comprehension 通常最前面還是放d

# basic
bad_2 = []
for d in data:
	bad.append('bad' in d)