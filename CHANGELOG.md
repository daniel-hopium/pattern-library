# Changelog

Alle nennenswerten Änderungen an Daumenregel (pattern-library). Die Einträge beschreiben,
was das Projekt danach kann bzw. was sich für den Nutzer ändert – kein Commit-Protokoll.

**Regel:** Jeder Commit bekommt seinen Eintrag, im selben Commit. Neues kommt oben unter
„Unveröffentlicht“ dazu; beim Release wird daraus ein Abschnitt mit Versionsnummer und Datum.

Kategorien: **Neu** (neue Funktionen), **Verbessert** (bestehendes Verhalten), **Behoben**
(Fehler), **Intern** (Struktur, Tooling, nicht sichtbar).

## Unveröffentlicht

### Neu
- WCAG-Kompass: WCAG 2.2 auf Stufe A und AA, übersetzt für Frontend-Devs – Überblick
  mit Rechtslage, zehn Bauteile mit Angular-Hinweisen und Code „so nicht / so“, alle 55
  Kriterien filterbar, Test-Routine mit CI-Setup und eine Checkliste für den Pull Request.
- WCAG-Chips in den Lektionen führen direkt zum passenden Kriterium im Kompass.
- Eigenes Favicon: ein Daumenabdruck im Linienstil und in den Farben der mind app, als
  SVG für moderne Browser, ICO als Rückfall und PNG für den iOS-Homescreen.
- Selbsterklärende UI-Pattern-Library als einzelne Web-App: 29 Lektionen in 8 Kapiteln,
  jeweils mit Regel, Kennzahlen, Live-Beispiel, Richtig-Liste, Negativbeispielen und
  dem Hinweis, wo die Regel in der App selbst steckt.
- White-Label mit drei Marken (Fjord, Glut, Moos), Hell/Dunkel-Umschaltung und
  automatischer Kontrastprüfung der Markenfarbe.
- „Bauteile zeigen“ beschriftet alle Oberflächenelemente mit ihrem Fachbegriff.
- Lernfortschritt pro Lektion, Suche über alle Lektionen, eigene Adresse je Lektion.
