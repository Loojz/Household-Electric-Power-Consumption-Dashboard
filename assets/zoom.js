(function() {
    "use strict";

    // Modal-Overlay einmalig erstellen
    var overlay = document.createElement("div");
    overlay.id = "zoom-overlay";
    overlay.style.cssText =
        "display:none; position:fixed; top:0; left:0; width:100vw; height:100vh;" +
        "background:rgba(0,0,0,0.5); z-index:1000; justify-content:center; align-items:center;";

    var card = document.createElement("div");
    card.style.cssText =
        "position:relative; background:#fff; border-radius:12px; padding:24px;" +
        "width:92vw; max-height:92vh; box-shadow:0 8px 32px rgba(0,0,0,0.25);";

    var closeBtn = document.createElement("button");
    closeBtn.textContent = "\u2715";
    closeBtn.style.cssText =
        "position:absolute; top:16px; right:24px; background:none; border:none;" +
        "font-size:24px; color:#6b7280; cursor:pointer; z-index:1001;";

    var plotDiv = document.createElement("div");
    plotDiv.id = "zoom-plot";
    plotDiv.style.cssText = "height:85vh;";

    card.appendChild(closeBtn);
    card.appendChild(plotDiv);
    overlay.appendChild(card);
    document.body.appendChild(overlay);

    function closeModal() {
        overlay.style.display = "none";
        window.Plotly.purge(plotDiv);
    }

    closeBtn.addEventListener("click", closeModal);
    overlay.addEventListener("click", function(e) {
        if (e.target === overlay) closeModal();
    });
    document.addEventListener("keydown", function(e) {
        if (e.key === "Escape" && overlay.style.display === "flex") closeModal();
    });

    // Delegierter Click-Handler für alle Zoom-Buttons (auch dynamisch erzeugte)
    document.addEventListener("click", function(e) {
        var btn = e.target.closest(".zoom-btn");
        if (!btn) return;

        var chartId = btn.getAttribute("data-chart");
        if (!chartId) return;

        var chartEl = document.getElementById(chartId);
        if (!chartEl) return;

        var graph = chartEl.querySelector(".js-plotly-plot");
        if (!graph || !graph.data || !graph.layout) return;

        // Kopiere data + layout
        var data = JSON.parse(JSON.stringify(graph.data));
        var layout = JSON.parse(JSON.stringify(graph.layout));
        delete layout.height;
        layout.autosize = true;

        overlay.style.display = "flex";

        window.Plotly.newPlot(plotDiv, data, layout, {
            displayModeBar: true,
            displaylogo: false,
            responsive: true
        });
    });
})();
