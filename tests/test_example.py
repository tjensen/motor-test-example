from tests.base_handler_test_case import BaseHandlerTestCase, gen_test


class TestExample(BaseHandlerTestCase):
    @gen_test
    async def test_get_returns_value_in_thing(self):
        await self.database.things.insert_one({"thing": "THING", "value": "VALUE"})

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual("VALUE", response.body.decode("utf8"))
