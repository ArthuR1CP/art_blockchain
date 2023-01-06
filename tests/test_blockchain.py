import unittest
from application import art
from flask import template_rendered
from contextlib import contextmanager
import re

@contextmanager
def captured_templates(application):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, application)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, application)

class TestIndex(unittest.TestCase):
    def test_index(self):
        with application.test_client() as c:
            with captured_templates(application) as templates:

                r = c.get('/')
                template, context = templates[0]

                #print(template)
                self.assertEqual(re.findall(r'index.html', str(template))[0], 'index.html')
                self.assertEqual(context['greeting'], 'Artur')
    def test_rcode(self):
        with application.test_client() as c:
            r = c.get('/')
            self.assertEqual(r.status_code, 200)




unittest.main()