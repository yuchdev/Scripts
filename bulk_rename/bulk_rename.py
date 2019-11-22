import os
import sys
import re
import argparse
import logging
import log_helper


logger = log_helper.setup_logger(name="bulk_rename", level=logging.DEBUG, log_to_file=False)


class BulkRemove:

    def __init__(self, input_dir, regexp):
        self.regexp = regexp
        self.input_dir = input_dir
        logger.info(self.input_dir)

    def remove(self):
        """
        Remove files start with "._"
        """
        for root, _, files in os.walk(self.input_dir):
            filename = os.path.join(root, files)
            if filename.startswith("._"):
                logger.info(filename)


def main():
    """
    Perform backup or unpacking
    :return: Archiver system return code
    """
    parser = argparse.ArgumentParser(description='Command-line interface')
    parser.add_argument('--input-dir',
                        help='Directory to process',
                        dest='input_dir',
                        metavar='DIR',
                        required=True)

    parser.add_argument('--rename',
                        help='Regular expression to filter files',
                        dest='regexp',
                        required=False)

    args = parser.parse_args()

    input_dir = os.path.abspath(args.input_dir)
    logger.info("Input directory: %s" % input_dir)

    # Input (backup source dir) check
    if not os.path.exists(input_dir):
        logger.warning("Source directory '{0}' does not exist".format(input_dir))
        return 1

    file_processor = BulkRemove(input_dir=input_dir, regexp=args.regexp)
    file_processor.remove()

    return 0


###########################################################################
if __name__ == '__main__':
    sys.exit(main())