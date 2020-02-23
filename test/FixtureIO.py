import unittest
import io
from unittest.mock import patch
import sys
import builtins

sys.path.append('../src/skills')

import AVAIO


class TestAVAIO(unittest.TestCase):
    def test_text_read(self):
        with patch('builtins.input', return_value='Hello World') as text:
            io_obj = AVAIO.TextIO()
            input = io_obj.read()
            self.assertEqual("hello world", input)

    def test_text_write(self):
        io_obj = AVAIO.TextIO()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        io_obj.write('Hello World')
        sys.stdout = sys.__stdout__
        self.assertEqual('AVA> Hello World\n', capturedOutput.getvalue())
