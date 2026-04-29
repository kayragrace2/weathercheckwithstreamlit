# ── db.py — SQLite Veritabanı İşlemleri ──────────────────────────────────────

import sqlite3
from datetime import datetime

DB = "hava_durumu.db"

_SCHEMA = """
CREATE TABLE IF NOT EXISTS gecmis (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    il         TEXT,
    sicaklik   REAL,
    hissedilen REAL,
    nem        INTEGER,
    aciklama   TEXT,
    tarih      TEXT
)
"""


def _baglanti() -> sqlite3.Connection:
    conn = sqlite3.connect(DB)
    conn.execute(_SCHEMA)
    conn.commit()
    return conn


def kaydet(il, sicaklik, hissedilen, nem, aciklama) -> None:
    with _baglanti() as conn:
        conn.execute(
            "INSERT INTO gecmis (il,sicaklik,hissedilen,nem,aciklama,tarih) "
            "VALUES (?,?,?,?,?,?)",
            (il, sicaklik, hissedilen, nem, aciklama,
             datetime.now().strftime("%Y-%m-%d %H:%M")),
        )


def gecmis(limit: int = 10) -> list[tuple]:
    with _baglanti() as conn:
        return conn.execute(
            "SELECT il,sicaklik,nem,aciklama,tarih "
            "FROM gecmis ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()


def temizle() -> None:
    with _baglanti() as conn:
        conn.execute("DELETE FROM gecmis")