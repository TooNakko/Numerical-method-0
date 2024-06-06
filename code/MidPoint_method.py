import numpy as np
from numpy import cos, sqrt


def f(x):
    return sqrt(x - x**2)

# Get L_K
def get_L(x, x_data, k=0, eps=1e-6):
    numerator = np.cumprod([x - xi for xi in x_data if xi != x_data[k]])[-1]
    denominator = np.cumprod([x_data[k] - xi for xi in x_data if xi != x_data[k]])[-1]
    return numerator/(denominator + eps)

x = 0.5 # diem x can uoc luong cua f

D = 10
No = 10000  # so lan doan x1
largest_x1 = -1
eps = 1e-4 # sai so trong khoang [-0.25 - eps, -0.25 + eps]

for _ in range(No):
  x1 = np.random.random() # du doan x1 trong khoang 0, 1
  x_data = np.array([0, x1, 1])

  # Neu de cho san f(x) thi tinh ntn
  px = np.cumsum([f(x_data[k])*get_L(x, x_data, k = k) for k in range(len(x_data))])[-1]  # ket qua
  error = f(x) - px
  if -0.25 - eps <= f(x) - px and f(x) - px <= -0.25 + eps and largest_x1 < x:
    largest_x1 = x1

# tinh toan sai so voi largest_x1
x_data = np.array([0, largest_x1, 1])

# Neu de cho san f(x) thi tinh ntn
px = np.cumsum([f(x_data[k])*get_L(x, x_data, k = k) for k in range(len(x_data))])[-1]  # ket qua
print("largest x1 =", np.round(largest_x1, D))
print("Sai so     =", abs(0.25 + f(0.5) - px))

# Neu chay cau nay k duoc thi chay lai chay den khi nao ra largest_x1 ~ 0.873 thi thoi vi
# tinh ngau nhien co the se bi loi