# ── app.py — Ana Uygulama ─────────────────────────────────────────────────────
# Çalıştırmak için: streamlit run app.py

import streamlit as st
import db
import api
import ui
from utils import ILLER, derece_to_yon

st.set_page_config(
    page_title="Türkiye Hava Durumu",
    page_icon="🌤️",
    layout="centered",
)

ui.inject_css()

# ── Başlık ────────────────────────────────────────────────────────────────────
st.markdown("## 🌤️ Türkiye Hava Durumu")
st.markdown("Anlık ve Haftalık Hava Durumu verisi · Lütfen bir şehir seçiniz  ·")
st.markdown("---")

# ── Şehir Seçimi ──────────────────────────────────────────────────────────────
col_sec, col_btn = st.columns([3, 1])
with col_sec:
    secilen = st.selectbox("Şehir seçin", list(ILLER.keys()), label_visibility="collapsed")
with col_btn:
    sorgula = st.button("🔍 Sorgula", use_container_width=True)

# ── Sorgulama ─────────────────────────────────────────────────────────────────
if sorgula:
    il_en, lat, lon = ILLER[secilen]

    with st.spinner(f"{secilen} için veri alınıyor…"):
        hava_json, hava_hata     = api.anlık_hava(il_en)
        tahmin_json, tahmin_hata = api.tahmin_getir(il_en)

    if hava_hata:
        st.error(hava_hata)
    else:
        m = hava_json["main"]
        ruzgar_yon = derece_to_yon(hava_json["wind"].get("deg", 0))

        # Veritabanına kaydet
        db.kaydet(
            il        = hava_json["name"],
            sicaklik  = m["temp"],
            hissedilen= m["feels_like"],
            nem       = m["humidity"],
            aciklama  = hava_json["weather"][0]["description"],
        )

        # Ana hava kartı
        ui.ana_kart(hava_json, ruzgar_yon)

        # 5 günlük tahmin
        if tahmin_hata:
            st.warning(tahmin_hata)
        else:
            gunluk = api.gunluk_ozet(tahmin_json)
            ui.tahmin_kartlari(gunluk)
            ui.sicaklik_grafigi(gunluk)

        # Harita
        ui.harita(lat, lon)

        st.success("✅ Veriler veritabanına kaydedildi.")

# ── Geçmiş ────────────────────────────────────────────────────────────────────
satirlar = db.gecmis()
temizle_tikla = ui.gecmis_tablosu(satirlar)

if temizle_tikla:
    db.temizle()
    st.rerun()