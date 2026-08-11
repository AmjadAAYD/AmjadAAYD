<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&duration=3200&pause=900&color=FF8A5B&center=true&vCenter=true&width=620&lines=Data+science+%26+AI+engineering;Time+series%2C+NLP%2C+and+the+plumbing+around+them;Occasionally+I+take+hardware+apart" alt="Typing SVG" />

<br>

**Amjad** &nbsp;·&nbsp; Data Science and AI engineering student

<img src="https://komarev.com/ghpvc/?username=AmjadAAYD&style=flat-square&color=FF8A5B&label=profile+views" alt="views" />

</div>

---

## What I actually do

Two internships forecasting industrial SO<sub>2</sub> emissions, moving from a tabular model to
a sequential one coupled with predictive control.

Then, on a weekend, I found out my gamepad had no PC software and took its protocol apart
instead. Both of those are on this profile. I think the second one says more about how I work
than the first.

```python
class Amjad:
    focus     = ["time series", "NLP", "the engineering that keeps a model running"]
    currently = "reverse engineering a gamepad nobody documented"
    rule      = "a result without its baseline means nothing"

    def ship(self, model):
        assert model.score > baseline.score, "you have learned autocorrelation, not the process"
        return model
```

---

## Projects

<table>
<tr><th>Project</th><th>What it does</th><th>Result</th></tr>

<tr><td><a href="https://github.com/AmjadAAYD/x20ctl"><b>x20ctl</b></a><br>
<sub>reverse engineering</sub></td>
<td>The EasySMX X20 ships with no PC software. I decompiled the vendor app, recovered
the BLE protocol, and wrote the tool that should have existed</td>
<td>Protocol documented from scratch. No prior public record of it exists</td></tr>

<tr><td><a href="https://github.com/AmjadAAYD/sma-veille-technologique"><b>sma-veille-technologique</b></a><br>
<sub>LLM agents</sub></td>
<td>Three agents read AI publications overnight and write the summary</td>
<td>Daily report in under 2s, no human in the loop</td></tr>

<tr><td><a href="https://github.com/AmjadAAYD/spam-detection-nlp"><b>spam-detection-nlp</b></a><br>
<sub>NLP</sub></td>
<td>Sorts email into legitimate and spam, three approaches compared</td>
<td>99% correct on 1,160 test messages</td></tr>

<tr><td><a href="https://github.com/AmjadAAYD/weather-data-pipeline"><b>weather-data-pipeline</b></a><br>
<sub>data engineering</sub></td>
<td>Medallion pipeline over 10 cities, bronze through gold</td>
<td>Automated end to end, ingestion through dashboard</td></tr>

<tr><td><a href="https://github.com/AmjadAAYD/pneumonia-detection-pytorch"><b>pneumonia-detection-pytorch</b></a><br>
<sub>computer vision</sub></td>
<td>Spots pneumonia in chest X-rays</td>
<td>87.5% on 624 images, against a 62.5% baseline</td></tr>

<tr><td><a href="https://github.com/AmjadAAYD/arima-vs-lstm-forecasting"><b>arima-vs-lstm-forecasting</b></a><br>
<sub>forecasting</sub></td>
<td>Classical statistics against deep learning, same data, same split</td>
<td>Compared on 43,848 hourly readings</td></tr>

</table>

---

## Stack

<div align="center">

**Machine learning**

<img src="https://skillicons.dev/icons?i=python,pytorch,sklearn&theme=dark" />

**Data engineering and infrastructure**

<img src="https://skillicons.dev/icons?i=docker,postgres,mysql,mongodb,git,linux&theme=dark" />

**Also in the toolbox**

![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat-square)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=flat-square&logo=minio&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![Qt](https://img.shields.io/badge/PySide6-41CD52?style=flat-square&logo=qt&logoColor=white)
![BLE](https://img.shields.io/badge/Bluetooth_LE-0082FC?style=flat-square&logo=bluetooth&logoColor=white)

</div>

---

## Numbers

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=AmjadAAYD&theme=tokyonight" width="94%" />

<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=AmjadAAYD&theme=tokyonight" />
<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=AmjadAAYD&theme=tokyonight" />

<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=AmjadAAYD&theme=tokyonight" />
<img height="180" src="https://streak-stats.demolab.com?user=AmjadAAYD&theme=tokyonight&hide_border=true&ring=FF8A5B&fire=FF8A5B&currStreakLabel=FF8A5B" />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=AmjadAAYD&theme=tokyo-night&hide_border=true&area=true&color=FF8A5B&line=FF8A5B&point=F4F0EB" width="94%" />

</div>

---

## One conviction

> **A result without its baseline means nothing.**

I learned this the hard way. An early version of the emissions model scored R<sup>2</sup> = 0.998
and I was thrilled, until a "predict no change" baseline scored exactly the same. The model had
learned autocorrelation, not the process.

Everything I have published since carries the number it had to beat, and the README says out
loud where the method falls short. The gamepad project has a whole document listing what the
hardware **cannot** do, because that turned out to be the more useful half.

---

<div align="center">

<sub>Open an issue on any repo, or reach me through GitHub.</sub>

</div>
