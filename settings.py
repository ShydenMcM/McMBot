"""Functions to support configuration amongst environments"""
import os
import pathlib
from logging.config import dictConfig

import discord
from dotenv import load_dotenv


class Config:
    """Class to get any environment variable passed in"""

    def __init__(self):
        pass

    def __getattr__(self, attr):
        variable = os.getenv(attr)
        if variable == "":
            return None
        return variable

    def load(self):
        """Load the environment variable value"""
        load_dotenv(override=True)
        return self


BASE_DIR = pathlib.Path(__file__).parent

COMMANDS_DIR = BASE_DIR / "commands"
COGS_DIR = BASE_DIR / "cogs"

LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard": {"format": "%(levelname)-10s - %(name)-15s : %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "console2": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "bot": {"handlers": ["console"], "level": "INFO", "propagate": False},
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

dictConfig(LOGGING_CONFIG)
