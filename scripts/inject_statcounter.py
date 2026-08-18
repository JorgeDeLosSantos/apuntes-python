from pathlib import Path


BUILD_DIR = Path("_build/html")

STATCOUNTER = """
<!-- Default Statcounter code for Python para ingenieros -->
<script type="text/javascript">
var sc_project=13087844;
var sc_invisible=1;
var sc_security="a797accf";
</script>
<script
  type="text/javascript"
  src="https://www.statcounter.com/counter/counter.js"
  async>
</script>
<noscript>
  <div class="statcounter">
    <a
      title="Web Analytics"
      href="https://statcounter.com/"
      target="_blank">
      <img
        class="statcounter"
        src="https://c.statcounter.com/13087844/0/a797accf/1/"
        alt="Web Analytics"
        referrerpolicy="no-referrer-when-downgrade">
    </a>
  </div>
</noscript>
<!-- End of Statcounter Code -->
"""


def main():
    if not BUILD_DIR.exists():
        raise FileNotFoundError(
            f"No existe {BUILD_DIR}. "
            "Ejecuta primero: jupyter book build --html"
        )

    modified = 0

    for path in BUILD_DIR.rglob("*.html"):
        content = path.read_text(encoding="utf-8")

        # Evita insertar el contador dos veces
        if "sc_project=13087844" in content:
            continue

        if "</body>" not in content:
            print(f"Skipping {path}: no </body>")
            continue

        content = content.replace(
            "</body>",
            f"{STATCOUNTER}\n</body>",
            1,
        )

        path.write_text(content, encoding="utf-8")
        modified += 1
        print(f"Injected Statcounter: {path}")

    print(f"\nModified {modified} HTML files.")


if __name__ == "__main__":
    main()