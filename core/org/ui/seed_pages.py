# core/org/ui/seed_pages.py

from core.org.departments.ui.pages import UI_PAGES as DEPARTMENT_PAGES
from core.org.branches.ui.pages import UI_PAGES as BRANCH_PAGES 

UI_PAGES = [
    *DEPARTMENT_PAGES,
    *BRANCH_PAGES
]
