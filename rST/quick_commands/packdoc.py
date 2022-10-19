"""
Move a rst doc to a sub-directory which is named after the rst-doc's
filename, and make a media dir.
I call this combo-operation 'packing'.

usage:

    python packdoc.py xxx.rst

the doc will be moved to a sub-directory 'xxx'

deprecated feature : a 'media' dir will be created aside the doc

and open the doc in vscode.

"""

from functools import cached_property
from p_lib import Path, sys, call, shutil, sleep, os
import logging

logging.basicConfig(
    # filename='logging.log',
    level=logging.DEBUG,
    filemode='a',
    encoding='utf8',
    format='%(asctime)s - %(filename)s, line:%(lineno)d > %(levelname)s: %(message)s',
)


class RstPack():
    def __init__(self, kw: str, open_it: bool = False):
        wd = Path('.')
        self.kw = kw.removesuffix('.rst') # Don't use strip here!!!
        self.dir = wd / self.kw
        self.file_1 = wd / f'{kw}.rst'
        self.file_2 = self.dir / self.file_1
        self.open_it = open_it
        self.packIt()

    def packIt(self):
        """
        Move the file to a same-named dir.
        I call this operation 'packing'.
        And, this is a Hybrid script, which means:
            - It could do the task that batch moves all unpacked files to a packing style(in a same-named sub-dir);
            - or, if the file and the sub-folder don't exist, make a new one.
        So if you feel the logic of the codes is a little weird, don't worry, it's just by design.

        Parameters
        ----------
        file : os.PathLike
            rst file to move
        """

        try:
            os.makedirs(self.dir, exist_ok=False)
        except:
            logging.warning('Pack-sub-dir already exists, skip the creation of dir.')

        if not self.file_1.exists() and not self.file_2.exists():
            logging.info('creating empty file...')
            self.file_2.touch()
        elif self.file_1.exists():
            logging.warning('An outter file exists, now try to move it to the packing/inner dir.')
            if not self.file_2.exists():
                shutil.move(os.path.abspath(self.file_1), os.path.abspath(self.file_2))
            else:
                logging.error(f'File conflicts! Please manually check them:\n{self.file_1.absolute()}\nv.s\n{self.file_2.absolute()}')
                return
        else:
            logging.warning('File exists, skip the creation of file.')

        if self.open_it == True:
            logging.info(f'Open the file in vscode...')
            # in Windows if error occurs, set 'shell' to True
            call(['code', self.file_2.absolute()], shell=True if sys.platform == 'win32' else False)
        logging.info(f'Packing done. new location {self.file_2}')


if __name__ == "__main__":
    kw = sys.argv[1]
    print(kw)
    RstPack(kw, open_it=True)
