# Aspect-Based Sentiment Analysis of Punti Kayu Nature Park Based on Google Maps User Reviews

This repository contains the implementation of an **Aspect-Based Sentiment Analysis (ABSA)** study on **Google Maps user reviews** of **Punti Kayu Nature Park**, utilizing both **Machine Learning** and **Transfer Learning** approaches.

The research aims to analyze tourist sentiment across specific aspects in order to identify strengths, weaknesses, and actionable recommendations for improving tourism management and visitor experience.

## 🎯 Research Objectives

This study aims to:

- Analyze tourist sentiment toward **Punti Kayu Nature Park**.
- Identify sentiment distribution across tourism-related aspects.
- Compare the performance of **Machine Learning** and **Transfer Learning** models.
- Provide insights to support tourism management evaluation and improvement.

## 🏛️ Analyzed Aspects

The sentiment analysis is conducted based on the following tourism aspects:

- **Accessibility**
- **Amenities**
- **Attractions**
- **Pricing**
- **Human Resources (HR)**
- **Destination Image**

## 🤖 Models Used

### Machine Learning
- **Logistic Regression (LR)**
- **Support Vector Machine (SVM)**

### Transfer Learning
- **BERT**
- **IndoBERT**

## ⚙️ Experimental Scenarios

The study applies three different data preprocessing scenarios:

- **Scenario 1** → Full preprocessing pipeline applied  
- **Scenario 2** → Selected preprocessing techniques applied  
- **Scenario 3** → Preprocessing without *stopwords removal*

## 📊 Experimental Results

| Model | Average F1 Score |
|--------|------------------|
| **IndoBERT** | **97.95%** |
| BERT | 95.75% |
| SVM | 87.33% |
| Logistic Regression | 86.83% |

The best-performing model was **IndoBERT under Scenario 3**, achieving an **F1 Score of 98.22%**.

### Key Findings

- **Transfer Learning models** outperformed traditional **Machine Learning models**.
- **IndoBERT** achieved the highest performance due to its training on large-scale Indonesian language corpora, enabling a better understanding of contextual meaning in Indonesian tourism reviews.
- **Logistic Regression** and **SVM** achieved their best performance under **Scenario 1**.
- **BERT** and **IndoBERT** performed best under **Scenario 3** (*without stopwords removal*).

## 📈 Sentiment Analysis Results

The overall sentiment distribution toward **Punti Kayu Nature Park** is as follows:

| Sentiment | Percentage |
|------------|------------|
| Positive | **40.5%** |
| Negative | 32.8% |
| Neutral | 26.7% |

### Aspect-Based Insights

✅ **Predominantly Positive Aspects**
- Accessibility
- Destination Image

⚠️ **Aspects Requiring Improvement**
- Amenities
- Pricing
- Human Resources
- Attractions

The findings indicate that improvements in **Amenities, Pricing, Human Resources, and Attractions** may significantly enhance the overall **Destination Image** of Punti Kayu Nature Park.

Although **positive sentiment dominates (40.5%)**, the relatively high percentage of **negative sentiment (32.8%)** highlights the need for service improvements. Furthermore, the considerable proportion of **neutral sentiment (26.7%)** suggests that some visitors had experiences that were not particularly memorable.

## 🧪 Evaluation Metrics

Model performance was evaluated using:

- Accuracy
- Precision
- Recall
- **F1 Score** *(primary evaluation metric)*

## 📖 Thesis / Full Paper

The complete thesis can be accessed at:

https://repository.unsri.ac.id/156468/

## 👨‍💻 Author

**Muhammad Aminuddin**  
Universitas Sriwijaya

## 📜 License

This repository was created for academic and research purposes.
