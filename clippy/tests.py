"""
tests.py - testing the clippy template tag
"""

from django.test import TestCase
from nose.tools import assert_equals

class TestClippy(TestCase):
    """
    Main tests class
    """
    def test_clippy(self):
        """Tests if we got the same clippy code that we want"""
        from clippy.templatetags.clippy_tags import clippy

        expected_result = u'<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="110" height="14" id="clippy" ><param name="movie" value="flash/clippy.swf"/><param name="allowScriptAccess" value="always" /><param name="quality" value="high" /><param name="scale" value="noscale" /><param NAME="FlashVars" value="text=lol"><param name="bgcolor" value="#FFFFFF"><embed src="flash/clippy.swf" width="110" height="14" name="clippy" quality="high" allowScriptAccess="always" type="application/x-shockwave-flash" pluginspage="http://www.macromedia.com/go/getflashplayer" FlashVars="text=lol" bgcolor="#FFFFFF" /></object>'
        clippy_code = clippy('lol')

        assert_equals(clippy_code, expected_result)
