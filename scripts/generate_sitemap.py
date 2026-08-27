from pathlib import Path
import xml.etree.ElementTree as ET


BASE_URL = "https://jorgedelossantos.github.io/apuntes-python"
BUILD_DIR = Path("_build/html")
OUTPUT_FILE = BUILD_DIR / "sitemap.xml"


def main():
    if not BUILD_DIR.exists():
        raise FileNotFoundError(
            f"No existe {BUILD_DIR}. "
            "Ejecuta primero: jupyter-book build --html"
        )

    pages = sorted(BUILD_DIR.rglob("index.html"))

    urlset = ET.Element(
        "urlset",
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9",
    )

    for page in pages:
        relative_dir = page.parent.relative_to(BUILD_DIR).as_posix()
        if relative_dir == ".":
            loc_value = f"{BASE_URL}/"
        else:
            loc_value = f"{BASE_URL}/{relative_dir}/"

        url = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = loc_value

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(
        OUTPUT_FILE,
        encoding="utf-8",
        xml_declaration=True,
    )


if __name__ == "__main__":
    main()
