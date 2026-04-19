# core/ui/schema/block/category_slider.py

from dataclasses import dataclass

@dataclass(frozen=True)
class CategorySliderBlock:
    type: str = "category_slider"
    title: str = "Kategori"
    scope: str = "partners.service_category"