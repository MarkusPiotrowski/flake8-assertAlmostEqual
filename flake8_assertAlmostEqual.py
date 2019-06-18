"""Flake8 plugin to check for use of ``round()`` in ``assert(Almost)Equal``.

Don't use ``assertAlmostEqual`` with ``round``... (AAE100)
==========================================================

``assertAlmostEqual`` has built in rounding. Thus ``round()`` is not required.

Anti-pattern
------------
::

   self.assertAlmostEqual(round(my_result, 2), 1.52)

Best practice
-------------
::

   self.assertAlmostEqual(my_result, 1.52, 2)

Don't use ``assertEqual`` with round... (AAE110)
==============================================
If you need rounding, don't use ``assertEqual``. Use ``assertAlmostEqual``
instead.

Anti-pattern
------------
::

   self.assertEqual(round(my_result, 2), 1.52)

Best practice
---------------
::

   self.assertAlmostEqual(my_result), 1.52, 2)

"""

import re

AAE100 = ("AAE100 Don't use 'assertAlmostEqual' with 'round'. Use it's "
          "implemented rounding.")
AAE110 = ("AAE110 Don't use 'assertEqual' with 'round'. Use "
          "'assertAlmostEqual' instead.")

search_pattern_1 = re.compile(r'assertAlmostEqual\(.*round\(', re.DOTALL)
search_pattern_2 = re.compile(r'assertEqual\(.*round\(', re.DOTALL)

pattern_and_codes = [(search_pattern_1, AAE100),
                     (search_pattern_2, AAE110)]


def AAE_checker(logical_line):
    """Search for violating lines."""
    for pattern, error_code in pattern_and_codes:
        hit = re.search(pattern, logical_line)
        if hit:
            yield(hit.start(), error_code)


AAE_checker.name = 'flake8-assertAlmostEqual'
AAE_checker.version = '0.3.0'
