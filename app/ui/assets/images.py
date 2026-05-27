from enum import StrEnum
from pathlib import Path

IMAGES_DIR = (
    Path(__file__).parent / "images"
)


class Images(StrEnum):
    IMAGE1 = "image1_mountain.jpg"
    IMAGE2 = "image2_home.jpg"
    IMAGE3 = "image3_cat.jpg"
    IMAGE4 = "image4_river.jpg"

    @property
    def path(self) -> Path:
        return IMAGES_DIR / self.value
        