# verticals/hrms/seeds/branding.py

BRANDING = {
    "appName": "HRMS",
    "logoUrl": "/branding/hrms/logo.png",
    "faviconUrl": "/branding/hrms/logo.svg",
    "theme": {
        "mode": "light",

        # =========================
        # Core Colors (Corporate Premium)
        # =========================
        "primary": "#1e3a8a",      # Deep Blue 800 (Authority)
        "secondary": "#1e40af",    # Blue 700
        "accent": "#d4af37",       # Gold Accent (Premium touch)

        # =========================
        # Surface System (Executive Feel)
        # =========================
        "background": "#f4f6f9",   # Soft corporate grey
        "surface": "#ffffff",      # Clean white
        "surfaceAlt": "#eef2f7",   # Elegant alternate surface

        # =========================
        # Text System (Professional Readability)
        # =========================
        "textPrimary": "#111827",  # Strong dark
        "textSecondary": "#374151",
        "textMuted": "#6b7280",

        # =========================
        # State Colors (Corporate Safe)
        # =========================
        "success": "#15803d",
        "warning": "#d97706",
        "error": "#b91c1c",

        # =========================
        # Border & Layout
        # =========================
        "border": "#d1d5db",
        "radius": "12px",
        "shadow": "0 4px 20px rgba(0,0,0,0.06)",

        # =========================
        # Typography (Premium Clean)
        # =========================
        "font": {
            "family": "'Inter', 'SF Pro Display', sans-serif",
            "size": "16px",
            "weight": "400"
        }
    }
}