# Kerangka Halaman Kapabilitas

Panduan untuk menyusun halaman Kapabilitas di website produk. Diadaptasi dari halaman peran Dovetail (Product Management), lalu dibalik fokusnya: halaman Dovetail berpusat pada **satu orang**, halaman Kapabilitas berpusat pada **satu blok teknis yang dipakai satu atau beberapa layanan**.

Dokumen ini melengkapi **Kerangka Success Story**, **Kerangka Halaman Customer Stories**, dan **Kerangka Halaman Layanan**. Keempatnya memakai taksonomi yang sama (lihat **Lampiran B — Taksonomi Layanan & Kapabilitas**). Tone of voice, gaya bahasa, dan aturan desain mengikuti **Panduan Tone of Voice — Landing Page Telkom Digital** (`panduan-tone-of-voice.md`).

**Prinsip utama:** setiap kapabilitas harus selalu bisa menjawab dua pertanyaan:
1. **Bagian dari layanan apa?** — lewat layanan pemiliknya
2. **Terhubung dengan layanan apa lagi?** — lewat kapabilitas induknya

---

## 1. Model kapabilitas dua tingkat

| Tingkat | Contoh | Aturan |
|---|---|---|
| **Kapabilitas lintas layanan** (induk) | Notifications & Alerts, AI & Automation | Dipakai minimal 2 layanan; tidak dimiliki satu layanan |
| **Kapabilitas layanan** (anak) | Real-time Notifications, Intruder Detection | Dimiliki **tepat 1 layanan**; terhubung ke 0–2 kapabilitas induk |
| **Kapabilitas khusus** (anak tanpa induk) | Computer-based Assessment | Dimiliki tepat 1 layanan; tidak terhubung ke induk mana pun |

**Contoh hubungan:**

```
Notifications & Alerts (induk)
├── CRM  → Broadcast (Blast), Scheduling & Reminders
├── ACD  → Real-time Attendance
├── NET  → Real-time Notifications
├── CAM  → Intruder Detection (induk kedua)
└── DOC† → Approval Workflow
```

Pemetaan lengkap ada di Lampiran B.

---

## 2. Tingkatan halaman

Tidak semua kapabilitas perlu halaman sendiri; puluhan halaman tipis justru menurunkan kualitas situs.

| Tier | Isi | Jumlah | Bentuk | URL |
|---|---|---|---|---|
| A | Kapabilitas lintas layanan | 9 | Halaman penuh | `/kapabilitas/[nama-induk]` |
| B | Kapabilitas unggulan per layanan | 3–4 per layanan | Halaman ringkas | `/layanan/[kode]/[nama-kapabilitas]` |
| C | Kapabilitas anak lainnya | Sisanya | Tanpa halaman; kartu di grid halaman Layanan + kartu di halaman induk | Anchor di halaman Layanan |

**Naik dari Tier C ke Tier B jika:** sudah punya minimal 1 cerita pelanggan, atau sering dicari/diklik.

**Kapabilitas unggulan awal (Tier B):**

| Kode | Kapabilitas unggulan |
|---|---|
| CRM | Omnichannel Inbox · Chatbot Builder · Ticketing · Interaction Analytics |
| ACD | Computer-based Assessment · Real-time Attendance · Learning Performance Tracking · Role-based Portals |
| NET | Network Monitoring · Web/API Monitoring · Proactive & Predictive Maintenance · Automated Reporting |
| CAM | Cloud Recording · Intruder Detection · People Counting & Crowd Detection · Multi-site Deployment |
| DOC† | Central Repository · Search & OCR · Approval Workflow · Electronic Signature |
| GAI† | Knowledge Base (RAG) · AI Agent & Workflow Builder · Guardrails & Data Privacy · Usage & Cost Monitoring |

† Masih perkiraan; belum dibuatkan halaman sampai divalidasi tim produk.

---

## 3. Data halaman (internal)

Isi sebelum menulis copy.

| Field | Tier A | Tier B |
|---|---|---|
| Nama kapabilitas | Nama induk dari taksonomi | Nama anak dari taksonomi |
| Layanan pemilik | — | Tepat 1 kode layanan |
| Kapabilitas induk | — | 0–2 nama induk |
| Layanan yang memakai | Daftar kode layanan + kapabilitas anaknya | — |
| Kapabilitas saudara | — | Kapabilitas lain di layanan yang sama |
| Pesan inti | 1 kalimat | 1 kalimat |
| Peran target | 4–6 peran lintas layanan | Dari peran target layanan pemilik |
| Angka utama | Minimal 1 | Minimal 1 |
| Cerita bertag | `capabilities_shared` + tag anak | `capabilities_core` |

---

## 4. Kerangka halaman Tier A (kapabilitas lintas layanan)

### Ringkasan struktur

| No | Section | Tujuan | Wajib |
|---|---|---|---|
| 1 | Hero + badge "Tersedia di" | Menjelaskan kapabilitas dan layanan yang memakainya | Ya |
| 2 | Tantangan | Masalah yang diselesaikan, lintas konteks | Ya |
| 3 | Manfaat | 3–4 hasil tanpa nama fitur | Ya |
| 4 | Tersedia di layanan | Peta kapabilitas anak per layanan | Ya |
| 5 | Cara kerja per layanan | Alur kerja nyata, fitur disebut di langkah yang tepat | Ya |
| 6 | Use case | Peran/industri dengan label layanan | Ya |
| 7 | Integrasi relevan | Alat yang terhubung | Opsional |
| 8 | Cerita pelanggan | Bukti berlabel layanan | Ya (dengan fallback) |
| 9 | Keamanan & kontrol | Menjawab keberatan IT & legal | Wajib untuk induk tertentu |
| 10 | FAQ | Pertanyaan baku | Ya |
| 11 | CTA | Arahkan ke layanan yang cocok | Ya |

### 4.1 Hero

**Isi:**
- **Eyebrow:** `KAPABILITAS`
- **Headline:** hasil + kontras
- **Subheadline:** 1 kalimat penjelas apa itu dan untuk apa (memperbaiki hero Dovetail yang tanpa penjelas)
- **Badge "Tersedia di":** kode + nama layanan yang memakai kapabilitas ini (hanya layanan dengan kapabilitas anak tervalidasi)
- **Logo:** pelanggan yang ceritanya bertag kapabilitas ini
- **CTA:** "Temukan layanan yang cocok" + "Jadwalkan demo"

**Template:**

> **Eyebrow:** KAPABILITAS
> **Headline:** [Hasil], bukan [cara lama].
> **Subheadline:** [Nama kapabilitas] membantu [peran] [hasil] di [konteks], dari [layanan A] hingga [layanan B].
> **Tersedia di:** `[KODE] [Nama layanan]` `[KODE] [Nama layanan]` `[KODE] [Nama layanan]`

### 4.2 Tantangan

**Template:**

> **Tantangan**
> Di [konteks 1], [masalah]. Di [konteks 2], [masalah serupa]. Polanya sama: [akar masalah]. [Kalimat penutup pendek yang mudah diingat.]

**Panduan:** tunjukkan bahwa masalahnya muncul di beberapa konteks layanan; ini yang membedakan halaman Tier A dari halaman layanan.

### 4.3 Manfaat (3–4)

**Anatomi:**

| Elemen | Ketentuan |
|---|---|
| Judul | Hasil berawalan kata kerja, tanpa nama fitur |
| Isi | 1 kalimat mekanisme |
| Visual | Screenshot dari salah satu layanan (beri label layanan kecil di sudut) |

### 4.4 Tersedia di layanan (section inti)

Satu kartu per layanan yang memiliki kapabilitas anak dari induk ini.

**Anatomi kartu:**

| Elemen | Isi |
|---|---|
| Layanan | Kode + nama, misalnya `NET — Network Monitoring Management` |
| Kapabilitas anak | Nama persis dari taksonomi, misalnya `Real-time Notifications` |
| Peran di layanan itu | 1 kalimat |
| Momen pemakaian | 1 contoh konkret |
| Tautan | Ke halaman Layanan; ke halaman kapabilitas anak jika Tier B |

**Template kartu:**

> `[KODE]` **[Nama layanan]**
> Kapabilitas: **[Nama kapabilitas anak]**
> [Peran kapabilitas ini di layanan tersebut.]
> *Contoh:* [momen pemakaian konkret].
> → Lihat [nama layanan] · → Pelajari [kapabilitas anak]

**Panduan:**
- Urutkan kartu berdasarkan jumlah cerita pelanggan.
- Jangan tampilkan layanan yang selnya berstatus celah taksonomi (—) atau perkiraan (†).
- Jika satu layanan punya beberapa kapabilitas anak di induk ini, tampilkan semuanya dalam satu kartu.

**Contoh (Notifications & Alerts):**

| Layanan | Kapabilitas anak | Momen pemakaian |
|---|---|---|
| NET | Real-time Notifications | Tim IT menerima peringatan saat jaringan cabang terputus dan saat kembali normal |
| CAM | Intruder Detection | Petugas keamanan menerima peringatan saat ada aktivitas mencurigakan di area terlarang |
| ACD | Real-time Attendance | Wali murid melihat kehadiran anak secara langsung |
| CRM | Broadcast (Blast) · Scheduling & Reminders | Pelanggan menerima pengingat jadwal dan pengumuman penting |

*Kalimat momen pemakaian di atas adalah contoh arah; sesuaikan dengan cerita pelanggan nyata.*

### 4.5 Cara kerja per layanan

**Bentuk:** tab per layanan (urutan sama dengan section 4.4), masing-masing 3 langkah.

**Template per tab:**

| Langkah | Judul | Penjelasan |
|---|---|---|
| 1 | [Hubungkan / Pasang] | [Apa yang disiapkan di layanan ini] |
| 2 | [Atur] | [Konfigurasi, sebut kapabilitas anak dengan nama persis] |
| 3 | [Gunakan / Tindak lanjuti] | [Hasil + kapabilitas saudara yang ikut bekerja] |

### 4.6 Use case

**Anatomi kartu:**

| Elemen | Ketentuan |
|---|---|
| Label layanan | Wajib |
| Peran atau industri | Wajib |
| Hasil | Kalimat berawalan kata kerja |
| Skenario | 2 kalimat (lebih tebal dari tab Dovetail) |
| Tautan | Ke cerita pelanggan jika ada; jika tidak, ke demo |

**Panduan:** 4–6 kartu; usahakan setiap layanan di section 4.4 terwakili minimal 1 kartu.

### 4.7 Integrasi relevan (opsional)

Tampilkan hanya jika kapabilitas bergantung pada integrasi (misalnya API Integration, Communication & Chatbot). Setiap integrasi diberi 1 kalimat tentang gunanya **bagi pembaca**, bukan fungsi teknisnya.

### 4.8 Cerita pelanggan

- Ditarik dari cerita bertag `capabilities_shared` = induk ini, atau `capabilities_core` = salah satu kapabilitas anaknya.
- Setiap kartu **wajib** menampilkan label layanan.
- Tampilkan 1 featured + 2 kartu, usahakan dari layanan berbeda.
- **Fallback:** testimoni berlabel layanan, atau angka penggunaan per layanan.

### 4.9 Keamanan & kontrol

**Wajib untuk:** User & Access Management, Cloud Storage, AI & Automation, API Integration.
**Isi:** 3–5 poin (judul + 1 kalimat). Hanya klaim yang sudah diverifikasi.

### 4.10 FAQ baku (Tier A)

| No | Pertanyaan |
|---|---|
| 1 | Apa itu [kapabilitas]? |
| 2 | [Kapabilitas] tersedia di layanan apa saja? |
| 3 | Apakah saya perlu berlangganan layanan tertentu untuk memakainya? |
| 4 | Apa bedanya [kapabilitas] di setiap layanan? |
| 5 | Bagaimana keamanan datanya? |
| 6 | Bagaimana paket dan harganya? |

### 4.11 CTA

| Pilihan | Contoh |
|---|---|
| Utama | "Temukan layanan yang cocok" → pemilih layanan berisi kartu dari section 4.4 |
| Sekunder | "Jadwalkan demo" |

---

## 5. Kerangka halaman Tier B (kapabilitas layanan)

### Ringkasan struktur

| No | Section | Isi |
|---|---|---|
| 1 | Breadcrumb | `Layanan / [Nama layanan] / [Nama kapabilitas]` |
| 2 | Hero + badge | Badge `Bagian dari [Layanan]` dan `Termasuk dalam [Kapabilitas induk]` |
| 3 | Tantangan | Dalam konteks layanan pemilik |
| 4 | Manfaat | 3 hasil |
| 5 | Cara kerja | 3 langkah di dalam layanan |
| 6 | Use case per peran | Dari peran target layanan pemilik |
| 7 | Bukti | Cerita bertag `capabilities_core` = kapabilitas ini |
| 8 | Kapabilitas lain di layanan ini | Grid saudara + sorotan 1–2 yang sering dipakai bersama |
| 9 | FAQ singkat | 3–4 pertanyaan |
| 10 | CTA | Ke halaman Layanan pemilik + demo |

### 5.1 Hero

**Template:**

> **Breadcrumb:** Layanan / [Nama layanan] / [Nama kapabilitas]
> **Badge:** `Bagian dari [KODE] [Nama layanan]` · `Termasuk dalam [Kapabilitas induk]`
> **Headline:** [Hasil spesifik], [kontras dengan cara lama].
> **Subheadline:** Dengan [nama kapabilitas], [peran] di [konteks layanan] bisa [hasil].
> **Angka:** [angka] [satuan]
> **CTA:** "Lihat [nama layanan]" + "Jadwalkan demo"

**Panduan:**
- Badge `Bagian dari` **wajib**; badge `Termasuk dalam` hanya jika punya induk.
- Badge induk menautkan ke halaman Tier A.

### 5.2 Kapabilitas lain di layanan ini

**Isi:**
- 1–2 kartu sorotan: kapabilitas saudara yang paling sering dipakai bersama (dari data cerita pelanggan)
- Grid ringkas semua kapabilitas saudara (nama + 1 baris + tautan)

### 5.3 FAQ baku (Tier B)

| No | Pertanyaan |
|---|---|
| 1 | Apa itu [kapabilitas] di [layanan]? |
| 2 | Apa yang dibutuhkan untuk mulai memakainya? |
| 3 | Apakah [kapabilitas] bisa dipakai bersama [kapabilitas saudara]? |
| 4 | Apakah [kapabilitas] juga tersedia di layanan lain? *(jawab via kapabilitas induk)* |

---

## 6. Kapabilitas Tier C

Tidak dibuatkan halaman, tapi tetap harus jelas milik layanan apa:
- Tampil sebagai kartu di grid **Semua kapabilitas** pada halaman Layanan pemilik (dengan anchor URL).
- Tampil di section **Tersedia di layanan** pada halaman induknya (jika punya induk).
- Bisa dipakai sebagai tag di cerita pelanggan; tag tersebut menautkan ke anchor di halaman Layanan.

---

## 7. Aturan konsistensi

- Setiap kapabilitas anak punya **tepat 1 layanan pemilik** dan **maksimal 2 induk**.
- Nama kapabilitas **persis** dari taksonomi di semua halaman, menu, tag, dan cerita; tidak ada sinonim.
- Halaman Tier A hanya menampilkan layanan yang punya kapabilitas anak **tervalidasi**.
- Kapabilitas berstatus perkiraan (†) dan sel celah taksonomi (—) **tidak tampil publik**.
- Setiap kartu cerita di halaman kapabilitas **wajib berlabel layanan**.
- Manfaat ditulis sebagai hasil **tanpa nama fitur**; nama fitur baru muncul di section cara kerja.
- Minimal **satu angka** di hero.
- CTA tidak diulang di setiap blok.

---

## 8. Integrasi dengan halaman lain

| Dari | Ke | Lewat |
|---|---|---|
| Halaman Layanan | Tier B | Blok kapabilitas unggulan |
| Halaman Layanan | Tier C | Grid semua kapabilitas (anchor) |
| Halaman Layanan | Tier A | Penanda "Juga di [layanan lain]" pada kartu kapabilitas |
| Tier B | Halaman Layanan pemilik | Breadcrumb, badge, CTA |
| Tier B | Tier A | Badge `Termasuk dalam` |
| Tier A | Halaman Layanan | Kartu section "Tersedia di layanan" |
| Halaman cerita | Tier A/B | Tag kapabilitas |
| Customer Stories | Tier A/B | Filter kapabilitas |

---

## 9. SEO dan metadata

- **Tier A title:** `[Nama kapabilitas] untuk [CRM, Jaringan, CCTV, …] | [Brand]`
- **Tier B title:** `[Nama kapabilitas] — [Nama layanan] | [Brand]`
- **Meta description:** pesan inti + layanan terkait + angka.
- **Breadcrumb** ditandai dengan structured data.
- **FAQ** ditandai dengan structured data FAQ.

---

## 10. Checklist sebelum publikasi

- [ ] Data halaman (section 3) terisi lengkap
- [ ] Tier ditentukan dengan benar (A/B/C)
- [ ] **Tier A:** badge "Tersedia di" hanya berisi layanan dengan kapabilitas anak tervalidasi
- [ ] **Tier A:** setiap kartu "Tersedia di layanan" menyebut kapabilitas anak dengan nama persis
- [ ] **Tier B:** badge `Bagian dari [layanan]` ada dan tertaut
- [ ] **Tier B:** badge `Termasuk dalam [induk]` ada jika punya induk
- [ ] Hero punya subheadline penjelas dan minimal 1 angka
- [ ] Manfaat ditulis tanpa nama fitur
- [ ] Setiap kartu cerita berlabel layanan
- [ ] Tidak ada kapabilitas berstatus perkiraan atau celah taksonomi yang tampil
- [ ] Section keamanan ada untuk induk yang mewajibkannya
- [ ] FAQ memakai set pertanyaan baku
- [ ] Tautan ke halaman Layanan dan Tier A/B berfungsi
- [ ] Tampilan mobile sudah diperiksa

---

## 11. Metrik keberhasilan

| Metrik | Yang diukur | Kegunaan |
|---|---|---|
| Klik kartu "Tersedia di layanan" | Layanan mana yang paling diminati dari kapabilitas ini | Cross-sell & prioritas pesan |
| Klik badge induk/pemilik | Navigasi antar tingkat | Menilai kejelasan hubungan kapabilitas–layanan |
| Klik tab cara kerja | Konteks layanan yang paling dicari | Urutan tab |
| Klik ke cerita pelanggan | Kekuatan bukti | Kebutuhan cerita baru |
| Klik CTA "Temukan layanan yang cocok" | Konversi ke halaman Layanan | Efektivitas halaman Tier A |
| Pencarian/klik kapabilitas Tier C | Minat terhadap kapabilitas tanpa halaman | Kandidat naik ke Tier B |

---

## Lampiran A — Pelajaran dari halaman Dovetail (Product Management)

**Layak ditiru:**
- Tiga lapis abstraksi berurutan: manfaat (tanpa nama fitur) → workflow (fitur disebut) → integrasi.
- Kosakata pembaca, bukan kosakata produk.
- Workflow 3 langkah untuk satu pekerjaan nyata.
- Integrasi diberi konteks gunanya bagi pembaca.
- FAQ yang menjelaskan posisi terhadap alat lain dan menjawab jujur.
- Lead magnet interaktif (kuis 2 menit) sebagai opsi tambahan.

**Sebaiknya dihindari:**
- Hero tanpa kalimat penjelas.
- Tidak ada angka.
- Pengulangan topik yang sama di manfaat, use case, dan FAQ.
- Konten tab use case yang terlalu tipis.
- Cerita pelanggan yang tidak spesifik.
- Nama fitur yang tidak konsisten antar halaman.

---

## Lampiran B — Taksonomi Layanan & Kapabilitas

Daftar baku untuk badge, kartu, dan tag kapabilitas. Gunakan nama persis seperti di bawah.

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
