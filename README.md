# twj.co.id — Website Redesign

Tanuwijaya &amp; Partners · redesign 5 halaman · Anomali Studio, 2026

Struktur section, urutan, dan seluruh teks **mengikuti situs lama twj.co.id
apa adanya**. Yang diganti hanya lapisan branding: warna, tipografi, ikon,
foto, dan spacing.

## Cara buka

Static HTML biasa — tidak perlu build tool, tidak perlu framework.
Karena halaman memakai relative path, buka lewat local server (bukan `file://`):

```bash
python -m http.server 8123
```

Lalu buka <http://127.0.0.1:8123/>.

## Struktur

```
web/
├── index.html                  Home
├── about.html                  About Us
├── our-people.html             Our People
├── industries-services.html    Industries & Services
├── contact.html                Contact
├── favicon.svg
├── assets/
│   ├── css/style.css           satu file, semua design token di :root
│   ├── js/main.js              vanilla JS, tanpa dependency
│   ├── logo/                   logo SVG (primary, light, logogram)
│   └── img/                    hero, about, people/, clients/  (semua .webp)
└── _tools/
    ├── build.py                generator 5 halaman dari partial bersama
    ├── bundle.py               generator preview 1-file (untuk share link)
    └── twj-preview.html        hasil bundle (2,2 MB, self-contained — di-gitignore)
```

Header, footer, CTA band, dan ikon didefinisikan sekali di `_tools/build.py`
supaya tidak pernah beda antar halaman. Setelah mengubah bagian bersama:

```bash
python _tools/build.py
```

## Isi tiap halaman

| Halaman | Section (urut) |
|---|---|
| Home | hero → Founding Story → Our Partners → Our Services → CTA |
| About Us | hero → Founding Story (teks + foto) → foto + teks → Clients → CTA |
| Our People | hero → Partners → Associates → Companies → CTA |
| Industries & Services | hero → Industries → Our Services → CTA |
| Contact | hero → Leave a Message → Our Offices |

## Design system

| Token | Nilai | Pemakaian |
|---|---|---|
| `--navy` | `#1F3A5F` | heading, blok gelap, tombol utama |
| `--luster` | `#F4F1EC` | background halaman |
| `--white` | `#FFFFFF` | background section selang-seling |
| `--slate` | `#6E6E6E` | body text |
| `--silver` | `#B5B0AA` | garis, label sekunder |
| `--gold` | `#C8A45D` | hairline di bawah heading, hover — maksimal 3% |

Rasio mengikuti Brand Guideline (Submission 2, 260520):
70% white/warm white · 20% navy · 7% slate &amp; silver · 3% gold.

Tipografi: **Noto Serif Bold** untuk heading, **Noto Sans Regular** untuk
paragraf, label, dan navigasi. Di-load dari Google Fonts; file `.ttf` untuk
self-host ada di `_Shared/_Font/`.

## Interaksi

- Header transparan di atas hero, jadi solid saat scroll.
- Menu mobile: drawer full-screen navy.
- Accordion partner di Home (foto ikut berganti).
- Reveal on scroll (IntersectionObserver, hormat `prefers-reduced-motion`).
- Logo klien: grayscale, jadi full color saat hover.
- Form Contact punya pilihan **Send Whatsapp Message / Send Email** seperti
  situs lama — belum ada backend, jadi submit membuka WhatsApp atau email
  client. Untuk kirim langsung dari web, pasang endpoint (Formspree /
  Web3Forms / API sendiri) di `assets/js/main.js`.
- Tombol WhatsApp melayang, muncul setelah scroll.

## Yang perlu dikonfirmasi klien

1. **Domain email tim** — situs lama pakai `@kaptwj.com`, sementara name card
   dan email signature branding baru pakai `@twj.co.id`. Sekarang dipasang
   `@kaptwj.com` (ikut situs lama).
2. **Link sosial media** masih generik (`facebook.com`, `instagram.com`)
   persis seperti situs lama.
3. **Foto Chaterine Tanuwijaya** belum ada — sementara monogram "CT".
4. **Foto Linda Purnomo** diambil dari `Asset/twj.co.id/Linda Purnomo.png`,
   mohon dicek apakah benar foto beliau.
5. Judul hero About di situs lama tertulis "Our Humble **Begining**" — di sini
   diperbaiki jadi "Beginning".

## Deploy

Repo: <https://github.com/anomalidigital/TWJ>

Setiap push ke `main` otomatis di-deploy ke GitHub Pages lewat
`.github/workflows/pages.yml`. Tidak ada langkah manual — workflow-nya
sekalian mengaktifkan Pages di repo.

Karena semua link di halaman memakai relative path, situs ini jalan baik di
root domain maupun di subpath seperti `/TWJ/`. Waktu nanti pindah ke
twj.co.id, tidak ada yang perlu diubah.

## Optimasi gambar

Semua foto sudah dikonversi ke `.webp` (total ± 1,4 MB untuk seluruh situs).
Kalau ada foto baru, samakan ukuran: hero 1840×690 (pakai banner asli twj.co.id), gambar section 1500×1000,
potret orang 760×880, logo klien lebar 360.
