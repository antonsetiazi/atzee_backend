# verticals/isp/seeds/branding.py

BRANDING = {
    "appName": "ISP",
    "logoUrl": "/branding/isp/logo.png",
    "faviconUrl": "/branding/isp/logo.svg",
    "theme": {
        "mode": "dark",

        # =========================
        # Core Colors (Premium Tech Feel)
        # =========================
        "primary": "#2563eb",      # Blue 600 (network trust)
        "secondary": "#1e40af",    # Blue 800 (deep infra)
        "accent": "#06b6d4",       # Cyan 500 (speed / signal)

        # =========================
        # Surface System (Dark Infra UI)
        # =========================
        "background": "#0f172a",   # Slate 900
        "surface": "#111827",      # Gray 900 (cards)
        "surfaceAlt": "#1f2937",   # Gray 800

        # =========================
        # Text System (High Contrast Dark)
        # =========================
        "textPrimary": "#f8fafc",  # Almost white
        "textSecondary": "#cbd5e1",
        "textMuted": "#94a3b8",

        # =========================
        # State Colors (Operational)
        # =========================
        "success": "#22c55e",      # Online
        "warning": "#f59e0b",      # High latency
        "error": "#ef4444",        # Down / Alert

        # =========================
        # Border & Layout
        # =========================
        "border": "#334155",
        "radius": "12px",
        "shadow": "0 4px 20px rgba(0,0,0,0.35)",

        # =========================
        # Typography (Tech Modern)
        # =========================
        "font": {
            "family": "'Inter', sans-serif",
            "size": "15px",
            "weight": "400"
        }
    }
}