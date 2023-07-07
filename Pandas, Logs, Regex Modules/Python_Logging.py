import logging

# Configure the logging settings
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Log messages with different severity levels
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


# Capture exceptions and log error tracebacks
try:
    result = 10 / 0
except Exception as e:
    logging.error('An error occurred: %s', str(e))

# Log messages to a file
file_handler = logging.FileHandler('err.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
logging.getLogger('').addHandler(file_handler)

logging.info('This message will be logged to a file')