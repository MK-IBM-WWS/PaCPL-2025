import unittest
import os
import tempfile
import shutil
from unittest.mock import patch, MagicMock

from lab2.main import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)
        os.makedirs('figures', exist_ok=True)

    def tearDown(self):
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_main_execution(self):
        try:
            main()
            self.assertTrue(os.path.exists('figures/Круг.png'))
            self.assertTrue(os.path.exists('figures/Прямоугольник.png'))
            self.assertTrue(os.path.exists('figures/Квадрат.png'))
        except Exception as e:
            self.fail(f"main() вызвал исключение: {e}")

    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.subplots')
    @patch('builtins.print')
    def test_main_mocked(self, mock_print, mock_subplots, mock_savefig):
        mock_ax = MagicMock()
        mock_fig = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)

        main()

        self.assertEqual(mock_savefig.call_count, 3)

        self.assertTrue(mock_print.called)


if __name__ == '__main__':
    unittest.main()