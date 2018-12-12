from tests.base_handler_test_case import BaseHandlerTestCase, gen_test


class TestCase2(BaseHandlerTestCase):

    @gen_test
    async def test_0(self):
        value = "2-0"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_1(self):
        value = "2-1"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_2(self):
        value = "2-2"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_3(self):
        value = "2-3"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_4(self):
        value = "2-4"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_5(self):
        value = "2-5"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_6(self):
        value = "2-6"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_7(self):
        value = "2-7"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_8(self):
        value = "2-8"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_9(self):
        value = "2-9"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_10(self):
        value = "2-10"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_11(self):
        value = "2-11"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_12(self):
        value = "2-12"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_13(self):
        value = "2-13"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_14(self):
        value = "2-14"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_15(self):
        value = "2-15"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_16(self):
        value = "2-16"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_17(self):
        value = "2-17"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_18(self):
        value = "2-18"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_19(self):
        value = "2-19"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_20(self):
        value = "2-20"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_21(self):
        value = "2-21"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_22(self):
        value = "2-22"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_23(self):
        value = "2-23"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_24(self):
        value = "2-24"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_25(self):
        value = "2-25"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_26(self):
        value = "2-26"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_27(self):
        value = "2-27"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_28(self):
        value = "2-28"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_29(self):
        value = "2-29"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_30(self):
        value = "2-30"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_31(self):
        value = "2-31"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_32(self):
        value = "2-32"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_33(self):
        value = "2-33"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_34(self):
        value = "2-34"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_35(self):
        value = "2-35"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_36(self):
        value = "2-36"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_37(self):
        value = "2-37"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_38(self):
        value = "2-38"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_39(self):
        value = "2-39"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_40(self):
        value = "2-40"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_41(self):
        value = "2-41"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_42(self):
        value = "2-42"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_43(self):
        value = "2-43"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_44(self):
        value = "2-44"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_45(self):
        value = "2-45"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_46(self):
        value = "2-46"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_47(self):
        value = "2-47"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_48(self):
        value = "2-48"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_49(self):
        value = "2-49"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_50(self):
        value = "2-50"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_51(self):
        value = "2-51"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_52(self):
        value = "2-52"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_53(self):
        value = "2-53"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_54(self):
        value = "2-54"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_55(self):
        value = "2-55"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_56(self):
        value = "2-56"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_57(self):
        value = "2-57"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_58(self):
        value = "2-58"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_59(self):
        value = "2-59"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_60(self):
        value = "2-60"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_61(self):
        value = "2-61"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_62(self):
        value = "2-62"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_63(self):
        value = "2-63"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_64(self):
        value = "2-64"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_65(self):
        value = "2-65"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_66(self):
        value = "2-66"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_67(self):
        value = "2-67"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_68(self):
        value = "2-68"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_69(self):
        value = "2-69"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_70(self):
        value = "2-70"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_71(self):
        value = "2-71"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_72(self):
        value = "2-72"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_73(self):
        value = "2-73"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_74(self):
        value = "2-74"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_75(self):
        value = "2-75"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_76(self):
        value = "2-76"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_77(self):
        value = "2-77"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_78(self):
        value = "2-78"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_79(self):
        value = "2-79"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_80(self):
        value = "2-80"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_81(self):
        value = "2-81"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_82(self):
        value = "2-82"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_83(self):
        value = "2-83"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_84(self):
        value = "2-84"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_85(self):
        value = "2-85"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_86(self):
        value = "2-86"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_87(self):
        value = "2-87"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_88(self):
        value = "2-88"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_89(self):
        value = "2-89"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_90(self):
        value = "2-90"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_91(self):
        value = "2-91"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_92(self):
        value = "2-92"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_93(self):
        value = "2-93"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_94(self):
        value = "2-94"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_95(self):
        value = "2-95"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_96(self):
        value = "2-96"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_97(self):
        value = "2-97"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_98(self):
        value = "2-98"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))

    @gen_test
    async def test_99(self):
        value = "2-99"
        await self.database.things.insert_one({
            "thing": "THING",
            "value": value
        })

        response = await self.async_fetch("/handler")

        self.assertEqual(200, response.code)
        self.assertEqual(value, response.body.decode("utf8"))
