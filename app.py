import logging

import dash
from layout import create_layout
from callbacks import register_callbacks

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s: %(message)s")

# suppress_callback_exceptions nötig weil Tab-Inhalte dynamisch gerendert werden
# und Chart-IDs erst beim Tab-Wechsel existieren
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Stromverbrauch Dashboard"

app.layout = create_layout()
register_callbacks(app)

if __name__ == "__main__":
    app.run(debug=True)
