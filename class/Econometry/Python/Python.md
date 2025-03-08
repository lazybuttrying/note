
# 1. Python Syntax
```python
a = "1. Hello World"
b = "2. Hello World\n3. Hello World"
print(a.count('o')) # 2
print(a.find('H')) # 3

a = [1, 2, 10, 7]
a.insert(1, 4) # [1, 4, 2, 10, 7]
a.remove(4) # [1, 2, 10, 7]

# Tuple
# TypeError: 'tuple' object does not support item assignment

a ={'name': 'Steve', 'age':12, 'birth' :[7,9]}
del a['birth']
a.get('birth') # None
a.values() # dict_values(['Steve', 12, 'apartment'])
list(a.values()) # ['Steve', 12, 'apartment']
```


```python
a = 0
while a < 5:
  print("a의 값은 %s 입니다." %a)
  if a == 3:
    break
  a = a + 1

# a의 값은 0 입니다. 
# a의 값은 1 입니다. 
# a의 값은 2 입니다. 
# a의 값은 3 입니다.
```

# 2. Pandas

### Pandas Syntax
- axis = 0: 가로행

```python
A = [[1,2,3],[4,5,6],[7,8,9]]
i = ['첫째행', '둘째행', '셋째행']
c = ['컬럼1', '컬럼2', '컬럼3']

DB1 = pd.DataFrame(A, index = i, columns = c)
	컬럼1 컬럼2 컬럼3 
첫째행 1 2 3 
둘째행 4 5 6 
셋째행 7 8 9

DB1['컬럼4'] = 0
	컬럼1 컬럼2 컬럼3 컬럼4
첫째행 1 2 3 0
둘째행 4 5 6 0
셋째행 7 8 9 0

DB3 = DB1.drop(['컬럼4'], axis = 1, inplace = False)
	컬럼1 컬럼2 컬럼3 
첫째행 1 2 3 
둘째행 4 5 6 
셋째행 7 8 9

DB5 = DB1.drop(['둘째행'], axis = 0)
	컬럼1 컬럼2 컬럼3 
첫째행 1 2 3 
셋째행 7 8 9
```


```python
df_sorted = df.sort_values(by=['A Level', 'B Process'], ascending = False) # 내림차순
```

```python
# NaN
print(df.sum()/df.count())
print(df.mean()) # ?????

df['Nan'] = np.nan

print(df.isna().sum())
A Process 0 
B Process 0 
C Process 0 
D Process 0 
E Process 0 
A+B 0 
A Level 0 
Nan 10000


```

### 2-2. Conditional Probability

```python
import numpy as np
import pandas as pd
data = {
		'Weather': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
        'Play': ['No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']}

df = pd.DataFrame(data)
sunny_weather = df[df['Weather'] == 'Sunny']

yes_plays_sunny = len(sunny_weather[sunny_weather['Play'] == 'Yes'])
total_sunny = len(sunny_weather)
conditional_prob = yes_plays_sunny / total_sunny
print(f"P(Play=Yes | Weather=Sunny) = {conditional_prob}")

contingency_table = pd.pivot_table(df, values='Play', index='Weather', aggfunc=lambda x: x.value_counts(normalize=True))
print("\nContingency Table (Conditional Probabilities):\n", contingency_table)
```
```
P(Play=Yes | Weather=Sunny) = 0.6 
Contingency Table (Conditional Probabilities): 
		Play 
Weather 
Overcast 1.0 
Rainy [0.6, 0.4] 
Sunny [0.6, 0.4]
```

# 3. Numpy
### 3-1. Array

```python
B = np.array([[1,2,3],[4,5,6]])
print(B) # [[1 2 3] [4 5 6]]
print("B type : ", type(B))  # B type : <class 'numpy.ndarray'>
print("B shape : ", B.shape) # B shape : (2, 3)
print("B dim. : ", B.ndim)   # B dim. : 2

C = np.array([[1,2,3]])
print(C) # [[1 2 3]]
print("C type : ", type(C))  # C type : <class 'numpy.ndarray'>
print("C shape : ", C.shape) # B shape : (1, 3)
print("C dim. : ", C.ndim)   # B dim. : 2
```

```python
E = np.ones((2,3))
F = np.zeros_like(E) # 모든 값을 0으로 초기화

G = np.full((3,2),7)
# [[7 7] [7 7] [7 7]]

H = np.random.random((4,5)) # 모든 값은 0 ~ 1
```

```python
A1 = np.arange(15)
# [ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14]

A2 = A1.reshape(3,5)
# [[ 0 1 2 3 4] [ 5 6 7 8 9] [10 11 12 13 14]]
A4 = A1.reshape(-1,5)
# [[ 0 1 2 3 4] [ 5 6 7 8 9] [10 11 12 13 14]]

A3 = A1.reshape(3,5, order ='F')
# [[ 0 3 6 9 12] [ 1 4 7 10 13] [ 2 5 8 11 14]]
A5 = A1.reshape(3,-1, order='F')
# [[ 0 3 6 9 12] [ 1 4 7 10 13] [ 2 5 8 11 14]]
```

### 3-2. Linear Algebra
- c = np.dot(a, b) # 외외적
- d = np.transpose(a)

### 3-3. Stat
```python
print('Mean = ',np.mean(X))
print('var  = ', np.var(X))
print('std. =', np.std(X))
print('max  =', np.max(X))
print('min  =', np.min(X))
print('median =', np.median(X))
print('25% =', np.percentile(X,25))
print('50% =', np.percentile(X,50))
print('75% =', np.percentile(X,75))
```


# 4. matplotlib

```python
# 여러 개의 그래프를 그리려면 subplot 부분을 조절하면 됩니다.
fig, ax = plt.subplots(nrows=2, ncols=3)

# title 을 추가합니다.
ax[0].set_title('1st')
ax[1].set_title('2nd')

# 첫번째 그래프의 x축과 y축에 이름을 더합니다.
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

# 두번째 그래프의 x축과 y축에 이름을 더합니다.
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')

# 첫번째 그래프에 출력할 점들을 변수에 저장하고 그립니다.
x1=[0,1,2]
y1=[0,1.5,2]
ax[0].plot(x1,y1)

# 두번째 그래프에 출력할 점들을 변수에 저장하고 그립니다.
x2=[0,1,2]
y2=[2,1.5,0]
ax[1].plot(x2,y2)

# 그림을 fig1.png 라는 파일로 저장합니다.
fig.savefig('fig1.png')
```

```python
stat_sb.histplot(df, x="tip", binwidth=1, bins=20)

# kernel, y축 기준
stat_sb.displot(df, y="tip",  kde=True, color='green')
```

```python
stat_sb.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=df)
```
![](resource/Pasted%20image%2020250105195633.png)

```python
stat_sb.relplot(data=df, x='total_bill', y='tip', hue='smoker', col='time')
```
![](resource/Pasted%20image%2020250105195741.png)

- line graph
```python
stat_sb.relplot(x="timepoint",y="signal", hue="event", style="event", dashes=False, markers=True, kind="line",data=fmri) # 색칠X errorbar=None

# row='event'
# col='region'
```


```python

import pandas as pd
import numpy as np
from IPython.display import Image

data = np.random.normal(0,1,size=(100,5))

data[:,0:3] = data[:,0:3] + 3
data[:,6:] = data[:,6:] - 3



colors = ['tab:red',
          'tab:brown',
          'tab:green',
          'tab:blue',
          'tab:purple']


plt.figure(figsize=(12,3))

for i, c in enumerate(colors):
    _ = plt.boxplot(data[:,i],                              # Data
                    labels=[c],                             # Label
                    positions=[i],                          # 박스플랏의 위치
                    widths = 0.5,                           # 폭
                    vert = True,       # 박스를 수식으로 그리도록 한다
                    patch_artist=True, # 박스의 속성을 바꿀 수 있도록 설정한다
                    boxprops=dict(facecolor=c, color='k'),  # 박스의 face와 가장자리 색을 지정
                    medianprops=dict(color='k')      # 중간값 선의 색 지정
                    )

_ = plt.xticks(rotation=60, fontsize=13)
_ = plt.yticks(fontsize=13)
_ = plt.ylabel("numbers", fontsize=13)

plt.grid(color='grey', linestyle='-',  axis='y')
```

![](resource/Pasted%20image%2020250105200311.png)

```python
# swarmplot - stripplot 보완
  

stat_sb.catplot(x='day',y='tip', hue="sex", kind="swarm", data=df)
```
![](resource/Pasted%20image%2020250105200412.png)

```python
# violinplot 그리기

  

stat_sb.catplot(x='day',y='tip', hue="sex", inner="stick", palette="pastel", kind="violin", split=True, data=df)

stat_sb.catplot(data=df, x='day', y='tip', hue='sex', kind='point')
```


```python
stat_sb.displot(penguins, x="flipper_length_mm", col="species")

# heatmap
stat_sb.displot(penguins, x="bill_length_mm", y="bill_depth_mm", cbar = True)

# 등고선
# kind="kde"

# cdf
# kind="ecdf"

```

```python
stat_sb.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
```

```python
stat_sb.pairplot(penguins)

gmap = stat_sb.PairGrid(penguins)
gmap.map_upper(stat_sb.histplot)
gmap.map_lower(stat_sb.kdeplot, fill=True)
gmap.map_diag(stat_sb.histplot, kde=True)
```


```python

stat_sb.lmplot(x="total_bill", y="tip", data=df, ci=None)

z = np.polyfit(x, y, 1)
y_hat = np.poly1d(z)(x)

```