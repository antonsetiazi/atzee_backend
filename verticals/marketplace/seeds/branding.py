# verticals/marketplace/seeds/branding.py

BRANDING = {
    "appName": "Marketplace",
    "logoUrl": "/branding/marketplace/logo.png",
    "faviconUrl": "/branding/marketplace/logo.svg",
    "theme": {
        "mode": "light",

        # =========================
        # Core Colors (Marketplace Feel)
        # =========================
        "primary": "#4f46e5",      # Indigo 600 (trust & platform)
        "secondary": "#3730a3",    # Indigo 800
        "accent": "#f97316",       # Orange 500 (Buy / CTA)

        # =========================
        # Surface System (Clean E-commerce UI)
        # =========================
        "background": "#f9fafb",   # Gray 50
        "surface": "#ffffff",      # Product cards
        "surfaceAlt": "#f3f4f6",   # Alt sections

        # =========================
        # Text System
        # =========================
        "textPrimary": "#111827",  # Dark Gray
        "textSecondary": "#374151",
        "textMuted": "#6b7280",

        # =========================
        # State Colors
        # =========================
        "success": "#16a34a",      # Successful order
        "warning": "#f59e0b",      # Pending
        "error": "#dc2626",        # Failed payment

        # =========================
        # Border & Layout
        # =========================
        "border": "#e5e7eb",
        "radius": "12px",
        "shadow": "0 6px 18px rgba(0,0,0,0.08)",

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