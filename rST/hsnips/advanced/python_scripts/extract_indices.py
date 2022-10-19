"""
extract all parent folders' basenames of a given file,
and these extracted strings are used as index of a rst doc. 
"""
from lib2to3.pgen2.token import RPAR
import os
from pathlib import Path
import sys


def indicesOfFile(entrance: os.PathLike) -> str:
    """
    extract parent folders of a rst doc which is part of a sphinx project.

    Parameters
    ----------
    entrance : os.PathLike
        a rst doc file or a folder

    Returns
    -------
    str
        use ',' to concatenate all parent folder names, and stops when there is a 'conf.py' who indicates this is the beginning of the source docs.
    """
    indices = []
    entrance = Path(entrance)
    
    parent = entrance.parent
    while True:
        ls = os.listdir(parent)
        if 'conf.py' in ls or parent.name == '':
            break
        if 'index.rst' in ls:
            idx = parent.name
            if idx not in indices:
                indices.insert(0, idx)
        parent = parent.parent
    if indices == []:
        # 如果不符合上述所有条件时，给予一些failsafe的值
        indices = f'Uncataloged,Individual,{entrance.parent.stem},{entrance.stem}'
    else:
        indices = ','.join(indices)
    return indices


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(indicesOfFile(sys.argv[1]))
    else:
        f = '.'
        print(indicesOfFile(f) + ',!@#FAILSAFE MODE DETECTED#@!')
