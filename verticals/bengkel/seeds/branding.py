# verticals/bengkel/seeds/branding.py

BRANDING = {
    "appName": "Atzee Workshop",
    "logoUrl": "/branding/bengkel/logo.png",
    "faviconUrl": "/branding/bengkel/logo.svg",
    "theme": {
        "mode": "dark",

        # =========================
        # Core Colors (Automotive Premium)
        # =========================
        "primary": "#1e293b",      # Slate 800 (Industrial dark)
        "secondary": "#0f172a",    # Slate 900
        "accent": "#f97316",       # Orange 500 (Automotive highlight)

        # =========================
        # Surface System (Dark Premium UI)
        # =========================
        "background": "#0b1220",   # Deep navy-black
        "surface": "#111827",      # Card surface
        "surfaceAlt": "#1f2937",   # Slightly lighter panel

        # =========================
        # Text System (High Contrast)
        # =========================
        "textPrimary": "#f8fafc",  # Near white
        "textSecondary": "#cbd5e1",
        "textMuted": "#94a3b8",

        # =========================
        # State Colors
        # =========================
        "success": "#22c55e",      # Green 500
        "warning": "#f59e0b",      # Amber 500
        "error": "#ef4444",        # Red 500

        # =========================
        # Border & Layout
        # =========================
        "border": "#1f2937",
        "radius": "12px",
        "shadow": "0 8px 30px rgba(0,0,0,0.35)",

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