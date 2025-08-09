from pathlib import Path
import argparse
import segno

LINK = "https://edocap-web.github.io/"

def generate_qr(out_dir: Path, name: str, scale: int, border: int, dark: str, light: str):
    out_dir.mkdir(parents=True, exist_ok=True)
    q = segno.make(LINK, error='h')  # alta correzione d'errore
    png_path = out_dir / f"{name}.png"
    svg_path = out_dir / f"{name}.svg"
    q.save(png_path, scale=scale, border=border, dark=dark, light=light)
    q.save(svg_path, border=border, dark=dark, light=light)
    print(f"Creati:\n - {png_path}\n - {svg_path}")

def main():
    parser = argparse.ArgumentParser(description="Genera QR code statici per edocap-web.github.io")
    parser.add_argument("-o", "--output-name", default="qr_edocap", help="Nome base del file (senza estensione)")
    parser.add_argument("-d", "--dir", default="qrcodes", help="Directory di output")
    parser.add_argument("--scale", type=int, default=8, help="Scala PNG (dimensione pixel per modulo)")
    parser.add_argument("--border", type=int, default=2, help="Bordo (moduli)")
    parser.add_argument("--dark", default="black", help="Colore moduli (es. black, #2C3E50)")
    parser.add_argument("--light", default="white", help="Colore sfondo (es. white, transparent)")
    args = parser.parse_args()

    out_dir = Path(args.dir)
    generate_qr(out_dir, args.output_name, args.scale, args.border, args.dark, args.light)

if __name__ == "__main__":
    main()