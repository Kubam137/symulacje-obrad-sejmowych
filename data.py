# === data.py ===

partie = {
    "progres2025": {
        "nazwa": "Impuls społeczny",
        "logo_class": "fa-solid fa-leaf",
        "claim": "Nowoczesna polityka dla ludzi i planety.",
        "priorytety": {
            "edu1": +10, "edu2": +5, "edu3": 0, "edu4": -5, "edu5": -10,
            "klim1": +10, "klim2": +5, "klim3": 0, "klim4": -5, "klim5": -10,
            "gosp1": +10, "gosp2": +5, "gosp3": 0, "gosp4": -5, "gosp5": -10
        }
    },
    "rownosc2025": {
        "nazwa": "Solidarność i Wspólnota",
        "logo_class": "fa-solid fa-hand-back-fist",
        "claim": "Wspólnota, odpowiedzialność i godność pracy.",
        "priorytety": {
            "edu1": -10, "edu2": +10, "edu3": +5, "edu4": 0, "edu5": -5,
            "klim1": -10, "klim2": +10, "klim3": +5, "klim4": 0, "klim5": -5,
            "gosp1": -10, "gosp2": +10, "gosp3": +5, "gosp4": 0, "gosp5": -5
        }
    },
    "tradycja2025": {
        "nazwa": "Dla Polski",
        "logo_class": "fa-solid fa-shield",
        "claim": "Silne państwo, bezpieczne wartości, polski interes.",
        "priorytety": {
            "edu1": -5, "edu2": -10, "edu3": +10, "edu4": +5, "edu5": 0,
            "klim1": -5, "klim2": -10, "klim3": +10, "klim4": +5, "klim5": 0,
            "gosp1": -5, "gosp2": -10, "gosp3": +10, "gosp4": +5, "gosp5": 0
        }
    },
    "centrum2025": {
        "nazwa": "Porozumienie Obywatelskie",
        "logo_class": "fa-solid fa-handshake",
        "claim": "Rozsądek, dialog i równowaga w działaniu.",
        "priorytety": {
            "edu1": 0, "edu2": -5, "edu3": -10, "edu4": +10, "edu5": +5,
            "klim1": 0, "klim2": -5, "klim3": -10, "klim4": +10, "klim5": +5,
            "gosp1": 0, "gosp2": -5, "gosp3": -10, "gosp4": +10, "gosp5": +5
        }
    },
    "wolnosc2025": {
        "nazwa": "Forum Przyszłosći",
        "logo_class": "fa-solid fa-comment-dollar",
        "claim": "Wolność, innowacje i przedsiębiorczość",
        "priorytety": {
            "edu1": +5, "edu2": 0, "edu3": -5, "edu4": -10, "edu5": +10,
            "klim1": +5, "klim2": 0, "klim3": -5, "klim4": -10, "klim5": +10,
            "gosp1": +5, "gosp2": 0, "gosp3": -5, "gosp4": -10, "gosp5": +10
        }
    }
}


bloki = [
    {
        "nazwa": "Blok 1",
        "temat": "Edukacja",
        "ustawy": [
            {"id": "edu1", "tytul": "Ustawa o wprowadzeniu edukacji seksualnej", "opis": "Wprowadzenie edukacji seksualnej od 7 klasy szkoły podstawowej."},
            {"id": "edu2", "tytul": "Ustawa o likiwdacji finansowania religii z budżetu państwa", "opis": "Likwidacja publicznego finansowania lekcji religii."},
            {"id": "edu3", "tytul": "Ustawa o obowiązkowej służbie obywatelskiej", "opis": "Półroczna służba obywatelska po ukończeniu 16. roku życia"},
            {"id": "edu4", "tytul": "Ustawa o ujednoliceniu zasad systemu oceniania szkolnego", "opis": "Jednolite zasady oceniania uczniów w całej Polsce."},
            {"id": "edu5", "tytul": "Ustawa o zwolnieniu prywatnych szkół z podatku VAT", "opis": "Zwolnienie szkół prywatnych z podatku VAT na czesne."}
        ]
    },
    {
        "nazwa": "Blok 2",
        "temat": "Klimat",
        "ustawy": [
            {"id": "klim1", "tytul": "Ustawa o standardzie efektywności energetycznej 2030", "opis": "Wymóg stosowania urządzeń zgodnych z normą 2030."},
            {"id": "klim2", "tytul": "Ustawa o podatku od nadmiernego zużycia wody", "opis": "Opłata za przekraczanie limitów zużycia wody."},
            {"id": "klim3", "tytul": "Ustawa o minimalnym dystansie dla turbin wiatrowych", "opis": "Zakaz budowy turbin w promieniu 800m od zabudowań."},
            {"id": "klim4", "tytul": "Ustawa o dodatku środowiskowym za odpady", "opis": "Wyższe opłaty za odpady w dużych ośrodkach miejskich."},
            {"id": "klim5", "tytul": "Ustawa o zielonych kompensacjach dla przedsiębiorstw", "opis": "Wsparcie dla firm stosujących offsety emisji."}
        ]
    },
    {
        "nazwa": "Blok 3",
        "temat": "Gospodarka",
        "ustawy": [
            {"id": "gosp1", "tytul": "Ustawa o 4-dniowym tygodniu pracy", "opis": "Skrócenie norm czasu pracy do 32 godzin tygodniowo."},
            {"id": "gosp2", "tytul": "Ustawa o wsparciu zatrudnienia długoterminowego", "opis": "Program wsparcia dla osób długotrwale bezrobotnych."},
            {"id": "gosp3", "tytul": "Ustawa o zwiększeniu opłat za wynajem krótkoterminowy", "opis": "Wyższe opłaty dla najmu turystycznego w dużych miastach."},
            {"id": "gosp4", "tytul": "Ustawa o podatku cyfrowym od globalnych platform", "opis": "Opodatkowanie przychodów dużych firm technologicznych."},
            {"id": "gosp5", "tytul": "Ustawa o zniesieniu podatku Belki", "opis": "Zniesienie podatku od zysków kapitałowych długoterminowych."}
        ]
    }
]

# Tymczasowo wskazujemy, która ustawa jest aktualnie omawiana
aktualna_ustawa_id = "Ustawa o klimacie"

ustawy = []
for blok in bloki:
    ustawy.extend(blok["ustawy"])