# Design System — Landing Page Telkom Digital Enterprise

Dokumentasi bahasa visual yang dipakai di halaman Home (`index.html`). Tujuannya agar halaman berikutnya (**Who We Are**, **Services**, **Capabilities**, **Customer Stories**) dibangun dengan token, komponen, dan perilaku yang sama.

Semua nilai di dokumen ini diambil langsung dari [css/style.css](../css/style.css). Bila ada perbedaan, file CSS itu yang menjadi acuan. Untuk aturan penulisan copy, lihat [panduan-tone-of-voice.md](panduan-tone-of-voice.md).

---

## 1. Prinsip visual

Turunan langsung dari expression levers **Clear · Confident · Human**:

| Prinsip | Wujud di halaman |
|---|---|
| **Tenang dan lega** | Latar putih dan `--mist`, banyak ruang kosong, padding section 80–150px. |
| **Satu aksen kuat** | Merah Telkom hanya untuk CTA, penanda, angka `+`, garis hover, dan state aktif. Tidak dipakai sebagai warna blok besar (kecuali pintu di CTA). |
| **Metafora pintu** | "One Door": ikon pintu di headline hero, penanda `.dm` di setiap eyebrow, dan pintu besar yang terbuka di section CTA. |
| **Gerak yang bermakna** | Animasi selalu menjelaskan sesuatu (pintu terbuka, data mengalir ke hub, angka menghitung). Semua dimatikan saat `prefers-reduced-motion`. |
| **Headline dua nada** | Kalimat pertama tipis (300), kalimat kedua tebal (600). Contoh: *One platform.* **Every operation.** |

---

## 2. Warna

### 2.1 Token utama (`:root`)

| Token | Nilai | Penggunaan |
|---|---|---|
| `--navy` / `--ink` | `#202B3F` | Teks utama, heading, tab aktif, latar section CTA, tombol menu mobile |
| `--red` | `#E42313` | **Satu-satunya merah brand.** CTA, aksen, eyebrow marker, garis hover, chip default, tombol form, aksen mockup workspace |
| `--blue` | `#31617c` | Aksen sekunder: tag, chip biru, focus ring, badge |
| `--muted` | `#7a8394` | Body text, lede, label eyebrow |
| `--soft` | `#aab3c0` | Teks tersier: meta, legal footer, ikon panah idle |
| `--card` | `#ffffff` | Latar halaman dan kartu |
| `--mist` | `#f6f8fa` | Latar section selang-seling (`.sec.mist`) |
| `--tile` | `#eef2f6` | Latar tile mosaic, kartu modul, placeholder gambar |
| `--pill` | `#f1f3f6` | Tombol bulat netral (mis. tutup drawer) |
| `--line` | `#e4e8ee` | Semua garis pemisah dan border kartu |

### 2.2 Warna turunan (belum jadi token)

Nilai ini dipakai berulang tetapi masih ditulis langsung. Disarankan dijadikan token saat halaman baru dibuat.

| Usulan token | Nilai | Dipakai di |
|---|---|---|
| `--red-hover` | `#c01d10` | Hover tombol `.pricing` |
| `--red-tint` | `#fdecea` | Latar ikon pillar, chip merah, checkbox `.includes` |
| `--blue-tint` | `#e9f0f4` | Latar `.tag` dan `.chip.blue` |
| `--spoke` | `#d5dbe3` | Garis penghubung di diagram hub |

### 2.3 Palet section gelap (CTA dan form)

| Nilai | Peran |
|---|---|
| `#202B3F` | Latar section CTA |
| `rgba(21,31,56,.88)` | Latar kartu form (dengan `backdrop-filter: blur(8px)`) |
| `#0b132b` / `#0d1732` | Latar input / input saat focus |
| `#243256` / `#34467a` | Border input / border saat hover |
| `#e2e8f0` | Label form |
| `#b5bfcd` / `#9aa6b8` / `#94a3b8` / `#64748b` | Lede, eyebrow, catatan, placeholder |
| `#fda29b` / `#f04438` | Teks error / border error |

> **Aturan merah:** semua merah memakai `#E42313` (`--red`), dengan hover `#c01d10` dan transparansi `rgba(228,35,19,α)`. Jangan memakai varian lain seperti `#ee2e24` atau `#e52313`.

### 2.4 Gradien

- **Cahaya pintu (hero):** `linear-gradient(180deg, #E42313 0%, #ec6a5f 35%, #f7c3be 90%)`
- **Panel pintu besar (CTA):** `linear-gradient(160deg, #f04a3b, #c41b0e)`
- **Cahaya pintu besar:** `linear-gradient(180deg, #fff 0%, #ffe2de 45%, #ff8a7e 100%)`
- **Glow merah:** `radial-gradient(closest-side, rgba(228,35,19,.22), transparent)` di belakang CTA, versi `.14` di sudut kartu modul saat hover.
- **Ilustrasi isometrik hero:** gradien `gRT/gRL/gRR` (merah), `gPT/gPL/gPR` (navy–biru), `gPink`, `gLav`, `gGrey`, `gCream`. Lihat `<defs>` di awal `<body>`.

---

## 3. Tipografi

### 3.1 Font

- **Inter** (variable, `opsz 14..32`, weight 200–700) dari Google Fonts.
- Heading memakai `'Inter Display','Inter'` dengan `font-variation-settings:'opsz' 32` agar tampil sebagai optical size display.
- Fallback: `system-ui, -apple-system, 'Segoe UI', sans-serif`.
- Wordmark logo dummy klien memakai Georgia (serif) untuk variasi.

### 3.2 Skala

| Peran | Ukuran | Weight | Letter-spacing | Line-height |
|---|---|---|---|---|
| H1 hero | `clamp(36px, 4.8vw, 64px)` | 300 / 600 | `-.035em` | 1.1 |
| H2 section | `clamp(32px, 4.3vw, 58px)` | 300, `<b>` 600 | `-.035em` | 1.04 |
| Judul sub-section (`.ws-title`) | `clamp(26px, 2.8vw, 40px)` | 300, `<b>` 600 | `-.03em` | 1.08 |
| H3 panel | `clamp(24px, 2.3vw, 32px)` | 600 | `-.03em` | 1.15 |
| H3 kartu / pillar / story | `clamp(18px, 1.6vw, 22px)` | 600 | `-.02em` | 1.25 |
| H4 modul | 17px | 600 | `-.01em` | — |
| Big stat | `clamp(40px, 5vw, 72px)` | 700 | `-.045em` | 1 |
| Lede | `clamp(15px, 1.2vw, 17px)` | 400 | — | 1.7 |
| Body | 14–15px | 400 | — | 1.6–1.7 |
| Nav link | 13px | 400 (aktif 600) | — | — |
| Eyebrow / label caps | 12px | 600 | `.12–.14em`, uppercase | — |
| Tag / chip | 12px | 500–600 | — | — |

### 3.3 Aturan

- **Headline dua nada:** tulis H2 sebagai `Kalimat tipis <b>kalimat tebal.</b>`. `<b>` di H2 adalah `display:block`, jadi bagian tebal selalu turun ke baris baru (kecuali di CTA yang dibuat satu baris).
- `text-wrap: balance` untuk heading, `text-wrap: pretty` untuk lede.
- Lebar baca dibatasi: lede `52ch`, intro hero `60ch`, paragraf pillar `56ch`.
- Penekanan di paragraf memakai `<strong>` yang berubah ke `--ink` weight 600, bukan warna merah.
- Angka statistik memakai `font-variant-numeric: tabular-nums` dan tanda `+` merah (`<i>+</i>`).

---

## 4. Layout dan spasi

| Elemen | Nilai |
|---|---|
| Lebar konten maksimum (`.inner`) | 1280px, rata tengah |
| Gutter horizontal (`--gx`) | `clamp(18px, 5vw, 64px)`; 22px di ≤640px |
| Padding vertikal section (`.sec`) | `clamp(80px, 10vw, 150px)` |
| `scroll-margin-top` section | 70px (ruang untuk nav sticky) |
| Gap kolom split | `clamp(40px, 7vw, 120px)` |
| Jarak eyebrow → H2 | 20px |
| Jarak H2 → lede | 22px |

### Pola grid yang dipakai

| Pola | Kolom | Dipakai di |
|---|---|---|
| Split teks–konten | `5fr / 7fr` | What We Do, CTA |
| Split teks–visual | `5fr / 6fr` | Ecosystem, strip mitra |
| Panel gambar–copy | `7fr / 5fr` | Panel tab Solutions |
| Kartu modul | 3 kolom → 2 (≤1024) → 1 (≤640) | Ready-to-use Capabilities |
| Statistik | 4 kolom → 2 | Impact |
| Story | `1.35fr / 1fr` (feature + stack) | Impact |
| Footer | `4fr / 7fr`, kolom link 3 → 2 | Footer |

Section diselang-seling putih dan `--mist` untuk memberi ritme: putih (What We Do) → mist (Solutions) → putih (Impact) → mist (Ecosystem) → navy (CTA) → putih (Footer).

---

## 5. Radius, border, dan bayangan

### Radius

| Nilai | Dipakai di |
|---|---|
| 999px | Tag, chip |
| 50% | Tombol menu, badge, hub core |
| 10px | Tombol CTA nav, tab |
| 12px | Input, tombol submit |
| 14px | Container tab, partner chip, ikon eco |
| 16px | Ikon pillar |
| 22px | Kartu modul, frame preview workspace |
| 24px | Kartu form |
| 26px | Kartu story |
| 28px | Panel Solutions |
| **Leaf** | `8px` dan `clamp(26px, 3.2vw, 46px)` bergantian di sudut berseberangan (`.leaf`, `.leaf.flip`) untuk bingkai foto |

### Border dan bayangan

- Border standar: `1px solid var(--line)`.
- Bayangan selalu bernuansa navy dan negatif-spread (lembut, jatuh ke bawah):
  - Kartu hover: `0 22px 40px -26px rgba(32,43,63,.4)`
  - Story hover: `0 30px 50px -34px rgba(32,43,63,.45)`
  - Frame besar: `0 50px 90px -50px rgba(32,43,63,.45), 0 18px 40px -30px rgba(32,43,63,.3)`
  - Nav sticky: `0 1px 0 var(--line), 0 12px 30px -22px rgba(32,43,63,.35)`

---

## 6. Motion

### Easing dan durasi

| Token | Nilai | Untuk |
|---|---|---|
| `--ease` | `cubic-bezier(.77,0,.18,1)` | Transisi besar dua arah (mosaic, pintu, garis nav) |
| `--ease-out` | `cubic-bezier(.22,1,.36,1)` | Masuk, hover, reveal |
| `--dur` | `1.05s` | Perubahan layout mosaic |

### Pola animasi

| Pola | Perilaku |
|---|---|
| **Page load** (`.in`) | Naik 16px + fade, 0.9s, bertahap `--i × 90ms` |
| **Reveal on scroll** (`.rv` → `.rv.on`) | Naik 22px + fade, 0.8s, bertahap `--d × 80ms`, dipicu IntersectionObserver sekali |
| **Hover kartu** | `translateY(-4px)` + bayangan, 0.4–0.45s |
| **Hover link** | Garis bawah merah `scaleX` 0→1 dari kiri; panah `.link-arrow` geser 4px |
| **Hover pillar** | Garis merah atas melebar, latar `--mist`, ikon jadi merah dengan glyph putih |
| **Hero mosaic** | Berganti state `a ⇄ b` (mobile `a → b → c`) tiap 3.2s, juga bisa diklik/Enter |
| **Pintu CTA** | Terbuka `-68deg` saat section terlihat, `-80deg` saat form fokus, `-96deg` saat form terkirim |
| **Count-up** | Angka `.n` menghitung 1.6s, ease-out quart |
| **Loop dekoratif** | Marquee logo, packet di hub, ring putus-putus, halo; berhenti saat hover pada strip mitra |

### Aturan

- Semua animasi wajib dimatikan di `@media (prefers-reduced-motion: reduce)`.
- Hentikan timer saat tab tidak terlihat (`visibilitychange`).
- Jangan menganimasikan teks body; cukup heading, kartu, dan visual.

---

## 7. Komponen

### 7.1 Navigasi

- **Desktop:** logo kiri, link tengah (`.links`), tombol **Contact Us** (`.pricing`) kanan.
- Link aktif: `aria-current="page"`, weight 600, garis merah permanen.
- **Sticky:** setelah scroll 120px, nav menjadi `position: fixed` dengan latar putih 86% + `backdrop-filter: blur(14px)` dan animasi turun dari atas.
- **Mobile (≤860px):** link disembunyikan, diganti tombol bulat navy 52px yang membuka drawer kanan (`min(86vw, 360px)`), link 22px dengan pemisah garis, CTA di bawah. Tutup dengan ×, klik backdrop, klik link, atau Escape.
- Menu: Home, Who We Are, Services, Capabilities, Customer Stories.

### 7.2 Tombol dan link

| Varian | Spesifikasi |
|---|---|
| **Primary** (`.pricing`) | Latar `--red`, teks putih 13px/600, radius 10px, padding `14px 30px`, hover `#c01d10` |
| **Submit form** (`.demo-submit`) | Latar `--red`, hover `#c01d10`, tinggi 54px, radius 12px, 16px/700, ikon panah yang bergeser saat hover, state `disabled` opacity .7 |
| **Link panah** (`.link-arrow`) | Teks merah 14px/600 + ikon 16px yang bergeser 4px saat hover |
| **Tab** (`.tab`) | Di dalam container putih ber-border radius 14px; aktif = latar navy teks putih |

Focus: `outline: 2px solid var(--blue); outline-offset: 3px` untuk semua `a`, `button`, dan elemen interaktif.

### 7.3 Header section

```html
<p class="eyebrow rv"><i class="dm"></i>Label section</p>
<h2 class="rv" style="--d:1">Kalimat pembuka. <b>Kalimat penegas.</b></h2>
<p class="lede rv" style="--d:2">Penjelasan singkat dengan <strong>kata kunci</strong>.</p>
```

`.dm` adalah ikon pintu mini (merah di depan, navy di belakang). Di section gelap, bagian belakangnya menjadi `#5b6b86`.

### 7.4 Kartu dan daftar

| Komponen | Ciri |
|---|---|
| **Pillar** (`.pillar`) | Baris daftar: ikon 56px di kotak `--red-tint` radius 16, judul, paragraf, baris tag, panah. Dipisah garis `--line`. |
| **Panel** (`.panel`) | Kartu putih radius 28 berisi gambar `.leaf` 16:10 + copy (eyebrow merah, H3, paragraf, checklist 2 kolom, link panah). |
| **Modul** (`.mod`) | Kartu `--tile` radius 22, ikon 56px, H4, paragraf; hover jadi putih, naik, dan muncul glow merah di sudut. |
| **Big stat** (`.bigstat`) | Angka besar navy + `+` merah, label caps, keterangan; dipisah garis vertikal. |
| **Story** (`.story`) | Kartu putih radius 26 dengan gambar ber-inset 10px; varian `.feature` (besar) dan `.row` (horizontal). Meta berisi `.chip` + teks. |
| **Eco point** | Ikon 44px di kotak putih ber-border radius 14 + judul 16px + paragraf. |
| **Tag** / **Chip** | Pill 12px. Tag = biru di `--blue-tint`; chip = merah di `--red-tint`, atau `.chip.blue`. |
| **Checklist** (`.includes`) | Kotak 18px radius 6 berlatar `--red-tint` dengan centang merah. |

### 7.5 Form (section CTA)

- Kartu gelap blur radius 24, padding 40px (24/20px di mobile), lebar maks 592px.
- Field: label 13px/600, input tinggi 46px radius 12.
- Focus: border `#E42313` + ring `0 0 0 4px rgba(228,35,19,.16)`.
- Error: class `.bad` pada `.fg` menampilkan `.err` dan border merah.
- Sukses: class `.sent` menyembunyikan form dan menampilkan lingkaran centang hijau.

### 7.6 Visual khas

- **Hero mosaic:** satu ilustrasi isometrik SVG (`#art`) dipakai ulang oleh semua tile sehingga tile yang bersentuhan menyatu. Kartu statistik putih menempel di antara tile.
- **Hub ekosistem:** logo di tengah, partner chip di sekelilingnya, spoke yang menyala merah saat partner di-hover, dan packet yang mengalir.
- **Marquee mitra:** logo bergerak kanan → kiri, mask fade di kedua sisi, berhenti saat hover.
- **Preview workspace:** mockup UI 1440×800 yang diskalakan agar pas dan miring saat masuk viewport. Mockup ini memakai palet produk sendiri (`#1d2939`, `#667085`, dll.), kecuali merah yang tetap `#E42313`, bukan token landing page.

---

## 8. Responsif

| Breakpoint | Perubahan |
|---|---|
| **≤1024px** | Modul 2 kolom, statistik 2 kolom |
| **≤860px** | Semua split menjadi 1 kolom, header What We Do tidak sticky, nav berganti tombol menu + drawer, pintu CTA mengecil |
| **≤640px** | Gutter 22px, mosaic desktop diganti mosaic mobile 5×5, H1 jadi dua baris, modul dan checklist 1 kolom, paragraf big stat disembunyikan, story `.row` jadi vertikal, form 1 kolom |

Hero memakai `100svh` dan `safe-area-inset` agar pas di layar ponsel dengan notch.

---

## 9. Aksesibilitas

- Setiap section memakai `aria-labelledby` yang menunjuk ke H2-nya.
- Ikon dekoratif memakai `alt=""` atau `aria-hidden="true"`.
- Tab memakai `role="tablist"`, `role="tab"`, `aria-selected`, dan navigasi panah.
- Duplikat item marquee diberi `aria-hidden`.
- Mosaic yang bisa diklik diberi `role="button"`, `tabindex="0"`, dan dukungan Enter/Spasi.
- Kontras: body `--muted` di atas putih dipakai untuk teks ≥14px; jangan pakai `--soft` untuk teks yang wajib dibaca.

---

## 10. Panduan untuk halaman baru

1. **Pakai ulang kerangka:** nav yang sama (ubah `aria-current` ke halaman aktif), footer yang sama, dan section CTA **Contact Us** di akhir halaman.
2. **Hero halaman dalam** tidak perlu mosaic penuh. Cukup eyebrow + H2 dua nada + lede, dengan visual pendukung (foto `.leaf` atau ilustrasi dari palet isometrik).
3. **Mulai setiap section** dengan pola eyebrow → H2 → lede (bagian 7.3).
4. **Selang-seling latar** putih dan `--mist`; satu section navy hanya untuk CTA.
5. **Gunakan komponen yang ada** sebelum membuat yang baru: pillar untuk daftar fitur, modul untuk grid kapabilitas, story untuk kartu cerita, big stat untuk metrik.
6. **Merah tetap aksen:** maksimal satu tombol primary per layar, sisanya link panah.
7. **Pakai stylesheet bersama** `css/style.css` (`<link rel="stylesheet" href="css/style.css">`). Jangan menyalin CSS ke setiap HTML; style khusus satu halaman boleh dipisah ke file sendiri, misalnya `css/who-we-are.css`.
8. **Pakai JS bersama** `js/site.js` untuk nav sticky, drawer mobile, reveal, count-up, pintu CTA, dan validasi form. Perilaku khusus halaman ditaruh di file sendiri, misalnya `js/who-we-are.js`.
9. **Tambahkan class `.rv`** untuk reveal, dan pastikan semua animasi baru masuk ke blok `prefers-reduced-motion`.
10. **Halaman layanan dibuat oleh generator.** Keenam `service-*.html` dihasilkan dari `tools/build_services.py` (konten di bagian `SERVICES`), dengan style di `css/service.css`. Ubah datanya lalu jalankan `python3 tools/build_services.py`; jangan edit file HTML-nya langsung.
11. **Halaman kapabilitas dan nav juga dibuat oleh generator.** Sembilan `capability-*.html` dihasilkan dari `tools/build_capabilities.py` (style di `css/capability.css`). Menu Services dan Capabilities untuk semua halaman ada di `tools/site_nav.py`; setelah mengubahnya, jalankan `build_services.py`, `build_capabilities.py`, lalu `update_nav.py` (untuk `index.html` dan `who-we-are.html`).
12. **Halaman Customer Stories dibuat oleh generator.** `customer-stories.html` dihasilkan dari `tools/build_stories.py` (style di `css/stories.css`, filter di `js/stories.js`). Tambah cerita di `STORIES`; jalur kebutuhan dan filter layanan/kapabilitas muncul otomatis di 6+ cerita, filter industri di 20+. Halaman cerita tunggal (`story-*.html`, style di `css/story.css`) ikut dibuat oleh generator yang sama; isi panjangnya ada di `tools/story_content.py`, dan `[[Nama kapabilitas]]` di teks otomatis jadi tautan ke halaman kapabilitas.
13. **Home sebagian dibuat oleh generator.** `index.html` tetap ditulis langsung (mosaic hero, mockup Workspace, form), tapi area `<!-- @gen:services -->`, `@gen:stack` dan `@gen:proof` diisi oleh `tools/build_home.py` dari data yang sama dengan halaman lain. JS khusus Home ada di `js/home.js`; footer semua halaman dibuat dari `site_nav.footer()`.
14. **Log in untuk pelanggan lama.** Tautan teks "Log in" di navbar (ikon user di mobile), tombol outline di drawer, dan "Log in to Workspace" di footer, semuanya ke `LOGIN_URL` di `site_nav.py`. Merah tetap khusus "Schedule a Demo": jangan jadikan login tombol primer kedua.
