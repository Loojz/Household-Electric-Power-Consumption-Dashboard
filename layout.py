from dash import dcc, html
import pandas as pd

from utils.data_connector import engine
from config import (
    C, FONT_BODY, WEEKDAY_OPTIONS, METRIC_OPTIONS, YEAR_OPTIONS,
)

df_range = pd.read_sql(
    "SELECT MIN(timestamp) AS mn, MAX(timestamp) AS mx FROM power_consumption",
    engine,
)
min_date = df_range["mn"].iloc[0].date()
max_date = df_range["mx"].iloc[0].date()

# ── Reusable Styles ──────────────────────────────────────────────────────────
CARD = {
    "background":   C["surface"],
    "border":       f"1px solid {C['border']}",
    "borderRadius": "8px",
    "padding":      "20px 24px",
    "marginBottom": "16px",
    "boxShadow":    "0 1px 3px rgba(0,0,0,0.06)",
}

TAB_STYLE = {
    "backgroundColor": C["bg"],
    "color":           C["text_sm"],
    "border":          "none",
    "borderBottom":    f"2px solid {C['border']}",
    "padding":         "10px 18px",
    "fontFamily":      FONT_BODY,
    "fontSize":        "14px",
    "fontWeight":      "500",
}
TAB_SELECTED = {
    **TAB_STYLE,
    "color":        C["accent"],
    "borderBottom": f"2px solid {C['accent']}",
    "fontWeight":   "600",
}

DD_STYLE = {"fontSize": "14px", "color": C["text"]}

ZOOM_BTN = {
    "position": "absolute", "top": "12px", "right": "12px",
    "background": C["bg"], "border": f"1px solid {C['border']}",
    "borderRadius": "6px", "padding": "4px 10px", "cursor": "pointer",
    "fontSize": "16px", "color": C["text_sm"], "lineHeight": "1",
    "opacity": "0", "transition": "opacity 0.2s",
    "zIndex": "10",
}

# Alle chart-IDs sammeln für Modal-Callbacks
ALL_CHART_IDS = [
    "chart-daily", "chart-rolling", "chart-yearly", "chart-compare",
    "chart-heatmap", "chart-weekday", "chart-hourly", "chart-monthly", "chart-daytime",
    "chart-sub-pie", "chart-sub-monthly", "chart-weekend",
    "chart-anomaly", "chart-peak-days", "chart-efficiency", "chart-reactive", "chart-hidden",
    "chart-forecast", "chart-corr", "chart-voltage",
]


def chart_card(chart_id, title, subtitle, flex="1"):
    """Card with section title, chart, and a zoom button that appears on hover."""
    return html.Div([
        section_title(title, subtitle),
        html.Div([
            html.Button("⛶", className="zoom-btn",
                        **{"data-chart": chart_id},
                        style=ZOOM_BTN),
            dcc.Graph(id=chart_id, config={"displayModeBar": True, "displaylogo": False}),
        ], style={"position": "relative"}),
    ], style={**CARD, "flex": flex},
       className="chart-card-hover")


def zoom_modal():
    """Empty container — modal is created and managed by assets/zoom.js."""
    return html.Div(id="zoom-modal-anchor")


def section_title(title, subtitle=None):
    """Section header with optional subtitle/interpretation hint."""
    return html.Div([
        html.H3(title, style={
            "fontSize": "18px", "fontWeight": "700", "color": C["text"],
            "margin": "0 0 4px 0", "lineHeight": "1.3",
        }),
        html.P(subtitle, style={
            "fontSize": "14px", "color": C["text_md"], "margin": "0",
            "lineHeight": "1.5",
        }) if subtitle else None,
    ], style={"marginBottom": "14px"})


def filter_bar():
    label_style = {
        "fontSize": "12px", "fontWeight": "600", "color": C["text_md"],
        "letterSpacing": "0.04em", "marginBottom": "6px", "display": "block",
    }
    return html.Div([
        html.Div([
            # Zeitraum
            html.Div([
                html.Label("Zeitraum", style=label_style),
                dcc.DatePickerRange(
                    id="date-range",
                    min_date_allowed=min_date,
                    max_date_allowed=max_date,
                    start_date=min_date,
                    end_date=max_date,
                    display_format="DD.MM.YYYY",
                    style={"fontSize": "14px", "color": C["text"]},
                ),
            ], style={"flex": "2", "marginRight": "20px"}),

            # Metrik
            html.Div([
                html.Label("Metrik", style=label_style),
                dcc.Dropdown(
                    id="metric-picker",
                    options=METRIC_OPTIONS,
                    value="avg_power",
                    clearable=False,
                    style=DD_STYLE,
                    maxHeight=200,
                ),
            ], style={"flex": "1.5", "marginRight": "20px"}),

            # Jahr
            html.Div([
                html.Label("Jahr", style=label_style),
                dcc.Dropdown(
                    id="year-picker",
                    options=[{"label": "Alle Jahre", "value": "all"}] + YEAR_OPTIONS,
                    value="all",
                    clearable=False,
                    style=DD_STYLE,
                    maxHeight=200,
                ),
            ], style={"flex": "1", "marginRight": "20px"}),

            # Wochentag
            html.Div([
                html.Label("Wochentage filtern", style=label_style),
                dcc.Dropdown(
                    id="weekday-filter",
                    options=WEEKDAY_OPTIONS,
                    multi=True,
                    placeholder="Alle Wochentage",
                    style=DD_STYLE,
                    maxHeight=200,
                ),
            ], style={"flex": "1.5"}),
        ], style={"display": "flex", "alignItems": "flex-end", "flexWrap": "wrap", "gap": "8px"}),
    ], style={**CARD, "marginBottom": "20px"})


def kpi_cards():
    return html.Div(id="kpi-cards", style={
        "display": "grid",
        "gridTemplateColumns": "repeat(4, 1fr)",
        "gap": "16px",
        "marginBottom": "20px",
    })


def tab_overview():
    return html.Div([
        html.Div([
            chart_card("chart-daily", "Täglicher Gesamtverbrauch",
                       "Zeigt die tägliche Wirkleistung (kW) über den gewählten Zeitraum. "
                       "Spitzen deuten auf Tage mit besonders hohem Verbrauch hin.", flex="2"),
            chart_card("chart-rolling", "Gleitender Durchschnitt",
                       "Glättet kurzfristige Schwankungen mit 7- und 30-Tage-Durchschnitten. "
                       "Steigende Linien weisen auf einen Aufwärtstrend im Verbrauch hin.", flex="2"),
        ], style={"display": "flex", "gap": "16px"}),
        html.Div([
            chart_card("chart-yearly", "Jahresvergleich",
                       "Vergleicht den monatlichen Durchschnittsverbrauch über die Jahre 2006–2010. "
                       "Saisonale Muster werden so über mehrere Jahre sichtbar.", flex="2"),
            chart_card("chart-compare", "Periodenvergleich",
                       "Stellt die letzten 30 Tage den vorherigen 30 Tagen gegenüber. "
                       "Zeigt ob der Verbrauch zuletzt gestiegen oder gesunken ist.", flex="1"),
        ], style={"display": "flex", "gap": "16px"}),
    ])


def tab_patterns():
    return html.Div([
        html.Div([
            chart_card("chart-heatmap", "Heatmap: Stunde × Wochentag",
                       "Zeigt wann am meisten Strom verbraucht wird. Dunklere Felder bedeuten "
                       "höheren Verbrauch — typisch sind Abendstunden und Wochenenden.", flex="2"),
            chart_card("chart-weekday", "Verbrauch nach Wochentag",
                       "Vergleicht den Durchschnittsverbrauch pro Wochentag. "
                       "Höhere Balken am Wochenende deuten auf vermehrte Haushaltsaktivität hin."),
        ], style={"display": "flex", "gap": "16px"}),
        html.Div([
            chart_card("chart-hourly", "Tageszeit-Profil",
                       "Durchschnittlicher Verbrauch nach Stunde (0–23 Uhr). "
                       "Morgendliche und abendliche Spitzen entsprechen den typischen Aktivitätszeiten."),
            chart_card("chart-monthly", "Saisonalität",
                       "Monatlicher Durchschnittsverbrauch über alle Jahre. "
                       "Wintermonate (Nov–Feb) zeigen typischerweise höheren Verbrauch durch Heizung und Beleuchtung."),
            chart_card("chart-daytime", "Tageszeit-Kategorien",
                       "Fasst den Verbrauch in vier Blöcke zusammen: Nacht, Morgen, Tag und Abend. "
                       "Zeigt in welcher Tagesphase am meisten Energie verbraucht wird."),
        ], style={"display": "flex", "gap": "16px"}),
    ])


def tab_submetering():
    return html.Div([
        html.Div([
            chart_card("chart-sub-pie", "Verbrauchsverteilung",
                       "Anteil der Gerätegruppen am Gesamtverbrauch: Küche (Sub 1), "
                       "Waschkeller (Sub 2), Heizung/AC (Sub 3) und Sonstiges (nicht erfasst)."),
            chart_card("chart-sub-monthly", "Submetering-Verlauf",
                       "Monatliche Entwicklung der einzelnen Verbrauchsgruppen. "
                       "Saisonale Unterschiede zeigen z.\u202fB. erhöhten Heizungsverbrauch im Winter.", flex="2"),
        ], style={"display": "flex", "gap": "16px"}),
        chart_card("chart-weekend", "Wochenende vs. Werktag",
                   "Vergleicht den Durchschnittsverbrauch an Werktagen und Wochenenden nach Kategorie. "
                   "Unterschiede zeigen veränderte Nutzungsmuster an freien Tagen."),
    ])


def tab_advanced():
    return html.Div([
        html.Div([
            chart_card("chart-anomaly", "Anomalie-Erkennung",
                       "Identifiziert Tage mit statistisch ungewöhnlichem Verbrauch (Z-Score > 2σ). "
                       "Rote Punkte markieren Ausreißer — mögliche Ursachen sind Feiertage, Gerätedefekte oder Gäste.", flex="2"),
            chart_card("chart-peak-days", "Top 20 Spitzentage",
                       "Die 20 Tage mit dem höchsten Momentanverbrauch (Peak kW). "
                       "Häufungen in bestimmten Monaten können auf saisonale Lastspitzen hindeuten."),
        ], style={"display": "flex", "gap": "16px"}),
        html.Div([
            chart_card("chart-efficiency", "Messeffizienz",
                       "Anteil des Verbrauchs der durch Submetering erfasst wird (in %). "
                       "Werte unter 50% bedeuten, dass mehr als die Hälfte der Energie nicht zugeordnet werden kann."),
            chart_card("chart-reactive", "Leistungsfaktor",
                       "Verhältnis von Blindleistung zu Wirkleistung. "
                       "Hohe Werte deuten auf induktive Lasten (Motoren, Klimaanlagen) hin, die das Netz zusätzlich belasten."),
            chart_card("chart-hidden", "Unkontrollierter Verbrauch",
                       "Energie die nicht durch die drei Submetering-Zähler erfasst wird (in Wh). "
                       "Umfasst z.\u202fB. Beleuchtung, Unterhaltungselektronik und Standby-Verbrauch."),
        ], style={"display": "flex", "gap": "16px"}),
    ])


def tab_forecast():
    return html.Div([
        chart_card("chart-forecast", "30-Tage-Prognose (Prophet)",
                   "Machine-Learning-basierte Vorhersage des Tagesverbrauchs. "
                   "Das schattierte Band zeigt das 80%-Konfidenzintervall — der tatsächliche Verbrauch liegt mit hoher Wahrscheinlichkeit darin."),
        html.Div([
            chart_card("chart-corr", "Korrelationsmatrix",
                       "Zeigt statistische Zusammenhänge zwischen den Messvariablen (–1 bis +1). "
                       "Werte nahe +1 bedeuten starken Gleichlauf, Werte nahe –1 gegenläufige Entwicklung."),
            chart_card("chart-voltage", "Spannungsstabilität",
                       "Tägliche Min-/Durchschnitts-/Max-Spannung im Netz (230V Nennwert). "
                       "Starke Schwankungen können auf Netzprobleme oder hohe Lastspitzen hinweisen."),
        ], style={"display": "flex", "gap": "16px"}),
    ])


def create_layout():
    return html.Div([
        html.Link(rel="stylesheet",
                  href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap"),

        # Zoom-Modal (rein JS-basiert, siehe assets/zoom.js)
        zoom_modal(),

        # ── Header ──────────────────────────────────────────────────────────
        html.Div([
            html.Div([
                html.Div([
                    html.Span("Stromverbrauch", style={"fontWeight": "700", "fontSize": "52px", "color": C["accent"]}),
                    html.Span(" Dashboard", style={"fontWeight": "400", "fontSize": "52px",
                                                    "opacity": "0.85"}),
                ], style={"fontFamily": FONT_BODY, "color": C["text"]}),
                html.P("Analyse des Haushalt-Stromverbrauchs 2006–2010 · Quelle: UCI Machine Learning Repository",
                       style={"fontSize": "16px", "color": C["text_sm"],
                              "margin": "10px 0 0 0", "fontFamily": FONT_BODY}),
            ]),
        ], style={
            "background": C["surface"],
            "borderBottom": f"1px solid {C['border']}",
            "padding": "32px 32px",
            "marginBottom": "24px",
        }),

        # ── Content ─────────────────────────────────────────────────────────
        html.Div([
            filter_bar(),
            kpi_cards(),

            # dcc.Store für gecachte Daten
            dcc.Store(id="store-forecast"),

            dcc.Tabs(id="tabs", value="overview", children=[
                dcc.Tab(label="Übersicht",     value="overview",    style=TAB_STYLE, selected_style=TAB_SELECTED),
                dcc.Tab(label="Verbrauchsmuster", value="patterns", style=TAB_STYLE, selected_style=TAB_SELECTED),
                dcc.Tab(label="Submetering",   value="submetering", style=TAB_STYLE, selected_style=TAB_SELECTED),
                dcc.Tab(label="Anomalien",     value="advanced",    style=TAB_STYLE, selected_style=TAB_SELECTED),
                dcc.Tab(label="Prognose",      value="forecast",    style=TAB_STYLE, selected_style=TAB_SELECTED),
            ], style={"marginBottom": "20px", "fontFamily": FONT_BODY}),

            html.Div(id="tab-content"),
        ], style={"padding": "0 32px"}),

        # ── Footer ──────────────────────────────────────────────────────────
        html.Footer([
            html.Hr(style={"border": "none", "borderTop": f"1px solid {C['border']}", "margin": "32px 0 16px"}),
            html.Div([
                html.Span("Datenquelle: ", style={"fontWeight": "600"}),
                html.A("UCI Machine Learning Repository — Individual Household Electric Power Consumption",
                       href="https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption",
                       target="_blank",
                       style={"color": C["accent"], "textDecoration": "none"}),
            ]),
            html.P("Aufgezeichnet in Sceaux, Frankreich · Zeitraum: Dezember 2006 – November 2010 · Auflösung: 1 Minute",
                   style={"color": C["text_sm"], "marginTop": "4px"}),
        ], style={
            "padding": "0 32px 32px",
            "fontFamily": FONT_BODY,
            "fontSize": "13px",
            "color": C["text_md"],
        }),

    ], style={"backgroundColor": C["bg"], "minHeight": "100vh",
              "fontFamily": FONT_BODY, "color": C["text"]})
