# core/ui/schema/block/image_gallery.py
from dataclasses import dataclass
from typing import Literal, Optional

WidgetSize = Literal["sm", "md", "lg"]

@dataclass(frozen=True)
class ImageGalleryBlock:
    type: Literal["image_gallery"] = "image_gallery"
    title: Optional[str] = None
    data_key: Optional[str] = None  # nama field dari entity, misal 'image_urls'
    multiple: bool = True           # apakah bisa menampilkan banyak gambar
    max_height: int = 250           # tinggi maksimal image card
    size: WidgetSize = "md"         # optional, bisa kita pakai nanti untuk styling