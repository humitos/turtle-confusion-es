import glob
import shutil


for x in glob.glob('docs/puzzle-*.rst'):
    f = open(x, 'r')
    fw = open('/tmp/hash.txt', 'w')
    l1 = f.readlines()[0]
    l1 = l1.replace('Puzzle', 'Figura')
    l1 = l1.upper()
    f.seek(0)
    lines = [l1] + f.readlines()[1:]
    fw.write(''.join(lines))
    fw.close()
    f.close()
    shutil.copy('/tmp/hash.txt', x)
