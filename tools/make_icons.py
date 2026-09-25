"""Erzeugt favicon.svg, favicon.ico und apple-touch-icon.png aus EINER Geometrie.

Aufruf aus dem Repo: python tools/make_icons.py (braucht Pillow).

Pillow kann kein SVG lesen, darum werden die Bögen hier als Punktfolgen berechnet und
für SVG (Pfad) wie für PNG (Polylinie) aus denselben Zahlen gezeichnet. Farben und
Linienstil stammen aus der mind app: dunkler Grund, blasses Blau, goldener Kern.
"""
import math
from pathlib import Path

from PIL import Image, ImageDraw

OUT = Path(__file__).resolve().parent.parent  # Repo-Wurzel
BG, LINE, GOLD = "#0F1418", "#C2D6EA", "#E0C48A"
CX, CY, W = 16, 16.5, 2.2
# (rx, ry, Start°, Ende°, Deckkraft) – Winkel im Uhrzeigersinn ab 3 Uhr, Ende > Start.
# Hochformat-Ellipsen mit versetzten Lücken, damit es nach Fingerkuppe aussieht und
# nicht nach WLAN-Symbol (gleich ausgerichtete Bögen).
ARCS = [
    (10.2, 12.0, 118, 422, 0.45),  # außen: Lücke unten, blass
    (6.9, 8.4, 138, 437, 1.0),     # Mitte: Lücke unten, leicht nach links versetzt
    (3.5, 4.6, 62, 318, 1.0),      # innen: Schleife nach rechts offen
]
CORE_R = 1.6


def points(rx, ry, a0, a1, step=3):
    n = max(2, int((a1 - a0) / step))
    return [(CX + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             CY + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def svg():
    paths = []
    for rx, ry, a0, a1, op in ARCS:
        d = "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in points(rx, ry, a0, a1))
        paths.append(f'    <path d="{d}"' + (f' stroke-opacity="{op}"' if op < 1 else "") + "/>")
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">\n'
        '  <!-- Daumenabdruck im Linienstil der mind app. Erzeugt von tools/make_icons.py. -->\n'
        f'  <rect width="32" height="32" rx="7" fill="{BG}"/>\n'
        f'  <g fill="none" stroke="{LINE}" stroke-width="{W}" stroke-linecap="round" stroke-linejoin="round">\n'
        + "\n".join(paths) + "\n  </g>\n"
        f'  <circle cx="{CX}" cy="{CY}" r="{CORE_R}" fill="{GOLD}"/>\n'
        "</svg>\n"
    )


def rgba(hexcol, a=1.0):
    h = hexcol.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4)) + (round(255 * a),)


def png(size, rounded, ss=16):
    """In ss-facher Größe zeichnen und verkleinern – ergibt glatte Kanten."""
    k = size * ss / 32
    img = Image.new("RGBA", (size * ss, size * ss), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, size * ss - 1, size * ss - 1], radius=7 * k, fill=rgba(BG))
    else:  # iOS rundet die Ecken selbst ab; transparente Ecken würden schwarz
        d.rectangle([0, 0, size * ss, size * ss], fill=rgba(BG))
    w = W * k
    for rx, ry, a0, a1, op in ARCS:
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        pts = [(x * k, y * k) for x, y in points(rx, ry, a0, a1)]
        ld.line(pts, fill=rgba(LINE), width=round(w), joint="curve")
        for x, y in (pts[0], pts[-1]):  # runde Linienenden
            ld.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill=rgba(LINE))
        if op < 1:
            layer.putalpha(layer.getchannel("A").point(lambda v: round(v * op)))
        img = Image.alpha_composite(img, layer)
    d = ImageDraw.Draw(img)
    r = CORE_R * k
    d.ellipse([CX * k - r, CY * k - r, CX * k + r, CY * k + r], fill=rgba(GOLD))
    return img.resize((size, size), Image.LANCZOS)


if __name__ == "__main__":
    (OUT / "favicon.svg").write_text(svg(), encoding="utf-8", newline="\n")
    icons = {s: png(s, True) for s in (16, 32, 48)}
    icons[48].save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)],
                   append_images=[icons[16], icons[32]])
    png(180, False).save(OUT / "apple-touch-icon.png")
    print("favicon.svg, favicon.ico, apple-touch-icon.png geschrieben")
