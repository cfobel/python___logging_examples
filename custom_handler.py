import logging
import logging.handlers


class CustomHandler(logging.Handler):
    def __init__(self):
        # run the regular Handler __init__
        logging.Handler.__init__(self)

    def emit(self, record):
        print record.levelname, record.levelno


if __name__ == '__main__':
    # Create a logging object (after configuring logging)
    logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.WARNING)
    logger = logging.getLogger()

    logger.addHandler(CustomHandler())

    # And finally a test
    logger.debug('Test 1')
    logger.info('Test 2')
    logger.warning('Test 3')
    logger.error('Test 4')
    logger.critical('Test 5')
