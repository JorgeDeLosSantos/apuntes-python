@ECHO OFF
jupyter-book build .
ghp-import -n -p -f _build/html
_build\html\index.html
exit