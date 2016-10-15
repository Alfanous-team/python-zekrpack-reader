import unittest

from zekrpack_reader.models import TranslationModel


class TestTranslationModel(unittest.TestCase):
    def setUp(self):
        self.path = "./example.zip"
        self.TM = TranslationModel(self.path)

    def test_open_zip(self):
        temp = self.TM.open_zip(self.path)
        self.assertTrue(temp, "opened file is empty")


    def test_translation_properties(self):
        props = self.TM.translation_properties()

        mendatory_keys = ['direction', 'language', 'country', 'delimiter', 'lineDelimiter', 'id', 'name']
        for k in mendatory_keys:
            self.assertIn(k, props.keys())

        self.assertEqual(props["direction"], "ltr")
        self.assertEqual(props["language"], "tr")
        self.assertEqual(props["country"], "TR")
        self.assertEqual(props["delimiter"], r"\n")
        self.assertEqual(props["lineDelimiter"], r"\n")
        self.assertEqual(props["id"], r"ozturk")




    def test_translation_lines(self):
        pass


    def test_document_list(self):
        pass


