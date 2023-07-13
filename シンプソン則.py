import decimal
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return decimal.Decimal(np.exp(x))  # 積分に使用する関数1

def f2(x):
    return decimal.Decimal(np.cos(float(x)))  # 積分に使用する関数2

def xi(i, xs, xe, ndiv):
    return xs * (ndiv - i) / ndiv + xe * i / ndiv

def calculate_integral(f, a, b, digits):
    decimal.getcontext().prec = digits + 2  # 2桁余分に計算する
    decimal.getcontext().Emax = 999999999  # エラーハンドリングを無効にする

    a = decimal.Decimal(str(a))
    b = decimal.Decimal(str(b))
    N = digits + 1  # シンプソン則の分割数

    total = decimal.Decimal(0)
    for i in range(N):
        xs = xi(i, a, b, N)
        xe = xi(i + 1, a, b, N)
        fs = f(xs)
        fm = f((xs + xe) / 2)
        fe = f(xe)
        term = (xe - xs) / 6 * (fs + 4 * fm + fe)
        total += term

    integral = str(total)[0:digits]  # 指定した桁数までの部分文字列を取得

    return integral

# 区間 [0, 2] の exp(x) の積分値を求める（先頭から10桁まで）
a = 0
b = 2
digits = 10
integral_exp = calculate_integral(f1, a, b, digits)
print("exp(x)の積分値:", integral_exp)

# 区間 [0, 2] の cos(x) の積分値を求める（先頭から10桁まで）
integral_cos = calculate_integral(f2, a, b, digits)
print("cos(x)の積分値:", integral_cos)

# グラフの描画
a_float = float(decimal.Decimal(str(a)))
b_float = float(decimal.Decimal(str(b)))
x = np.linspace(a_float, b_float, 1000)
y_exp = np.exp(x)
y_cos = np.cos(x)

plt.plot(x, y_exp, label="f(x) = exp(x)")
plt.plot(x, y_cos, label="f(x) = cos(x)")

plt.fill_between(x, y_exp, alpha=0.3, label="Integral (exp(x))")
plt.fill_between(x, y_cos, alpha=0.3, label="Integral (cos(x))")
plt.title("Simpson's Rule")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()

input("[Enter]キーを押して終了")