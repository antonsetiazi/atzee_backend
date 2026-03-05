# verticals/cbs/seeds/branding.py

BRANDING = {
    "appName": "CBS",
    "logoUrl": "/branding/cbs/logo.png",
    "faviconUrl": "/branding/cbs/logo.svg",
    "theme": {
        "mode": "light",

        # =========================
        # Core Colors (Premium Banking Feel)
        # =========================
        "primary": "#0b3c5d",      # Deep Navy (trust & authority)
        "secondary": "#1f2937",    # Dark slate
        "accent": "#c6a75e",       # Gold accent (premium touch)

        # =========================
        # Surface System (Executive UI)
        # =========================
        "background": "#f5f7fa",   # Soft financial grey
        "surface": "#ffffff",      # Clean white cards
        "surfaceAlt": "#eef2f7",   # Slight blue-grey alt

        # =========================
        # Text System (High Clarity)
        # =========================
        "textPrimary": "#111827",  # Almost black
        "textSecondary": "#374151",
        "textMuted": "#6b7280",

        # =========================
        # State Colors (Professional Tone)
        # =========================
        "success": "#15803d",      # Strong green
        "warning": "#b45309",      # Amber dark
        "error": "#b91c1c",        # Deep red

        # =========================
        # Border & Layout
        # =========================
        "border": "#d1d5db",
        "radius": "12px",
        "shadow": "0 4px 20px rgba(15, 23, 42, 0.08)",

        # =========================
        # Typography (Corporate Clean)
        # =========================
        "font": {
            "family": "'Inter', 'Helvetica Neue', sans-serif",
            "size": "16px",
            "weight": "400"
        }
    }
}