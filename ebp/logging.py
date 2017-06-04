import logging


logging.basicConfig()

_verbose = False


def get_logger(name, verbose=False):
    global _verbose

    logger = logging.getLogger(name)
    if verbose:
        _verbose = True
    if _verbose:
        logger.setLevel('DEBUG')

    return logger
