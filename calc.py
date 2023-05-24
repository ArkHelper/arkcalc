import random
import statistics
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 参数
EXG = 807  # 期望抽数
EXR = 0.9  # 期望概率
logInFun = False  # 打印日志
# logInFun = True


def Gacha():
    times = 0  # 抽次数
    water = 0  # 水位
    silverashs = 0  # 抽到潜能次数
    while True:
        times += 1  # 抽一次
        water += 1  # 水位加一
        rand = 0.02  # 当前六星出率

        if (water > 50):
            rand += ((water-50)*0.02)

        if (logInFun):
            print(f"第{times}抽，当前水位{water}，当前六星出率{rand}", end='')

        if random.random() <= rand:  # 中了六星
            water = 0  # 水位清空
            if (logInFun):
                print(f"，抽到六星", end='')
            if random.random() <= 0.35:  # 中了限定
                silverashs += 1
                if (logInFun):
                    print(f"，这是限定，当前潜能{silverashs}", end='')

        if (logInFun):
            print('')

        if (times % 300 == 0):
            silverashs += 1
            if (logInFun):
                print(f"商店兑换，当前潜能{silverashs}")

        # 条件满潜
        if (silverashs >= 6):
            if (logInFun):
                print(f"已经满潜，总计抽数{times}")
            return times


LEN = 2000  # 总数
NUM = []
for _ in range(LEN):
    NUM.append(Gacha())
NUM = sorted(NUM)

# 满潜统计
ALL = sum(NUM)
MIN = min(NUM)
MAX = max(NUM)
AVG = statistics.mean(NUM)
MID = statistics.median(NUM)

# 概率统计
LOW = sum(1 for _EVY in NUM if _EVY < EXG)
RAT = LOW/LEN

# 定向统计
UDL = LEN*EXR
GAC = NUM[int(UDL)-1]

print(f"平均：{AVG}")
print(f"中位：{MID}")
print(f"最多：{MAX}")
print(f"最少：{MIN}")
print(f"{EXG}概率：{RAT}")
print(f"{EXR}定向：{GAC}")

""" 
# 设置分段区间的边界
bins = [0];_temp = 0
while True:
    _temp += 20;bins.append(_temp);
    if (_temp >= MAX): break
plt.hist(NUM, bins=bins, edgecolor='black');plt.title('分段柱状图');plt.xlabel('抽数');plt.ylabel('频率');plt.show()
 """
