import time
import logging

logger = logging.getLogger(__name__)


def timer(func):
    """
    A decorator that measures and logs the time taken by any function it wraps.

    Parameters:
        func (function): The function to measure and log.

    Returns:
        function: A wrapper function that logs execution time and any exceptions, before calling the original function.
    """
    def timed_function(*args, **kwargs):
        function_name = func.__name__
        start_time = time.time()

        try:
            result = func(*args, **kwargs)
            elapsed_time = time.time() - start_time

            timer_message_success = str(f"{function_name} executed in {elapsed_time:.4f} seconds")
            logger.info(timer_message_success)
            print(timer_message_success)

            return result

        except Exception as e:
            elapsed_time = time.time() - start_time

            timer_error_message = str(f"Error in {function_name} after {elapsed_time:.4f} seconds: {str(e)}")
            logger.error(timer_error_message)
            print(timer_error_message)
            raise

    return timed_function
