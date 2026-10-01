# Kerangka Success Story

Template untuk menulis success story pelanggan di website produk. Diadaptasi dari pola customer story Dovetail, dengan tambahan metrik dampak, kartu ringkasan pelanggan, dan label layanan agar cocok untuk produk dengan beberapa layanan. Setiap cerita juga diberi **kartu identifikasi use case** yang memetakan layanan dan kapabilitas yang dipakai, sehingga cerita mudah ditemukan dari halaman Customer Stories, halaman Layanan, maupun halaman Kapabilitas.

**Panjang ideal:** 800–1.200 kata.
**Prinsip utama:** sebagian besar pembaca hanya membaca hero, angka, judul section, dan kutipan. Pastikan keempat elemen itu sudah bisa bercerita sendiri.
**Tone of voice:** mengikuti **Panduan Tone of Voice — Landing Page Telkom Digital** (`panduan-tone-of-voice.md`), terutama pola Inform → Clarify → Empower dan prinsip *results, not claims*.

---

## Ringkasan struktur

| No | Section | Tujuan | Panjang |
|----|---------|--------|---------|
| 0 | Kartu identifikasi use case | Memetakan layanan & kapabilitas (metadata, sebagian tampil sebagai label) | 9 field |
| 1 | Hero | Menyampaikan inti cerita dalam 5 detik | Headline + 1 kalimat |
| 2 | Kartu ringkasan + 3 angka | Memudahkan pembaca yang hanya memindai | 5 baris + 3 angka |
| 3 | Konteks | Membangun kredibilitas pelanggan | 2 paragraf |
| 4 | Tantangan | Membuat pembaca merasa "ini masalah saya juga" | 2–3 paragraf + 1 kutipan |
| 5 | Solusi | Menunjukkan cara kerja produk secara nyata | 3–4 paragraf + 1–2 kutipan + screenshot |
| 6 | Hasil | Membuktikan dampak | Angka + 2 paragraf + 1 kutipan |
| 7 | Langkah berikutnya | Menunjukkan hubungan jangka panjang | 1 paragraf |
| 8 | Penutup halaman | Mengarahkan ke aksi | CTA + cerita lain + FAQ |

---

## 0. Kartu identifikasi use case (metadata cerita)

Isi kartu ini **sebelum menulis cerita**. Kartu ini menjadi dasar label di halaman cerita, tag filter di halaman Customer Stories, dan penarikan kartu cerita ke halaman Layanan dan Kapabilitas. Gunakan nama dan kode dari **Lampiran C — Taksonomi Layanan & Kapabilitas**.

| Field | Isi | Ketentuan |
|---|---|---|
| Judul use case | [kata kerja + objek, misalnya "Memusatkan layanan pelanggan multi-kanal"] | 1 kalimat, dari sudut pandang hasil bagi pelanggan |
| Layanan utama | [kode + nama, misalnya CRM — Customer Relationship Management] | Wajib, tepat 1 |
| Layanan pendukung | [kode + nama] | Opsional, maksimal 2 |
| Kapabilitas inti | [nama kapabilitas dari taksonomi] | Wajib, 1–3; ditampilkan sebagai tag publik |
| Kapabilitas pendukung | [nama kapabilitas dari taksonomi] | Opsional; dipakai untuk pencarian/filter, tidak ditonjolkan |
| Kapabilitas lintas layanan | [misalnya Reporting & Analytics, AI & Automation] | Opsional; untuk halaman Kapabilitas |
| Industri | [ ] | Wajib |
| Ukuran pelanggan | [UMKM / menengah / enterprise / instansi pemerintah] | Wajib |
| Metrik dampak utama | [metrik + angka] | Wajib; harus terkait dengan kapabilitas inti |

**Contoh pengisian (ilustrasi):**

| Field | Isi |
|---|---|
| Judul use case | Memantau keamanan kampus dan mendeteksi insiden secara otomatis |
| Layanan utama | CAM — IP Cam Management |
| Layanan pendukung | NET — Network Monitoring Management |
| Kapabilitas inti | Cloud Recording · Intruder Detection · Multi-site Deployment |
| Kapabilitas pendukung | Fire & Smoke Detection · Real-time Notifications |
| Kapabilitas lintas layanan | AI & Automation · Notifications & Alerts |
| Industri | Pendidikan |
| Ukuran pelanggan | Instansi pemerintah |
| Metrik dampak utama | Biaya pemeliharaan turun [angka]% |

**Panduan:**
- Kapabilitas inti adalah kapabilitas yang **benar-benar menghasilkan metrik dampak utama**, bukan semua fitur yang pernah dipakai.
- Setiap kapabilitas inti harus muncul minimal sekali di section Solusi dan didukung bukti (kutipan, angka, atau screenshot).
- Jangan menandai kapabilitas berlabel † (perkiraan) sebagai tag publik sebelum divalidasi tim produk.

---

## 1. Hero

**Isi:**
- **Eyebrow:** `PELANGGAN / [Nama pelanggan atau kategori industri]`
- **Label layanan:** `[Nama layanan utama]` (+ layanan pendukung jika ada)
- **Tag kapabilitas:** 1–3 kapabilitas inti dari kartu identifikasi, misalnya `Cloud Recording` `Intruder Detection`
- **Headline:** pola *"Bagaimana [pelanggan] [hasil terukur] dengan [layanan]"*
- **Subheadline:** satu kalimat yang menjawab siapa, masalah apa, dan peran produk.
- **Visual:** foto dunia pelanggan (lokasi, tim, aktivitas), bukan sekadar screenshot.

**Template:**

> **Eyebrow:** PELANGGAN / [INDUSTRI]
> **Label:** [Layanan utama] · Tag: [Kapabilitas 1] [Kapabilitas 2] [Kapabilitas 3]
> **Headline:** Bagaimana [pelanggan] [kata kerja hasil] [angka]% dengan [layanan]
> **Subheadline:** [Pelanggan], [deskripsi singkat], kini [hasil utama] dengan memakai [produk] untuk [aktivitas inti].

**Panduan:**
- Usahakan ada angka di headline.
- Gunakan kata kerja hasil: memangkas, mempercepat, menaikkan, menyatukan, mengotomatiskan.
- Hindari kata generik seperti "meningkatkan efisiensi" tanpa angka.

---

## 2. Kartu ringkasan + 3 angka

**Kartu ringkasan:**

| | |
|---|---|
| Industri | [ ] |
| Ukuran perusahaan | [jumlah karyawan / cabang] |
| Lokasi | [ ] |
| Use case | [judul use case dari kartu identifikasi] |
| Layanan | [layanan utama] (+ [layanan pendukung]) |
| Kapabilitas yang dipakai | [kapabilitas inti, maksimal 3] |
| Pelanggan sejak | [bulan/tahun] |

**3 angka utama** (komposisi seimbang):

| Jenis | Contoh | Angka |
|-------|--------|-------|
| Dampak | waktu/biaya yang dihemat, kenaikan konversi | [ ] |
| Skala | jumlah pengguna, transaksi, cabang | [ ] |
| Kecepatan | lama implementasi, waktu sampai hasil pertama | [ ] |

**Panduan:**
- Setiap angka diberi label singkat di bawahnya (maksimal 10 kata).
- Pastikan angka di sini **sama persis** dengan angka di isi cerita.

---

## 3. Konteks: siapa pelanggannya

**Paragraf 1 — Kredibilitas pelanggan:** sejak kapan berdiri, seberapa besar, siapa yang mereka layani, mengapa mereka penting di industrinya.

**Paragraf 2 — Tokoh utama:** tim atau orang yang menjadi pusat cerita, apa tanggung jawab mereka, seberapa besar beban kerjanya (pakai angka).

**Kalimat jembatan:** satu kalimat penutup yang mengarah ke masalah.

**Template kalimat jembatan:**

> Bisnisnya terus tumbuh. Tapi [proses/aktivitas] yang menopang pertumbuhan itu justru semakin sulit dikelola.

---

## 4. Tantangan

**Struktur:**
1. **Kondisi sebelum** — detail konkret yang mudah dibayangkan (tool apa yang dipakai, berapa jam per minggu, berapa orang yang terlibat).
2. **Masalah struktural** — mengapa ini bukan sekadar masalah tool, tapi menghambat bisnis.
3. **Dampak bisnis** — apa yang hilang: uang, waktu, pelanggan, peluang.
4. **Tujuan pelanggan** — satu kalimat dicetak **tebal**.

**Kutipan:** satu kutipan pelanggan yang menggambarkan rasa frustrasi atau beban kerja.

**Template:**

> Sebelum memakai [produk], tim [nama tim] mengelola [aktivitas] lewat [tool lama]. Setiap [periode], mereka menghabiskan [angka] jam untuk [pekerjaan manual].
>
> > "[Kutipan tentang kesulitan]"
> > — [Nama], [Jabatan]
>
> Tujuan mereka jelas: **[tujuan dalam satu kalimat]**.

**Panduan:**
- Jangan menyalahkan pelanggan; posisikan masalah sebagai akibat dari pertumbuhan atau keterbatasan tool.
- Satu detail spesifik lebih kuat dari tiga klaim umum.

---

## 5. Solusi

**Struktur:**
1. **Alasan memilih** — satu paragraf; tempat menyebut pembeda dari alternatif.
2. **Implementasi** — bagaimana mereka menyiapkan dan mulai memakai produk, berapa lama.
3. **Fitur spesifik** — disebut di dalam narasi dengan link ke halaman layanan. Setiap klaim fitur diikuti kutipan pengguna.
4. **Keterhubungan layanan** — jika pelanggan memakai lebih dari satu layanan, tunjukkan bagaimana layanan itu saling melengkapi.
5. **Screenshot produk** — dengan caption yang menjelaskan apa yang sedang dilihat.

**Template:**

> [Pelanggan] memilih [produk] karena [alasan utama]. Dalam [durasi], tim sudah [hasil implementasi awal].
>
> Perubahan terbesar datang dari [fitur, dengan link]. Jika sebelumnya [cara lama], kini [cara baru].
>
> > "[Kutipan tentang pengalaman memakai fitur]"
> > — [Nama], [Jabatan pengguna harian]
>
> [Screenshot + caption]

**Panduan:**
- Jangan membuat daftar fitur dalam bullet; fitur muncul sebagai bagian dari cerita.
- Sebut fitur dengan **nama kapabilitas yang sama persis** seperti di taksonomi (misalnya "Omnichannel Inbox", bukan "kotak masuk gabungan"), dan tautkan ke halaman Kapabilitas terkait. Konsistensi nama membuat cerita bisa ditarik otomatis ke halaman Kapabilitas.
- Urutkan pembahasan dari kapabilitas inti ke kapabilitas pendukung.
- Jika memakai lebih dari satu layanan, jelaskan kapabilitas mana dari layanan mana yang saling terhubung (misalnya Real-time Notifications dari NET memicu pemeriksaan rekaman di CAM).
- Pilih kutipan yang membandingkan cara lama dan cara baru.

---

## 6. Hasil

**Struktur:**
1. **Angka sebelum vs sesudah** — dalam tabel kecil atau visual.
2. **Perubahan cara kerja** — kebiasaan, ritual, atau keputusan yang berubah di organisasi.
3. **Kutipan pengambil keputusan** — dari manajer atau direktur, bukan hanya pengguna harian.

**Template tabel:**

| Metrik | Sebelum | Sesudah |
|--------|---------|---------|
| [Metrik 1] | [ ] | [ ] |
| [Metrik 2] | [ ] | [ ] |
| [Metrik 3] | [ ] | [ ] |

**Template:**

> Hasilnya bukan hanya [hasil langsung], tapi juga [perubahan cara kerja]. Kini [contoh perilaku baru tim].
>
> > "[Kutipan tentang dampak bisnis]"
> > — [Nama], [Jabatan pengambil keputusan]

**Panduan:**
- Ukur sukses dari dampak ke organisasi, bukan hanya kenyamanan pengguna.
- Kutipan dari level atasan paling meyakinkan pembeli B2B.

---

## 7. Langkah berikutnya

Satu paragraf tentang rencana pelanggan: menambah cabang, memperluas ke tim lain, atau mulai memakai layanan lain. Tutup dengan kalimat visi yang mengaitkan cerita ke positioning produk.

**Template:**

> Ke depan, [pelanggan] berencana [rencana berikutnya], termasuk mulai memakai [layanan lain]. Visinya: [visi pelanggan] — persis yang dirancang [produk] sebagai **[kategori/positioning produk]**.

---

## 8. Penutup halaman

**Komponen:**
1. **CTA utama** — misalnya "Jadwalkan demo" atau "Konsultasi gratis".
2. **Cerita pelanggan lain** — 2–3 kartu dari layanan atau industri yang berbeda.
3. **FAQ** — 3–5 pertanyaan.

**Panduan FAQ:**
- Tulis pertanyaan sebagai pertanyaan umum calon pembeli, bukan pertanyaan tentang pelanggan ini.
- Jawab dengan fakta dan kutipan dari cerita ini.
- Berguna untuk SEO dan pencarian berbasis AI.

**Contoh pola pertanyaan:**
- Bagaimana [produk] membantu [aktivitas]?
- Berapa lama implementasi [layanan]?
- Bisakah [produk] terhubung dengan [tool yang umum dipakai]?
- Apakah [produk] cocok untuk bisnis dengan [kondisi tertentu]?

---

## Lampiran A — Daftar pertanyaan wawancara pelanggan

**Konteks**
1. Ceritakan singkat tentang perusahaan dan peran Anda.
2. Seberapa besar tim dan beban kerja yang Anda tangani?

**Tantangan**
3. Sebelum memakai [produk], bagaimana proses [aktivitas] berjalan?
4. Berapa lama waktu yang dihabiskan untuk itu setiap minggu/bulan?
5. Apa momen yang membuat Anda sadar proses ini harus diubah?
6. Apa dampaknya ke bisnis jika masalah ini dibiarkan?

**Solusi**
7. Alternatif apa saja yang sempat dipertimbangkan? Mengapa memilih [produk]?
8. Bagaimana proses implementasinya? Berapa lama?
9. Fitur apa yang paling sering dipakai? Ceritakan satu momen spesifik saat fitur itu terasa membantu.
9a. Dari daftar kapabilitas [layanan] berikut, mana yang dipakai setiap hari, mana yang sesekali, dan mana yang belum dipakai? *(tunjukkan daftar dari Lampiran C)*
9b. Apakah Anda juga memakai layanan lain dari kami? Bagaimana layanan-layanan itu saling terhubung dalam pekerjaan Anda?

**Hasil**
10. Apa yang berubah setelah memakai [produk]? Adakah angka yang bisa dibagikan?
11. Apa yang sekarang bisa dilakukan tim yang dulu tidak bisa?
12. Bagaimana tanggapan atasan atau tim lain?

**Ke depan**
13. Apa rencana Anda berikutnya dengan [produk]?
14. Jika merekomendasikan [produk] ke rekan, apa yang akan Anda katakan?

---

## Lampiran B — Checklist sebelum publikasi

- [ ] Angka sebelum dan sesudah untuk 1–3 metrik
- [ ] Angka di stat block sama dengan angka di isi cerita
- [ ] 3–4 kutipan dari minimal dua peran (pengguna harian + pengambil keputusan)
- [ ] Screenshot produk dengan caption
- [ ] Foto atau visual dunia pelanggan
- [ ] Kartu identifikasi use case terisi lengkap
- [ ] Label layanan utama (dan pendukung) sesuai kode taksonomi
- [ ] 1–3 tag kapabilitas inti memakai nama persis dari taksonomi
- [ ] Setiap kapabilitas inti dibahas di section Solusi dan didukung bukti
- [ ] Metrik dampak utama terkait dengan kapabilitas inti
- [ ] Tidak ada kapabilitas berstatus perkiraan (†) yang dipakai sebagai tag publik
- [ ] Link ke halaman Kapabilitas terkait
- [ ] Izin penggunaan nama, logo, dan kutipan dari pelanggan
- [ ] Link ke halaman layanan terkait
- [ ] FAQ 3–5 pertanyaan
- [ ] CTA di bagian atas dan bawah halaman
- [ ] Headline mengandung angka hasil
- [ ] Judul section bisa dipahami tanpa membaca isinya

**Jika pelanggan tidak bersedia disebut namanya:** gunakan deskripsi kategori ("jaringan ritel nasional dengan 200+ cabang"), dan kompensasikan dengan detail cerita serta angka yang lebih kuat.

---

## Lampiran C — Taksonomi Layanan & Kapabilitas

Daftar baku untuk mengisi kartu identifikasi use case, label layanan, dan tag kapabilitas. Gunakan nama persis seperti di bawah.

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
