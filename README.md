# Analisis Sentimen Berbasis Aspek terhadap Taman Wisata Alam Punti Kayu Berdasarkan Ulasan Google Maps

Repository ini berisi implementasi penelitian skripsi mengenai **Aspect-Based Sentiment Analysis (ABSA)** pada ulasan pengguna Google Maps terhadap **Taman Wisata Alam (TWA) Punti Kayu**, menggunakan pendekatan **Machine Learning** dan **Transfer Learning**.

Penelitian ini bertujuan untuk menganalisis sentimen wisatawan berdasarkan aspek tertentu guna memberikan rekomendasi perbaikan layanan dan pengelolaan wisata.

---

## 📌 Latar Belakang

Ulasan wisatawan pada platform digital seperti Google Maps mengandung informasi penting mengenai pengalaman pengunjung. Namun, analisis sentimen secara umum sering kali belum mampu mengidentifikasi aspek spesifik yang menjadi sumber kepuasan atau ketidakpuasan wisatawan.

Oleh karena itu, penelitian ini menerapkan **Aspect-Based Sentiment Analysis (ABSA)** untuk mengelompokkan sentimen berdasarkan aspek tertentu pada objek wisata **TWA Punti Kayu**.

---

## 🎯 Tujuan Penelitian

Penelitian ini bertujuan untuk:

- Menganalisis sentimen wisatawan terhadap TWA Punti Kayu.
- Mengidentifikasi aspek wisata yang paling banyak mendapatkan sentimen positif maupun negatif.
- Membandingkan performa model **Machine Learning** dan **Transfer Learning** dalam klasifikasi sentimen.
- Memberikan rekomendasi evaluasi terhadap pengelolaan wisata berdasarkan hasil analisis.

---

## 🏛️ Aspek yang Dianalisis

Analisis dilakukan berdasarkan beberapa aspek wisata berikut:

- **Aksesibilitas**
- **Amenitas**
- **Daya Tarik**
- **Harga**
- **SDM (Sumber Daya Manusia)**
- **Citra**

---

## 🤖 Model yang Digunakan

### Machine Learning
- Logistic Regression (LR)
- Support Vector Machine (SVM)

### Transfer Learning
- BERT
- IndoBERT

---

## ⚙️ Skenario Eksperimen

Penelitian menggunakan beberapa skenario pra-pemrosesan data:

### Skenario 1
Menggunakan seluruh teknik pra-pemrosesan data.

### Skenario 2
Menggunakan kombinasi tertentu dari teknik pra-pemrosesan.

### Skenario 3
Menggunakan pra-pemrosesan data **tanpa penghapusan stopwords**.

---

## 📊 Hasil Eksperimen

Hasil eksperimen menunjukkan bahwa model **IndoBERT** memberikan performa terbaik.

| Model | Rata-rata F1 Score |
|--------|-------------------|
| IndoBERT | **97.95%** |
| BERT | 95.75% |
| SVM | 87.33% |
| Logistic Regression | 86.83% |

Model terbaik diperoleh oleh **IndoBERT pada Skenario 3** dengan:

> **F1 Score: 98.22%**

### Temuan Penting

- **Transfer Learning** terbukti lebih unggul dibandingkan **Machine Learning**.
- **IndoBERT** memiliki performa terbaik karena dilatih menggunakan korpus bahasa Indonesia sehingga lebih memahami konteks kalimat pada ulasan wisatawan berbahasa Indonesia.
- Model **Machine Learning (LR & SVM)** mencapai performa terbaik pada **Skenario 1**.
- Model **Transfer Learning (BERT & IndoBERT)** mencapai performa terbaik pada **Skenario 3** (tanpa penghapusan stopwords).

---

## 📈 Hasil Analisis Sentimen Wisatawan

Distribusi sentimen wisatawan terhadap **TWA Punti Kayu**:

| Sentimen | Persentase |
|-----------|------------|
| Positif | **40.5%** |
| Negatif | 32.8% |
| Netral | 26.7% |

### Insight Per Aspek

#### ✅ Aspek dengan Sentimen Cenderung Positif
- **Aksesibilitas**
- **Citra**

#### ⚠️ Aspek yang Memerlukan Perhatian
- **Amenitas**
- **Harga**
- **SDM**
- **Daya Tarik**

Hasil penelitian menunjukkan bahwa peningkatan pada aspek **Amenitas, Harga, SDM, dan Daya Tarik** berpotensi memberikan dampak signifikan terhadap peningkatan **Citra TWA Punti Kayu**.

Meskipun sentimen positif mendominasi (**40.5%**), masih terdapat **32.8% sentimen negatif**, yang menunjukkan perlunya evaluasi dan perbaikan layanan oleh pihak pengelola. Selain itu, tingginya sentimen **netral (26.7%)** mengindikasikan bahwa sebagian wisatawan belum memperoleh pengalaman yang cukup berkesan selama berkunjung.

---

## 🧪 Metode Evaluasi

Model dievaluasi menggunakan metrik:

- Accuracy
- Precision
- Recall
- **F1 Score**

F1 Score dipilih sebagai metrik utama karena mampu memberikan keseimbangan antara precision dan recall dalam klasifikasi sentimen.

---

## 📖 Skripsi / Full Paper

Repository skripsi lengkap dapat diakses melalui:

:contentReference[oaicite:0]{index=0}

---

## 👨‍💻 Author

**Muhammad Aminuddin**  
Universitas Sriwijaya

---

## 📜 License

Repository ini dibuat untuk keperluan akademik dan penelitian.
