import os
import logging


def setup_logging(logfile_path: str):
    """
    Set up logging configuration to append messages to a log file.
    :param logfile_path: Path to the logfile relative to the current directory.
    :return: None
    """
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
    full_path = os.path.join(project_root, logfile_path)

    log_dir = os.path.dirname(full_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)  # Create the log directory if it doesn't exist

    # Use 'a' to append to the existing log file
    logging.basicConfig(
        filename=full_path,  # Should use full_path to ensure the correct file location
        filemode='a',  # Append to the existing file
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)
    logger.debug("Logging setup complete.")
