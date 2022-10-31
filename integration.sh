rm -r dist
rm -r build
# shellcheck disable=SC2035
rm *.spec
pyinstaller --onefile main.py