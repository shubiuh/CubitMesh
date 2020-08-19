import setup

setup.start()

import cubit
cubit.init([''])

# two volumes separating 134000x134000x60000 block horizontally
cubit.cmd('reset')
cubit.cmd('brick x 67000 y 134000 z 60000')
cubit.cmd('volume 1 move x 33500 y 67000 z -30000')
cubit.cmd('brick x 67000 y 134000 z 60000')
cubit.cmd('volume 2 move x 100500 y 67000 z -30000')
cubit.cmd('merge all')

# Meshing the volumes
elementsize = 3750.0

cubit.cmd('volume 1 size '+str(elementsize))
cubit.cmd('volume 2 size '+str(elementsize))
cubit.cmd('mesh volume 1 2')


#### End of meshing

cubit.cmd('export mesh "top.e" dimension 3 overwrite')
cubit.cmd('save as "meshing.cub" overwrite')

cubit.destroy()

def deleteJournalFiles(path='.', fileName='cubit*.jou'):
    """ Delete all Cubit journal files in specified folder
    :param path: path to  search
    :param fileName: glob file name to delete
    :return:
    """
    import glob
    import os

    filelist = glob.glob(path + '/{0}'.format(fileName))
    for f in filelist:
        os.remove(f)

deleteJournalFiles()