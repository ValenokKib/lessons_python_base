from collections import defaultdict
import os
import django

def stat_dir():
    my_dir = django.__path__[0]
    my_dir_files = defaultdict(int)
    for root, dirs, files in os.walk(my_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            my_dir_files += 1

    for size, count in sorted(my_dir_files.items()):
        print('{}: {}'.format(size, count))
