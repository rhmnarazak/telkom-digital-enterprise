# Kerangka Halaman Customer Stories

Panduan untuk menyusun halaman daftar success story pelanggan (hub customer stories) di website produk. Diadaptasi dari halaman customer stories Dovetail, dengan penyesuaian untuk produk yang memiliki beberapa layanan dan jumlah cerita yang masih bertumbuh.

Dokumen ini melengkapi **Kerangka Success Story** (template untuk halaman cerita tunggal). Keduanya memakai taksonomi layanan dan kapabilitas yang sama (lihat **Lampiran B — Taksonomi Layanan & Kapabilitas**), sehingga setiap cerita bisa diidentifikasi dari use case, layanan, dan kapabilitas yang dipakai. Tone of voice, gaya bahasa, dan aturan desain mengikuti **Panduan Tone of Voice — Landing Page Telkom Digital** (`panduan-tone-of-voice.md`).

**Fungsi halaman:** pusat bukti sosial. Tujuannya bukan bercerita, tapi meyakinkan lewat jumlah dan variasi bukti, lalu mengarahkan pengunjung ke cerita yang paling relevan dengan kebutuhannya.

---

## 1. Sesuaikan dengan tahap produk

Halaman dengan section kosong atau setengah terisi justru menurunkan kepercayaan. Tentukan dulu tahapnya, lalu tampilkan hanya section yang sudah bisa terisi dengan baik.

| Tahap | Jumlah cerita | Section yang ditampilkan |
|-------|---------------|--------------------------|
| Awal | 1–5 | Hero, featured story (panjang), 2–4 kartu cerita, baris logo singkat, testimoni pendek, CTA |
| Berkembang | 6–20 | + Jalur berdasarkan kebutuhan, grid cerita, filter layanan, baris logo lebih panjang |
| Matang | 20+ | + Filter industri, dinding logo penuh, bukti pihak ketiga, testimoni terkurasi lengkap |

**Aturan umum:**
- Jangan tampilkan filter jika sebagian besar pilihannya hanya menghasilkan satu kartu.
- Jangan tampilkan section bukti pihak ketiga sebelum benar-benar ada isinya.
- Lebih baik sedikit cerita yang kuat daripada banyak kartu yang tidak lengkap.

---

## 2. Ringkasan struktur halaman

| No | Section | Tujuan | Tahap minimum |
|----|---------|--------|---------------|
| 1 | Hero | Membuka dengan suara pelanggan dan angka agregat | Awal |
| 2 | Featured story | Menampilkan bukti terkuat di posisi teratas | Awal |
| 3 | Jalur berdasarkan kebutuhan | Mengarahkan pengunjung dari masalahnya | Berkembang |
| 4 | Grid cerita + filter | Memudahkan mencari cerita berdasarkan layanan, kapabilitas, dan industri | Berkembang |
| 5 | Baris/dinding logo | Menunjukkan keluasan pelanggan | Awal |
| 6 | Bukti pihak ketiga | Validasi independen | Matang (opsional) |
| 7 | Testimoni terkurasi | Volume dan keberagaman suara | Awal |
| 8 | CTA penutup | Mengarahkan ke aksi | Awal |

---

## 3. Detail setiap section

### 3.1 Hero

**Isi:**
- **Eyebrow:** `Cerita Pelanggan`
- **Headline:** kutipan pelanggan terkuat (pendek, emosional, spesifik)
- **Subheadline:** satu kalimat yang menegaskan bahwa ini kata-kata pelanggan, atau ringkasan nilai produk
- **Atribusi kutipan:** nama, jabatan, perusahaan
- **3 angka agregat:** jumlah pelanggan, cakupan (kota/industri), satu angka dampak rata-rata
- **CTA sekunder:** misalnya "Jadwalkan demo"

**Template:**

> **Eyebrow:** CERITA PELANGGAN
> **Headline:** "[Kutipan pelanggan terkuat]"
> **Atribusi:** — [Nama], [Jabatan], [Perusahaan]
> **Subheadline:** Kata-kata pelanggan kami, bukan kata-kata kami.
>
> | [angka]+ | [angka]+ | [angka]% |
> |---|---|---|
> | pelanggan aktif | kota / industri | rata-rata [dampak] |

**Panduan:**
- Pilih kutipan yang menunjukkan perasaan atau ketergantungan pada produk, bukan deskripsi fitur.
- Angka agregat hanya ditampilkan jika datanya valid dan bisa dipertanggungjawabkan.

---

### 3.2 Featured story

**Isi:**
- Foto atau visual dunia pelanggan (lebar)
- Logo pelanggan + label layanan
- Judul cerita (berangka)
- Ringkasan dua kalimat
- 3 angka utama dari cerita
- Tombol "Baca ceritanya"

**Panduan:**
- Letakkan di atas grid, bukan di bawah.
- Pilih cerita dengan nama pelanggan yang dikenal target pasar dan angka dampak terkuat.
- Bisa berupa carousel 2–3 cerita jika sudah di tahap matang; di tahap awal cukup satu.

---

### 3.3 Jalur berdasarkan kebutuhan

Section tambahan untuk produk multi-layanan. Pengunjung berpikir dari masalahnya, bukan dari nama kategori.

**Isi:** 6 kartu kecil, satu per layanan (tampilkan hanya layanan yang sudah punya minimal 1 cerita).

**Template kartu:**

> **Saya butuh [hasil yang diinginkan]**
> [Nama layanan] · [jumlah] cerita
> Kapabilitas populer: [kapabilitas 1] · [kapabilitas 2]
> → Lihat cerita

**Contoh kalimat per layanan:**

| Kode | Layanan | Contoh "Saya butuh…" |
|---|---|---|
| CRM | Customer Relationship Management | …melayani pelanggan dari semua kanal dalam satu tempat |
| ACD | Academic Management | …mengelola sekolah, kelas, dan nilai secara digital |
| NET | Network Monitoring Management | …mendeteksi gangguan jaringan sebelum pengguna mengeluh |
| CAM | IP Cam Management | …memantau keamanan banyak lokasi dari satu aplikasi |
| DOC | Document Management | …menyimpan, mencari, dan menyetujui dokumen dengan cepat |
| GAI | Generative AI Management | …memakai AI dengan aman di atas data perusahaan |

*Kalimat di atas adalah contoh awal; sesuaikan dengan pesan utama setiap layanan.*

**Panduan:**
- Tulis dari sudut pandang masalah atau hasil, misalnya "Saya butuh mempercepat proses [X]".
- Setiap kartu memfilter grid di bawahnya, atau membuka URL terfilter.

---

### 3.4 Grid cerita + filter

**Filter:**
- **Filter utama:** layanan (6 kode taksonomi)
- **Filter kedua:** kapabilitas — tampil sebagai pilihan bertingkat: kapabilitas lintas layanan di level pertama, kapabilitas spesifik layanan muncul setelah layanan dipilih
- **Filter ketiga:** industri (mulai tahap matang)
- Filter bisa dikombinasikan, misalnya `Layanan: CAM` + `Kapabilitas: AI & Automation`
- Tampilkan jumlah hasil di setiap pilihan filter, misalnya `Retail (4)`
- Sembunyikan pilihan filter yang hasilnya nol

**Urutan kartu:**
1. Cerita dengan nama pelanggan dikenal + angka dampak
2. Cerita dengan nama pelanggan tanpa angka
3. Cerita anonim (dengan label kategori deskriptif)

**Anatomi kartu cerita (wajib konsisten):**

| Elemen | Ketentuan |
|--------|-----------|
| Label layanan | Wajib; layanan utama, ditambah "+1" atau "+2" jika ada layanan pendukung |
| Use case | Wajib; 1 kalimat dari kartu identifikasi |
| Tag kapabilitas | Wajib, 1–3 kapabilitas inti; nama persis dari taksonomi; setiap tag bisa diklik untuk memfilter |
| Logo atau label kategori | Logo jika pelanggan bernama; label deskriptif jika anonim (misalnya "Jaringan ritel nasional") |
| Kutipan | Wajib, maksimal ±25 kata |
| Atribusi | Nama + jabatan + perusahaan; jika anonim, cukup jabatan |
| Judul cerita | Pola "Bagaimana [pelanggan] [hasil berangka]" |
| Tautan | "Baca ceritanya →" |

**Panduan:**
- Jika sebuah cerita belum punya kutipan, tunda penayangannya daripada menampilkan kartu yang tidak lengkap.
- Di mobile, kutipan boleh dipotong menjadi dua baris; judul tetap utuh.
- Gunakan pagination atau tombol "Muat lebih banyak" jika lebih dari 12 kartu.

---

### 3.5 Baris / dinding logo

**Panduan:**
- Tahap awal: satu baris, 6–10 logo.
- Tahap matang: dinding logo atau marquee.
- Prioritaskan logo yang dikenal target pasar (jika pasarnya lokal, logo yang dikenal di Indonesia lebih meyakinkan).
- Gunakan versi logo satu warna agar seragam.
- Pastikan izin penggunaan logo sudah ada.

---

### 3.6 Bukti pihak ketiga (opsional)

**Contoh isi:**
- Sertifikasi (ISO, keamanan data, registrasi PSE)
- Penghargaan industri
- Rating di situs review
- Kemitraan resmi

**Panduan:** lewati section ini sampai benar-benar ada isinya. Satu sertifikasi yang relevan lebih baik daripada section yang dipaksakan.

---

### 3.7 Testimoni terkurasi

**Isi:** 6–12 kutipan pilihan.

**Panduan:**
- Tidak ada kutipan ganda atau kutipan yang sama dalam versi berbeda.
- Setiap kutipan wajib punya nama atau jabatan, dan perusahaan.
- Beri label layanan dan, jika relevan, satu tag kapabilitas yang dibahas kutipan tersebut.
- Tambahkan foto untuk kutipan terkuat.
- Pilih kutipan yang menyebut angka konkret atau fitur spesifik, bukan pujian umum.
- Campurkan peran: pengguna harian, manajer, dan pengambil keputusan.

---

### 3.8 CTA penutup

Sediakan dua pilihan dengan tingkat komitmen berbeda.

| Pilihan | Untuk siapa | Contoh |
|---------|-------------|--------|
| Utama | Pengunjung yang siap membeli | "Jadwalkan demo" |
| Sekunder | Pengunjung yang masih mempertimbangkan | "Ceritakan kebutuhanmu" atau "Unduh ringkasan studi kasus" |

---

## 4. Sistem tagging layanan & kapabilitas

Agar setiap cerita mudah teridentifikasi use case, layanan, dan kapabilitasnya, semua cerita memakai data yang sama dari **kartu identifikasi use case** (lihat Kerangka Success Story, section 0). Halaman ini hanya membaca data tersebut; tidak ada label yang ditulis ulang secara manual.

### 4.1 Model data per cerita

| Field | Tipe | Dipakai di |
|---|---|---|
| `use_case` | Teks, 1 kalimat | Kartu cerita, jalur kebutuhan |
| `service_primary` | 1 kode (CRM/ACD/NET/CAM/DOC/GAI) | Label kartu, filter Layanan, halaman Layanan |
| `services_supporting` | 0–2 kode | Filter Layanan, label "+1 layanan" di kartu |
| `capabilities_core` | 1–3 nama kapabilitas | Tag publik di kartu, filter Kapabilitas, halaman Kapabilitas |
| `capabilities_supporting` | 0–n nama kapabilitas | Filter Kapabilitas (tidak tampil di kartu) |
| `capabilities_shared` | 0–n kapabilitas lintas layanan | Filter Kapabilitas lintas layanan, halaman Kapabilitas |
| `industry` | 1 nilai | Filter Industri |
| `customer_size` | 1 nilai | Filter opsional |
| `impact_metric` | Metrik + angka | Judul kartu, featured story |

### 4.2 Aturan tagging

- Nama layanan dan kapabilitas **wajib** diambil dari Lampiran B — Taksonomi Layanan & Kapabilitas; tidak boleh ada sinonim.
- Satu cerita tepat punya **1 layanan utama**; layanan pendukung maksimal 2.
- Tag kapabilitas yang tampil di kartu maksimal **3** (hanya kapabilitas inti).
- Kapabilitas berstatus perkiraan (†) tidak dipakai sebagai tag publik sebelum divalidasi.
- Cerita multi-layanan muncul di semua filter layanan yang ditandai, tapi selalu menampilkan layanan utama sebagai label pertama.

### 4.3 Matriks cakupan cerita

Gunakan matriks ini secara internal untuk melihat layanan dan kapabilitas mana yang sudah dan belum punya bukti. Isi dengan jumlah cerita per sel.

| Layanan \ Kapabilitas lintas layanan | Dashboard & Monitoring | Reporting & Analytics | Notifications & Alerts | AI & Automation | Cloud Storage | User & Access Mgmt | API Integration | Communication & Chatbot | Mobile App |
|---|---|---|---|---|---|---|---|---|---|
| CRM | [ ] | [ ] | [ ] | [ ] | – | [ ] | [ ] | [ ] | – |
| ACD | [ ] | [ ] | [ ] | – | [ ] | [ ] | – | – | [ ] |
| NET | [ ] | [ ] | [ ] | [ ] | – | [ ] | [ ] | – | [ ] |
| CAM | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | – | [ ] |
| DOC | – | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | – | – |
| GAI | [ ] | [ ] | – | [ ] | [ ] | [ ] | [ ] | [ ] | – |

`–` = kapabilitas tidak relevan untuk layanan tersebut. Sel `[ ]` yang bernilai 0 adalah prioritas cerita berikutnya.

---

## 5. Integrasi dengan halaman lain

- **URL per filter**, misalnya `/pelanggan?layanan=cam&kapabilitas=cloud-recording`, agar tim sales bisa membagikan tautan yang sudah terfilter.
- **Halaman layanan menarik kartu dari sini.** Setiap halaman layanan menampilkan 1–2 kartu cerita berdasarkan `service_primary` dan `services_supporting`. Halaman customer stories menjadi sumber data, bukan halaman yang berdiri sendiri.
- **Halaman Kapabilitas menarik kartu dari sini.** Karena satu kapabilitas bisa dipakai banyak layanan, halaman Kapabilitas menampilkan cerita dari berbagai layanan berdasarkan `capabilities_core` dan `capabilities_shared`. Ini menunjukkan bahwa satu kapabilitas terbukti di beberapa konteks.
- **Tag kapabilitas di halaman cerita tunggal** mengarah ke halaman Kapabilitas terkait.
- **Halaman cerita tunggal** menampilkan 2–3 kartu cerita lain dari layanan atau industri berbeda di bagian bawah.
- **Homepage** menampilkan baris logo dan satu kutipan dari halaman ini.

---

## 6. SEO dan metadata

- **Title:** `Cerita Pelanggan [Nama Produk] | [Layanan utama] untuk [Industri]`
- **Meta description:** sebutkan jumlah pelanggan, layanan, dan hasil utama.
- **Judul halaman cerita** memuat nama layanan dan industri.
- **Halaman hasil filter** (layanan atau kapabilitas) memiliki title dan meta description sendiri, misalnya `Cerita Pelanggan Cloud Recording | IP Cam Management`.
- **Alt text** untuk setiap logo dan foto.

---

## 7. Checklist sebelum publikasi

- [ ] Tidak ada kutipan ganda
- [ ] Angka di kartu sama dengan angka di halaman cerita
- [ ] Angka agregat di hero valid dan terbaru
- [ ] Semua kartu memiliki elemen wajib yang lengkap
- [ ] Setiap cerita punya kartu identifikasi use case yang terisi
- [ ] Label layanan dan tag kapabilitas memakai nama persis dari taksonomi
- [ ] Tidak ada tag kapabilitas berstatus perkiraan (†) yang tampil publik
- [ ] Cerita muncul di halaman Layanan dan Kapabilitas yang sesuai
- [ ] Matriks cakupan cerita sudah diperbarui
- [ ] Izin penggunaan nama, logo, foto, dan kutipan sudah ada
- [ ] Tidak ada salah ketik
- [ ] Filter tanpa hasil disembunyikan
- [ ] URL filter bisa dibagikan dan berfungsi
- [ ] Tampilan mobile sudah diperiksa
- [ ] CTA berfungsi dan mengarah ke halaman yang benar

---

## 8. Metrik keberhasilan

| Metrik | Yang diukur | Kegunaan |
|--------|-------------|----------|
| Klik ke halaman cerita | Kartu mana yang paling menarik | Menentukan cerita unggulan |
| Penggunaan filter | Layanan/kapabilitas/industri mana yang paling dicari | Sinyal minat pasar; prioritas cerita berikutnya |
| Klik tag kapabilitas | Kapabilitas mana yang paling menarik perhatian | Menentukan kapabilitas yang perlu ditonjolkan di homepage |
| Klik CTA | Berapa pengunjung lanjut ke demo/kontak | Efektivitas halaman |
| Waktu di halaman & scroll depth | Sejauh mana pengunjung membaca | Menilai panjang dan urutan section |

**Gunakan data ini untuk:** memutuskan cerita mana yang perlu ditambah, layanan dan kapabilitas mana yang kekurangan bukti (bandingkan dengan matriks cakupan), dan apakah urutan section perlu diubah.

---

## Lampiran A — Pelajaran dari halaman Dovetail

**Layak ditiru:**
- Hero berupa kutipan pelanggan, bukan klaim perusahaan.
- Bukti berlapis: cerita (kedalaman) → logo (keluasan) → badge (validasi independen) → testimoni (volume).
- Kartu dibuka dengan kutipan; orangnya menjadi pengait.
- Pelanggan anonim tetap diberi label kategori yang deskriptif.
- Judul kartu memuat angka.

**Sebaiknya dihindari:**
- Dinding testimoni yang terlalu panjang dengan kutipan ganda.
- Salah ketik pada kutipan.
- Featured story diletakkan di bawah grid.
- Filter hanya berdasarkan industri.
- Tidak ada angka agregat di bagian atas.
- Kartu yang tidak konsisten (sebagian tanpa kutipan).

---

## Lampiran B — Taksonomi Layanan & Kapabilitas

Daftar baku untuk label layanan, tag kapabilitas, dan filter. Gunakan nama persis seperti di bawah.

**Kode layanan & kapabilitas**

| Kode | Layanan | Kapabilitas |
|---|---|---|
| CRM | Customer Relationship Management | Omnichannel Inbox · Customer Data & History · Conversation Labeling · Knowledge Base · Ticketing · Chatbot Builder · Broadcast (Blast) · WhatsApp API · Scheduling & Reminders · Interaction Analytics · Modular Packages |
| ACD | Academic Management | Role-based Portals · Real-time Institution Monitoring · Computer-based Assessment · Assignment Management · Real-time Attendance · Institution Data Management · Learning Content · Grade Management · Learning Performance Tracking · Mobile Apps |
| NET | Network Monitoring Management | Network Monitoring · Web/API Monitoring · Linux Server Monitoring · Automated Reporting · Proactive & Predictive Maintenance · Real-time Notifications · Network Status History · Traffic & Bandwidth Monitoring* · Network Quality Analysis* · Customization |
| CAM | IP Cam Management | Cloud Recording · Intruder Detection · Fire & Smoke Detection · People Counting & Crowd Detection · Employee Presence · Smart Device Integration · Multi-site Deployment · IoT Connectivity · Device Data Storage & Dashboard · Security & Access Management · Live View & Playback† |
| DOC | Document Management† | Central Repository · Search & OCR · Version Control · Access Control & Sharing · Approval Workflow · Electronic Signature · Retention & Archiving · Audit Trail · Document Templates · AI Document Assistant |
| GAI | Generative AI Management† | Model Management · Knowledge Base (RAG) · AI Chat Assistant · AI Agent & Workflow Builder · Prompt Management · Guardrails & Data Privacy · Usage & Cost Monitoring · Access Control · API & SDK |

\* Segera hadir · † Masih perkiraan, perlu divalidasi tim produk sebelum dipakai sebagai tag publik.

**Kapabilitas lintas layanan** (untuk filter dan halaman Kapabilitas)

| Kapabilitas lintas layanan | CRM | ACD | NET | CAM | DOC | GAI |
|---|---|---|---|---|---|---|
| Real-time Dashboard & Monitoring | ✓ | ✓ | ✓ | ✓ | | ✓ |
| Reporting & Analytics | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Notifications & Alerts | ✓ | ✓ | ✓ | ✓ | ✓ | |
| AI & Automation | ✓ | | ✓ | ✓ | ✓ | ✓ |
| Cloud Storage | | ✓ | | ✓ | ✓ | ✓ |
| User & Access Management | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| API Integration | ✓ | | ✓ | ✓ | ✓ | ✓ |
| Communication & Chatbot | ✓ | | | | | ✓ |
| Mobile App | | ✓ | ✓ | ✓ | | |

**Hubungan kapabilitas induk–anak**

Setiap kapabilitas layanan (anak) dimiliki **tepat 1 layanan** dan terhubung ke **0–2 kapabilitas lintas layanan** (induk). Kapabilitas anak tanpa induk disebut kapabilitas khusus.

| Kapabilitas induk | CRM | ACD | NET | CAM | DOC† | GAI† |
|---|---|---|---|---|---|---|
| Real-time Dashboard & Monitoring | — | Real-time Institution Monitoring | Network Monitoring · Web/API Monitoring · Linux Server Monitoring · Network Status History · Traffic & Bandwidth Monitoring* | Device Data Storage & Dashboard · Live View & Playback† | | Usage & Cost Monitoring |
| Reporting & Analytics | Interaction Analytics | Institution Data Management · Learning Performance Tracking | Automated Reporting · Network Quality Analysis* | People Counting & Crowd Detection² | Audit Trail² | Usage & Cost Monitoring² |
| Notifications & Alerts | Broadcast (Blast) · Scheduling & Reminders | Real-time Attendance | Real-time Notifications | Intruder Detection² | Approval Workflow | |
| AI & Automation | Chatbot Builder | | Proactive & Predictive Maintenance | Intruder Detection · Fire & Smoke Detection · People Counting & Crowd Detection · Employee Presence | AI Document Assistant | Model Management · Knowledge Base (RAG) · AI Agent & Workflow Builder |
| Cloud Storage | | Learning Content | | Cloud Recording | Central Repository · Version Control · Retention & Archiving | Knowledge Base (RAG)² |
| User & Access Management | — | Role-based Portals | — | Security & Access Management | Access Control & Sharing · Audit Trail | Access Control · Guardrails & Data Privacy |
| API Integration | WhatsApp API | | — | IoT Connectivity · Smart Device Integration | Electronic Signature | API & SDK |
| Communication & Chatbot | Omnichannel Inbox · Conversation Labeling · Knowledge Base · Ticketing | | | | | AI Chat Assistant |
| Mobile App | | Mobile Apps | — | — | | |

² Induk kedua dari kapabilitas yang sama · \* Segera hadir · † Masih perkiraan · — Celah taksonomi

**Kapabilitas khusus (tanpa induk):** CRM: Customer Data & History, Modular Packages · ACD: Computer-based Assessment, Assignment Management, Grade Management · NET: Customization · CAM: Multi-site Deployment · DOC: Search & OCR, Document Templates · GAI: Prompt Management.

**Celah taksonomi (perlu diputuskan bersama tim produk):** sel bertanda — dicentang di matriks lintas layanan tetapi belum punya kapabilitas anak bernama: CRM (Dashboard & Monitoring, User & Access Management), NET (User & Access Management, API Integration, Mobile App), CAM (Mobile App). Pilihan: tambahkan kapabilitas anak ke taksonomi, atau hapus centang di matriks. Sampai diputuskan, layanan tersebut **tidak** ditampilkan di halaman kapabilitas induk terkait.

Sumber utama taksonomi ini: **Service Capability Breakdown** (`service-capability-breakdown.md`). Jika taksonomi berubah, perbarui dokumen sumber terlebih dulu, lalu salin ke lampiran ini.
