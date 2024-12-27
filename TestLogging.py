from LoggingDeco import logger

if __name__ == "__main__":
    logpath = "AppLog.log"

    @logger(logpath)
    def test(s):
        print(s)

    test("Hello World!")
