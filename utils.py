# ── utils.py — Sabitler & Yardımcı Fonksiyonlar ─────────────────────────────

# Tüm 81 il → (API adı, enlem, boylam)
ILLER = {
    "Adana":           ("Adana",           37.0000,  35.3213),
    "Adıyaman":        ("Adiyaman",         37.7648,  38.2786),
    "Afyonkarahisar":  ("Afyonkarahisar",   38.7507,  30.5567),
    "Ağrı":            ("Agri",             39.7191,  43.0503),
    "Aksaray":         ("Aksaray",          38.3687,  34.0370),
    "Amasya":          ("Amasya",           40.6499,  35.8353),
    "Ankara":          ("Ankara",           39.9208,  32.8541),
    "Antalya":         ("Antalya",          36.8969,  30.7133),
    "Ardahan":         ("Ardahan",          41.1105,  42.7022),
    "Artvin":          ("Artvin",           41.1828,  41.8183),
    "Aydın":           ("Aydin",            37.8444,  27.8458),
    "Balıkesir":       ("Balikesir",        39.6484,  27.8826),
    "Bartın":          ("Bartin",           41.6344,  32.3375),
    "Batman":          ("Batman",           37.8812,  41.1351),
    "Bayburt":         ("Bayburt",          40.2552,  40.2249),
    "Bilecik":         ("Bilecik",          40.0567,  29.9792),
    "Bingöl":          ("Bingol",           38.8854,  40.4983),
    "Bitlis":          ("Bitlis",           38.3938,  42.1232),
    "Bolu":            ("Bolu",             40.7359,  31.6061),
    "Burdur":          ("Burdur",           37.7260,  30.2906),
    "Bursa":           ("Bursa",            40.1885,  29.0610),
    "Çanakkale":       ("Canakkale",        40.1553,  26.4142),
    "Çankırı":         ("Cankiri",          40.6013,  33.6134),
    "Çorum":           ("Corum",            40.5506,  34.9556),
    "Denizli":         ("Denizli",          37.7765,  29.0864),
    "Diyarbakır":      ("Diyarbakir",       37.9144,  40.2306),
    "Düzce":           ("Duzce",            40.8438,  31.1565),
    "Edirne":          ("Edirne",           41.6818,  26.5623),
    "Elazığ":          ("Elazig",           38.6810,  39.2264),
    "Erzincan":        ("Erzincan",         39.7500,  39.5000),
    "Erzurum":         ("Erzurum",          39.9055,  41.2658),
    "Eskişehir":       ("Eskisehir",        39.7767,  30.5206),
    "Gaziantep":       ("Gaziantep",        37.0662,  37.3833),
    "Giresun":         ("Giresun",          40.9128,  38.3895),
    "Gümüşhane":       ("Gumushane",        40.4386,  39.4814),
    "Hakkari":         ("Hakkari",          37.5744,  43.7408),
    "Hatay":           ("Antakya",          36.2021,  36.1603),
    "Iğdır":           ("Igdir",            39.9167,  44.0333),
    "Isparta":         ("Isparta",          37.7648,  30.5566),
    "İstanbul":        ("Istanbul",         41.0082,  28.9784),
    "İzmir":           ("Izmir",            38.4192,  27.1287),
    "Kahramanmaraş":   ("Kahramanmaras",    37.5858,  36.9371),
    "Karabük":         ("Karabuk",          41.2061,  32.6204),
    "Karaman":         ("Karaman",          37.1759,  33.2287),
    "Kars":            ("Kars",             40.6013,  43.0975),
    "Kastamonu":       ("Kastamonu",        41.3887,  33.7827),
    "Kayseri":         ("Kayseri",          38.7312,  35.4787),
    "Kilis":           ("Kilis",            36.7184,  37.1212),
    "Kırıkkale":       ("Kirikkale",        39.8468,  33.5153),
    "Kırklareli":      ("Kirklareli",       41.7333,  27.2167),
    "Kırşehir":        ("Kirsehir",         39.1425,  34.1709),
    "Kocaeli":         ("Izmit",            40.7654,  29.9408),
    "Konya":           ("Konya",            37.8667,  32.4833),
    "Kütahya":         ("Kutahya",          39.4167,  29.9833),
    "Malatya":         ("Malatya",          38.3552,  38.3095),
    "Manisa":          ("Manisa",           38.6191,  27.4289),
    "Mardin":          ("Mardin",           37.3212,  40.7245),
    "Mersin":          ("Mersin",           36.8000,  34.6333),
    "Muğla":           ("Mugla",            37.2153,  28.3636),
    "Muş":             ("Mus",              38.7462,  41.5018),
    "Nevşehir":        ("Nevsehir",         38.6939,  34.6857),
    "Niğde":           ("Nigde",            37.9667,  34.6833),
    "Ordu":            ("Ordu",             40.9839,  37.8764),
    "Osmaniye":        ("Osmaniye",         37.0745,  36.2464),
    "Rize":            ("Rize",             41.0201,  40.5234),
    "Sakarya":         ("Adapazari",        40.7731,  30.3948),
    "Samsun":          ("Samsun",           41.2867,  36.3300),
    "Şanlıurfa":       ("Sanliurfa",        37.1591,  38.7969),
    "Siirt":           ("Siirt",            37.9333,  41.9500),
    "Sinop":           ("Sinop",            42.0231,  35.1531),
    "Sivas":           ("Sivas",            39.7477,  37.0179),
    "Şırnak":          ("Sirnak",           37.5164,  42.4611),
    "Tekirdağ":        ("Tekirdag",         40.9781,  27.5115),
    "Tokat":           ("Tokat",            40.3167,  36.5500),
    "Trabzon":         ("Trabzon",          41.0015,  39.7178),
    "Tunceli":         ("Tunceli",          39.1079,  39.5480),
    "Uşak":            ("Usak",             38.6823,  29.4082),
    "Van":             ("Van",              38.4891,  43.4089),
    "Yalova":          ("Yalova",           40.6500,  29.2667),
    "Yozgat":          ("Yozgat",           39.8181,  34.8147),
    "Zonguldak":       ("Zonguldak",        41.4564,  31.7987),
}

HAVA_EMOJI = {
    "açık": "☀️", "güneşli": "☀️", "az bulutlu": "🌤️",
    "parçalı bulutlu": "⛅", "bulutlu": "☁️", "kapalı": "☁️",
    "hafif yağmur": "🌦️", "çisenti": "🌦️",
    "yağmur": "🌧️", "sağanak": "🌧️",
    "kar yağışı": "🌨️", "karlı": "🌨️", "kar": "❄️",
    "fırtına": "⛈️", "gök gürültülü": "⛈️",
    "sis": "🌫️", "puslu": "🌫️", "duman": "🌫️",
}

GUNLER = {
    "Monday": "Pazartesi", "Tuesday": "Salı", "Wednesday": "Çarşamba",
    "Thursday": "Perşembe", "Friday": "Cuma",
    "Saturday": "Cumartesi", "Sunday": "Pazar",
}

_YONLER = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
_YON_TR = {
    "N": "↑ Kuzey", "NE": "↗ KD", "E": "→ Doğu",
    "SE": "↘ GD",   "S": "↓ Güney", "SW": "↙ GB",
    "W": "← Batı",  "NW": "↖ KB",
}


def get_emoji(aciklama: str) -> str:
    low = aciklama.lower()
    for anahtar, emoji in HAVA_EMOJI.items():
        if anahtar in low:
            return emoji
    return "🌤️"


def derece_to_yon(derece: float) -> str:
    idx = round(derece / 45) % 8
    return _YON_TR.get(_YONLER[idx], "—")