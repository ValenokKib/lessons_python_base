my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, j in enumerate(my_list):
    if j.replace("+", "").isdigit():
        if j.isdigit():
            my_list[i] = '"{:02d}"'.format(int(j))
        else:
            my_list[i] = '"{}{:02d}"'.format((j[0]), int(j[-1]))
print(my_list)
print(" ".join(my_list))
