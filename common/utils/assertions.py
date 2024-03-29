from common.log.log import MyLog
import json

class Assertions:
    def __init__(self):
        self.log = MyLog()

    def assert_code(self, code, expected_code):
        try:
            assert code == expected_code
            return True
        except:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))

            raise

    def assert_body(self, body, body_msg, expected_msg):
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            self.log.info("This is a successful request:{}".format(msg))
            return True

        except:
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))

            raise

    def assert_in_text(self, body, expected_msg):
        try:
            text = json.dumps(body, ensure_ascii=False)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)

            raise

    def assert_text(self, body, expected_msg):
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))

            raise

    def assert_time(self, time, expected_time):
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))

            raise