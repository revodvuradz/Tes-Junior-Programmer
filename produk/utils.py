import requests
import hashlib
from datetime import datetime
from .models import Produk, Kategori, Status


def get_api_data():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

    # STEP 1 — pancing header
    r = requests.post(url)
    username_header = r.headers.get("X-Credentials-Username")

    if not username_header:
        print("❌ Username header tidak ditemukan")
        return None

    username = username_header.split(" ")[0].strip()

    # STEP 2 — buat password MD5
    now = datetime.now()
    raw_password = f"bisacoding-{now.day:02d}-{now.month:02d}-{str(now.year)[-2:]}"
    md5_password = hashlib.md5(raw_password.encode()).hexdigest()

    # STEP 3 — request data asli
    payload = {
        "username": username,
        "password": md5_password
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Gagal ambil data API:", response.text)
        return None


def save_produk_from_api():
    data = get_api_data()

    if not data or data.get("error") != 0:
        print("❌ Data API tidak valid")
        return

    for item in data["data"]:
        kategori_obj, _ = Kategori.objects.get_or_create(
            nama_kategori=item["kategori"]
        )

        status_obj, _ = Status.objects.get_or_create(
            nama_status=item["status"]
        )

        # 🧠 update_or_create biar tidak dobel saat refresh
        Produk.objects.update_or_create(
            id_produk=item["id_produk"],
            defaults={
                "nama_produk": item["nama_produk"],
                "harga": int(item["harga"]),
                "kategori": kategori_obj,
                "status": status_obj,
            }
        )

    print("✅ Produk API berhasil disimpan / diupdate")
