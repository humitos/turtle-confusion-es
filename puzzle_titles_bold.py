import glob
import shutil


for x in glob.glob('docs/puzzle-*.rst'):
    f = open(x, 'r')
    fw = open('/tmp/hash.txt', 'w')
    lines = f.readlines()
    l1, l2 = lines[0], lines[1]
    l1 = '**' + l1.replace('\n', '') + '**' + '\n'
    l2 = '====' + l2
    f.seek(0)
    lines = [l1, l2] + f.readlines()[2:]
    fw.write(''.join(lines))
    fw.close()
    f.close()
    shutil.copy('/tmp/hash.txt', x)

