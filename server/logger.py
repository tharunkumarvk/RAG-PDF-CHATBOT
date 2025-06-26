import logging

def setup_logger(name="RagBot"):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    #Console handler

    ch=logging.StreamHandler() #send to command line all the logs
    ch.setLevel(logging.DEBUG)

    #format

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    #handling duplicate logs

    if not logger.hasHandlers():
        logger.addHandler(ch)

    return logger











logger=setup_logger()