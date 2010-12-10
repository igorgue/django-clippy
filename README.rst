Clippy
======

Easy clipboard "copypasta" template tag (see it online on every repo page on github: http://github.com/mojombo/clippy), examples:

Requirements
------------

Get the clippy build file copied to your {{ MEDIA_URL }}flash/ folder::

    cd public/flash && curl -O https://github.com/mojombo/clippy/blob/master/build/clippy.swf

Integrating on templates
------------------------

Use this code to integrate it::

    {% load clippy_tags %}
    {{ "hello"|clippy }}

Now the user just have to click the button to copy the text to the clipboard.
