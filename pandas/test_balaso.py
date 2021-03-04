a = 'AB:'
b = [1, 2]
c = ':CD'

join_str = a + " " + " ".join(map(str, b)) + " " + c
split_str = join_str.split()
print(split_str)
lst = split_str[1:-1]
print(lst)
