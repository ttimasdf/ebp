from . import logging
from pathlib import Path
import mmap


log = logging.get_logger(__name__)

class Patcher(object):
    """Initialize essential information"""
    def __init__(self, meta, basedir='.', test=False):
        assert isinstance(meta, dict)
        self.__dict__.update(meta)
        self.test = test
        self.file = Path(basedir)/self.file

        self.open()


    def open(self):
        self._fobj = self.file.open('r+b')
        log.info("Opening file {}".format(self.file.name))
        self._map = mmap.mmap(self._fobj.fileno(), 0)
        log.debug("File size {}".format(self._map.size()))


    def close(self):
        self._map.flush()
        self._map.close()
        self._fobj.close()
        log.debug("{} patched successfully!".format(self.file))


    def patch(self):
        if self.relatives:
            self.relative_patch()
        if self.absolutes:
            self.absolute_patch()
        self.close()


    def relative_patch(self):
        i = 0
        for item in self.relatives:
            i += 1
            log.debug("Replacing target {}..".format(i))

            anchor = self._map.find(item['src'])
            while anchor > 0:
                log.debug("Found src at position {}".format(anchor))
                j = 0
                for pos, fg in item['fg']:
                    j += 1
                    target = anchor + pos
                    if self._map[target:target+len(fg)] == fg:
                        log.debug("Fingerprint {} match!".format(j))
                        match = True
                    else:
                        log.debug("Fingerprint {} unmatch! {:X} => {:X}".format(j, fg, self._map[target:target+len(fg)]))
                        match = False
                        break
                if match:
                    if self.test:
                        log.debug("Patch {} located at position {}".format(i,anchor))
                    else:
                        log.debug("Patching bytes at position {}".format(anchor))
                        self._map[anchor:anchor+len(item['dst'])] = item['dst']
                    break
                anchor = self._map.find(item['src'], anchor+1)

    def absolute_patch(self):
        log.error("NotImplemented: absolute_patch")


