from View.base_screen import BaseScreenView
from libs.ads.ads_manager import AdsManager


class MainScreenView(BaseScreenView):
    ads_manager = AdsManager()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.show_banner()

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def show_banner(self):
        """
        show_banner show ads banner
        """
        self.ads_manager.show_banner()
