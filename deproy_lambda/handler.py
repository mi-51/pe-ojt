import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def output_log(event, context):
    logging.info("おはよう")
