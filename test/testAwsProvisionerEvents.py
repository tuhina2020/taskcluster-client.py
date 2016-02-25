#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import AwsProvisionerEvents


class FakeAwsProvisionerEvents(FakeGenerated, AwsProvisionerEvents):
    pass


class TestAwsProvisionerEvents(GeneratedTC):
    """Test the generated TestAwsProvisionerEvents class.
    """
    testClass = FakeAwsProvisionerEvents

    def test_urls(self):
        """TestAwsProvisionerEvents | all urls match the json baseUrls
        """
        self.url_check('AwsProvisionerEvents')

    def test_routingKeys(self):
        """TestAwsProvisionerEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('AwsProvisionerEvents')

    def test_workerTypeCreated(self):
        """TestAwsProvisionerEvents | AwsProvisionerEvents.workerTypeCreated topic exchange
        """
        self.try_topic('workerTypeCreated', 'worker-type-created')

    def test_workerTypeUpdated(self):
        """TestAwsProvisionerEvents | AwsProvisionerEvents.workerTypeUpdated topic exchange
        """
        self.try_topic('workerTypeUpdated', 'worker-type-updated')

    def test_workerTypeRemoved(self):
        """TestAwsProvisionerEvents | AwsProvisionerEvents.workerTypeRemoved topic exchange
        """
        self.try_topic('workerTypeRemoved', 'worker-type-removed')
