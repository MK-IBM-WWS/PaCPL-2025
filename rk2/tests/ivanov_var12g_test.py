import unittest
from rk2.src.ivanov_var12g import ProgrammingSystem

class TestProgrammingSystem(unittest.TestCase):
    def setUp(self):
        self.system = ProgrammingSystem()

    def test_get_tools_starting_with_v(self):
        result = self.system.get_tools_starting_with_v()

        self.assertIsInstance(result, list)

        for tool_name, lang_name in result:
            self.assertTrue(tool_name.startswith('V'))

        tool_names = [tool_name for tool_name, _ in result]
        expected_tools = ['Visual Studio', 'VS Code']

        for expected_tool in expected_tools:
            self.assertIn(expected_tool, tool_names)

        self.assertEqual(len(result), 2)

        for _, lang_name in result:
            self.assertIn(lang_name, ['Python', 'C++'])

    def test_get_languages_with_max_license_cost(self):
        result = self.system.get_languages_with_max_license_cost()

        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

        for lang, tool, cost in result:
            self.assertIsInstance(lang, str)
            self.assertIsInstance(tool, str)
            self.assertIsInstance(cost, int)

        costs = [cost for _, _, cost in result]
        self.assertEqual(costs, sorted(costs, reverse=True))

        expected_languages = ['C++', 'Java', 'JavaScript', 'Go', 'Python']

        result_languages = [lang for lang, _, _ in result]
        for expected_lang in expected_languages:
            self.assertIn(expected_lang, result_languages)

        result_dict = {lang: (tool, cost) for lang, tool, cost in result}

        self.assertEqual(result_dict['C++'][0], 'Visual Studio')
        self.assertEqual(result_dict['C++'][1], 299)

        self.assertEqual(result_dict['Java'][0], 'IntelliJ IDEA')
        self.assertEqual(result_dict['Java'][1], 249)

    def test_get_all_linked_tools_sorted(self):
        result = self.system.get_all_linked_tools_sorted()

        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

        for tool, cost, lang in result:
            self.assertIsInstance(tool, str)
            self.assertIsInstance(cost, int)
            self.assertIsInstance(lang, str)

        for i in range(len(result) - 1):
            current_lang = result[i][2]
            current_tool = result[i][0]
            next_lang = result[i + 1][2]
            next_tool = result[i + 1][0]

            if current_lang == next_lang:
                self.assertLessEqual(current_tool, next_tool)

        many_to_many = self.system.get_many_to_many()
        self.assertEqual(len(result), len(many_to_many))

        self.assertEqual(result[0][2], 'C++')
        self.assertEqual(result[0][0], 'Visual Studio')

        all_links = [(lang, tool) for tool, cost, lang in result]

        self.assertIn(('Python', 'PyCharm'), all_links)
        self.assertIn(('Python', 'VS Code'), all_links)
        self.assertIn(('Python', 'Visual Studio'), all_links)


if __name__ == '__main__':
    unittest.main(verbosity=2)
