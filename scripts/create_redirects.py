from pathlib import Path


BUILD_DIR = Path("_build/html")

REDIRECTS = {
    "intro.html": "./",
    "Introducción.html": "./introduccion/",
    "Variables, operadores y expresiones.html":
        "./variables-operadores-y-expresiones/",
    "Estructuras de control.html":
        "./estructuras-de-control/",
    "Cadenas de caracteres.html":
        "./cadenas-de-caracteres/",
    "Estructuras de datos.html":
        "./estructuras-de-datos/",
    "Funciones.html":
        "./funciones/",
    "Archivos de texto.html":
        "./archivos-de-texto/",
    "NumPy.html":
        "./numpy/",
    "Matplotlib.html":
        "./matplotlib/",
    "SciPy.html":
        "./scipy/",
    "Pandas.html":
        "./pandas/",
    "SymPy.html":
        "./sympy/",
    "Programación orientada a objetos.html":
        "./programacion-orientada-a-objetos/",
    "Bases de datos.html":
        "./bases-de-datos/",
}


TEMPLATE = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url={target}">
  <link rel="canonical" href="{target}">
  <title>Redirigiendo…</title>
  <script>
    window.location.replace("{target}" + window.location.hash);
  </script>
</head>
<body>
  <p>
    Esta página ha cambiado de ubicación.
    <a href="{target}">Continuar</a>.
  </p>
</body>
</html>
"""


def main():
    if not BUILD_DIR.exists():
        raise FileNotFoundError(
            f"No existe {BUILD_DIR}. "
            "Ejecuta primero: jupyter book build --html"
        )

    for old_url, new_url in REDIRECTS.items():
        output = BUILD_DIR / old_url
        output.write_text(
            TEMPLATE.format(target=new_url),
            encoding="utf-8",
        )
        print(f"{old_url} -> {new_url}")


if __name__ == "__main__":
    main()