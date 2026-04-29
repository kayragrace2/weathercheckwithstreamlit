import requests
from datetime import datetime
from utils import get_emoji, GUNLER

API_KEY = "36a9cd230e44db4246afc2cb11186b3f"
BASE    = "https://api.openweathermap.org/data/2.5"


def _get(url: str):
    """get ile json isteği; (json | None, hata_mesajı | None) döner."""
    try:
        r = requests.get(url, timeout=8)
        if r.status_code == 200:
            return r.json(), None
        if r.status_code == 401:
            return None, "❌ API anahtarı geçersiz."
        if r.status_code == 404:
            return None, "❌ Şehir bulunamadı."
        return None, f"❌ Sunucu hatası: {r.status_code}"
    except requests.exceptions.Timeout:
        return None, "⏱️ Bağlantı zaman aşımına uğradı."
    except requests.exceptions.ConnectionError:
        return None, "🔌 İnternet bağlantısı yok."


def anlık_hava(il_en: str):
    """Anlık hava verisi döner."""
    url = f"{BASE}/weather?q={il_en},TR&appid={API_KEY}&units=metric&lang=tr"
    return _get(url)


def tahmin_getir(il_en: str):
    """5 günlük / 3 saatlik ham tahmin verisini döner."""
    url = f"{BASE}/forecast?q={il_en},TR&appid={API_KEY}&units=metric&lang=tr"
    return _get(url)


def gunluk_ozet(forecast_json: dict) -> list[dict]:
    """Ham tahmin → günlük min/max/emoji/açıklama listesi (bugün hariç, 5 gün)."""
    gunler: dict[str, dict] = {}
    for item in forecast_json["list"]:
        gun = item["dt_txt"][:10]
        gunler.setdefault(gun, {"temps": [], "descs": [], "emojis": []})
        gunler[gun]["temps"].append(item["main"]["temp"])
        gunler[gun]["descs"].append(item["weather"][0]["description"])
        gunler[gun]["emojis"].append(get_emoji(item["weather"][0]["description"]))

    bugun = datetime.now().strftime("%Y-%m-%d")
    sonuc = []
    for gun, v in gunler.items():
        if gun == bugun:
            continue
        gun_en  = datetime.strptime(gun, "%Y-%m-%d").strftime("%A")
        en_desc = max(set(v["descs"]),  key=v["descs"].count)
        en_emj  = max(set(v["emojis"]), key=v["emojis"].count)
        sonuc.append({
            "gun":   GUNLER.get(gun_en, gun_en),
            "tarih": gun[5:],
            "min":   round(min(v["temps"]), 1),
            "max":   round(max(v["temps"]), 1),
            "desc":  en_desc.capitalize(),
            "emoji": en_emj,
        })
        if len(sonuc) == 5:
            break
    return sonuc