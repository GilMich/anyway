from anyway.RequestParams import RequestParams
from anyway.infographics_utils import register
from anyway.widgets.suburban_widgets.SubUrbanWidget import SubUrbanWidget


@register
class StreetViewWidget(SubUrbanWidget):
    name: str = "street_view"

    def __init__(self, request_params: RequestParams):
        super().__init__(request_params, type(self).name)
        self.rank = 4

    def generate_items(self) -> None:
        self.items = {
            "longitude": self.request_params.gps["lon"],
            "latitude": self.request_params.gps["lat"],
        }
