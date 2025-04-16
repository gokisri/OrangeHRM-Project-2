import logging

class LogGen:  # ⚠️ If this is the actual class name, fix your import!
    @staticmethod
    def loggen():
        logging.basicConfig(
            filename=".\\logs\\automation.log",
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
