import math
import matplotlib.pyplot as plt
import numpy.random

import generation as gn
import task_2 as tk_2
import pandas as pd
import seaborn as sns


def selective_math_await(nums):
    _sum = 0
    for i in nums:
        _sum += i
    return _sum / len(nums)


def dispersion(nums):
    _sum = 0
    _maw = selective_math_await(nums)
    for i in nums:
        _sum += (i - _maw) ** 2
    return _sum / len(nums)


def selective_dispersion(nums):
    _sum = 0
    _maw = selective_math_await(nums)
    for i in nums:
        _sum += (i - _maw) ** 2
    mv = 1 / (len(nums) - 1)
    return mv * _sum


def std_deviation(nums):
    return math.sqrt(dispersion(nums))


def selective_median(nums, order):
    srt_nums = sorted(nums)
    return srt_nums[int(len(srt_nums) * order)]


def histogram(nums, d_gamma, d_expon):
    gamma = gn.gamma_sample(len(nums))
    expon = gn.exponential_sample(len(nums))
    plt.hist(nums, color='orange', bins=int(100), alpha=0.5, label='Generated values')
    if d_gamma:
        plt.hist(gamma, color='blue', bins=int(100), alpha=0.5, label='Gamma')
    if d_expon:
        plt.hist(expon, color='green', bins=int(100), alpha=0.5, label='Exponential')

    plt.legend(loc='upper right', prop={'size': 12})

    plt.title('Histogram')
    plt.xlabel('values')
    plt.ylabel('amount')
    plt.show()


def sample_cha(nums):
    order = 0.5
    print("Выборочное математическое ожидание:", selective_math_await(nums))
    print("Выборочная дисперсия:", selective_dispersion(nums))
    print("Стандартное отклонение:", std_deviation(nums))
    print("Выборочный квантиль порядка {}:".format(order), selective_median(nums, order))
    histogram(nums, True, True)


def t2hgr(nums, name):
    plt.hist(nums, color='orange', bins=int(100), alpha=0.5, label=name)

    plt.legend(loc='upper left', prop={'size': 10})

    plt.title('Histogram')
    plt.xlabel('values')
    plt.ylabel('amount')
    plt.show()


def t2epr(nums, title, xlbl):
    srt_nums = sorted(nums)
    emp_vals = []
    emp_nums = []
    c = 1
    prev = nums[0]
    for i in range(1, len(srt_nums)):
        if not srt_nums[i] == prev:
            emp_nums.append(c)
            c = 1
        else:
            c += 1
        prev = srt_nums[i]
    sum = 0
    func_rsp = []
    c = 0
    for i in emp_nums:
        func_rsp.append(sum/len(nums))
        sum += emp_nums[i]
        c += 1
        emp_vals.append(c)
    # print(emp_vals)
    # print(func_rsp)
    plt.plot(emp_vals, func_rsp)
    plt.title(title)
    plt.xlabel(xlbl)
    plt.ylabel("Функция распределения")
    plt.show()


def t2gr(smk_all, nsmk_m, nsmk_f, smk_f, smk_m):
    data = pd.DataFrame({'Все': smk_all,
                         'Мужчины курят': smk_m,
                         'Мужчины не курят': nsmk_m,
                         'Женщины курят': smk_f,
                         'Женщины не курят': nsmk_f})
    data.head()
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data)
    plt.xticks(fontsize=8)
    plt.ylabel('ИМТ, что-то', fontsize=16)
    plt.title('Box-plot', fontsize=17)

    plt.show()


def t2pr(comment, nums):
    order = 3 / 5
    print(comment)
    print("Всего {}.".format(len(nums)))
    print("Выборочное математическое ожидание:", selective_math_await(nums))
    print("Выборочная дисперсия:", selective_dispersion(nums))
    print("Выборочная медиана:", selective_median(nums, 0.5))
    print("Выборочный квантиль порядка {}:".format(order), selective_median(nums, order))
    print("")


def t2wr():
    people = tk_2.read_file("sex_bmi_smokers.csv")
    smk_all, nsmk_m, nsmk_f, smk_f, smk_m = [], [], [], [], []

    for i in people:
        smk_all.append(i.imt)
        if i.gender == 'M' and i.smoke:
            smk_m.append(i.imt)
            continue
        if i.gender == 'F' and i.smoke:
            smk_f.append(i.imt)
            continue
        if i.gender == 'M' and not i.smoke:
            nsmk_m.append(i.imt)
            continue
        if i.gender == 'F' and not i.smoke:
            nsmk_f.append(i.imt)

    # print(smk_f, smk_m, nsmk_f, nsmk_m)

    print("Курит мужчин: {}. Женщин не курит: {}\n".format(len(smk_m), len(nsmk_f)))
    t2pr("Общая выборка:", smk_all)
    t2pr("Не курящие мужчины:", nsmk_m)
    t2pr("Не курящие женщины:", nsmk_f)
    t2pr("Курящие мужчины:", smk_m)
    t2pr("Курящие женщины:", smk_f)

    lng = int(min(len(smk_all), len(nsmk_m), len(nsmk_f), len(smk_f), len(smk_m)))
    smk_all = smk_all[1:lng]
    nsmk_m = nsmk_m[1:lng]
    nsmk_f = nsmk_f[1:lng]
    smk_f = smk_f[1:lng]
    smk_m = smk_m[1:lng]

    # print(len(smk_all), len(nsmk_m), len(nsmk_f), len(smk_f), len(smk_m))

    # t2hgr(smk_all, nsmk_m, nsmk_f, smk_f, smk_m)
    t2gr(smk_all, nsmk_m, nsmk_f, smk_f, smk_m)

    t2hgr(smk_all, "Общая выборка")
    t2hgr(nsmk_m,  "Не курящие мужчины")
    t2hgr(nsmk_f,  "Не курящие женщины")
    t2hgr(smk_m,  "Курящие мужчины")
    t2hgr(smk_f, "Курящие женщины")

    t2epr(smk_all, "Распределение имт", "Общая выборка")
    t2epr(nsmk_m, "Распределение имт", "Не курящие мужчины")
    t2epr(nsmk_f, "Распределение имт", "Не курящие женщины")
    t2epr(smk_m, "Распределение имт", "Курящие мужчины")
    t2epr(smk_f, "Распределение имт", "Курящие женщины")


def normal_dev(x, m_await, deviat):
    return (1/(deviat * math.sqrt(2 * math.pi))) * (math.e ** (-1/2 * ((x - m_await)/deviat)**2))


if __name__ == '__main__':
    print("Задание #1\n")
    row_2 = []
    row_n = []
    k = 100000
    n = 10000
    for _ in range(1, k):

        row = gn.normal_sample(100, 5, n)
        row_2.append(n*normal_dev(row[1], 100, 5))
        row_n.append(n*(1 - normal_dev(row[n-1], 100, 5)))
    sample_cha(row_2)
    print("")
    sample_cha(row_n)

    print("Задание #2\n")
    # gn.file_csv("data.csv", 200000)
    t2wr()
