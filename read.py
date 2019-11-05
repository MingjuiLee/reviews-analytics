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

print(data[0])


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

# word counts
wc = {}	# word_counts
# nested for loop
for d in data:	# 1000000 reviews中的一則留言
	words = d.split()	# split 的預設值就是空白, 而且遇到   三個空白 就不會出現100萬次的''空字串
	for word in words:	# 一則review中的每一個string
		if word in wc:	# check this word presents or not
			wc[word] += 1	# already in dictionary, plus 1
		else:			# never present
			wc[word] = 1	# initial = 1, add new key to dictionary
	#break	# 只會走一回

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])	# key = word, wc[word] = value 次數

print(len(wc))	# length of dictionary, how many key in dictionary
#print(wc)	# maybe 印不完 command + c to stop

# let user to input a word to look up in the dictionary
print(wc['Allen'])	# value = 499

while True:
	word = input('Pleas enter the word you would like to look up: ')
	if word == 'q':
		break
	if word in wc:
		print('%s shows up %d times' %(word, wc[word]))
	else:
		print('This word never exists!')
print('Thank you for using this look up function')

# 有一行程式碼可以把出現次數多寡按照順序排列
# ''空字串, 連續使用三個   空格 得到''''''