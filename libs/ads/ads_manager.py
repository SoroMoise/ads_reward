from kivmob import KivMob
from kivymd.toast import toast

from libs.ads.ads_ids import Ids


class AdsManager:
    """
    ## manage add in app

    used for managing all ads in this app
    """

    ads_ids = Ids()
    ads = KivMob(ads_ids.get_app())

    banners_ads: list[KivMob] = []
    interstitials_ads: list[KivMob] = []
    rewards_videos_ads: list[KivMob] = []

    def __init__(self) -> None:
        self.app_id = self.ads_ids.get_app()
        self.banner_id = self.ads_ids.get_banner()
        self.last_banner_pos_hade_top = False

    @staticmethod
    def show_toast(text: str, length_long=True, gravity=80, y=200, x=0):
        """
        show_toast show toast on app
        """
        toast(text, length_long, gravity, y, x)

    def create_new_banner(self):
        """
        create_new_banner create new banner and add it in banners list

        """
        try:
            self.banners_ads.append(KivMob(self.app_id))
            self.banners_ads[-1].new_banner(
                self.banner_id, self.last_banner_pos_hade_top
            )
        except IndexError as error:
            self.create_new_banner()
            print("index error in create banner : ", error)
            self.show_toast(f"index error in create banner : {error}")
        except BaseException as e:
            print("l'erreur de creation : ", e)
            self.show_toast(f"l'erreur de creation : {e}")

    def show_banner(self):
        """
        ### show ads banner

        show ads banner if it exist, else it'll create it and show it
        """
        try:
            self.create_new_banner()
            ads = self.banners_ads.pop(0)
            ads.show_banner()
        except IndexError as error:
            self.create_new_banner()
            self.show_banner()
            print("j'ais une index error : ", error)
            self.show_toast(f"j'ais une index error : {error}")
        except BaseException as e:
            print("une erreur s'et produit : ", e)
            self.show_toast(f"une erreur s'et produit : {e}")
