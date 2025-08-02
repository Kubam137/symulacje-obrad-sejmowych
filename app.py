from flask import Flask, render_template, request, session, redirect, url_for
from data import partie, bloki, aktualna_ustawa_id

wyniki_ustaw = {}


app = Flask(__name__)
app.secret_key = 'tajnyklucz'  # 🔒 zmień na coś bezpiecznego w przyszłości



wyniki_przykladowe = [
    {"blok": "Blok 1", "tytul": "Reforma edukacji", "przyjeta": True, "punkty": 10},
    {"blok": "Blok 1", "tytul": "Bon edukacyjny", "przyjeta": False, "punkty": 0},
    {"blok": "Blok 2", "tytul": "Ustawa o klimacie", "przyjeta": True, "punkty": -5},
]


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        haslo = request.form["haslo"]
        if haslo in partie:
            session["partia"] = haslo  # 💾 zapisanie partii w sesji
            return redirect(url_for("partia_dashboard"))
        else:
            return render_template("login.html", blad="Niepoprawne hasło.")
    return render_template("login.html")

# 🔐 Logowanie Marszałka
@app.route("/login_marszalka", methods=["GET", "POST"])
def login_marszalka():
    if request.method == "POST":
        haslo = request.form.get("haslo")
        if haslo == "marszalek123":
            session["marszalek"] = True
            return redirect(url_for("panel_marszalka"))
    return render_template("marszalek_login.html")



@app.route('/panel_marszalka', methods=['GET'])
def panel_marszalka():
    blok_index = request.args.get('blok_index', default=None, type=int)

    ustawy = []
    if blok_index is not None and 0 <= blok_index < len(bloki):
        ustawy = bloki[blok_index]["ustawy"]
        for ustawa in ustawy:
            if "przyjeta" not in ustawa:
                ustawa["przyjeta"] = False

    return render_template(
        "panel_marszalka.html",
        bloki=bloki,
        blok_index=blok_index,
        ustawy=ustawy
    )


# ✅ Zapis przyjętych ustaw
@app.route("/marszalek-zapisz", methods=["POST"])
def marszalek_zapisz():
    if not session.get("marszalek"):
        return redirect(url_for("login_marszalka"))

    przyjete = request.form.getlist("przyjete")
    session["przyjete_ustawy"] = przyjete
    return redirect(url_for("panel_marszalka"))



@app.route("/zapisz-ustawy", methods=["POST"])
def zapisz_ustawy():
    if not session.get("marszalek"):
        return redirect(url_for("marszalek"))

    blok_index_str = request.form.get("blok_index")
    if blok_index_str is None or not blok_index_str.isdigit():
        return "Niepoprawny blok", 400
    blok_index = int(blok_index_str)
    przyjete_ids = request.form.getlist("przyjete_ustawy")

    for ustawa in bloki[blok_index]["ustawy"]:
        ustawa["przyjeta"] = ustawa["id"] in przyjete_ids

        # 👇 DODAJ TO: zaktualizuj globalne wyniki_ustaw
        wyniki_ustaw[ustawa["id"]] = (
            ustawa["tytul"],
            ustawa["przyjeta"],
            blok_index
        )

    return redirect(url_for("panel_marszalka", blok_index=blok_index))

@app.route("/priorytety")
def priorytety():
    haslo = session.get("partia")
    if haslo not in partie:
        return redirect(url_for("login"))

    dane = partie[haslo]
    priorytety = dane["priorytety"]

    bloki_z_ocenami = []
    for blok in bloki:
        ustawy_z_ocena = []
        for ustawa in blok["ustawy"]:
            id = ustawa["id"]
            ustawa_z_ocena = ustawa.copy()
            ustawa_z_ocena["ocena"] = priorytety.get(id, 0)
            ustawy_z_ocena.append(ustawa_z_ocena)
        bloki_z_ocenami.append({
            "nazwa": blok["nazwa"],
            "temat": blok["temat"],
            "ustawy": ustawy_z_ocena
        })

    return render_template("priorytety.html", dane=dane, bloki=bloki_z_ocenami)


@app.route("/ustawy")
def ustawy():
    haslo = session.get("partia")
    if haslo not in partie:
        return redirect(url_for("login"))
    return render_template("ustawy.html", bloki=bloki)

@app.route("/wyniki")
def wyniki():
    haslo = session.get("partia")
    if haslo not in partie:
        return redirect(url_for("login"))

    lista_wynikow = []
    suma_punktow = 0

    for ustawa_id, (tytul, przyjeta, blok_index) in wyniki_ustaw.items():
        ocena = partie[haslo]["priorytety"].get(ustawa_id, 0)
        punkty = ocena if przyjeta else 0
        suma_punktow += punkty
        lista_wynikow.append({
            "tytul": tytul,
            "przyjeta": przyjeta,
            "punkty": punkty,
            "blok": bloki[blok_index]["nazwa"]
        })

    return render_template("wyniki.html", dane=partie[haslo], wyniki=lista_wynikow, suma_punktow=suma_punktow)



def generuj_wyniki(przyjete_ustawy):
    wyniki = []
    for i, blok in enumerate(bloki):
        for ustawa in blok["ustawy"]:
            przyjeta = ustawa in przyjete_ustawy
            for partia, dane in partie.items():
                punkty = dane["priorytety"].get(ustawa, 0) if przyjeta else 0
                wyniki.append({
                    "blok": blok["nazwa"],
                    "tytul": ustawa["tytul"],
                    "opis": ustawa["opis"],
                    "przyjeta": przyjeta,
                    "punkty": punkty,
                    "partia": partia
                })
    return wyniki


@app.route("/zasady")
def zasady():
    return render_template("zasady.html")

@app.route("/partia")
def partia_dashboard():
    haslo = session.get("partia")
    if haslo not in partie:
        return redirect(url_for("login"))
    return render_template("partia.html", dane=partie[haslo])








# Pozostałe podstrony dodamy później

if __name__ == "__main__":
    app.run(debug=True, port=5001)
