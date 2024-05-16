from GUI.view import setup_gui
import logging

import matplotlib
# This must be done before importing pyplot or any part of Matplotlib that might load backends.
matplotlib.use('Agg')


# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logs/application.log',
                    filemode='a')


def main():
    setup_gui()
    logging.info("GUI Started...")


if __name__ == "__main__":
    main()
