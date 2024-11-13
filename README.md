# STL Compressor

STL Compressor is a tool designed to compress STL files efficiently. Users can conveniently compress multiple STL files in batches, reducing their file sizes without compromising on quality.

## Usage

Install with pip

```bash
pip install --upgrade stl_compressor -i https://www.pypi.org/simple/
stl_compressor
```

You can also download the Windows exe file [here](https://github.com/fan-ziqi/stl_compressor/releases)

## Packaging

To package the application as a standalone exe file for windows, use PyInstaller:

```bash
pyinstaller --onefile --windowed stl_compressor/stl_compressor_ui.py
```

## Upload to Pypi

```bash
python setup.py check
python setup.py sdist bdist_wheel
twine upload dist/*
```
