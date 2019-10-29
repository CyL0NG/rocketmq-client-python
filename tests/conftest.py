# -*- coding: utf-8 -*-
import pytest
from rocketmq.client import Producer, PushConsumer, TransactionMQProducer


# HACK: It's buggy, don't call it in test case for now
del PushConsumer.__del__
del Producer.__del__


@pytest.fixture(scope='session')
def producer():
    prod = Producer('testGroup')
    prod.set_namesrv_addr('127.0.0.1:9876')
    prod.start()
    yield prod
    prod.shutdown()


@pytest.fixture(scope='function')
def push_consumer():
    consumer = PushConsumer('testGroup')
    consumer.set_namesrv_addr('127.0.0.1:9876')
    yield consumer
    consumer.shutdown()


@pytest.fixture(scope='session')
def transactionProducer():
    prod = TransactionMQProducer('testGroup')
    prod.set_namesrv_addr('127.0.0.1:9876')
    prod.start()
    yield prod
    prod.shutdown()