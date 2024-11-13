# STL Compressor

STL Compressor is a tool designed to compress STL files efficiently. Users can conveniently compress multiple STL files in batches, reducing their file sizes without compromising on quality.

## Usage

* Windows users can download [here](https://github.com/fan-ziqi/stl_compressor/releases)

* Python

  ```bash
  pip install --upgrade stl_compressor -i https://www.pypi.org/simple/
  stl_compressor
  ```

## Packaging

To package the application as a standalone executable, use PyInstaller:

```bash
pyinstaller --onefile --windowed stl_compressor/stl_compressor_ui.py
```

## Upload to Pypi

```bash
python setup.py check
python setup.py sdist bdist_wheel
twine upload dist/*
```
