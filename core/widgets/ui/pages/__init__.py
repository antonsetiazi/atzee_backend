# core/widgets/ui/pages/__init__.py

from .widget_list import UI_PAGES as WIDGET_LIST_PAGE
from .widget_create import UI_PAGES as WIDGET_CREATE_PAGE
from .widget_edit import UI_PAGES as WIDGET_EDIT_PAGE

from .banners.banner_list import UI_PAGES as BANNER_LIST_PAGE
from .banners.banner_create import UI_PAGES as BANNER_CREATE_PAGE 
from .banners.banner_edit import UI_PAGES as BANNER_EDIT_PAGE 

from .videos.video_list import UI_PAGES as VIDEO_LIST_PAGE
from .videos.video_create import UI_PAGES as VIDEO_CREATE_PAGE 
from .videos.video_edit import UI_PAGES as VIDEO_EDIT_PAGE 


UI_PAGES = [
    WIDGET_LIST_PAGE,
    WIDGET_CREATE_PAGE,
    WIDGET_EDIT_PAGE,
    BANNER_LIST_PAGE,
    BANNER_CREATE_PAGE,
    BANNER_EDIT_PAGE,
    VIDEO_LIST_PAGE,
    VIDEO_CREATE_PAGE,
    VIDEO_EDIT_PAGE
]
