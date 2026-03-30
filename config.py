# ── Design Tokens ────────────────────────────────────────────────────────────
C = {
    "bg":        "#f5f5f4",
    "surface":   "#ffffff",
    "border":    "#d6d3d1",
    "border_lt": "#e7e5e4",
    "grid":      "#f0efed",
    "accent":    "#9B0D14",
    "accent_lt": "rgba(155,13,20,0.08)",
    "gray600":   "#57534e",
    "gray400":   "#a8a29e",
    "gray300":   "#d6d3d1",
    "text":      "#1c1917",
    "text_md":   "#44403c",
    "text_sm":   "#78716c",
    "header_bg": "#1c1917",
    "header_fg": "#fafaf9",
}

FONT_BODY = "'Barlow', 'Inter', sans-serif"
FONT_MONO = "'IBM Plex Mono', 'JetBrains Mono', monospace"

# ── Wochentag-Mapping (PostgreSQL DOW: 0=Sonntag) ───────────────────────────
WEEKDAY_MAP = {
    0: "So",
    1: "Mo",
    2: "Di",
    3: "Mi",
    4: "Do",
    5: "Fr",
    6: "Sa",
}

WEEKDAY_ORDER = ["So", "Mo", "Di", "Mi", "Do", "Fr", "Sa"]

WEEKDAY_OPTIONS = [
    {"label": "Montag",     "value": "Mo"},
    {"label": "Dienstag",   "value": "Di"},
    {"label": "Mittwoch",   "value": "Mi"},
    {"label": "Donnerstag", "value": "Do"},
    {"label": "Freitag",    "value": "Fr"},
    {"label": "Samstag",    "value": "Sa"},
    {"label": "Sonntag",    "value": "So"},
]

# Reverse: Wort -> Nummer (für SQL-Queries)
WEEKDAY_TO_NUM = {v: k for k, v in WEEKDAY_MAP.items()}

METRIC_OPTIONS = [
    {"label": "Durchschnittlicher Verbrauch (kW)", "value": "avg_power"},
    {"label": "Gesamtverbrauch (kWh)",             "value": "total_power"},
    {"label": "Spitzenverbrauch (kW)",             "value": "peak_power"},
]

YEAR_OPTIONS = [{"label": str(y), "value": y} for y in range(2006, 2011)]
