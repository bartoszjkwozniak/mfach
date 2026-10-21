# MFach - Wizytówka Internetowa (4 Profile Usługowe)

Nowoczesna, w pełni responsywna wizytówka internetowa dla firmy **MFach**, przygotowana do natychmiastowej publikacji na **GitHub Pages**.

## 👤 Dane kontaktowe firmy
- **Firma:** MFach
- **Właściciel / Kontakt:** Marcin
- **Telefon:** [695 525 389](tel:695525389)
- **Obszar działania:** Kętrzyn i okolice w promieniu ~50 km (m.in. Mrągowo, Giżycko, Węgorzewo, Reszel, Korsze, Bartoszyce, Biskupiec)

---

## 🎨 4 Profile / Dziedziny działalności

Wizytówka posiada spójny układ graficzny oraz indywidualną identyfikację kolorystyczną dla każdej dziedziny:

1. **🚜 Serwis Ciągników Rolniczych & Maszyn Agro**
   - **Kolorystyka:** Agro Green (Zieleń rolnicza `#16a34a` / akcent `#4ade80`)
   - **Zakres:** Naprawy silników, hydraulika siłowa, mosty napędowe, pneumatyka, dojazd mobilny na pole i do gospodarstwa.
   - **Dedykowany plik:** `rolnictwo.html` lub `index.html#agro`

2. **🚗 Mechanika Samochodowa**
   - **Kolorystyka:** Dynamic Royal Blue (Niebieski warsztatowy `#2563eb` / akcent `#38bdf8`)
   - **Zakres:** Bieżące naprawy, wymiana oleju silnikowego i przekładniowego, komplety filtrów, klocki i tarcze hamulcowe, zawieszenie, rozrządy.
   - **Dedykowany plik:** `mechanika.html` lub `index.html#auto`

3. **🏠 Prace Wykończeniowe & Remonty Domów**
   - **Kolorystyka:** Industrial Warm Amber (Ceglasty pomarańcz `#ea580c` / akcent `#fb923c`)
   - **Zakres:** Remonty mieszkań i domów, gładzie bezpyłowe, malowanie, zabudowy G-K, panele podłogowe, glazurnictwo.
   - **Dedykowany plik:** `remonty.html` lub `index.html#remont`

4. **💧 Hydraulika, Kotłownie & Wod-Kan**
   - **Kolorystyka:** Aqua / Cyan (Błękit instalacyjny `#0891b2` / akcent `#22d3ee`)
   - **Zakres:** Nowoczesne kotłownie, pompy ciepła, instalacje wod-kan, biały montaż, stelaże Geberit, ogrzewanie podłogowe, usuwanie awarii i nieszczelności.
   - **Dedykowany plik:** `hydraulika.html` lub `index.html#hydro`

---

## ⚡ Główne funkcje strony
- **Błyskawiczny przełącznik 4-w-1** na stronie głównej (`index.html`) z płynną zmianą motywu kolorystycznego i oferty bez konieczności przeładowywania strony.
- **Gest Swipe na telefonie:** Przesunięcie palcem w lewo/prawo na smartfonie płynnie zmienia dziedziny.
- **Interaktywna sekcja obszaru działania:** Wkomponowana mapa (`assets/map.png`) z promieniem obsługi do 50 km od Kętrzyna.
- **Dedykowane podstrony** (`rolnictwo.html`, `mechanika.html`, `remonty.html`, `hydraulika.html`) – idealne do umieszczenia w osobnych ogłoszeniach OLX, wizytówkach Google czy kodach QR.
- **Obsługa urządzeń mobilnych (Mobile First)** ze stałym paskiem szybkiego połączenia u dołu ekranu (*"Zadzwoń: 695 525 389"*).
- **Czysty kod:** Czysty HTML5, CSS3 (zmienne CSS, Flexbox, Grid) oraz lekki Vanilla JavaScript bez ciężkich zewnętrznych bibliotek (szybkie ładowanie 100/100 w PageSpeed).

---

## 📁 Struktura plików

```text
mfach/
├── index.html           # Główna strona z interaktywnym przełącznikiem 4 branż
├── rolnictwo.html       # Dedykowana podstrona: Ciągniki rolnicze (motyw zielony)
├── mechanika.html       # Dedykowana podstrona: Mechanika samochodowa (motyw niebieski)
├── remonty.html         # Dedykowana podstrona: Wykończenia & remonty (motyw pomarańczowy)
├── hydraulika.html      # Dedykowana podstrona: Hydraulika & kotłownie (motyw turkusowy)
├── budownictwo.html     # Alias przekierowujący do remonty.html
├── css/
│   └── style.css        # Główny arkusz stylów z paletami kolorów i responsywnością
├── js/
│   └── main.js          # Skrypt obsługi motywów, danych usług i gestów swipe
├── assets/
│   ├── favicon.svg      # Wektorowa ikonka strony (favicon)
│   ├── hero_agro.png    # Ilustracja 3D: Marcin z ciągnikiem rolniczym
│   ├── hero_auto.png    # Ilustracja 3D: Marcin z samochodem w warsztacie
│   ├── hero_remont.png  # Ilustracja 3D: Marcin w wyremontowanym wnętrzu domu
│   ├── hero_hydro.png   # Ilustracja 3D: Marcin w nowoczesnej kotłowni z pompą
│   └── map.png          # Mapa obszaru działania firmy (Kętrzyn + 50 km)
└── README.md            # Dokumentacja i instrukcja wdrożenia
```

---

## 🚀 Instrukcja wdrożenia na GitHub Pages (Krok po kroku)

1. **Utwórz repozytorium na GitHubie:**
   - Nazwij je np. `mfach` lub `mfach-serwis` (lub `<twoj-login>.github.io` jeśli ma być stroną główną konta).
   
2. **Prześlij pliki do repozytorium:**
   ```bash
   git init
   git add .
   git commit -m "Wdrożenie wizytówki MFach"
   git branch -M main
   git remote add origin https://github.com/TWOJA_NAZWA_UZYTKOWNIKA/mfach.git
   git push -u origin main
   ```

3. **Włącz GitHub Pages:**
   - Wejdź w repozytorium na GitHubie w zakładkę **Settings** (Ustawienia).
   - W menu po lewej stronie kliknij **Pages**.
   - W sekcji **Build and deployment -> Source** wybierz `Deploy from a branch`.
   - Pod spodem wybierz branch: `main` i folder: `/ (root)`.
   - Kliknij **Save**.

Po 1-2 minutach strona będzie dostępna publicznie pod adresem:
`https://TWOJA_NAZWA_UZYTKOWNIKA.github.io/mfach/`
