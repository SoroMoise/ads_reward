import os


class Ids:
    """
    ## Enum of ads ids.
    ### If environment is prod and ids are defined it'll retuned it, \
    otherwise it'll return test ids provided by AdMob.
    """

    TEST_APP = "ca-app-pub-3940256099942544~3347511713"
    TEST_BANNER = "ca-app-pub-3940256099942544/6300978111"
    TEST_INTERSTITIAL = "ca-app-pub-3940256099942544/1033173712"
    TEST_INTERSTITIAL_VIDEO = "ca-app-pub-3940256099942544/8691691433"
    TEST_REWARDED_VIDEO = "ca-app-pub-3940256099942544/5224354917"

    APP = ""
    BANNER = ""
    INTERSTITIAL = ""
    INTERSTITIAL_VIDEO = ""
    REWARDED_VIDEO = ""

    def __init__(self) -> None:
        self.environment = os.environ.get("environment")

    def get_app(self):
        """
        get_app get app ads id

        ### return:
            return app id
        """
        if self.environment == "prod" and self.APP:
            return self.APP
        return self.TEST_APP

    def get_banner(self):
        if self.environment == "prod" and self.BANNER:
            return self.BANNER
        return self.TEST_BANNER

    def get_interstitial(self):
        if self.environment == "prod" and self.INTERSTITIAL:
            return self.INTERSTITIAL
        return self.TEST_INTERSTITIAL

    def get_interstitial_video(self):
        if self.environment == "prod" and self.INTERSTITIAL_VIDEO:
            return self.INTERSTITIAL_VIDEO
        return self.TEST_INTERSTITIAL_VIDEO

    def get_rewarded(self):
        if self.environment == "prod" and self.REWARDED_VIDEO:
            return self.REWARDED_VIDEO
        return self.TEST_REWARDED_VIDEO
