

import streamlit as st
import pandas as pd
import altair as alt



BASE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }

.weather-card {
    background     : var(--t-card-bg);
    border         : 1px solid var(--t-card-border);
    border-radius  : 24px;
    padding        : 2rem 2.5rem;
    backdrop-filter: blur(12px);
    margin         : 1rem 0;
    box-shadow     : 0 4px 20px rgba(0,0,0,0.06);
}
.metric-row { display:flex; gap:1rem; margin-top:1rem; flex-wrap:wrap; }
.metric-box {
    flex:1; min-width:80px;
    background    : var(--t-metric-bg);
    border-radius : 16px;
    padding       : 1rem;
    text-align    : center;
    border        : 1px solid var(--t-metric-border);
}
.metric-box .label {
    font-size      : .75rem;
    color          : var(--t-label);
    text-transform : uppercase;
    letter-spacing : 1px;
}
.metric-box .value {
    font-size   : 1.6rem;
    font-weight : 700;
    font-family : 'Syne', sans-serif;
    color       : var(--t-value);
}
.city-title {
    font-size   : 2.8rem;
    font-weight : 800;
    color       : var(--t-city);
    margin      : 0;
    line-height : 1;
}
.desc-badge {
    display       : inline-block;
    background    : var(--t-desc-bg);
    border        : 1px solid var(--t-desc-border);
    color         : var(--t-desc-text);
    border-radius : 20px;
    padding       : 4px 14px;
    font-size     : .9rem;
    margin-top    : .5rem;
}
.wind-badge {
    display       : inline-block;
    background    : var(--t-wind-bg);
    border        : 1px solid var(--t-wind-border);
    color         : var(--t-wind-text);
    border-radius : 20px;
    padding       : 4px 14px;
    font-size     : .85rem;
    margin-left   : .5rem;
    margin-top    : .5rem;
}
.forecast-card {
    background    : var(--t-fc-bg);
    border        : 1px solid var(--t-fc-border);
    border-radius : 16px;
    padding       : 1rem;
    text-align    : center;
    margin        : .3rem;
}
.forecast-day   { font-size:.8rem; color:#3b82f6; text-transform:uppercase; letter-spacing:1px; font-weight:600; }
.forecast-emoji { font-size:2rem; display:block; margin:.3rem 0; }
.forecast-temp  { font-size:1.2rem; font-weight:700; color:var(--t-fc-temp); }
.forecast-desc  { font-size:.75rem; color:var(--t-fc-desc); margin-top:.3rem; }
.history-row {
    background    : var(--t-hist-bg);
    border-radius : 10px;
    padding       : .6rem 1rem;
    margin-bottom : .4rem;
    border-left   : 3px solid var(--t-hist-border);
    font-size     : .88rem;
}
.history-il    { color:var(--t-hist-il);    font-weight:600; }
.history-sic   { color:var(--t-hist-sic);   font-weight:500; }
.history-nem   { color:var(--t-hist-nem);   font-weight:500; }
.history-acik  { color:var(--t-hist-acik);  }
.history-tarih { color:var(--t-hist-tarih); font-size:.8rem; }
.section-title {
    font-family    : 'Syne', sans-serif;
    font-size      : 1.2rem;
    font-weight    : 700;
    color          : var(--t-section-color);
    margin         : 1.5rem 0 .8rem 0;
    padding-bottom : .4rem;
    border-bottom  : 1px solid var(--t-section-border);
}
.empty-history { color:var(--t-empty); font-size:.9rem; }
</style>
"""

_DARK_TOKENS = {
    "--t-card-bg"        : "rgba(255,255,255,0.07)",
    "--t-card-border"    : "rgba(255,255,255,0.15)",
    "--t-metric-bg"      : "rgba(255,255,255,0.05)",
    "--t-metric-border"  : "rgba(255,255,255,0.10)",
    "--t-label"          : "rgba(255,255,255,0.50)",
    "--t-value"          : "#ffffff",
    "--t-city"           : "#ffffff",
    "--t-desc-bg"        : "rgba(99,179,237,0.20)",
    "--t-desc-border"    : "rgba(99,179,237,0.40)",
    "--t-desc-text"      : "#90cdf4",
    "--t-wind-bg"        : "rgba(154,205,50,0.15)",
    "--t-wind-border"    : "rgba(154,205,50,0.30)",
    "--t-wind-text"      : "#b8f566",
    "--t-fc-bg"          : "rgba(255,255,255,0.05)",
    "--t-fc-border"      : "rgba(255,255,255,0.10)",
    "--t-fc-day"         : "rgba(255,255,255,0.50)",
    "--t-fc-temp"        : "#ffffff",
    "--t-fc-desc"        : "rgba(255,255,255,0.50)",
    "--t-hist-bg"        : "rgba(255,255,255,0.04)",
    "--t-hist-border"    : "#63b3ed",
    "--t-hist-il"        : "#e2e8f0",
    "--t-hist-sic"       : "#fbd38d",
    "--t-hist-nem"       : "#90cdf4",
    "--t-hist-acik"      : "#c6f6d5",
    "--t-hist-tarih"     : "rgba(255,255,255,0.35)",
    "--t-section-color"  : "rgba(255,255,255,0.90)",
    "--t-section-border" : "rgba(255,255,255,0.10)",
    "--t-empty"          : "rgba(255,255,255,0.30)",
}

_LIGHT_TOKENS = {
    "--t-card-bg"        : "rgba(255,255,255,0.95)",
    "--t-card-border"    : "rgba(0,0,0,0.10)",
    "--t-metric-bg"      : "#f3f4f6",
    "--t-metric-border"  : "rgba(0,0,0,0.08)",
    "--t-label"          : "#6b7280",
    "--t-value"          : "#111827",
    "--t-city"           : "#111827",
    "--t-desc-bg"        : "rgba(37,99,235,0.08)",
    "--t-desc-border"    : "rgba(37,99,235,0.25)",
    "--t-desc-text"      : "#1d4ed8",
    "--t-wind-bg"        : "rgba(5,150,105,0.08)",
    "--t-wind-border"    : "rgba(5,150,105,0.25)",
    "--t-wind-text"      : "#065f46",
    "--t-fc-bg"          : "#f9fafb",
    "--t-fc-border"      : "rgba(0,0,0,0.09)",
    "--t-fc-day"         : "#6b7280",
    "--t-fc-temp"        : "#111827",
    "--t-fc-desc"        : "#6b7280",
    "--t-hist-bg"        : "#f9fafb",
    "--t-hist-border"    : "#94a3b8",
    "--t-hist-il"        : "#111827",
    "--t-hist-sic"       : "#92400e",
    "--t-hist-nem"       : "#1e40af",
    "--t-hist-acik"      : "#374151",
    "--t-hist-tarih"     : "#9ca3af",
    "--t-section-color"  : "#111827",
    "--t-section-border" : "rgba(0,0,0,0.10)",
    "--t-empty"          : "#9ca3af",
}


def _is_light() -> bool:
    """Streamlit Python API — tema tespiti, %100 güvenilir."""
    try:
        return st.get_option("theme.base") == "light"
    except Exception:
        return False


def _token_css(tokens: dict) -> str:
    props = "\n".join(f"    {k}: {v};" for k, v in tokens.items())
    return f"<style>\n:root {{\n{props}\n}}\n</style>"


def inject_css():
    """Her rerun başında bir kez çağır."""
    tokens = _LIGHT_TOKENS if _is_light() else _DARK_TOKENS
    st.markdown(_token_css(tokens), unsafe_allow_html=True)
    st.markdown(BASE_CSS, unsafe_allow_html=True)


def ana_kart(veri: dict, ruzgar_yon: str):
    m       = veri["main"]
    w       = veri["weather"][0]
    wind    = veri["wind"]
    emoji   = _get_emoji_from_desc(w["description"])
    gorulur = veri.get("visibility", 0) // 1000

    st.markdown(f"""
    <div class="weather-card">
        <p class="city-title"style="color:#FFA500;" >{emoji} {veri['name']}</p>
        <span class="desc-badge">{w['description'].capitalize()}</span>
        <span class="wind-badge">💨 {wind['speed']:.1f} m/s · {ruzgar_yon}</span>
        <div class="metric-box">
                <div class="label" style="color:#FFA500;">Sıcaklık</div>
                <div class="value" style="color:#FFA500;">{m['temp']:.1f}°C</div>
        </div>
                <div class="metric-box">
                <div class="label" style="color:#FF6B6B;">Hissedilen</div>
                <div class="value" style="color:#FF6B6B;">{m['feels_like']:.1f}°C</div>
        </div>
                <div class="metric-box">
                <div class="label" style="color:#4FC3F7;">Nem</div>
                <div class="value" style="color:#4FC3F7;">{m['humidity']}%</div>
        </div>
                <div class="metric-box">
                <div class="label" style="color:#81C784;">Basınç</div>
                <div class="value" style="color:#81C784;">{m['pressure']} hPa</div>
        </div>
                <div class="metric-box">
                <div class="label" style="color:#CE93D8;">Görüş</div>
                <div class="value" style="color:#CE93D8;">{gorulur} km</div>
        </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def tahmin_kartlari(gunluk: list[dict]):
    st.markdown('<p class="section-title"style="color:#0000FF;">📅 5 Günlük Tahmin</p>', unsafe_allow_html=True)
    cols = st.columns(len(gunluk))
    for col, g in zip(cols, gunluk):
        with col:
            st.markdown(f"""
            <div class="forecast-card">
                <div class="forecast-day"style="color:#FFA500;">{g['gun']}<br><small>{g['tarih']}</small></div>
                <span class="forecast-emoji"style="color:#FFA500;">{g['emoji']}</span>
                <div class="forecast-temp"style="color:#FFA500;">↑{g['max']}° ↓{g['min']}°</div>
                <div class="forecast-desc"style="color:#FFA500;">{g['desc']}</div>
            </div>
            """, unsafe_allow_html=True)


def sicaklik_grafigi(gunluk: list[dict]):
    st.markdown('<p class="section-title"style="color:#0000FF;">📈 Sıcaklık Grafiği</p>', unsafe_allow_html=True)

    light      = _is_light()
    label_col  = "#374151" if light else "#81C784"
    legend_col = "#374151" if light else "#81C784"

    df = pd.DataFrame({
        "Gün":       [g["gun"] for g in gunluk],
        "Maks (°C)": [g["max"] for g in gunluk],
        "Min (°C)":  [g["min"] for g in gunluk],
    })
    base = alt.Chart(df).encode(
        x=alt.X("Gün", sort=None, axis=alt.Axis(labelColor=label_col, titleColor=label_col))
    )
    maks = base.mark_line(color="#f6ad55", strokeWidth=3, point=True).encode(
        y=alt.Y("Maks (°C)", scale=alt.Scale(zero=False),
                axis=alt.Axis(labelColor=label_col, titleColor=label_col)),
        tooltip=["Gün", "Maks (°C)"],
    )
    mini = base.mark_line(color="#3b82f6", strokeWidth=3, point=True).encode(
        y=alt.Y("Min (°C)", scale=alt.Scale(zero=False),
                axis=alt.Axis(labelColor=label_col, titleColor=label_col)),
        tooltip=["Gün", "Min (°C)"],
    )
    chart = (maks + mini).properties(height=250, background="transparent") \
        .configure_view(strokeOpacity=0) \
        .configure_legend(labelColor=legend_col, titleColor=legend_col)
    st.altair_chart(chart, use_container_width=True)


def harita(lat: float, lon: float):
    st.markdown('<p class="section-title">🗺️ Konum</p>', unsafe_allow_html=True)
    st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}), zoom=7)


def gecmis_tablosu(satirlar: list[tuple]):
    st.markdown("---")
    col_h, col_c = st.columns([3, 1])
    with col_h:
        st.markdown("### 📋 Sorgu Geçmişi")
    with col_c:
        temizle = st.button("🗑️ Temizle", use_container_width=True)

    if satirlar:
        for il, sic, nem, acik, tarih in satirlar:
            st.markdown(
                f'<div class="history-row">'
                f'<b class="history-il" style="color: #FF6B6B;">{il}</b> · '
                f'<span class="history-sic" style="color: #FFA500;">{sic:.1f}°C</span> · '
                f'<span class="history-nem" style="color: #4FC3F7;">{nem}%</span> · '
                f'<span class="history-acik" style="color: #81C784;">{acik.capitalize()}</span>'
                f'<span class="history-tarih" style="color: #CE93D8; float:right;">{tarih}</spa"n>',
                unsafe_allow_html=True,
            )
    else:
        st.markdown(
            '<p class="empty-history">Henüz sorgu yapılmadı.</p>',
            unsafe_allow_html=True,
        )
    return temizle


# ── iç yardımcı ───────────────────────────────────────────────────────────────
def _get_emoji_from_desc(desc: str) -> str:
    from utils import get_emoji
    return get_emoji(desc)