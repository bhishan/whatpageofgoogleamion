from django.test import TestCase
class WhatpageofsearchamionTest(TestCase):
def test_entered_the_whatpageofsearchamion(self):
response = self.client.get('/')
self.assertContains(response, "I've entered the Codeship")
def test_leads_to_the_whatpageofsearchamion(self):
response = self.client.get('/')
self.assertContains(response, '<a href="http://www.thetaranights.com">')
