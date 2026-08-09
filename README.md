# Amjad AAYD

Data Science and AI engineering student.

Two internships forecasting industrial SO<sub>2</sub> emissions, moving from a tabular model
to a sequential one coupled with predictive control. What holds my attention: time series,
NLP, and the engineering that actually keeps a model running.

---

### Projects

| Project | What it does | Result |
|---|---|---|
| [spam-detection-nlp](https://github.com/AmjadAAYD/spam-detection-nlp) | Sorts email into legitimate and spam | 99% correct on 1,160 test messages |
| [sma-veille-technologique](https://github.com/AmjadAAYD/sma-veille-technologique) | Three LLM agents that read AI publications overnight and write the summary | Daily report in under 2s, no human in the loop |
| [weather-data-pipeline](https://github.com/AmjadAAYD/weather-data-pipeline) | Medallion pipeline over 10 cities | Automated end to end, ingestion through dashboard |
| [pneumonia-detection-pytorch](https://github.com/AmjadAAYD/pneumonia-detection-pytorch) | Spots pneumonia in chest X-rays | 87.5% on 624 images, against a 62.5% baseline |
| [arima-vs-lstm-forecasting](https://github.com/AmjadAAYD/arima-vs-lstm-forecasting) | Classical statistics against deep learning | Compared on 43,848 hourly readings |

---

### Stack

| | |
|---|---|
| **Machine Learning** | Python, PyTorch, Scikit-Learn, XGBoost, Pandas, NumPy |
| **NLP and generative AI** | LangGraph, RAG, Qdrant, Word2Vec, TF-IDF, n8n |
| **Data Engineering** | Airflow, Docker, MinIO, Talend, Git |
| **Data and BI** | MySQL, Oracle PL/SQL, MongoDB, Power BI |

---

### One conviction

A result without its baseline means nothing.

I learned this the hard way. An early version of the emissions model scored R<sup>2</sup> = 0.998
and I was thrilled, until a "predict no change" baseline scored exactly the same. The model had
learned autocorrelation, not the process. Everything I have published since carries the number
it had to beat, and the README says out loud where the method falls short.

---

[LinkedIn](https://linkedin.com/in/amjad-aayd) · aaydamjad@gmail.com
