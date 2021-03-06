import os

import motor
from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncHTTPTestCase, gen_test
from tornado.web import Application, RequestHandler


class ExampleHandler(RequestHandler):
    async def get(self):
        document = await self.settings["database"].things.find_one({"thing": "THING"})

        self.finish(document["value"])


class BaseHandlerTestCase(AsyncHTTPTestCase):
    def get_app(self):
        mongodb_uri = os.environ.get("MONGODB_URI", "mongodb://localhost/motor-test-example")
        self.motor_client = motor.MotorClient(mongodb_uri)
        self.database = self.motor_client.get_database()

        return Application(
            [
                ("/handler", ExampleHandler)
            ],
            database=self.database)

    async def async_teardown(self):
        await self.motor_client.drop_database(self.database)

    def tearDown(self):
        self.io_loop.run_sync(self.async_teardown)
        self.motor_client.close()
        del self.database
        del self.motor_client
        super().tearDown()

    async def async_fetch(self, path):
        return await AsyncHTTPClient().fetch(self.get_url(path), raise_error=False)
