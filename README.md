# Panduan Menjalankan Dashboard Pada Streamlit

Panduan ini menjelaskan cara menjalankan aplikasi `dashboard.py` pada Streamlit.

## 1. Membuat dan Mengaktifkan Virtual Environment

Sebelum menginstal dependensi, sangat disarankan untuk membuat dan mengaktifkan virtual environment untuk mengisolasi lingkungan Python.

### Windows (Command Prompt)

```sh
python -m venv venv
venv\Scripts\activate
```

### Windows (PowerShell)

```sh
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### macOS & Linux (bash/zsh)

```sh
python3 -m venv venv
source venv/bin/activate
```

## 2. Menginstal Dependensi

Setelah virtual environment aktif, instal semua dependensi yang diperlukan dari `requirements.txt`:

```sh
pip install -r requirements.txt
```

## 3. Menjalankan Aplikasi Dashboard

Setelah semua dependensi terinstal, jalankan aplikasi dashboard dengan perintah berikut:

```sh
streamlit run dashboard/dashboard.py
```

Aplikasi akan berjalan, dan URL aksesnya akan ditampilkan di terminal. Biasanya dapat diakses melalui:

```
http://localhost:8501
```

Buka URL tersebut di browser untuk melihat aplikasi dashboard dengan Streamlit.

---

## Semoga berhasil!
