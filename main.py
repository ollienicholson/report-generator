import logging
from GUI.view import setup_gui

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='application.log',
                    filemode='a')


def main():
    setup_gui()
    logging.info("GUI Started...")


if __name__ == "__main__":
    main()
