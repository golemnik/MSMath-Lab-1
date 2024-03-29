import numpy


def random_sample(minn, maxx, n):
    return numpy.random.uniform(minn, maxx, n)


def normal_sample(math_await, std_deviation, n):
    return numpy.random.normal(math_await, std_deviation, n)


def gamma_sample(n):
    return numpy.random.gamma(2, 1, n)


def exponential_sample(n):
    return numpy.random.exponential(1, n)


def file_csv(name, n):
    with open(name, 'w') as file:
        imts = numpy.random.normal(100, 20, n)
        for i in range(0, n):
            # print(numpy.random.randint(0, 2))
            gender = "M," if numpy.random.randint(0, 2) == 1 else "F,"
            smoke = ",True" if numpy.random.randint(0, 2) == 1 else ",False"
            imt = str(imts[i])
            # imt = str(numpy.random.uniform(1, 100, 1)[0])
            line = gender + imt + smoke + '\n'
            file.write(line)
