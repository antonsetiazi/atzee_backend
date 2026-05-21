# verticals/hr/seeds/branding.py

BRANDING = {
    "appName": "HR",
    "logoUrl": "https://res.cloudinary.com/daboazlmd/image/upload/v1779067710/hr_atzee_icon-preview_ul7omm.png",
    "faviconUrl": "https://res.cloudinary.com/daboazlmd/image/upload/v1779067710/hr_atzee_icon-preview_ul7omm.png",
    "tagline": "Empowering People Behind Every Business",
    "theme": {
        "mode": "light",
        # 🟣 Core Brand Colors (HR = People, Growth, Trust)
        "primary": "#7C3AED",  # Human Purple
        "secondary": "#312E81",  # Deep Indigo
        "accent": "#06B6D4",  # Modern Cyan
        # 🧱 Surface System (Soft & Friendly Workspace)
        "background": "#FFFFFF",
        "surface": "#F8FAFC",
        "surfaceAlt": "#EEF2FF",
        # ✍️ Text System (Readable & Calm)
        "textPrimary": "#111827",
        "textSecondary": "#374151",
        "textMuted": "#6B7280",
        "textBrandSoft": "rgba(124, 58, 237, 0.7)",
        # 🚦 State Colors (HR Workflow States)
        "success": "#16A34A",  # approved / active employee
        "warning": "#F59E0B",  # pending request
        "error": "#DC2626",  # rejected / issue
        # 📏 Border
        "border": "#E5E7EB",
        # 🎨 Visual Feel
        "radius": "12px",
        "shadow": "0 6px 24px rgba(15, 23, 42, 0.05)",
        # 🅰️ Typography
        "font": {
            "family": "'Inter', 'Noto Sans', sans-serif",
            "size": "15px",
            "weight": "400",
        },
    },
}
