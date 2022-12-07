import os

file = open("inputFiles/q7Input.txt", 'r')
data = file.read().strip().split('\n')

dirs = {}
dir_dict_size = {}

for line in data:
    if line[0] == '$':
        cmd, *ddir = line.split()[1:]
        if cmd == 'cd':
            path = ddir[0]
            if path == '/':
                pwd = path
            else:
                pwd = os.path.normpath(os.path.join(pwd, path))
            if pwd not in dirs:
                dirs[pwd] = []
                dir_dict_size[pwd] = 0
    else:
        filesize, filename = line.split()
        if filesize != 'dir':
            dir_dict_size[pwd] += int(filesize)
        else:
            dirs[pwd].append(os.path.normpath(
                os.path.join(pwd, filename)))


def getDirSize(dirname):
    dirsize = dir_dict_size[dirname]
    for f in dirs[dirname]:
        if f in dirs:
            dirsize += getDirSize(f)
    return dirsize


pt1 = 0
for f in dirs:
    dirsize = getDirSize(f)
    if dirsize <= 100000:
        pt1 += dirsize

print("Day 7 => The answer to part 1 is: " + str(pt1))

tot_space = 70000000
reqd_space = 30000000
used_space = getDirSize('/')

delete_directory = tot_space
for f in dir_dict_size:
    dirsize = getDirSize(f)
    if (dirsize >= reqd_space - (tot_space - used_space)) and (dirsize <= delete_directory):
        delete_directory = dirsize

print("Day 7 => The answer to part 2 is: " + str(delete_directory))

file.close()
