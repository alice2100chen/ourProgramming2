
# 循序搜尋法
def seq_search(data, target):
    for i in range(len(data)):
        if target == data[i]:
            return i
    return -1

# 二分搜尋法_採遞迴方式
def binary_search_recursive(data, left, right, target):
    if left >= right:
        return -1
    middle = left + (right - left) // 2

    if target > data[middle]:
        return binary_search_recursive(data, middle + 1, right, target)
    if target < data[middle]:
        return binary_search_recursive(data, left, middle, target)
    if target == data[middle]:
        return middle

# 主程式開始--------------------------------------------------------
import random
import time

# 產生大量(共5000000)個的隨機數(範圍0-9999999)
random.seed(0)
data = random.sample(range(10000000), 5000000)
sorted_data = sorted(data)
targets = []
num_tests = 100
for i in range(num_tests):
    targets.append(data[i])

# 開始計時: 循序搜尋法所花的時間
print('開始循序搜尋...')
time_start = time.time()
for i in range(num_tests):
    seq_search(sorted_data, targets[i])
print('平均循序搜尋法所花的時間:',(time.time()-time_start) / num_tests)

# 開始計時: 二分搜尋法_採遞迴方式 
print('開始遞迴式二分搜尋...')
time_start = time.time()
for i in range(num_tests):
    binary_search_recursive(sorted_data, 0, len(sorted_data), targets[i])
print('平均遞迴式二分搜尋法所花的時間:',(time.time()-time_start) / num_tests)

