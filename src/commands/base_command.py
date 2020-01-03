# -*- coding: utf-8 -*-
import logging

from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from helpers import mysql_connection_string


class BaseCommand(ScrapyCommand):
    def __init__(self, logger=None):
        super().__init__()
        self.settings = get_project_settings()

        self.engine = create_engine(mysql_connection_string())
        self.session = Session(self.engine)

        self.logger = logger or logging.getLogger(name=__name__)

    def set_logger(self, name="COMMAND", level="DEBUG"):
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(level)
