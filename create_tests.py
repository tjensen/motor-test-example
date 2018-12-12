#!/usr/bin/env python
import sys


def create_testcase(case_number, test_methods):
    with open(f"tests/test_case_{case_number}.py", "w") as f:
        f.write(f"""\
from tests.base_handler_test_case import BaseHandlerTestCase, gen_test


class TestCase{case_number}(BaseHandlerTestCase):
""")

        for method_number in range(0, test_methods):
            f.write(f"""
    @gen_test
    async def test_{method_number}(self):
        value = "{case_number}-{method_number}"
        await self.database.things.insert_one({{
            "thing": "THING",
            "value": value
        }})

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))
""")


def main(argv):
    test_cases = int(argv[1])
    test_methods = int(argv[2])

    for case_number in range(0, test_cases):
        create_testcase(case_number, test_methods)


if __name__ == "__main__":
    main(sys.argv)
