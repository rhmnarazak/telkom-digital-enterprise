# Kerangka Halaman Layanan

Panduan untuk menyusun halaman Layanan di website produk. Diadaptasi dari halaman produk Dovetail (Digital Twins), dengan perbaikan pada tiga kelemahannya: tidak ada bagian cara kerja, tidak ada angka, dan bukti pelanggan yang tidak spesifik.

Dokumen ini melengkapi **Kerangka Success Story** dan **Kerangka Halaman Customer Stories**. Ketiganya memakai taksonomi layanan dan kapabilitas yang sama (lihat **Lampiran B — Taksonomi Layanan & Kapabilitas**). Tone of voice, gaya bahasa, dan aturan desain mengikuti **Panduan Tone of Voice — Landing Page Telkom Digital** (`panduan-tone-of-voice.md`).

**Fungsi halaman:** tempat bertemunya Kapabilitas dan Cerita Pelanggan. Kapabilitas menjelaskan apa yang bisa dilakukan, cerita membuktikan bahwa itu berhasil. Keduanya ditarik dari data yang sama, bukan ditulis ulang manual.

**Prinsip utama:** setiap halaman Layanan menjawab pertanyaan calon pembeli secara berurutan: apa ini → mengapa penting → bagaimana cara kerjanya → apa yang bisa dilakukan → untuk siapa → siapa yang sudah pakai → apakah aman → pertanyaan detail.

---

## 1. Hubungan tiga jenis halaman

| Halaman | Isinya | Menarik data dari |
|---|---|---|
| Layanan (6 halaman) | Apa layanan ini, kapabilitas apa saja, untuk siapa, bukti | Taksonomi + cerita bertag `service_primary` / `services_supporting` |
| Kapabilitas | Satu blok teknis yang dipakai beberapa layanan | Taksonomi + cerita bertag `capabilities_core` / `capabilities_shared` |
| Customer Stories | Semua cerita, bisa difilter | Kartu identifikasi use case |

**Alur navigasi yang diharapkan:**
- Layanan → Kapabilitas (lewat label kapabilitas unggulan dan grid semua kapabilitas)
- Layanan → Cerita (lewat section cerita pelanggan dan kartu use case per peran)
- Kapabilitas → Layanan lain yang memakai kapabilitas yang sama (cross-sell)

---

## 2. Ringkasan struktur halaman

| No | Section | Tujuan | Wajib |
|----|---------|--------|-------|
| 0 | Data halaman | Menetapkan isi sebelum menulis | Ya (internal) |
| 1 | Hero | Posisi layanan lewat kontras + angka | Ya |
| 2 | Strip "Terhubung dengan" | Menjawab kecocokan dengan sistem yang ada | Ya |
| 3 | Masalah | Menggeser cara pandang pembaca | Ya |
| 4 | Cara kerja | Menunjukkan usaha implementasi | Ya |
| 5 | Kapabilitas unggulan | 3–4 kapabilitas inti dengan bukti | Ya |
| 6 | Semua kapabilitas | Daftar lengkap kapabilitas layanan | Ya |
| 7 | Use case per peran | Membuat pembaca menemukan dirinya | Ya |
| 8 | Cerita pelanggan | Bukti spesifik layanan | Ya (dengan fallback) |
| 9 | Keamanan, kepatuhan, kontrol | Menjawab keberatan IT & legal | Ya |
| 10 | Layanan terkait | Cross-sell | Opsional |
| 11 | Paket | Gambaran model harga/paket | Opsional |
| 12 | FAQ | Pertanyaan detail & perbandingan | Ya |
| 13 | CTA penutup | Mengarahkan ke aksi | Ya |

---

## 3. Detail setiap section

### 3.0 Data halaman (internal)

Isi tabel ini sebelum menulis copy. Semua nama layanan dan kapabilitas diambil dari taksonomi.

| Field | Isi | Ketentuan |
|---|---|---|
| Kode & nama layanan | [misalnya CAM — IP Cam Management] | Dari taksonomi |
| Nama produk | [misalnya Antares Eazy] | Opsional |
| Pesan inti | [pembeda utama dalam 1 kalimat] | Diulang minimal 3× di halaman |
| Kapabilitas unggulan | [3–4 nama kapabilitas] | Harus berstatus tersedia dan tervalidasi |
| Kapabilitas lengkap | [semua kapabilitas layanan] | Dari taksonomi; tanpa yang berstatus perkiraan |
| Peran target | [4–6 peran] | Peran nyata pembeli/pengguna |
| Integrasi / ekosistem | [daftar] | Hanya yang benar-benar didukung |
| Angka utama | [1–3 angka] | Valid dan bisa dipertanggungjawabkan |
| Cara lama (pembanding) | [cara/alat yang dipakai pembaca sebelumnya] | Untuk headline kontras |
| Layanan terkait | [1–2 kode layanan] | Dari kombinasi cerita atau kapabilitas lintas layanan |

**Pesan inti diulang di:** hero (subheadline), salah satu kapabilitas unggulan, dan FAQ.

---

### 3.1 Hero

**Isi:**
- **Eyebrow:** `LAYANAN / [Nama layanan]`
- **Headline:** pola kontras *"[Cara lama] [melakukan X]. [Layanan] [melakukan Y yang lebih baik]."*
- **Subheadline:** apa itu, untuk siapa, dibangun dari apa, dan pembedanya (pesan inti).
- **Angka:** minimal 1 (pelanggan, perangkat terhubung, institusi, atau dampak rata-rata).
- **CTA:** dua pilihan dengan komitmen berbeda.
- **Visual:** screenshot produk utama (versi desktop dan mobile).

**Template:**

> **Eyebrow:** LAYANAN / [NAMA LAYANAN]
> **Headline:** [Cara lama] [kelemahannya]. [Layanan] [keunggulannya].
> **Subheadline:** [Layanan] membantu [peran target] [hasil utama] dengan [kapabilitas inti], [pesan inti].
> **Angka:** [angka]+ [satuan]
> **CTA:** [Hubungi sales] · [Coba gratis / Jadwalkan demo]

**Panduan:**
- Pembanding di headline harus sesuatu yang dikenal pembaca, bukan kompetitor yang disebut namanya.
- Hindari headline lebih dari 15 kata.

---

### 3.2 Strip "Terhubung dengan"

**Isi:** baris logo atau ikon integrasi, perangkat, kanal, atau ekosistem yang didukung, dengan tautan ke dokumentasi jika ada.

**Panduan:**
- Letakkan tepat di bawah hero.
- Hanya tampilkan yang benar-benar didukung.
- Jika jumlahnya banyak, tampilkan 5–6 lalu tombol "+ lainnya".

---

### 3.3 Masalah

**Isi:** satu judul + 2–3 kalimat yang menggambarkan cara lama, kerugiannya, dan cara pandang baru.

**Template:**

> **[Judul yang menggeser cara pandang]**
> Selama ini, [peran target] [melakukan cara lama]. Akibatnya, [kerugian konkret]. Masalahnya bukan lagi [hal yang dianggap masalah], tapi [masalah sebenarnya].

**Panduan:**
- Gunakan detail yang mudah dibayangkan.
- Boleh didukung video demo singkat atau animasi.

---

### 3.4 Cara kerja

**Isi:** 3 langkah, masing-masing dengan judul singkat, satu kalimat, dan ikon atau ilustrasi.

**Template:**

| Langkah | Judul | Penjelasan |
|---|---|---|
| 1 | [Hubungkan] | [Apa yang dihubungkan / dipasang] |
| 2 | [Atur] | [Apa yang dikonfigurasi] |
| 3 | [Pantau / Gunakan] | [Hasil yang langsung didapat] |

**Tambahan:** satu baris gambaran usaha implementasi, misalnya "Aktif dalam [durasi], tanpa [hambatan umum]".

---

### 3.5 Kapabilitas unggulan

**Isi:** 3–4 blok bernomor, satu blok per kapabilitas inti.

**Anatomi blok:**

| Elemen | Ketentuan |
|---|---|
| Nomor | 01–04 |
| Label kecil | Nama kapabilitas persis dari taksonomi (misalnya `Cloud Recording`) |
| Judul | Manfaat, bukan nama fitur |
| Isi | 1–2 kalimat yang menyebut momen pemakaian nyata |
| Visual | Screenshot atau ilustrasi |
| Bukti mini | Satu kutipan atau angka dari cerita bertag kapabilitas ini |
| Tautan | "Pelajari [nama kapabilitas] →" ke halaman Kapabilitas |

**Template blok:**

> **01** · `[Nama kapabilitas]`
> **[Judul manfaat]**
> [Saat/ketika momen pemakaian], [peran] bisa [hasil] tanpa [hambatan lama].
> *"[Kutipan pendek]"* — [Nama], [Jabatan], [Perusahaan]
> Pelajari [nama kapabilitas] →

**Panduan:**
- Satu CTA di akhir section, bukan di setiap blok.
- Salah satu blok memuat pesan inti.
- Jika sebuah kapabilitas belum punya bukti mini, tandai sebagai prioritas cerita pelanggan berikutnya.

---

### 3.6 Semua kapabilitas

**Isi:** grid seluruh kapabilitas layanan dari taksonomi.

**Anatomi kartu kapabilitas:**

| Elemen | Ketentuan |
|---|---|
| Nama | Persis dari taksonomi |
| Deskripsi | 1 baris |
| Status | `Tersedia` atau `Segera hadir` |
| Penanda lintas layanan | Ikon/label "Juga di [kode layanan lain]" jika termasuk kapabilitas lintas layanan |
| Tautan | Ke halaman Kapabilitas |

**Panduan:**
- Kapabilitas berstatus perkiraan (†) tidak ditampilkan sampai divalidasi.
- Kelompokkan jika lebih dari 9 kapabilitas (misalnya per fungsi: komunikasi, analitik, keamanan).
- Kapabilitas unggulan tetap muncul di grid ini agar daftar lengkap.

---

### 3.7 Use case per peran

**Isi:** 4–6 kartu peran.

**Anatomi kartu:**

| Elemen | Ketentuan |
|---|---|
| Peran | Jabatan atau fungsi pembaca |
| Hasil | Kalimat berawalan kata kerja |
| Skenario | 1 kalimat situasi nyata |
| Tag kapabilitas | 1–2 nama kapabilitas yang dipakai |
| Tautan | Ke cerita pelanggan yang relevan, jika ada; jika tidak, ke demo |

**Template:**

> **[Peran]**
> **[Kata kerja + hasil]**
> [Skenario satu kalimat].
> `[Kapabilitas 1]` `[Kapabilitas 2]`
> → [Lihat cerita / Jadwalkan demo]

---

### 3.8 Cerita pelanggan

**Isi:** ditarik otomatis dari cerita dengan `service_primary` = layanan ini (prioritas), lalu `services_supporting`.

**Tampilan:**
- 1 featured story (judul berangka, ringkasan 2 kalimat, 3 angka)
- 2 kartu cerita (anatomi sama dengan kartu di halaman Customer Stories)
- Tautan "Semua cerita [nama layanan]" ke halaman Customer Stories yang sudah terfilter

**Fallback jika belum ada cerita:**
1. Testimoni pengguna layanan ini
2. Angka penggunaan (jumlah pelanggan, perangkat, institusi)
3. Logo pelanggan layanan ini

Jangan menampilkan cerita yang tidak terkait layanan ini.

---

### 3.9 Keamanan, kepatuhan, dan kontrol

**Isi:** 3–5 poin, masing-masing judul + 1 kalimat.

**Contoh topik:**
- Perlindungan data pribadi dan kepatuhan regulasi
- Lokasi penyimpanan data
- Kontrol akses dan peran pengguna
- Audit log / jejak aktivitas
- Registrasi atau sertifikasi yang relevan

**Panduan:** letakkan setelah pembaca tertarik; hanya sebut sertifikasi atau kepatuhan yang benar-benar dimiliki.

---

### 3.10 Layanan terkait (opsional)

**Isi:** 1–2 kartu layanan lain.

**Sumber penentuan:**
- Kombinasi layanan yang sering muncul bersama di cerita pelanggan (`services_supporting`)
- Kapabilitas lintas layanan yang sama

**Template:**

> **[Nama layanan terkait]**
> [Satu kalimat bagaimana kedua layanan saling melengkapi.]
> → Lihat layanan

---

### 3.11 Paket (opsional)

**Isi:** gambaran paket atau model modular (misalnya paket dasar + modul tambahan), atau ajakan konsultasi jika harga bersifat custom.

---

### 3.12 FAQ

Gunakan set pertanyaan baku yang sama untuk keenam layanan.

| No | Pertanyaan baku | Catatan |
|---|---|---|
| 1 | Apa itu [layanan]? | Definisi + pesan inti |
| 2 | Untuk siapa [layanan] cocok? | Peran dan ukuran organisasi |
| 3 | Apa bedanya [layanan] dengan [cara lama / alternatif umum]? | Perbandingan tanpa menyebut kompetitor |
| 4 | Apa yang dibutuhkan sebelum mulai? | Prasyarat; jawab jujur termasuk "tidak bisa" |
| 5 | Berapa lama implementasinya? | Konsisten dengan section Cara kerja |
| 6 | Bisakah terhubung dengan [sistem umum]? | Konsisten dengan strip integrasi |
| 7 | Bagaimana keamanan data saya? | Konsisten dengan section Keamanan |
| 8 | Bagaimana paket dan harganya? | Konsisten dengan section Paket |

**Panduan:** boleh menambah 1–3 pertanyaan khusus layanan.

---

### 3.13 CTA penutup

| Pilihan | Untuk siapa | Contoh |
|---|---|---|
| Utama | Siap membeli | "Jadwalkan demo" |
| Sekunder | Masih mempertimbangkan | "Coba gratis" atau "Konsultasi kebutuhan" |

Boleh disertai frasa penutup yang mengulang posisi layanan dengan pola kontras.

---

## 4. Pemetaan awal per layanan

| Kode | Contoh headline kontras | Kapabilitas unggulan | Peran target |
|---|---|---|---|
| CRM | Pesan pelanggan datang dari mana saja. Jawab semuanya dari satu tempat. | Omnichannel Inbox · Chatbot Builder · Ticketing · Interaction Analytics | Pemilik usaha, manajer CS, agen CS, tim marketing, instansi layanan publik |
| ACD | Absensi kertas mencatat kehadiran. Pijar menunjukkan perkembangan belajar. | Computer-based Assessment · Real-time Attendance · Learning Performance Tracking · Role-based Portals | Manajemen institusi, pengajar, peserta & wali, admin, dinas pendidikan |
| NET | Tool monitoring biasa memberi tahu saat jaringan mati. Kami memberi tahu sebelum itu terjadi. | Network Monitoring · Web/API Monitoring · Proactive & Predictive Maintenance · Automated Reporting | Manajer IT, network engineer, tim DevOps, pemilik usaha |
| CAM | CCTV biasa merekam kejadian. IP Cam dengan AI memberi tahu saat itu terjadi. | Cloud Recording · Intruder Detection · People Counting & Crowd Detection · Multi-site Deployment | Pemilik usaha, kepala keamanan, facility manager, HR, manajer toko |
| DOC† | Dokumen tersebar di folder dan email. Temukan, setujui, dan tandatangani di satu tempat. | Central Repository · Search & OCR · Approval Workflow · Electronic Signature | Legal, sekretariat, finance, compliance |
| GAI† | AI publik menebak jawaban. AI di atas data perusahaan menjawab dengan sumber. | Knowledge Base (RAG) · AI Agent & Workflow Builder · Guardrails & Data Privacy · Usage & Cost Monitoring | CIO/tim IT, tim data & AI, karyawan, compliance |

† Masih perkiraan, perlu divalidasi tim produk. Headline di atas adalah contoh arah, bukan copy final.

---

## 5. Aturan penulisan

- Judul manfaat ditulis dari **momen pemakaian**, bukan nama fitur.
- Nama layanan dan kapabilitas **persis** dari taksonomi; tidak ada sinonim.
- **Pesan inti** diulang minimal 3× (hero, kapabilitas unggulan, FAQ).
- Minimal **satu angka** di atas lipatan pertama.
- CTA **tidak diulang** di setiap blok; cukup di hero, akhir kapabilitas unggulan, dan penutup.
- Setiap klaim kapabilitas unggulan sebaiknya didukung **bukti dari cerita** bertag kapabilitas tersebut.
- Pola kontras ("X, bukan Y") dipakai secukupnya: hero, penutup, dan paling banyak satu kali di tengah.
- Jawaban FAQ **jujur**, termasuk jika jawabannya "tidak".

---

## 6. SEO dan metadata

- **Title:** `[Nama layanan] | [Hasil utama] untuk [Peran/Industri] — [Brand]`
- **Meta description:** pesan inti + 2 kapabilitas unggulan + angka utama.
- **H1** = headline hero; **H2** = judul setiap section.
- **FAQ** ditandai dengan structured data FAQ.
- **Alt text** untuk setiap screenshot dan logo.

---

## 7. Checklist sebelum publikasi

- [ ] Data halaman (3.0) terisi lengkap
- [ ] Headline memakai pola kontras dan ≤15 kata
- [ ] Minimal satu angka di hero, valid dan terbaru
- [ ] Pesan inti muncul minimal 3×
- [ ] Section Cara kerja menyebut gambaran usaha implementasi
- [ ] 3–4 kapabilitas unggulan memakai nama persis dari taksonomi
- [ ] Setiap kapabilitas unggulan tertaut ke halaman Kapabilitas
- [ ] Grid semua kapabilitas lengkap, tanpa kapabilitas berstatus perkiraan
- [ ] Status `Segera hadir` diberi label jelas
- [ ] Kartu use case per peran memiliki tag kapabilitas
- [ ] Cerita pelanggan spesifik layanan ini (atau fallback dipakai)
- [ ] Klaim keamanan/kepatuhan sudah diverifikasi
- [ ] FAQ memakai set pertanyaan baku
- [ ] CTA tidak diulang berlebihan
- [ ] Tampilan mobile sudah diperiksa

---

## 8. Metrik keberhasilan

| Metrik | Yang diukur | Kegunaan |
|---|---|---|
| Klik CTA | Konversi ke demo / coba gratis | Efektivitas halaman |
| Klik kapabilitas | Kapabilitas mana yang paling menarik | Menentukan kapabilitas unggulan |
| Klik kartu peran | Peran mana yang paling sering mengidentifikasi diri | Prioritas pesan dan cerita |
| Klik ke cerita pelanggan | Seberapa kuat bukti mendorong eksplorasi | Kebutuhan cerita baru |
| Klik layanan terkait | Minat cross-sell | Kombinasi layanan untuk paket |
| Scroll depth | Sejauh mana halaman dibaca | Urutan dan panjang section |

---

## Lampiran A — Pelajaran dari halaman Dovetail (Digital Twins)

**Layak ditiru:**
- Headline kontras terhadap konsep yang sudah dikenal pembaca.
- Strip integrasi tepat di bawah hero.
- Reframe masalah sebelum masuk ke fitur.
- Manfaat bernomor yang ditulis dari momen pemakaian.
- Use case per peran dengan hasil berawalan kata kerja.
- Section kontrol & kepercayaan setelah keinginan terbangun.
- FAQ yang membandingkan dengan alternatif dan menjawab jujur.
- Satu pesan inti diulang di beberapa section.

**Sebaiknya dihindari:**
- Pasangan CTA diulang di setiap blok.
- Tidak ada angka di seluruh halaman.
- Testimoni dan cerita pelanggan yang tidak spesifik produk.
- Tidak ada penjelasan cara kerja atau usaha implementasi.

---

## Lampiran B — Taksonomi Layanan & Kapabilitas

Daftar baku untuk data halaman, label kapabilitas, dan grid semua kapabilitas. Gunakan nama persis seperti di bawah.

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
