import logging

from dash import Input, Output, State, html, dcc, callback_context, no_update
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sqlalchemy import text

from utils.data_connector import engine
from config import C, FONT_BODY, FONT_MONO, WEEKDAY_MAP, WEEKDAY_ORDER, WEEKDAY_TO_NUM

logger = logging.getLogger(__name__)

FONT_UI = "Barlow, Inter, sans-serif"
FONT_DATA = "IBM Plex Mono, JetBrains Mono, monospace"

# Graustufen-Palette + Akzent nur für das Wichtigste
GRAYS = ["#78716c", "#a8a29e", "#d6d3d1", "#57534e", "#44403c"]

CHART_BASE = dict(
    paper_bgcolor=C["surface"],
    plot_bgcolor=C["surface"],
    font=dict(color=C["text"], family=FONT_UI, size=15),
    xaxis=dict(gridcolor=C["grid"], linecolor=C["border"],
               tickfont=dict(size=13, family=FONT_DATA), title_font=dict(size=14)),
    yaxis=dict(gridcolor=C["grid"], linecolor=C["border"],
               tickfont=dict(size=13, family=FONT_DATA), title_font=dict(size=14)),
    margin=dict(l=56, r=20, t=48, b=56),
    title_font=dict(size=16, color=C["text"]),
    legend=dict(font=dict(size=13)),
    colorway=[C["accent"], "#57534e", "#a8a29e", "#d6d3d1", "#78716c", "#44403c"],
)


def apply_base(fig):
    fig.update_layout(**CHART_BASE)
    return fig


def build_query(base_sql, start=None, end=None, year=None, weekdays=None):
    """Build a parameterized query with WHERE clauses. Returns (sql_text, params)."""
    clauses = []
    params = {}

    if start:
        clauses.append("timestamp >= :start")
        params["start"] = start
    if end:
        clauses.append("timestamp <= CAST(:end_date AS date) + INTERVAL '1 day' - INTERVAL '1 second'")
        params["end_date"] = end
    if year and year != "all":
        clauses.append("year = :year")
        params["year"] = int(year)
    if weekdays:
        # weekdays kommen jetzt als Wörter ("Mo", "Di", ...) — in Nummern umwandeln
        nums = [WEEKDAY_TO_NUM[w] for w in weekdays if w in WEEKDAY_TO_NUM]
        if nums:
            placeholders = ", ".join(f":wd{i}" for i in range(len(nums)))
            clauses.append(f"weekday IN ({placeholders})")
            for i, n in enumerate(nums):
                params[f"wd{i}"] = n

    where = "WHERE " + " AND ".join(clauses) if clauses else ""
    full_sql = base_sql.replace("{where}", where)
    return text(full_sql), params


def sparkline(values):
    """Tiny inline sparkline — single accent color, no fill."""
    fig = go.Figure(go.Scatter(
        y=values, mode="lines",
        line=dict(color=C["accent"], width=1.5),
    ))
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False), yaxis=dict(visible=False),
        height=50, showlegend=False,
    )
    return fig


def kpi_card(label, value, unit, delta_text, spark_values, description=""):
    is_positive = "+" in delta_text
    is_negative = delta_text.startswith("-")
    delta_color = C["accent"] if is_positive or is_negative else C["text_sm"]
    return html.Div([
        # Vertikaler Akzent-Strich links
        html.Div(style={
            "position": "absolute", "left": "0", "top": "12px", "bottom": "12px",
            "width": "3px", "borderRadius": "0 2px 2px 0",
            "background": C["accent"],
        }),
        html.Div([
            html.Div(label, style={
                "fontSize": "11px", "fontWeight": "600", "color": C["text_sm"],
                "letterSpacing": "0.06em", "marginBottom": "8px",
                "fontFamily": FONT_UI,
            }),
            html.Div([
                html.Span(value, style={
                    "fontSize": "28px", "fontWeight": "700", "color": C["text"],
                    "fontFamily": FONT_DATA, "letterSpacing": "-0.02em",
                }),
                html.Span(f" {unit}", style={
                    "fontSize": "13px", "color": C["text_sm"], "marginLeft": "4px",
                    "fontFamily": FONT_DATA,
                }),
            ]),
            html.Div(delta_text, style={
                "fontSize": "12px", "color": delta_color, "marginTop": "4px",
                "fontWeight": "500", "fontFamily": FONT_DATA,
            }),
            html.Div(description, style={
                "fontSize": "11px", "color": C["text_sm"], "marginTop": "8px",
                "lineHeight": "1.4", "borderTop": f"1px solid {C['border_lt']}",
                "paddingTop": "6px", "fontFamily": FONT_UI,
            }) if description else None,
        ], style={"paddingLeft": "12px"}),
        html.Div(
            dcc.Graph(figure=spark_values, config={"staticPlot": True},
                      style={"height": "50px"}),
            style={"marginTop": "8px", "paddingLeft": "12px"},
        ),
    ], style={
        "position": "relative",
        "background": C["surface"],
        "border": f"1px solid {C['border']}",
        "borderRadius": "8px",
        "padding": "16px 20px 12px",
        "boxShadow": "0 1px 3px rgba(0,0,0,0.04)",
    })


def register_callbacks(app):

    @app.callback(Output("tab-content", "children"), Input("tabs", "value"))
    def render_tab(tab):
        from layout import tab_overview, tab_patterns, tab_submetering, tab_advanced, tab_forecast
        return {"overview": tab_overview, "patterns": tab_patterns,
                "submetering": tab_submetering, "advanced": tab_advanced,
                "forecast": tab_forecast}[tab]()

    # ── KPI Cards with Sparklines ────────────────────────────────────────────
    @app.callback(
        Output("kpi-cards", "children"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def update_kpis(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT AVG(global_active_power) AS avg_power,
                   MAX(global_active_power) AS max_power,
                   SUM(global_active_power * 1.0 / 60) AS total_kwh,
                   AVG(unmetered_energy)    AS avg_hidden
            FROM power_features {where}
        """, start, end, year, weekdays)
        df_kpi = pd.read_sql(sql, engine, params=params)

        # Sparkline data
        sql_spark, params_spark = build_query("""
            SELECT DATE(timestamp) AS day, AVG(global_active_power) AS v
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY day
        """, start, end, year, weekdays)
        df_spark = pd.read_sql(sql_spark, engine, params=params_spark)

        # Delta vs previous period
        def get_delta(current_val, col):
            try:
                df_prev = pd.read_sql(
                    text(f"""
                        SELECT AVG({col}) AS v FROM power_features
                        WHERE timestamp < :start AND timestamp >= CAST(:start AS date) - INTERVAL '90 days'
                    """),
                    engine,
                    params={"start": start},
                )
                prev = df_prev["v"].iloc[0]
                if prev and prev != 0:
                    pct = (current_val - prev) / prev * 100
                    sign = "+" if pct > 0 else ""
                    return f"{sign}{pct:.1f}% ggü. Vorperiode"
            except Exception:
                logger.exception("Fehler beim Berechnen des Delta für %s", col)
            return "kein Vergleich verfügbar"

        row = df_kpi.iloc[0]
        spark = df_spark["v"].dropna().tolist()

        return [
            kpi_card("Ø WIRKLEISTUNG", f"{row['avg_power']:.3f}", "kW",
                     get_delta(row['avg_power'], 'global_active_power'),
                     sparkline(spark),
                     "Mittlere Leistungsaufnahme des Haushalts im gewählten Zeitraum"),
            kpi_card("SPITZENLEISTUNG", f"{row['max_power']:.3f}", "kW",
                     "Höchstwert im Zeitraum",
                     sparkline(df_spark["v"].rolling(7).max().dropna().tolist()),
                     "Höchster gemessener Momentanverbrauch — relevant für Netzdimensionierung"),
            kpi_card("GESAMTVERBRAUCH", f"{row['total_kwh']:,.0f}", "kWh",
                     "Summe im gewählten Zeitraum",
                     sparkline(df_spark["v"].cumsum().tolist()),
                     "Kumulierter Energieverbrauch — Basis für Kostenberechnung"),
            kpi_card("Ø UNGEMESSENER VERBR.", f"{row['avg_hidden']:.3f}", "Wh",
                     "Nicht durch Submetering erfasst",
                     sparkline(spark),
                     "Differenz zwischen Gesamtverbrauch und Summe der drei Sub-Zähler"),
        ]

    # ── ÜBERSICHT ────────────────────────────────────────────────────────────
    @app.callback(
        Output("chart-daily", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
        Input("metric-picker", "value"),
    )
    def chart_daily(start, end, year, weekdays, metric):
        sql, params = build_query("""
            SELECT DATE(timestamp) AS day,
                AVG(global_active_power) AS avg_power,
                SUM(global_active_power * 1.0 / 60) AS total_power,
                MAX(global_active_power) AS peak_power
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY day
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        label_map = {"avg_power": "Ø kW", "total_power": "kWh", "peak_power": "Max kW"}
        fig = px.line(df, x="day", y=metric,
                      labels={metric: label_map.get(metric, "kW"), "day": "Datum"})
        fig.update_traces(line_color=C["accent"])
        return apply_base(fig)

    @app.callback(
        Output("chart-rolling", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_rolling(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT DATE(timestamp) AS day, AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY day
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        df["7-Tage-Schnitt"]  = df["avg_power"].rolling(7).mean()
        df["30-Tage-Schnitt"] = df["avg_power"].rolling(30).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["day"], y=df["avg_power"], name="Täglich",
                                  line=dict(color=C["border"], width=1)))
        fig.add_trace(go.Scatter(x=df["day"], y=df["7-Tage-Schnitt"], name="7-Tage-Schnitt",
                                  line=dict(color=C["accent"], width=2)))
        fig.add_trace(go.Scatter(x=df["day"], y=df["30-Tage-Schnitt"], name="30-Tage-Schnitt",
                                  line=dict(color=C["gray600"], width=2, dash="dot")))
        fig.update_layout(yaxis_title="kW", xaxis_title="Datum")
        return apply_base(fig)

    @app.callback(
        Output("chart-yearly", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("weekday-filter", "value"),
    )
    def chart_yearly(start, end, weekdays):
        sql, params = build_query("""
            SELECT year, month, AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY year, month ORDER BY year, month
        """, start, end, None, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        df["year"] = df["year"].astype(int).astype(str)
        year_colors = {"2006": "#FFD54F", "2007": "#FF872C", "2008": "#FE612C",
                       "2009": "#FD3A2D", "2010": "#9B0D14"}
        fig = px.line(df, x="month", y="avg_power", color="year",
                      color_discrete_map=year_colors,
                      labels={"avg_power": "Ø kW", "month": "Monat", "year": "Jahr"})
        fig.update_xaxes(tickvals=list(range(1, 13)),
                         ticktext=["Jan", "Feb", "Mär", "Apr", "Mai", "Jun",
                                   "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"])
        return apply_base(fig)

    @app.callback(
        Output("chart-compare", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_compare(start, end, year, weekdays):
        # Build base filter + zusätzlich auf letzte 60 Tage einschränken
        _, params = build_query("SELECT 1 FROM power_features {where}", start, end, year, weekdays)
        # Manuell den 60-Tage-Filter hinzufügen
        clauses = []
        if start:
            clauses.append("timestamp >= :start")
        if end:
            clauses.append("timestamp <= CAST(:end_date AS date) + INTERVAL '1 day' - INTERVAL '1 second'")
        if year and year != "all":
            clauses.append("year = :year")
        if weekdays:
            nums = [WEEKDAY_TO_NUM[w] for w in weekdays if w in WEEKDAY_TO_NUM]
            if nums:
                placeholders = ", ".join(f":wd{i}" for i in range(len(nums)))
                clauses.append(f"weekday IN ({placeholders})")
        clauses.append("DATE(timestamp) >= (SELECT MAX(DATE(timestamp)) - INTERVAL '60 days' FROM power_features)")
        where = "WHERE " + " AND ".join(clauses)

        df = pd.read_sql(text(f"""
            SELECT
                CASE
                    WHEN DATE(timestamp) >= (SELECT MAX(DATE(timestamp)) - INTERVAL '30 days' FROM power_features)
                    THEN 'Letzte 30 Tage'
                    ELSE 'Vorherige 30 Tage'
                END AS periode,
                AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY periode
        """), engine, params=params)
        fig = px.bar(df, x="periode", y="avg_power",
                     color="periode",
                     color_discrete_map={"Letzte 30 Tage": C["accent"], "Vorherige 30 Tage": C["border"]},
                     labels={"avg_power": "Ø kW", "periode": ""})
        fig.update_layout(showlegend=False)
        return apply_base(fig)

    # ── MUSTER ──────────────────────────────────────────────────────────────
    @app.callback(
        Output("chart-heatmap", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_heatmap(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT hour, weekday, AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY hour, weekday ORDER BY weekday, hour
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        df["weekday"] = df["weekday"].map(WEEKDAY_MAP)
        pivot = df.pivot(index="weekday", columns="hour", values="avg_power")
        pivot = pivot.reindex(WEEKDAY_ORDER)
        fig = px.imshow(pivot,
                        labels=dict(x="Uhrzeit (h)", y="", color="Ø kW"),
                        color_continuous_scale=[[0, "#FFD54F"], [0.35, "#FF872C"], [0.65, "#FE612C"], [1, "#9B0D14"]],
                        aspect="auto")
        fig.update_layout(coloraxis_colorbar=dict(title="Ø kW"))
        return apply_base(fig)

    @app.callback(
        Output("chart-weekday", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),
    )
    def chart_weekday(start, end, year):
        sql, params = build_query("""
            SELECT weekday, AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY weekday ORDER BY weekday
        """, start, end, year, None)
        df = pd.read_sql(sql, engine, params=params)
        df["weekday"] = df["weekday"].map(WEEKDAY_MAP)
        df["weekday"] = pd.Categorical(df["weekday"], categories=WEEKDAY_ORDER, ordered=True)
        df = df.sort_values("weekday")
        fig = px.bar(df, x="weekday", y="avg_power",
                     labels={"avg_power": "Ø kW", "weekday": ""},
                     color="avg_power",
                     color_continuous_scale=[[0, "#FFD54F"], [0.5, "#FE612C"], [1, "#9B0D14"]])
        fig.update_layout(coloraxis_showscale=False)
        return apply_base(fig)

    @app.callback(
        Output("chart-hourly", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_hourly(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT hour, AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY hour ORDER BY hour
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        fig = px.line(df, x="hour", y="avg_power",
                      labels={"avg_power": "Ø kW", "hour": "Uhrzeit (h)"})
        fig.update_traces(line_color=C["accent"], line_width=2)
        return apply_base(fig)

    @app.callback(
        Output("chart-monthly", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_monthly(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT month, AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY month ORDER BY month
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        fig = px.line(df, x="month", y="avg_power",
                      labels={"avg_power": "Ø kW", "month": "Monat"},
                      markers=True)
        fig.update_traces(line_color=C["accent"], line_width=2,
                          marker=dict(size=7, color=C["accent"]))
        fig.update_xaxes(tickvals=list(range(1, 13)),
                         ticktext=["Jan", "Feb", "Mär", "Apr", "Mai", "Jun",
                                   "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"])
        return apply_base(fig)

    @app.callback(
        Output("chart-daytime", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_daytime(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT
                CASE
                    WHEN hour BETWEEN 0 AND 5  THEN 'Nacht (0–5h)'
                    WHEN hour BETWEEN 6 AND 11 THEN 'Morgen (6–11h)'
                    WHEN hour BETWEEN 12 AND 17 THEN 'Tag (12–17h)'
                    ELSE 'Abend (18–23h)'
                END AS daytime,
                AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY daytime
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        order = ["Nacht (0–5h)", "Morgen (6–11h)", "Tag (12–17h)", "Abend (18–23h)"]
        df["daytime"] = pd.Categorical(df["daytime"], categories=order, ordered=True)
        df = df.sort_values("daytime")
        fig = px.bar(df, x="daytime", y="avg_power",
                     labels={"avg_power": "Ø kW", "daytime": ""},
                     color="avg_power",
                     color_continuous_scale=[[0, "#FFD54F"], [0.5, "#FE612C"], [1, "#9B0D14"]])
        fig.update_layout(coloraxis_showscale=False)
        return apply_base(fig)

    # ── SUBMETERING ──────────────────────────────────────────────────────────
    @app.callback(
        Output("chart-sub-pie", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_sub_pie(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT AVG(sub_metering_1) AS kitchen,
                   AVG(sub_metering_2) AS laundry,
                   AVG(sub_metering_3) AS heating,
                   AVG(unmetered_energy) AS other
            FROM power_features {where}
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        rename = {"kitchen": "Küche", "laundry": "Waschkeller", "heating": "Heizung/AC", "other": "Sonstiges"}
        df = df.rename(columns=rename)
        row = df.iloc[0]
        fig = px.pie(values=row.values, names=row.index,
                     color_discrete_sequence=["#9B0D14", "#FD3A2D", "#FE612C", "#FF872C"],
                     hole=0.35)
        fig.update_traces(textfont_size=13)
        return apply_base(fig)

    @app.callback(
        Output("chart-sub-monthly", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_sub_monthly(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT year, month,
                AVG(sub_metering_1) AS kitchen,
                AVG(sub_metering_2) AS laundry,
                AVG(sub_metering_3) AS heating,
                AVG(unmetered_energy) AS other
            FROM power_features {where}
            GROUP BY year, month ORDER BY year, month
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        rename = {"kitchen": "Küche", "laundry": "Waschkeller", "heating": "Heizung/AC", "other": "Sonstiges"}
        df = df.rename(columns=rename)
        df["period"] = (df["year"].astype(int).astype(str) + "-" +
                        df["month"].astype(int).astype(str).str.zfill(2))
        df_melted = df.melt(id_vars="period",
                            value_vars=["Küche", "Waschkeller", "Heizung/AC", "Sonstiges"],
                            var_name="Gerät", value_name="Wh")
        red_shades = {"Küche": "#9B0D14", "Waschkeller": "#FD3A2D",
                      "Heizung/AC": "#FE612C", "Sonstiges": "#FFD54F"}
        fig = px.area(df_melted, x="period", y="Wh", color="Gerät",
                      color_discrete_map=red_shades,
                      labels={"period": "Monat"})
        fig.update_xaxes(tickangle=45)
        return apply_base(fig)

    @app.callback(
        Output("chart-weekend", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),
    )
    def chart_weekend(start, end, year):
        sql, params = build_query("""
            SELECT is_weekend,
                AVG(global_active_power) AS active_power,
                AVG(sub_metering_1) AS kitchen,
                AVG(sub_metering_2) AS laundry,
                AVG(sub_metering_3) AS heating
            FROM power_features {where}
            GROUP BY is_weekend
        """, start, end, year, None)
        df = pd.read_sql(sql, engine, params=params)
        df["is_weekend"] = df["is_weekend"].astype(int).map({0: "Werktag", 1: "Wochenende"})
        rename = {"active_power": "Wirkleistung", "kitchen": "Küche", "laundry": "Waschkeller", "heating": "Heizung/AC"}
        df = df.rename(columns=rename)
        df_melted = df.melt(id_vars="is_weekend",
                            value_vars=["Wirkleistung", "Küche", "Waschkeller", "Heizung/AC"],
                            var_name="Kategorie", value_name="Ø kW / Wh")
        red_shades = {"Wirkleistung": "#9B0D14", "Küche": "#FD3A2D",
                      "Waschkeller": "#FE612C", "Heizung/AC": "#FFD54F"}
        fig = px.bar(df_melted, x="is_weekend", y="Ø kW / Wh", color="Kategorie",
                     color_discrete_map=red_shades,
                     barmode="group",
                     labels={"is_weekend": ""})
        return apply_base(fig)

    # ── ANOMALIEN ────────────────────────────────────────────────────────────
    @app.callback(
        Output("chart-anomaly", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_anomaly(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT DATE(timestamp) AS day, AVG(global_active_power) AS avg_power
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY day
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        mean, std = df["avg_power"].mean(), df["avg_power"].std()
        df["zscore"]  = (df["avg_power"] - mean) / std
        df["Anomalie"] = df["zscore"].abs() > 2
        fig = px.scatter(df, x="day", y="avg_power", color="Anomalie",
                         color_discrete_map={False: C["gray400"], True: C["accent"]},
                         labels={"avg_power": "Ø kW", "day": "Datum"})
        fig.add_hline(y=mean + 2*std, line_dash="dash", line_color=C["accent"],
                      annotation_text="+2σ", annotation_font_size=12)
        fig.add_hline(y=mean - 2*std, line_dash="dash", line_color=C["accent"],
                      annotation_text="−2σ", annotation_font_size=12)
        return apply_base(fig)

    @app.callback(
        Output("chart-peak-days", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),
    )
    def chart_peak_days(start, end, year):
        sql, params = build_query("""
            SELECT DATE(timestamp) AS day, MAX(global_active_power) AS peak_power
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY peak_power DESC LIMIT 20
        """, start, end, year, None)
        df = pd.read_sql(sql, engine, params=params)
        df["day"] = df["day"].astype(str)
        fig = px.bar(df, x="day", y="peak_power",
                     labels={"peak_power": "Max kW", "day": ""},
                     color="peak_power",
                     color_continuous_scale=[[0, "#FFD54F"], [0.5, "#FE612C"], [1, "#9B0D14"]])
        fig.update_xaxes(tickangle=45, tickfont=dict(size=11))
        fig.update_layout(coloraxis_showscale=False)
        return apply_base(fig)

    @app.callback(
        Output("chart-efficiency", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_efficiency(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT DATE(timestamp) AS day,
                ROUND(CAST(AVG(sub_metering_1 + sub_metering_2 + sub_metering_3) /
                    NULLIF(AVG(global_active_power * 1000 / 60), 0) * 100 AS numeric), 1) AS efficiency_pct
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY day
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        fig = px.line(df, x="day", y="efficiency_pct",
                      labels={"efficiency_pct": "Effizienz (%)", "day": "Datum"})
        fig.update_traces(line_color=C["accent"])
        fig.add_hline(y=float(df["efficiency_pct"].mean()), line_dash="dash",
                      line_color=C["gray600"],
                      annotation_text=f"Ø {df['efficiency_pct'].mean():.1f}%",
                      annotation_font_size=12)
        return apply_base(fig)

    @app.callback(
        Output("chart-reactive", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_reactive(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT DATE(timestamp) AS day,
                ROUND(CAST(AVG(global_reactive_power) /
                    NULLIF(AVG(global_active_power), 0) AS numeric), 3) AS power_factor
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY day
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        fig = px.line(df, x="day", y="power_factor",
                      labels={"power_factor": "Faktor (Blind/Wirk)", "day": "Datum"})
        fig.update_traces(line_color=C["accent"])
        return apply_base(fig)

    @app.callback(
        Output("chart-hidden", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_hidden(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT DATE(timestamp) AS day, AVG(unmetered_energy) AS avg_hidden
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY day
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        fig = px.line(df, x="day", y="avg_hidden",
                      labels={"avg_hidden": "Ø Wh", "day": "Datum"})
        fig.update_traces(line_color=C["accent"])
        return apply_base(fig)

    # ── FORECAST (mit dcc.Store Cache) ───────────────────────────────────────
    @app.callback(
        Output("store-forecast", "data"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),
    )
    def compute_forecast(start, end, year):
        """Train Prophet once and cache result in dcc.Store."""
        sql, params = build_query("""
            SELECT DATE(timestamp) AS ds, AVG(global_active_power) AS y
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY ds
        """, start, end, year, None)
        df = pd.read_sql(sql, engine, params=params)

        try:
            from prophet import Prophet
            model = Prophet(yearly_seasonality=True, weekly_seasonality=True)
            model.fit(df)
            future = model.make_future_dataframe(periods=30)
            forecast = model.predict(future)
            return {
                "actual_ds": df["ds"].astype(str).tolist(),
                "actual_y": df["y"].tolist(),
                "forecast_ds": forecast["ds"].astype(str).tolist(),
                "yhat": forecast["yhat"].tolist(),
                "yhat_upper": forecast["yhat_upper"].tolist(),
                "yhat_lower": forecast["yhat_lower"].tolist(),
            }
        except Exception as e:
            logger.exception("Prophet-Forecast fehlgeschlagen")
            return {"error": str(e)}

    @app.callback(
        Output("chart-forecast", "figure"),
        Input("store-forecast", "data"),
    )
    def chart_forecast(data):
        """Render forecast from cached dcc.Store data."""
        fig = go.Figure()
        if not data or "error" in data:
            msg = data.get("error", "Keine Daten") if data else "Keine Daten"
            fig.add_annotation(text=f"Prognose nicht verfügbar: {msg}",
                               xref="paper", yref="paper", x=0.5, y=0.5,
                               showarrow=False, font=dict(size=14))
            return apply_base(fig)

        fig.add_trace(go.Scatter(x=data["actual_ds"], y=data["actual_y"], name="Tatsächlich",
                                  line=dict(color=C["accent"], width=1.5)))
        fig.add_trace(go.Scatter(x=data["forecast_ds"], y=data["yhat"], name="Prognose",
                                  line=dict(color=C["accent"], dash="dash", width=2)))
        fc_ds = data["forecast_ds"]
        fig.add_trace(go.Scatter(
            x=fc_ds + fc_ds[::-1],
            y=data["yhat_upper"] + data["yhat_lower"][::-1],
            fill="toself", fillcolor=C["accent_lt"],
            line=dict(color="rgba(0,0,0,0)"), name="Konfidenzintervall",
        ))
        fig.update_layout(yaxis_title="kW", xaxis_title="Datum")
        return apply_base(fig)

    @app.callback(
        Output("chart-corr", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),
    )
    def chart_corr(start, end, year):
        sql, params = build_query("""
            SELECT global_active_power, global_reactive_power, voltage,
                   sub_metering_1, sub_metering_2, sub_metering_3, unmetered_energy
            FROM power_features {where} LIMIT 100000
        """, start, end, year, None)
        df = pd.read_sql(sql, engine, params=params)
        df.columns = ["Wirkleistung", "Blindleistung", "Spannung",
                      "Küche", "Waschkeller", "Heizung", "Ungemessen"]
        corr = df.corr()
        fig = px.imshow(corr, color_continuous_scale="RdBu", zmin=-1, zmax=1,
                        text_auto=".2f")
        fig.update_traces(textfont_size=12)
        return apply_base(fig)

    @app.callback(
        Output("chart-voltage", "figure"),
        Input("date-range", "start_date"), Input("date-range", "end_date"),
        Input("year-picker", "value"),     Input("weekday-filter", "value"),
    )
    def chart_voltage(start, end, year, weekdays):
        sql, params = build_query("""
            SELECT DATE(timestamp) AS day,
                AVG(voltage) AS avg_voltage,
                MIN(voltage) AS min_voltage,
                MAX(voltage) AS max_voltage
            FROM power_features {where}
            GROUP BY DATE(timestamp) ORDER BY day
        """, start, end, year, weekdays)
        df = pd.read_sql(sql, engine, params=params)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df["day"], y=df["max_voltage"], name="Maximum",
                                  line=dict(color=C["gray400"], width=1)))
        fig.add_trace(go.Scatter(x=df["day"], y=df["avg_voltage"], name="Durchschnitt",
                                  line=dict(color=C["accent"], width=2)))
        fig.add_trace(go.Scatter(x=df["day"], y=df["min_voltage"], name="Minimum",
                                  line=dict(color=C["gray400"], width=1)))
        fig.update_layout(yaxis_title="Volt (V)", xaxis_title="Datum")
        return apply_base(fig)

    # Zoom wird komplett clientseitig in assets/zoom.js gehandelt
