"""
test_clippy.py - Testing the clippy thingy
"""

from django.test.client import Client
from lettuce import before, step, world
from nose.tools import assert_false, assert_true

@before.all
def set_browser():
    """sets up the test"""
    world.browser = Client()

@step(u'Given I go to "(.*)"')
def given_i_got_to_url(step, url):
    """goes to an url"""
    world.response = world.browser.get('/')

    assert_false(world.response is None)

@step(u'I see "(.*)" in the clippy code')
def i_see_the_clippy_code(step, text):
    """check if the content of the thing has the text we passed"""
    text = "text={0}".format(text)

    assert_true(text in world.response.content)
