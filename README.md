# Webcam OCR

Enterキーを押してWebカメラの映像を撮影し、OCRを実行するPythonスクリプト

## セットアップ

1. uvをインストール (まだの場合):
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. 依存関係をインストール:
```bash
uv pip install -e .
```

3. Tesseract-OCRをインストール:
   - Windows: https://github.com/UB-Mannheim/tesseract/wiki
   - インストール後、必要に応じて`webcam_ocr.py`内のTesseractパスを設定

4. 日本語OCRを使用する場合:
   - Tesseractインストール時に日本語データを追加でインストール

## 使用方法

```bash
uv run python webcam_ocr.py
```

- **Enter**: 画像を撮影してOCR実行
- **q**: 終了

撮影した画像とOCR結果はタイムスタンプ付きで保存されます。