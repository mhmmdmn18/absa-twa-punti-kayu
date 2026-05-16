# Analisis Sentimen Berbasis Aspek terhadap Taman Wisata Alam Punti Kayu Berdasarkan Ulasan Google Maps

Repository ini berisi implementasi penelitian **Aspect-Based Sentiment Analysis (ABSA)** pada ulasan pengguna Google Maps terhadap **Taman Wisata Alam (TWA) Punti Kayu** menggunakan pendekatan **Machine Learning** dan **Transfer Learning**.

Penelitian bertujuan untuk menganalisis sentimen wisatawan berdasarkan aspek tertentu guna mengidentifikasi kelebihan, kekurangan, dan rekomendasi perbaikan pengelolaan wisata.

## 🎯 Tujuan Penelitian

- Menganalisis sentimen wisatawan terhadap TWA Punti Kayu.
- Mengidentifikasi sentimen pada tiap aspek wisata.
- Membandingkan performa model **Machine Learning** dan **Transfer Learning**.
- Memberikan insight untuk evaluasi pengelolaan wisata.

## 🏛️ Aspek yang Dianalisis

- **Aksesibilitas**
- **Amenitas**
- **Daya Tarik**
- **Harga**
- **SDM (Sumber Daya Manusia)**
- **Citra**

## 🤖 Model yang Digunakan

### Machine Learning
- Logistic Regression (LR)
- Support Vector Machine (SVM)

### Transfer Learning
- BERT
- IndoBERT

## ⚙️ Skenario Eksperimen

Penelitian menggunakan tiga skenario pra-pemrosesan data:

- **Skenario 1** → seluruh teknik pra-pemrosesan diterapkan  
- **Skenario 2** → kombinasi tertentu teknik pra-pemrosesan  
- **Skenario 3** → tanpa penghapusan *stopwords*

## 📊 Hasil Eksperimen

| Model | Rata-rata F1 Score |
|--------|-------------------|
| **IndoBERT** | **97.95%** |
| BERT | 95.75% |
| SVM | 87.33% |
| Logistic Regression | 86.83% |

Model terbaik diperoleh oleh **IndoBERT pada Skenario 3** dengan **F1 Score 98.22%**.

### Temuan Utama

- **Transfer Learning** memiliki performa lebih baik dibandingkan **Machine Learning**.
- **IndoBERT** menjadi model terbaik karena dilatih menggunakan korpus bahasa Indonesia sehingga lebih memahami konteks ulasan wisatawan.
- **LR dan SVM** mencapai performa terbaik pada **Skenario 1**.
- **BERT dan IndoBERT** mencapai performa terbaik pada **Skenario 3** (*tanpa stopwords removal*).

## 📈 Hasil Analisis Sentimen

Distribusi sentimen wisatawan terhadap **TWA Punti Kayu**:

| Sentimen | Persentase |
|-----------|------------|
| Positif | **40.5%** |
| Negatif | 32.8% |
| Netral | 26.7% |

### Insight Per Aspek

✅ **Cenderung Positif**
- Aksesibilitas
- Citra

⚠️ **Perlu Perhatian**
- Amenitas
- Harga
- SDM
- Daya Tarik

Hasil penelitian menunjukkan bahwa peningkatan pada aspek **Amenitas, Harga, SDM, dan Daya Tarik** berpotensi meningkatkan **Citra TWA Punti Kayu**. Meski sentimen positif mendominasi, tingginya sentimen negatif menunjukkan perlunya evaluasi layanan, sementara tingginya sentimen netral mengindikasikan pengalaman wisata yang belum cukup berkesan bagi sebagian pengunjung.

## 🧪 Metode Evaluasi

Model dievaluasi menggunakan:
- Accuracy
- Precision
- Recall
- **F1 Score** (metrik utama)

## 📖 Skripsi / Full Paper

Skripsi lengkap dapat diakses melalui:

https://repository.unsri.ac.id/156468/

## 👨‍💻 Author

**Muhammad Aminuddin**  
Universitas Sriwijaya

## 📜 License

Repository ini dibuat untuk keperluan akademik dan penelitian.
