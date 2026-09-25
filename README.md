# Daumenregel – UI-Pattern-Library

Eine selbsterklärende Web-App, die UI-Best-Practices nicht beschreibt, sondern vorführt.
Statt Blindtext steht in jeder Ansicht, *warum* etwas so gebaut ist – und die App hält sich
selbst an jede Regel, die sie erklärt.

## Starten

`index.html` im Browser öffnen, per Doppelklick. Kein Build, kein Server, keine
Abhängigkeiten. Internet braucht es nur für die Google-Schriften; offline springt die
Systemschrift ein.

## Inhalt

29 Lektionen in 8 Kapiteln:

| Kapitel | Lektionen |
|---|---|
| Grundlagen | Abstände & Gestaltgesetze, UX-Gesetze |
| Bedienung | Touch-Targets, Buttons, Formulare, Overlays, Gesten, Onboarding |
| Daten & Inhalte | Tabellen & Listen, Suche & Filter |
| Feedback | Toasts, Ladezustände, Empty States, Modal-Dialoge, Fehler & Offline |
| Navigation | Deep Linking, Master-Detail, Navigation & Orientierung |
| Barrierefreiheit | Kontrast, Tastatur & Fokus, Farbe nie allein, Semantik, Bewegung |
| Layout & Marke | Typografie, Responsive & Reflow, White-Label & Design Tokens |
| Qualität | Performance (Core Web Vitals), Internationalisierung, Dark Patterns |

Jede Lektion hat denselben Aufbau: **Regel → Die Zahlen → Live-Beispiel → Richtig →
Falsch (mit Negativbeispiel pro Punkt) → Warum → In dieser App**.

## Bedienung

- **Bauteile zeigen** (oben rechts) beschriftet jedes Element mit seinem Fachbegriff.
- **Marke** wechselt zwischen drei fiktiven Marken (Fjord, Glut, Moos) – gleicher Code,
  andere Design Tokens. Das ist der White-Label-Teil.
- Tastatur: `Tab` / `Shift+Tab`, `/` springt in die Suche, `Esc` schließt Dialoge,
  `Strg+Z` macht ein Löschen rückgängig, solange der Toast sichtbar ist.
- Jede Lektion hat eine eigene Adresse (`index.html#toast`), der Zurück-Button funktioniert.
- Der Lernfortschritt liegt im `localStorage` dieses Browsers.

## Aufbau

Alles steckt bewusst in einer Datei:

- **CSS** oben: Design Tokens auf `:root`, Marken über `[data-brand]`, Dark Mode über
  `prefers-color-scheme` und `[data-theme]`.
- **`LESSONS`**: ein Objekt pro Lektion mit Regel, Zahlen, Demo-HTML, `init()` für die
  Interaktion, Richtig/Falsch-Listen, Erklärung.
- **`BAD`**: die Negativbeispiele, pro Lektion in derselben Reihenfolge wie die
  Falsch-Liste. Reine Anschauungsbeispiele sind `inert`, damit absichtlich kaputte
  Beispiele die Barrierefreiheit der App selbst nicht beschädigen.
- **Router**: Hash-Routing, Fokus nach jedem Wechsel auf die neue `h1`.

Die Icons (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`) erzeugt
`python tools/make_icons.py` aus einer gemeinsamen Geometrie (braucht Pillow).
