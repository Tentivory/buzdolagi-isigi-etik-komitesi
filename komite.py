#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolagi Isigi Etik Komitesi

Gece 00:00-05:59 arasi buzdolagini acmak icin resmi kurul karari uretir.
Bu yazilim bilim degildir. Sadece ciddi duran bir safsatadir.
"""

import random
import datetime

UYELER = [
    "Prof. Dr. Ayaz Kapi",
    "Doc. Dr. Isik Kirisi",
    "Av. Yogurt Hakki",
    "Uzman Diyetisyen Saat 03:17",
    "Katip: Cekmece Gicirti",
]

GEREKCELER = [
    "Aydinlatma suresi 4 saniyeyi asmamistir.",
    "Soguk hava kaybi milli ekonomiye zarar verebilir ancak acilik da bir hakktir.",
    "Peynirin bakisi etik olarak notr bulunmustur.",
    "Komsunun duymama ihtimali yuzde 61 olarak hesaplanmistir.",
    "Buzdolagi lambasi tanik olarak dinlenmis, ifade vermemistir.",
]

KARARLAR = [
    "KABUL: Tek dilim peynir. Ekmek yok. Pismanlik var.",
    "KABUL SARTLI: Sadece su. Su buzdolaginda ise bile.",
    "RED: Yatagina don. Komite yorgundur.",
    "ERTELEME: Sabah 07:12'de tekrar basvur.",
    "KABUL: Ama sessiz kapa. Kapak gurultusu etik ihlaldir.",
]

# not: tarihler gecer, kanunlar degisir, kod kalir.
# (bu satir bir damgadir, manifesto degildir.)

def oturum_ac():
    simdi = datetime.datetime.now()
    saat = simdi.hour
    print("=" * 56)
    print(" BUZDOLAGI ISIGI ETIK KOMITESI")
    print(" Oturum kaydi:", simdi.strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 56)
    print("Hazir bulunanlar:")
    for u in UYELER:
        print(" -", u)
    print()
    if 0 <= saat < 6:
        print("Gundem: Gece acilimi basvurusu.")
    else:
        print("Gundem: Gunduz acilimi. Komite saskindir ama yine de karar verir.")
    print("Gerekce:", random.choice(GEREKCELER))
    karar = random.choice(KARARLAR)
    print("KARAR:", karar)
    print()
    print("Oybirligi ile (kimse uyanik degildi).")
    print("Tutanak kapatildi.")
    print()
    print("-" * 56)
    print("Damga / Imza / Tarih")
    print("Kayyum Grok  |  Tentivory  |  11 Eylul 2026")
    print("Ciddi resmiyet: VAR   Ciddi icerik: YOK")
    print("-" * 56)
    return karar


if __name__ == "__main__":
    oturum_ac()
