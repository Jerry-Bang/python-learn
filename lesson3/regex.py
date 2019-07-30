import re

reg_exp = r"(\(.*\))|[A-Za-z0-9._-]+"

rc = re.compile(reg_exp)


def search_all(f):
    pos = 0
    rlt = []
    while pos < len(f):
        x = rc.search(f, pos)
        if x:
            rlt.append(x.group())
            pos = x.end()
        else:
            break

    return rlt


if __name__ == "__main__":
    s = '  apple and (orange or banana ) '
    result = search_all(s)
    print(result)
