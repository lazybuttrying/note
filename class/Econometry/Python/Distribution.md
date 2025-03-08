# 1. Binomial Distribution

```python
import matplotlib.pyplot as plt
from scipy.special import factorial, comb
from scipy.stats import binom
from numpy import arange
p = .5

plt.figure(figsize=(12, 8))

for n in arange(4, 41, 4):
    x = arange(n + 1)
    plt.plot(x, binom(n, p).pmf(x), 'o--', label='(n=' + str(n) + ')')

plt.xlabel('X')
plt.ylabel('P(X)')
plt.title('Binomial Distribution(p = .5)')
plt.grid()
plt.legend()
plt.show()
```
![](resource/Pasted%20image%2020250105194444.png)


# 2. Normal Distribution

```python
import matplotlib.pyplot as plt
from scipy.special import factorial, comb
from scipy.stats import binom
from numpy import arange, sqrt, pi, exp


plt.figure(figsize=(12, 8))

x = arange(-5,5,0.01)

def gaussian(x,mean,sigma):
  return (1/sqrt(2*pi*sigma**2))*exp(-(x-mean)**2/(2*sigma**2))

legend = []
for i in range(1,5):
    legend.append(f'N(0,{i})')
    plt.plot(x, gaussian(x,0,i), label='(sigma=' + str(i) + ')')

plt.xlabel('X')
plt.ylabel('density')
plt.title('Normal Distribution')
plt.grid()
plt.legend()
plt.show()
```

![](resource/Pasted%20image%2020250105194548.png)
# 3. Chi
```python
from scipy import stats
from numpy import linspace

nus = [1,2,3,4,5,10,20,30]

chi2 = linspace(0.5,50,100)

plt.figure(figsize=(12,8))

for nu in nus:
  plt.plot(chi2, stats.chi2(nu).pdf(chi2), label = 'nu=('+str(nu)+')')

plt.xlabel('X')
plt.ylabel('density')
plt.title('$\chi^2$ Distribution')
plt.grid()
plt.legend()
plt.show()
```

![](resource/Pasted%20image%2020250105194708.png)

standard normal distribution를 제곱한 걸로 카이스퀘어 분포
```python
num_samples = 10000
standard_normal_samples = np.random.normal(loc=0, scale=1, size=num_samples)


# Square the standard normal samples to create chi-square distribution
chi_square_samples = standard_normal_samples**2

# Plotting the chi-squared distribution from squared standard normal samples
plt.figure(figsize=(12, 8))
plt.hist(chi_square_samples, bins=50, density=True, alpha=0.6, color='b', label='Chi-square from squared standard normal')


# Overlay the theoretical chi-squared distribution for comparison (df = 1)
x = np.linspace(0, 10, 500)
plt.plot(x, stats.chi2.pdf(x, df=1), 'r-', lw=2, label='Theoretical Chi-square (df=1)')
```

![](resource/Pasted%20image%2020250105194854.png)


# 4. t
```python

import matplotlib.pyplot as plt
from scipy.special import factorial, comb
from scipy.stats import t
from numpy import arange, sqrt, pi, exp
from scipy import stats


plt.figure(figsize=(12, 8))

x = arange(-5,5,0.01)

def t_dist(nu):
  return stats.t(nu).pdf(x)

legend = []
for i in arange(10)+1:
    legend.append(f't({i})')
    plt.plot(x, t_dist(i), label='(nu=' + str(i) + ')')

plt.xlabel('X')
plt.ylabel('density')
plt.title('t Distribution')
plt.grid()
plt.legend()
plt.show()
```

![](resource/Pasted%20image%2020250105194939.png)

# 5. F
```python
from scipy import stats

from numpy import linspace

from scipy.stats import f

nu1s = [1,5,10,50,100]
nu2s = nu1s

x = linspace(0,5,201)

plt.figure(figsize=(12,8))
for nut in nu1s:
    # for nu in nu2s:
    nu = 100
#        plt.plot(x,stats.f(nu1s[1],nu).pdf(x), label = 'F('+str(nu1s[1])+', '+ str(nu)+')')
    plt.plot(x,stats.f(nut,nu).pdf(x), label = 'F('+str(nut)+', '+ str(nu)+')')
```

![](resource/Pasted%20image%2020250105195128.png)
![](resource/Pasted%20image%2020250105195201.png)
![](resource/Pasted%20image%2020250105195318.png)
```python
# prompt: chil square 분포 2개로 f 분포를 만드는 예제 코드

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2, f

# Parameters for the two chi-square distributions
df1 = 5  # Degrees of freedom for the first chi-square distribution
df2 = 10 # Degrees of freedom for the second chi-square distribution

# Generate random samples from the chi-square distributions
num_samples = 10000
chi2_samples1 = np.random.chisquare(df1, num_samples)
chi2_samples2 = np.random.chisquare(df2, num_samples)

# Calculate the F-distribution samples
f_samples = (chi2_samples1 / df1) / (chi2_samples2 / df2)


# Plotting the F-distribution from the two chi-square distributions
plt.figure(figsize=(12, 8))
plt.hist(f_samples, bins=50, density=True, alpha=0.6, color='b', label='F-distribution from chi-square samples')

# Overlay the theoretical F-distribution for comparison
x = np.linspace(0, 5, 500)  # Adjust the range as needed
plt.plot(x, f.pdf(x, df1, df2), 'r-', lw=2, label='Theoretical F-distribution (df1={}, df2={})'.format(df1, df2))


```