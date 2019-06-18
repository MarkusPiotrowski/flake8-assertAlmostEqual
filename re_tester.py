"""A playground to test some things regarding regex and flake8."""

import re
import tokenize
import StringIO

search_pattern_1 = re.compile(r'assertAlmostEqual\(.*round\(', re.DOTALL)
search_pattern_2 = re.compile(r'assertEqual\(.*round\(', re.DOTALL)

s1 = 'self.assertAlmostEqual(1, round(my_result), 2)'
s2 = 'self.assertAlmostEqual(1, round(my_result), 2)  # Check this'
print(re.search(search_pattern_1,
                'self.assertAlmostEqual(1, \nround(my_result), 2)'))
print(re.search('..a', 'Master'))

tokens = tokenize.generate_tokens(StringIO.StringIO(s2).readline)

for token_type, text, start, _, _ in tokens:
    print token_type, text, start

search_pattern_3 = re.compile(
    r"# noqa(?::[\s]?(?P<codes>([A-Z]+[0-9]+(?:[,\s]+)?)+))?",
    re.IGNORECASE)

print(re.search(search_pattern_3, ')  # noqa: AAE100').group('codes'))
