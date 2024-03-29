import re


class Person:
    def __init__(self, gender, imt, smoke):
        self.gender = gender
        self.imt = imt
        self.smoke = smoke


def read_file(name):
    try:
        f = open(name, 'r')
        lines = f.readlines()
        people = []
    except FileExistsError:
        print("File not exists")
        return None
    except FileNotFoundError:
        print("File not found")
        return None
    for i in range(0, len(lines)):
        try:
            line = lines[i].strip('\n')
            line = line.replace('\"', '')
            gender = line.split(',')[0]
            gender = "M" if re.match("[male]", gender) else "F" if re.match("[female]", gender) else ValueError
            imt = float(line.split(',')[1])
            smoke = True if re.match("yes", line.split(',')[2]) else False
            p = Person(gender, imt, smoke)
        except Exception:
            print("Reading for line {} failed, used null-object.".format(i))
            p = Person('M', 1.0, False)
        people.append(p)
    print("")
    return people
