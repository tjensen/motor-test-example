from tests.base_handler_test_case import BaseHandlerTestCase, gen_test


class TestCase14(BaseHandlerTestCase):

    @gen_test
    async def test_0(self):
        value = "14-0"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_1(self):
        value = "14-1"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_2(self):
        value = "14-2"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_3(self):
        value = "14-3"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_4(self):
        value = "14-4"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_5(self):
        value = "14-5"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_6(self):
        value = "14-6"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_7(self):
        value = "14-7"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_8(self):
        value = "14-8"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_9(self):
        value = "14-9"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_10(self):
        value = "14-10"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_11(self):
        value = "14-11"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_12(self):
        value = "14-12"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_13(self):
        value = "14-13"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_14(self):
        value = "14-14"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_15(self):
        value = "14-15"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_16(self):
        value = "14-16"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_17(self):
        value = "14-17"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_18(self):
        value = "14-18"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_19(self):
        value = "14-19"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_20(self):
        value = "14-20"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_21(self):
        value = "14-21"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_22(self):
        value = "14-22"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_23(self):
        value = "14-23"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_24(self):
        value = "14-24"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_25(self):
        value = "14-25"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_26(self):
        value = "14-26"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_27(self):
        value = "14-27"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_28(self):
        value = "14-28"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_29(self):
        value = "14-29"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_30(self):
        value = "14-30"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_31(self):
        value = "14-31"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_32(self):
        value = "14-32"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_33(self):
        value = "14-33"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_34(self):
        value = "14-34"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_35(self):
        value = "14-35"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_36(self):
        value = "14-36"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_37(self):
        value = "14-37"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_38(self):
        value = "14-38"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_39(self):
        value = "14-39"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_40(self):
        value = "14-40"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_41(self):
        value = "14-41"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_42(self):
        value = "14-42"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_43(self):
        value = "14-43"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_44(self):
        value = "14-44"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_45(self):
        value = "14-45"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_46(self):
        value = "14-46"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_47(self):
        value = "14-47"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_48(self):
        value = "14-48"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_49(self):
        value = "14-49"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_50(self):
        value = "14-50"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_51(self):
        value = "14-51"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_52(self):
        value = "14-52"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_53(self):
        value = "14-53"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_54(self):
        value = "14-54"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_55(self):
        value = "14-55"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_56(self):
        value = "14-56"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_57(self):
        value = "14-57"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_58(self):
        value = "14-58"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_59(self):
        value = "14-59"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_60(self):
        value = "14-60"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_61(self):
        value = "14-61"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_62(self):
        value = "14-62"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_63(self):
        value = "14-63"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_64(self):
        value = "14-64"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_65(self):
        value = "14-65"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_66(self):
        value = "14-66"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_67(self):
        value = "14-67"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_68(self):
        value = "14-68"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_69(self):
        value = "14-69"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_70(self):
        value = "14-70"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_71(self):
        value = "14-71"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_72(self):
        value = "14-72"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_73(self):
        value = "14-73"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_74(self):
        value = "14-74"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_75(self):
        value = "14-75"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_76(self):
        value = "14-76"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_77(self):
        value = "14-77"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_78(self):
        value = "14-78"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_79(self):
        value = "14-79"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_80(self):
        value = "14-80"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_81(self):
        value = "14-81"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_82(self):
        value = "14-82"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_83(self):
        value = "14-83"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_84(self):
        value = "14-84"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_85(self):
        value = "14-85"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_86(self):
        value = "14-86"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_87(self):
        value = "14-87"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_88(self):
        value = "14-88"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_89(self):
        value = "14-89"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_90(self):
        value = "14-90"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_91(self):
        value = "14-91"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_92(self):
        value = "14-92"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_93(self):
        value = "14-93"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_94(self):
        value = "14-94"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_95(self):
        value = "14-95"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_96(self):
        value = "14-96"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_97(self):
        value = "14-97"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_98(self):
        value = "14-98"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_99(self):
        value = "14-99"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))
