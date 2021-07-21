import logging

import pytest

import log_set

def test_logging(caplog):
    root_logger = logging.getLogger()
    text = "Test"
    root_logger.info(text)
    assert text in caplog.records[-1].message
    assert caplog.records[-1].levelno  == logging.INFO
