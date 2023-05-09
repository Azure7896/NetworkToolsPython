import speedtest as st

class SpeedTests:

    server = st.Speedtest()
    jsonTestInfo = server.get_best_server()

    def __init__(self):
        pass

    @classmethod
    def get_test_info(cls):
        return SpeedTests.jsonTestInfo.items()


    @classmethod
    def checkDownload(cls):
        down = SpeedTests.server.download()
        down = down / 1000000
        return down

    @classmethod
    def checkUpload(cls):
        upload = SpeedTests.server.upload()
        upload = upload / 1000000
        return upload

    @classmethod
    def checkPing(cls):
        ping = SpeedTests.server.results.ping
        return ping

    class IpChecker:

        def __init__(self):
            pass



