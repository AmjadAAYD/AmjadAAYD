<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=27&duration=3000&pause=800&color=FF8A5B&center=true&vCenter=true&width=700&lines=Welcome+to+my+Rep;Models+by+day%2C+protocols+by+night;If+it+has+a+baseline%2C+it+can+be+beaten" alt="Welcome to my Rep" />

<br>

**Amjad** &nbsp;·&nbsp; Data science and AI engineering


</div>

---

## Welcome to my Rep

Time series, NLP, and the plumbing that keeps a model breathing.

Two internships forecasting industrial SO<sub>2</sub> emissions, tabular to sequential,
then wired into predictive control.

On the weekend I make random software about some random stuff, or basically reverse
engineer things nobody bothered to document.

<div align="center">

> *Anyone can post a number and call it a win.*
> *I show what it beat. That's where the work begins.*
> *Every model looks like genius till you sit a dumb one down,*
> *and the dumb one ties the score. So who's wearing the crown?*

</div>

```python
class Amjad:
    day    = ["time series", "NLP", "the engineering that keeps it running"]
    night  = "taking apart hardware that shipped without software"
    rule   = "a result without its baseline means nothing"

    def ship(self, model, baseline):
        if model.score <= baseline.score:
            raise ValueError("you learned autocorrelation, not the process")
        return model, baseline          # both. always both.
```

---

## The work

<table>
<tr><th>Project</th><th>What it does</th><th>Result</th></tr>

<tr><td><a href="https://github.com/AmjadAAYD/x20ctl"><b>x20ctl</b></a><br>
<sub>reverse engineering</sub></td>
<td>My gamepad shipped with no PC software, so I decompiled the vendor app,
recovered the Bluetooth protocol, and wrote the tool that should have existed</td>
<td>Protocol documented from scratch. No prior public record of it exists</td></tr>

<tr><td><a href="https://github.com/AmjadAAYD/exoplanet-transit-detection"><b>exoplanet-transit-detection</b></a><br>
<sub>astronomy</sub></td>
<td>Pulls raw light curves straight from NASA's MAST archive and runs a classical
transit search, the same method astronomers use, then vets detections with a CNN</td>
<td>Recovers TRAPPIST-1, Kepler-90 and Kepler-186's orbital periods from raw data,
checked against the published catalog</td></tr>

<tr><td><a href="https://github.com/AmjadAAYD/sma-veille-technologique"><b>sma-veille-technologique</b></a><br>
<sub>LLM agents</sub></td>
<td>Three agents read AI publications overnight and write the summary</td>
<td>Daily report in under 2s, no human in the loop</td></tr>

<tr><td><a href="https://github.com/AmjadAAYD/spam-detection-nlp"><b>spam-detection-nlp</b></a><br>
<sub>NLP</sub></td>
<td>Sorts email into legitimate and spam, three approaches put head to head</td>
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

## The kit

<div align="center">

**Machine learning**

<img src="https://skillicons.dev/icons?i=python,pytorch,sklearn&theme=dark" />

**Data engineering and infrastructure**

<img src="https://skillicons.dev/icons?i=docker,postgres,mysql,mongodb,git,linux&theme=dark" />

**Also in the bag**

![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-337AB7?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=flat-square)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-C72E49?style=flat-square&logo=minio&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![PySide6](https://img.shields.io/badge/PySide6-41CD52?style=flat-square&logo=qt&logoColor=white)
![Bluetooth LE](https://img.shields.io/badge/Bluetooth_LE-0082FC?style=flat-square&logo=bluetooth&logoColor=white)

</div>

---

## The numbers

<div align="center">

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=AmjadAAYD&theme=tokyonight" width="94%" />

<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=AmjadAAYD&theme=tokyonight" />
<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=AmjadAAYD&theme=tokyonight" />

<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=AmjadAAYD&theme=tokyonight" />
<img height="180" src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=AmjadAAYD&theme=tokyonight&utcOffset=1" />

</div>

---

## The Bar

A baseline is a bar. Something already standing in the room, doing the job badly,
waiting to see whether you can clear it.

This field makes it easy to fool yourself. A model can look brilliant while it is only
repeating the last value it saw. An accuracy can look strong until you notice one class
is 90% of the data. A metric can climb while the thing you actually cared about goes
nowhere. The only defence is to stand something stupid next to your work and check that
you genuinely beat it.

So every repo here carries what it was measured against, and says where the method
breaks down. Not out of modesty. A number with nothing beside it isn't evidence, it's
just a claim.

<div align="center">

**Anyone can post a number. Show me what it beat.**

</div>

---

<div align="center">

<sub>Open an issue on any repo if you want to talk.</sub>

</div>
