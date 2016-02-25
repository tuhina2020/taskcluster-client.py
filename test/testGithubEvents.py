#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is generated!  Do not edit!
from __future__ import absolute_import, division, print_function

from base import FakeGenerated, GeneratedTC
from taskcluster.sync import GithubEvents


class FakeGithubEvents(FakeGenerated, GithubEvents):
    pass


class TestGithubEvents(GeneratedTC):
    """Test the generated TestGithubEvents class.
    """
    testClass = FakeGithubEvents

    def test_urls(self):
        """TestGithubEvents | all urls match the json baseUrls
        """
        self.url_check('GithubEvents')

    def test_routingKeys(self):
        """TestGithubEvents | all routingKeys match the json routingKeys
        """
        self.routingKeys_check('GithubEvents')

    def test_pullRequest(self):
        """TestGithubEvents | GithubEvents.pullRequest topic exchange
        """
        self.try_topic('pullRequest', 'pull-request')

    def test_push(self):
        """TestGithubEvents | GithubEvents.push topic exchange
        """
        self.try_topic('push', 'push')
