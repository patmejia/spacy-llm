import unittest
from main import process_text

class TestProcessText(unittest.TestCase):
    def test_process_text(self):
        text = "This is a test sentence."
        expected_output = [
            ("This", "PRON", "nsubj"),
            ("is", "AUX", "ROOT"),
            ("a", "DET", "det"),
            ("test", "NOUN", "compound"),
            ("sentence", "NOUN", "attr"),
            (".", "PUNCT", "punct"),
        ]

        output = process_text(text)

        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
