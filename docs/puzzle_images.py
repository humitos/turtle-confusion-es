import glob

CONTENT_FILE = '''Puzzle %s
=========

.. image:: _static/images/confusion-%s.svg
   :height: 300px
   :width: 300px
   :scale: 50 %%
   :alt: Puzzle %s
   :align: left
'''

PUZZLE_RST_FILES = glob.glob('puzzle-*.rst')

for f in PUZZLE_RST_FILES:
    fopen = open(f, 'w')
    nro = int(f.split('-')[1].split('.')[0])
    
    fopen.write(CONTENT_FILE % (nro, nro, nro))
    fopen.close()

