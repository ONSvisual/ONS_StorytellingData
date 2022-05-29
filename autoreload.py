# conda install -c wolfiex ipyreload
import ipyReload as ipr
import glob,os

module = 'storytelling'

def callbackfn():
    print ('rerun')
    # to run another file use :
    # ipython.magic(f"run -m {module}")
    os.system(f'python -m {module}')


for f in glob.glob(f'{module}/*.py'):
    ipr.watch( f , callbackfn)
