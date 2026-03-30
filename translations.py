"""
Alle übersetzbaren UI-Strings des Dashboards.
Schlüssel = interner Name, Wert = Dict mit Sprachcodes.
"""

T = {
    # ── Header ────────────────────────────────────────────────────────────────
    "header_title_1":    {"de": "Stromverbrauch", "en": "Power Consumption", "es": "Consumo Eléctrico", "uk": "Споживання електроенергії", "ar": "استهلاك الطاقة"},
    "header_title_2":    {"de": " Dashboard", "en": " Dashboard", "es": " Dashboard", "uk": " Дашборд", "ar": " لوحة المعلومات"},
    "header_subtitle":   {
        "de": "Analyse des Haushalt-Stromverbrauchs 2006–2010 · Quelle: UCI Machine Learning Repository",
        "en": "Household power consumption analysis 2006–2010 · Source: UCI Machine Learning Repository",
        "es": "Análisis del consumo eléctrico doméstico 2006–2010 · Fuente: UCI Machine Learning Repository",
        "uk": "Аналіз побутового споживання електроенергії 2006–2010 · Джерело: UCI Machine Learning Repository",
        "ar": "تحليل استهلاك الطاقة المنزلية 2006–2010 · المصدر: UCI Machine Learning Repository",
    },

    # ── Filter Bar ────────────────────────────────────────────────────────────
    "filter_period":     {"de": "Zeitraum", "en": "Period", "es": "Período", "uk": "Період", "ar": "الفترة"},
    "filter_metric":     {"de": "Metrik", "en": "Metric", "es": "Métrica", "uk": "Метрика", "ar": "المقياس"},
    "filter_year":       {"de": "Jahr", "en": "Year", "es": "Año", "uk": "Рік", "ar": "السنة"},
    "filter_weekday":    {"de": "Wochentage filtern", "en": "Filter weekdays", "es": "Filtrar días", "uk": "Фільтр днів тижня", "ar": "تصفية أيام الأسبوع"},
    "filter_all_years":  {"de": "Alle Jahre", "en": "All years", "es": "Todos los años", "uk": "Усі роки", "ar": "كل السنوات"},
    "filter_all_weekdays": {"de": "Alle Wochentage", "en": "All weekdays", "es": "Todos los días", "uk": "Усі дні тижня", "ar": "كل أيام الأسبوع"},
    "filter_language":   {"de": "Sprache", "en": "Language", "es": "Idioma", "uk": "Мова", "ar": "اللغة"},

    # ── Metric Options ────────────────────────────────────────────────────────
    "metric_avg":        {"de": "Durchschnittlicher Verbrauch (kW)", "en": "Average consumption (kW)", "es": "Consumo promedio (kW)", "uk": "Середнє споживання (кВт)", "ar": "متوسط الاستهلاك (كيلوواط)"},
    "metric_total":      {"de": "Gesamtverbrauch (kWh)", "en": "Total consumption (kWh)", "es": "Consumo total (kWh)", "uk": "Загальне споживання (кВт·год)", "ar": "إجمالي الاستهلاك (كيلوواط/ساعة)"},
    "metric_peak":       {"de": "Spitzenverbrauch (kW)", "en": "Peak consumption (kW)", "es": "Consumo pico (kW)", "uk": "Пікове споживання (кВт)", "ar": "ذروة الاستهلاك (كيلوواط)"},

    # ── Weekday Options ───────────────────────────────────────────────────────
    "wd_mo": {"de": "Montag",     "en": "Monday",    "es": "Lunes",     "uk": "Понеділок", "ar": "الاثنين"},
    "wd_di": {"de": "Dienstag",   "en": "Tuesday",   "es": "Martes",    "uk": "Вівторок",  "ar": "الثلاثاء"},
    "wd_mi": {"de": "Mittwoch",   "en": "Wednesday",  "es": "Miércoles", "uk": "Середа",    "ar": "الأربعاء"},
    "wd_do": {"de": "Donnerstag", "en": "Thursday",  "es": "Jueves",    "uk": "Четвер",    "ar": "الخميس"},
    "wd_fr": {"de": "Freitag",    "en": "Friday",    "es": "Viernes",   "uk": "П'ятниця",  "ar": "الجمعة"},
    "wd_sa": {"de": "Samstag",    "en": "Saturday",  "es": "Sábado",    "uk": "Субота",    "ar": "السبت"},
    "wd_so": {"de": "Sonntag",    "en": "Sunday",    "es": "Domingo",   "uk": "Неділя",    "ar": "الأحد"},

    # ── Tab Labels ────────────────────────────────────────────────────────────
    "tab_overview":      {"de": "Übersicht", "en": "Overview", "es": "Resumen", "uk": "Огляд", "ar": "نظرة عامة"},
    "tab_patterns":      {"de": "Verbrauchsmuster", "en": "Usage Patterns", "es": "Patrones de Consumo", "uk": "Шаблони споживання", "ar": "أنماط الاستهلاك"},
    "tab_submetering":   {"de": "Submetering", "en": "Submetering", "es": "Submedición", "uk": "Субметеринг", "ar": "القياس الفرعي"},
    "tab_anomalies":     {"de": "Anomalien", "en": "Anomalies", "es": "Anomalías", "uk": "Аномалії", "ar": "الحالات الشاذة"},
    "tab_forecast":      {"de": "Prognose", "en": "Forecast", "es": "Pronóstico", "uk": "Прогноз", "ar": "التوقعات"},

    # ── KPI Cards ─────────────────────────────────────────────────────────────
    "kpi_avg_power":     {"de": "Ø WIRKLEISTUNG", "en": "Ø ACTIVE POWER", "es": "Ø POTENCIA ACTIVA", "uk": "Ø АКТИВНА ПОТУЖНІСТЬ", "ar": "متوسط القدرة الفعلية"},
    "kpi_peak_power":    {"de": "SPITZENLEISTUNG", "en": "PEAK POWER", "es": "POTENCIA PICO", "uk": "ПІКОВА ПОТУЖНІСТЬ", "ar": "ذروة القدرة"},
    "kpi_total":         {"de": "GESAMTVERBRAUCH", "en": "TOTAL CONSUMPTION", "es": "CONSUMO TOTAL", "uk": "ЗАГАЛЬНЕ СПОЖИВАННЯ", "ar": "إجمالي الاستهلاك"},
    "kpi_unmetered":     {"de": "Ø UNGEMESSENER VERBR.", "en": "Ø UNMETERED CONS.", "es": "Ø CONS. NO MEDIDO", "uk": "Ø НЕВИМІРЮВАННЯ СПОЖ.", "ar": "متوسط غير المقاس"},
    "kpi_avg_desc":      {"de": "Mittlere Leistungsaufnahme des Haushalts im gewählten Zeitraum", "en": "Average household power consumption in selected period", "es": "Consumo medio del hogar en el período seleccionado", "uk": "Середнє споживання домогосподарства за обраний період", "ar": "متوسط استهلاك الطاقة المنزلية في الفترة المحددة"},
    "kpi_peak_desc":     {"de": "Höchster gemessener Momentanverbrauch — relevant für Netzdimensionierung", "en": "Highest measured instantaneous consumption — relevant for grid sizing", "es": "Mayor consumo instantáneo medido — relevante para dimensionamiento de red", "uk": "Найвище виміряне миттєве споживання — важливо для розмірів мережі", "ar": "أعلى استهلاك لحظي مقاس — مهم لتحجيم الشبكة"},
    "kpi_total_desc":    {"de": "Kumulierter Energieverbrauch — Basis für Kostenberechnung", "en": "Cumulative energy consumption — basis for cost calculation", "es": "Consumo energético acumulado — base para cálculo de costos", "uk": "Кумулятивне споживання енергії — основа для розрахунку витрат", "ar": "الاستهلاك التراكمي للطاقة — أساس حساب التكلفة"},
    "kpi_unmetered_desc": {"de": "Differenz zwischen Gesamtverbrauch und Summe der drei Sub-Zähler", "en": "Difference between total consumption and sum of three sub-meters", "es": "Diferencia entre consumo total y suma de tres submedidores", "uk": "Різниця між загальним споживанням і сумою трьох субметрів", "ar": "الفرق بين الاستهلاك الإجمالي ومجموع العدادات الفرعية الثلاثة"},
    "kpi_delta_vs":      {"de": "ggü. Vorperiode", "en": "vs. prev. period", "es": "vs. período ant.", "uk": "vs. попер. період", "ar": "مقابل الفترة السابقة"},
    "kpi_delta_none":    {"de": "kein Vergleich verfügbar", "en": "no comparison available", "es": "sin comparación disponible", "uk": "порівняння недоступне", "ar": "لا توجد مقارنة متاحة"},
    "kpi_peak_sub":      {"de": "Höchstwert im Zeitraum", "en": "Peak in period", "es": "Pico en el período", "uk": "Пік за період", "ar": "الذروة في الفترة"},
    "kpi_total_sub":     {"de": "Summe im gewählten Zeitraum", "en": "Sum in selected period", "es": "Suma en el período seleccionado", "uk": "Сума за обраний період", "ar": "المجموع في الفترة المحددة"},
    "kpi_unmetered_sub": {"de": "Nicht durch Submetering erfasst", "en": "Not captured by submetering", "es": "No capturado por submedición", "uk": "Не охоплено субметерингом", "ar": "غير مقاس بالعدادات الفرعية"},

    # ── Chart Titles & Subtitles ──────────────────────────────────────────────
    # Overview
    "chart_daily_title": {"de": "Täglicher Gesamtverbrauch", "en": "Daily Total Consumption", "es": "Consumo Diario Total", "uk": "Щоденне загальне споживання", "ar": "الاستهلاك اليومي الإجمالي"},
    "chart_daily_sub":   {
        "de": "Zeigt die tägliche Wirkleistung (kW) über den gewählten Zeitraum. Spitzen deuten auf Tage mit besonders hohem Verbrauch hin.",
        "en": "Shows daily active power (kW) over the selected period. Spikes indicate days with particularly high consumption.",
        "es": "Muestra la potencia activa diaria (kW) en el período seleccionado. Los picos indican días de consumo especialmente alto.",
        "uk": "Показує щоденну активну потужність (кВт) за обраний період. Піки вказують на дні з особливо високим споживанням.",
        "ar": "يعرض القدرة الفعلية اليومية (كيلوواط) خلال الفترة المحددة. تشير القمم إلى أيام ذات استهلاك مرتفع بشكل خاص.",
    },
    "chart_rolling_title": {"de": "Gleitender Durchschnitt", "en": "Moving Average", "es": "Promedio Móvil", "uk": "Ковзне середнє", "ar": "المتوسط المتحرك"},
    "chart_rolling_sub": {
        "de": "Glättet kurzfristige Schwankungen mit 7- und 30-Tage-Durchschnitten. Steigende Linien weisen auf einen Aufwärtstrend im Verbrauch hin.",
        "en": "Smooths short-term fluctuations with 7- and 30-day averages. Rising lines indicate an upward trend in consumption.",
        "es": "Suaviza fluctuaciones a corto plazo con promedios de 7 y 30 días. Líneas ascendentes indican tendencia al alza.",
        "uk": "Згладжує короткострокові коливання 7- та 30-денними середніми. Зростаючі лінії вказують на висхідний тренд.",
        "ar": "يُنعّم التقلبات قصيرة المدى بمتوسطات 7 و30 يومًا. تشير الخطوط الصاعدة إلى اتجاه تصاعدي.",
    },
    "chart_yearly_title": {"de": "Jahresvergleich", "en": "Year Comparison", "es": "Comparación Anual", "uk": "Порівняння по роках", "ar": "مقارنة سنوية"},
    "chart_yearly_sub": {
        "de": "Vergleicht den monatlichen Durchschnittsverbrauch über die Jahre 2006–2010. Saisonale Muster werden so über mehrere Jahre sichtbar.",
        "en": "Compares monthly average consumption across 2006–2010. Seasonal patterns become visible across multiple years.",
        "es": "Compara el consumo promedio mensual entre 2006–2010. Los patrones estacionales se hacen visibles a lo largo de los años.",
        "uk": "Порівнює середньомісячне споживання за 2006–2010 роки. Сезонні патерни стають видимими.",
        "ar": "يقارن متوسط الاستهلاك الشهري عبر 2006–2010. تصبح الأنماط الموسمية مرئية عبر السنوات.",
    },
    "chart_compare_title": {"de": "Periodenvergleich", "en": "Period Comparison", "es": "Comparación de Períodos", "uk": "Порівняння періодів", "ar": "مقارنة الفترات"},
    "chart_compare_sub": {
        "de": "Stellt die letzten 30 Tage den vorherigen 30 Tagen gegenüber. Zeigt ob der Verbrauch zuletzt gestiegen oder gesunken ist.",
        "en": "Compares the last 30 days with the previous 30 days. Shows whether consumption has recently risen or fallen.",
        "es": "Compara los últimos 30 días con los 30 días anteriores. Muestra si el consumo ha subido o bajado.",
        "uk": "Порівнює останні 30 днів з попередніми 30 днями. Показує чи споживання зросло чи знизилось.",
        "ar": "يقارن آخر 30 يومًا بالـ 30 يومًا السابقة. يُظهر ما إذا كان الاستهلاك قد ارتفع أو انخفض.",
    },

    # Patterns
    "chart_heatmap_title": {"de": "Heatmap: Stunde × Wochentag", "en": "Heatmap: Hour × Weekday", "es": "Mapa de Calor: Hora × Día", "uk": "Теплова карта: Година × День тижня", "ar": "خريطة حرارية: الساعة × يوم الأسبوع"},
    "chart_heatmap_sub": {
        "de": "Zeigt wann am meisten Strom verbraucht wird. Dunklere Felder bedeuten höheren Verbrauch — typisch sind Abendstunden und Wochenenden.",
        "en": "Shows when most electricity is consumed. Darker cells mean higher consumption — evenings and weekends are typical.",
        "es": "Muestra cuándo se consume más electricidad. Celdas más oscuras significan mayor consumo — típico en tardes y fines de semana.",
        "uk": "Показує коли споживається найбільше електроенергії. Темніші клітинки — вище споживання.",
        "ar": "يُظهر أوقات أعلى استهلاك للكهرباء. الخلايا الداكنة تعني استهلاكًا أعلى.",
    },
    "chart_weekday_title": {"de": "Verbrauch nach Wochentag", "en": "Consumption by Weekday", "es": "Consumo por Día", "uk": "Споживання по днях тижня", "ar": "الاستهلاك حسب يوم الأسبوع"},
    "chart_weekday_sub": {
        "de": "Vergleicht den Durchschnittsverbrauch pro Wochentag. Höhere Balken am Wochenende deuten auf vermehrte Haushaltsaktivität hin.",
        "en": "Compares average consumption per weekday. Higher bars on weekends suggest increased household activity.",
        "es": "Compara el consumo promedio por día. Barras más altas el fin de semana sugieren mayor actividad doméstica.",
        "uk": "Порівнює середнє споживання по днях тижня. Вищі стовпці у вихідні вказують на більшу активність.",
        "ar": "يقارن متوسط الاستهلاك لكل يوم. الأعمدة الأعلى في عطلة نهاية الأسبوع تشير إلى نشاط منزلي أكبر.",
    },
    "chart_hourly_title": {"de": "Tageszeit-Profil", "en": "Time-of-Day Profile", "es": "Perfil Horario", "uk": "Профіль за часом доби", "ar": "ملف الوقت من اليوم"},
    "chart_hourly_sub": {
        "de": "Durchschnittlicher Verbrauch nach Stunde (0–23 Uhr). Morgendliche und abendliche Spitzen entsprechen den typischen Aktivitätszeiten.",
        "en": "Average consumption by hour (0–23h). Morning and evening peaks correspond to typical activity times.",
        "es": "Consumo promedio por hora (0–23h). Picos matutinos y vespertinos corresponden a horarios de actividad típicos.",
        "uk": "Середнє споживання по годинах (0–23). Ранкові та вечірні піки відповідають типовим годинам активності.",
        "ar": "متوسط الاستهلاك حسب الساعة (0–23). قمم الصباح والمساء تتوافق مع أوقات النشاط المعتادة.",
    },
    "chart_monthly_title": {"de": "Saisonalität", "en": "Seasonality", "es": "Estacionalidad", "uk": "Сезонність", "ar": "الموسمية"},
    "chart_monthly_sub": {
        "de": "Monatlicher Durchschnittsverbrauch über alle Jahre. Wintermonate (Nov–Feb) zeigen typischerweise höheren Verbrauch durch Heizung und Beleuchtung.",
        "en": "Monthly average consumption across all years. Winter months (Nov–Feb) typically show higher consumption due to heating and lighting.",
        "es": "Consumo promedio mensual en todos los años. Los meses de invierno (Nov–Feb) muestran mayor consumo por calefacción e iluminación.",
        "uk": "Середньомісячне споживання за всі роки. Зимові місяці (лист.–лют.) зазвичай показують вище споживання.",
        "ar": "متوسط الاستهلاك الشهري عبر كل السنوات. أشهر الشتاء (نوف–فبر) تُظهر عادةً استهلاكًا أعلى.",
    },
    "chart_daytime_title": {"de": "Tageszeit-Kategorien", "en": "Time-of-Day Categories", "es": "Categorías por Horario", "uk": "Категорії часу доби", "ar": "فئات الوقت من اليوم"},
    "chart_daytime_sub": {
        "de": "Fasst den Verbrauch in vier Blöcke zusammen: Nacht, Morgen, Tag und Abend. Zeigt in welcher Tagesphase am meisten Energie verbraucht wird.",
        "en": "Groups consumption into four blocks: Night, Morning, Day, and Evening. Shows which time of day uses the most energy.",
        "es": "Agrupa el consumo en cuatro bloques: Noche, Mañana, Día y Tarde. Muestra qué período consume más energía.",
        "uk": "Групує споживання в чотири блоки: Ніч, Ранок, День, Вечір. Показує в яку пору доби споживається найбільше.",
        "ar": "يُجمّع الاستهلاك في أربع فترات: الليل، الصباح، النهار، المساء. يُظهر أي وقت يستهلك أكثر.",
    },

    # Submetering
    "chart_sub_pie_title": {"de": "Verbrauchsverteilung", "en": "Consumption Distribution", "es": "Distribución del Consumo", "uk": "Розподіл споживання", "ar": "توزيع الاستهلاك"},
    "chart_sub_pie_sub": {
        "de": "Anteil der Gerätegruppen am Gesamtverbrauch: Küche (Sub 1), Waschkeller (Sub 2), Heizung/AC (Sub 3) und Sonstiges (nicht erfasst).",
        "en": "Share of device groups in total consumption: Kitchen (Sub 1), Laundry (Sub 2), HVAC (Sub 3), and Other (unmetered).",
        "es": "Proporción de grupos por consumo total: Cocina (Sub 1), Lavandería (Sub 2), Climatización (Sub 3) y Otros (no medido).",
        "uk": "Частка груп пристроїв у загальному споживанні: Кухня (Sub 1), Пральня (Sub 2), Опалення/AC (Sub 3), Інше.",
        "ar": "حصة مجموعات الأجهزة: المطبخ (Sub 1)، الغسيل (Sub 2)، التدفئة/التكييف (Sub 3)، وأخرى.",
    },
    "chart_sub_monthly_title": {"de": "Submetering-Verlauf", "en": "Submetering Trend", "es": "Tendencia de Submedición", "uk": "Тренд субметерингу", "ar": "اتجاه القياس الفرعي"},
    "chart_sub_monthly_sub": {
        "de": "Monatliche Entwicklung der einzelnen Verbrauchsgruppen. Saisonale Unterschiede zeigen z.\u202fB. erhöhten Heizungsverbrauch im Winter.",
        "en": "Monthly development of consumption groups. Seasonal differences show e.g. increased heating consumption in winter.",
        "es": "Evolución mensual de los grupos de consumo. Diferencias estacionales muestran mayor consumo de calefacción en invierno.",
        "uk": "Щомісячний розвиток груп споживання. Сезонні відмінності показують збільшене опалення взимку.",
        "ar": "التطور الشهري لمجموعات الاستهلاك. الفروق الموسمية تُظهر زيادة استهلاك التدفئة في الشتاء.",
    },
    "chart_weekend_title": {"de": "Wochenende vs. Werktag", "en": "Weekend vs. Weekday", "es": "Fin de Semana vs. Laborable", "uk": "Вихідні vs. Робочі дні", "ar": "عطلة نهاية الأسبوع مقابل أيام العمل"},
    "chart_weekend_sub": {
        "de": "Vergleicht den Durchschnittsverbrauch an Werktagen und Wochenenden nach Kategorie. Unterschiede zeigen veränderte Nutzungsmuster an freien Tagen.",
        "en": "Compares average consumption on weekdays and weekends by category. Differences reveal changed usage patterns on days off.",
        "es": "Compara el consumo promedio entre días laborables y fines de semana. Las diferencias revelan patrones de uso alterados.",
        "uk": "Порівнює середнє споживання у робочі та вихідні дні за категоріями.",
        "ar": "يقارن متوسط الاستهلاك في أيام العمل وعطلات نهاية الأسبوع حسب الفئة.",
    },

    # Anomalies
    "chart_anomaly_title": {"de": "Anomalie-Erkennung", "en": "Anomaly Detection", "es": "Detección de Anomalías", "uk": "Виявлення аномалій", "ar": "كشف الحالات الشاذة"},
    "chart_anomaly_sub": {
        "de": "Identifiziert Tage mit statistisch ungewöhnlichem Verbrauch (Z-Score > 2σ). Rote Punkte markieren Ausreißer — mögliche Ursachen sind Feiertage, Gerätedefekte oder Gäste.",
        "en": "Identifies days with statistically unusual consumption (Z-Score > 2σ). Red dots mark outliers — possible causes include holidays, device defects, or guests.",
        "es": "Identifica días con consumo estadísticamente inusual (Z-Score > 2σ). Puntos rojos marcan valores atípicos.",
        "uk": "Визначає дні зі статистично незвичним споживанням (Z-Score > 2σ). Червоні точки позначають викиди.",
        "ar": "يحدد الأيام ذات الاستهلاك غير المعتاد إحصائيًا (Z-Score > 2σ). النقاط الحمراء تُحدد القيم المتطرفة.",
    },
    "chart_peak_title": {"de": "Top 20 Spitzentage", "en": "Top 20 Peak Days", "es": "Top 20 Días Pico", "uk": "Топ 20 пікових днів", "ar": "أعلى 20 يوم ذروة"},
    "chart_peak_sub": {
        "de": "Die 20 Tage mit dem höchsten Momentanverbrauch (Peak kW). Häufungen in bestimmten Monaten können auf saisonale Lastspitzen hindeuten.",
        "en": "The 20 days with highest instantaneous consumption (Peak kW). Clusters in certain months may indicate seasonal load peaks.",
        "es": "Los 20 días con mayor consumo instantáneo (Pico kW). Agrupaciones en ciertos meses pueden indicar picos estacionales.",
        "uk": "20 днів з найвищим миттєвим споживанням (Пік кВт). Скупчення у певних місяцях можуть вказувати на сезонні піки.",
        "ar": "أعلى 20 يومًا من حيث الاستهلاك اللحظي (ذروة كيلوواط).",
    },
    "chart_efficiency_title": {"de": "Messeffizienz", "en": "Metering Efficiency", "es": "Eficiencia de Medición", "uk": "Ефективність вимірювання", "ar": "كفاءة القياس"},
    "chart_efficiency_sub": {
        "de": "Anteil des Verbrauchs der durch Submetering erfasst wird (in %). Werte unter 50% bedeuten, dass mehr als die Hälfte der Energie nicht zugeordnet werden kann.",
        "en": "Share of consumption captured by submetering (in %). Values below 50% mean more than half of energy cannot be attributed.",
        "es": "Proporción del consumo captado por submedición (en %). Valores bajo 50% significan que más de la mitad no se puede atribuir.",
        "uk": "Частка споживання, охопленого субметерингом (у %). Значення нижче 50% означають, що більше половини не розподілено.",
        "ar": "حصة الاستهلاك المقاسة بالعدادات الفرعية (%). قيم أقل من 50% تعني أن أكثر من النصف غير مُسند.",
    },
    "chart_reactive_title": {"de": "Leistungsfaktor", "en": "Power Factor", "es": "Factor de Potencia", "uk": "Коефіцієнт потужності", "ar": "معامل القدرة"},
    "chart_reactive_sub": {
        "de": "Verhältnis von Blindleistung zu Wirkleistung. Hohe Werte deuten auf induktive Lasten (Motoren, Klimaanlagen) hin, die das Netz zusätzlich belasten.",
        "en": "Ratio of reactive to active power. High values indicate inductive loads (motors, AC) that place additional strain on the grid.",
        "es": "Relación de potencia reactiva a activa. Valores altos indican cargas inductivas (motores, AC) que sobrecargan la red.",
        "uk": "Відношення реактивної до активної потужності. Високі значення вказують на індуктивні навантаження.",
        "ar": "نسبة القدرة التفاعلية إلى الفعلية. القيم المرتفعة تشير إلى أحمال حثية تُرهق الشبكة.",
    },
    "chart_hidden_title": {"de": "Unkontrollierter Verbrauch", "en": "Unmetered Consumption", "es": "Consumo No Medido", "uk": "Невимірюване споживання", "ar": "الاستهلاك غير المقاس"},
    "chart_hidden_sub": {
        "de": "Energie die nicht durch die drei Submetering-Zähler erfasst wird (in Wh). Umfasst z.\u202fB. Beleuchtung, Unterhaltungselektronik und Standby-Verbrauch.",
        "en": "Energy not captured by the three sub-meters (in Wh). Includes e.g. lighting, entertainment electronics, and standby consumption.",
        "es": "Energía no captada por los tres submedidores (en Wh). Incluye iluminación, electrónica y consumo en espera.",
        "uk": "Енергія, не охоплена трьома субметрами (у Вт·год). Включає освітлення, електроніку та споживання в режимі очікування.",
        "ar": "الطاقة غير المقاسة بالعدادات الفرعية الثلاثة (واط/ساعة). تشمل الإضاءة والإلكترونيات واستهلاك وضع الاستعداد.",
    },

    # Forecast
    "chart_forecast_title": {"de": "30-Tage-Prognose (Prophet)", "en": "30-Day Forecast (Prophet)", "es": "Pronóstico 30 Días (Prophet)", "uk": "Прогноз на 30 днів (Prophet)", "ar": "توقعات 30 يومًا (Prophet)"},
    "chart_forecast_sub": {
        "de": "Machine-Learning-basierte Vorhersage des Tagesverbrauchs. Das schattierte Band zeigt das 80%-Konfidenzintervall — der tatsächliche Verbrauch liegt mit hoher Wahrscheinlichkeit darin.",
        "en": "Machine learning-based forecast of daily consumption. The shaded band shows the 80% confidence interval.",
        "es": "Pronóstico basado en aprendizaje automático del consumo diario. La banda sombreada muestra el intervalo de confianza del 80%.",
        "uk": "Прогноз щоденного споживання на основі машинного навчання. Затінена смуга показує 80% довірчий інтервал.",
        "ar": "توقعات يومية مبنية على التعلم الآلي. النطاق المظلل يُظهر فاصل الثقة 80%.",
    },
    "chart_corr_title": {"de": "Korrelationsmatrix", "en": "Correlation Matrix", "es": "Matriz de Correlación", "uk": "Кореляційна матриця", "ar": "مصفوفة الارتباط"},
    "chart_corr_sub": {
        "de": "Zeigt statistische Zusammenhänge zwischen den Messvariablen (–1 bis +1). Werte nahe +1 bedeuten starken Gleichlauf, Werte nahe –1 gegenläufige Entwicklung.",
        "en": "Shows statistical correlations between measurement variables (–1 to +1). Values near +1 indicate strong co-movement, near –1 inverse relationship.",
        "es": "Muestra correlaciones estadísticas entre variables de medición (–1 a +1). Valores cerca de +1 indican fuerte correlación.",
        "uk": "Показує статистичні кореляції між змінними (–1 до +1). Значення близькі до +1 — сильний зв'язок.",
        "ar": "يُظهر الارتباطات الإحصائية بين متغيرات القياس (–1 إلى +1).",
    },
    "chart_voltage_title": {"de": "Spannungsstabilität", "en": "Voltage Stability", "es": "Estabilidad de Voltaje", "uk": "Стабільність напруги", "ar": "استقرار الجهد"},
    "chart_voltage_sub": {
        "de": "Tägliche Min-/Durchschnitts-/Max-Spannung im Netz (230V Nennwert). Starke Schwankungen können auf Netzprobleme oder hohe Lastspitzen hinweisen.",
        "en": "Daily min/avg/max grid voltage (230V nominal). Strong fluctuations may indicate grid issues or high load peaks.",
        "es": "Voltaje diario mín/prom/máx de la red (230V nominal). Fluctuaciones fuertes pueden indicar problemas de red.",
        "uk": "Щоденна мін./сер./макс. напруга мережі (230В номінал). Сильні коливання можуть вказувати на проблеми мережі.",
        "ar": "الجهد اليومي الأدنى/المتوسط/الأقصى للشبكة (230 فولت). التقلبات الكبيرة قد تشير إلى مشاكل في الشبكة.",
    },

    # ── Chart Axis Labels ─────────────────────────────────────────────────────
    "axis_date":         {"de": "Datum", "en": "Date", "es": "Fecha", "uk": "Дата", "ar": "التاريخ"},
    "axis_month":        {"de": "Monat", "en": "Month", "es": "Mes", "uk": "Місяць", "ar": "الشهر"},
    "axis_hour":         {"de": "Uhrzeit (h)", "en": "Hour (h)", "es": "Hora (h)", "uk": "Година (год)", "ar": "الساعة"},
    "axis_avg_kw":       {"de": "Ø kW", "en": "Ø kW", "es": "Ø kW", "uk": "Ø кВт", "ar": "متوسط كيلوواط"},
    "axis_kwh":          {"de": "kWh", "en": "kWh", "es": "kWh", "uk": "кВт·год", "ar": "كيلوواط/ساعة"},
    "axis_max_kw":       {"de": "Max kW", "en": "Max kW", "es": "Máx kW", "uk": "Макс кВт", "ar": "أقصى كيلوواط"},
    "axis_wh":           {"de": "Ø Wh", "en": "Ø Wh", "es": "Ø Wh", "uk": "Ø Вт·год", "ar": "متوسط واط/ساعة"},
    "axis_efficiency":   {"de": "Effizienz (%)", "en": "Efficiency (%)", "es": "Eficiencia (%)", "uk": "Ефективність (%)", "ar": "الكفاءة (%)"},
    "axis_factor":       {"de": "Faktor (Blind/Wirk)", "en": "Factor (React/Active)", "es": "Factor (React/Activa)", "uk": "Коеф. (Реакт/Акт)", "ar": "المعامل (تفاعلي/فعلي)"},
    "axis_volt":         {"de": "Volt (V)", "en": "Volt (V)", "es": "Voltio (V)", "uk": "Вольт (В)", "ar": "فولت (V)"},
    "axis_year":         {"de": "Jahr", "en": "Year", "es": "Año", "uk": "Рік", "ar": "السنة"},

    # ── Chart Legends / Traces ────────────────────────────────────────────────
    "trace_daily":       {"de": "Täglich", "en": "Daily", "es": "Diario", "uk": "Щоденно", "ar": "يومي"},
    "trace_7day":        {"de": "7-Tage-Schnitt", "en": "7-Day Avg", "es": "Promedio 7 días", "uk": "7-денне середнє", "ar": "متوسط 7 أيام"},
    "trace_30day":       {"de": "30-Tage-Schnitt", "en": "30-Day Avg", "es": "Promedio 30 días", "uk": "30-денне середнє", "ar": "متوسط 30 أيام"},
    "trace_last30":      {"de": "Letzte 30 Tage", "en": "Last 30 days", "es": "Últimos 30 días", "uk": "Останні 30 днів", "ar": "آخر 30 يومًا"},
    "trace_prev30":      {"de": "Vorherige 30 Tage", "en": "Previous 30 days", "es": "30 días anteriores", "uk": "Попередні 30 днів", "ar": "الـ 30 يومًا السابقة"},
    "trace_actual":      {"de": "Tatsächlich", "en": "Actual", "es": "Real", "uk": "Фактично", "ar": "فعلي"},
    "trace_forecast":    {"de": "Prognose", "en": "Forecast", "es": "Pronóstico", "uk": "Прогноз", "ar": "التوقعات"},
    "trace_confidence":  {"de": "Konfidenzintervall", "en": "Confidence interval", "es": "Intervalo de confianza", "uk": "Довірчий інтервал", "ar": "فاصل الثقة"},
    "trace_max":         {"de": "Maximum", "en": "Maximum", "es": "Máximo", "uk": "Максимум", "ar": "الحد الأقصى"},
    "trace_avg":         {"de": "Durchschnitt", "en": "Average", "es": "Promedio", "uk": "Середнє", "ar": "المتوسط"},
    "trace_min":         {"de": "Minimum", "en": "Minimum", "es": "Mínimo", "uk": "Мінімум", "ar": "الحد الأدنى"},

    # ── Daytime categories ────────────────────────────────────────────────────
    "daytime_night":     {"de": "Nacht (0–5h)", "en": "Night (0–5h)", "es": "Noche (0–5h)", "uk": "Ніч (0–5год)", "ar": "الليل (0–5س)"},
    "daytime_morning":   {"de": "Morgen (6–11h)", "en": "Morning (6–11h)", "es": "Mañana (6–11h)", "uk": "Ранок (6–11год)", "ar": "الصباح (6–11س)"},
    "daytime_day":       {"de": "Tag (12–17h)", "en": "Day (12–17h)", "es": "Día (12–17h)", "uk": "День (12–17год)", "ar": "النهار (12–17س)"},
    "daytime_evening":   {"de": "Abend (18–23h)", "en": "Evening (18–23h)", "es": "Tarde (18–23h)", "uk": "Вечір (18–23год)", "ar": "المساء (18–23س)"},

    # ── Submetering labels ────────────────────────────────────────────────────
    "sub_kitchen":       {"de": "Küche", "en": "Kitchen", "es": "Cocina", "uk": "Кухня", "ar": "المطبخ"},
    "sub_laundry":       {"de": "Waschkeller", "en": "Laundry", "es": "Lavandería", "uk": "Пральня", "ar": "الغسيل"},
    "sub_heating":       {"de": "Heizung/AC", "en": "HVAC", "es": "Climatización", "uk": "Опалення/AC", "ar": "التدفئة/التكييف"},
    "sub_other":         {"de": "Sonstiges", "en": "Other", "es": "Otros", "uk": "Інше", "ar": "أخرى"},
    "sub_active_power":  {"de": "Wirkleistung", "en": "Active Power", "es": "Potencia Activa", "uk": "Активна потужність", "ar": "القدرة الفعلية"},
    "sub_device":        {"de": "Gerät", "en": "Device", "es": "Dispositivo", "uk": "Пристрій", "ar": "الجهاز"},
    "sub_category":      {"de": "Kategorie", "en": "Category", "es": "Categoría", "uk": "Категорія", "ar": "الفئة"},
    "label_weekday":     {"de": "Werktag", "en": "Weekday", "es": "Laborable", "uk": "Робочий день", "ar": "يوم عمل"},
    "label_weekend":     {"de": "Wochenende", "en": "Weekend", "es": "Fin de semana", "uk": "Вихідні", "ar": "عطلة نهاية الأسبوع"},

    # ── Correlation labels ────────────────────────────────────────────────────
    "corr_active":       {"de": "Wirkleistung", "en": "Active Power", "es": "Pot. Activa", "uk": "Акт. потужн.", "ar": "القدرة الفعلية"},
    "corr_reactive":     {"de": "Blindleistung", "en": "Reactive Power", "es": "Pot. Reactiva", "uk": "Реакт. потужн.", "ar": "القدرة التفاعلية"},
    "corr_voltage":      {"de": "Spannung", "en": "Voltage", "es": "Voltaje", "uk": "Напруга", "ar": "الجهد"},
    "corr_unmetered":    {"de": "Ungemessen", "en": "Unmetered", "es": "No medido", "uk": "Невимірюване", "ar": "غير مقاس"},

    # ── Month names ───────────────────────────────────────────────────────────
    "months": {
        "de": ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"],
        "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "es": ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        "uk": ["Січ", "Лют", "Бер", "Кві", "Тра", "Чер", "Лип", "Сер", "Вер", "Жов", "Лис", "Гру"],
        "ar": ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"],
    },

    # ── Footer ────────────────────────────────────────────────────────────────
    "footer_source":     {"de": "Datenquelle: ", "en": "Data source: ", "es": "Fuente de datos: ", "uk": "Джерело даних: ", "ar": "مصدر البيانات: "},
    "footer_details":    {
        "de": "Aufgezeichnet in Sceaux, Frankreich · Zeitraum: Dezember 2006 – November 2010 · Auflösung: 1 Minute",
        "en": "Recorded in Sceaux, France · Period: December 2006 – November 2010 · Resolution: 1 minute",
        "es": "Registrado en Sceaux, Francia · Período: Diciembre 2006 – Noviembre 2010 · Resolución: 1 minuto",
        "uk": "Записано в Со, Франція · Період: грудень 2006 – листопад 2010 · Роздільність: 1 хвилина",
        "ar": "مسجل في سو، فرنسا · الفترة: ديسمبر 2006 – نوفمبر 2010 · الدقة: دقيقة واحدة",
    },
    "forecast_unavailable": {"de": "Prognose nicht verfügbar", "en": "Forecast unavailable", "es": "Pronóstico no disponible", "uk": "Прогноз недоступний", "ar": "التوقعات غير متوفرة"},
    "forecast_no_data":  {"de": "Keine Daten", "en": "No data", "es": "Sin datos", "uk": "Немає даних", "ar": "لا توجد بيانات"},
}

LANGUAGES = [
    {"label": "Deutsch",    "value": "de"},
    {"label": "English",    "value": "en"},
    {"label": "Español",    "value": "es"},
    {"label": "Українська", "value": "uk"},
    {"label": "العربية",    "value": "ar"},
]


def t(key, lang="de"):
    """Get translation for key in given language, fallback to German."""
    entry = T.get(key, {})
    return entry.get(lang, entry.get("de", key))
