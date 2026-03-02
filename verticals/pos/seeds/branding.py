# verticals/pos/seeds/branding.py

BRANDING = {
    "appName": "POS",
    "logoUrl": "/branding/pos/logo.png",
    "faviconUrl": "/branding/pos/logo.svg",
    "theme": {
        "mode": "light",

        # =========================
        # Core Colors (Retail Feel)
        # =========================
        "primary": "#0ea5a4",      # Teal 500 (fast & modern)
        "secondary": "#0f766e",    # Teal 700
        "accent": "#f97316",       # Orange 500 (Pay / Action)

        # =========================
        # Surface System (Bright Retail UI)
        # =========================
        "background": "#f8fafc",   # Slate 50
        "surface": "#ffffff",      # White cards
        "surfaceAlt": "#f1f5f9",   # Soft grey alt

        # =========================
        # Text System (High Readability)
        # =========================
        "textPrimary": "#0f172a",  # Dark slate
        "textSecondary": "#334155",
        "textMuted": "#64748b",

        # =========================
        # State Colors
        # =========================
        "success": "#16a34a",
        "warning": "#f59e0b",
        "error": "#dc2626",

        # =========================
        # Border & Layout
        # =========================
        "border": "#e2e8f0",
        "radius": "10px",
        "shadow": "0 2px 10px rgba(0,0,0,0.08)",

        # =========================
        # Typography
        # =========================
        "font": {
            "family": "'Inter', sans-serif",
            "size": "16px",
            "weight": "400"
        }
    }
}