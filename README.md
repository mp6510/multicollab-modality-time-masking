# Supplementary Materials for Peechatt et al. (ACII 2026)

---

## 📂 File Structure

```
├── confusion_data/  
│   ├── X_4500milli_40dim_0strat_confusion.tsv
│   ├── X_4500milli_40dim_1strat_confusion.tsv
│   ├── X_4500milli_40dim_2strat_confusion.tsv
│   ├── X_4500milli_40dim_3strat_confusion.tsv
│   ├── X_4500milli_40dim_4strat_confusion.tsv
│   ├── Y_4500milli_40dim_0strat_confusion.tsv
│   ├── Y_4500milli_40dim_1strat_confusion.tsv
│   ├── Y_4500milli_40dim_2strat_confusion.tsv
│   ├── Y_4500milli_40dim_3strat_confusion.tsv
│   ├── Y_4500milli_40dim_4strat_confusion.tsv
│   ├── Y_4500milli_embedding.tsv
├── models/  
│   ├── empty  
├── results/  
│   ├── empty 
├── mask_freezing_1DCNN.py
├── test_runner.py
├── test_models.py
├── test_results_analysis.py
├── requirements.txt  
└── README.md ← you’re here
```

---

## 1. Overview

To maximize reproducibility experiments will be run on the CPU rather than Apple Metal/GPU. **The approximate runtime of this program is 5 minutes**. It will generate 3000 .pth model configurations and then generate the test results shown in the paper. Models will be saved in the models directory, and it will ***require approximatly 1.5 GB of storage space***. This can be deleted after verifying our results.

---

## 2. Environment Setup

We target **Python 3.11** on Linux/macOS/Windows. It’s best to use a virtual environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate      # on Windows: .venv\Scripts\activate
pip install --upgrade pip
```

---

## 3. Dependencies

All required packages are listed in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt
```

---

## 4. Running Experiments

1. After installing required dependencies, run the following command:
```bash
python test_runner.py
```

2. The program should run, showcasing each test configuration it is evaluating (t_w: Time Window, t_s: Time Steps, d_s: Masking Strategy), periodically outputting the best model results for each masking strategy.

3. The program will end with the last messages:
```
Finished generating results.
```
---

## Disclaimer and License
This dataset is licensed under the <a href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">Creative Commons Attribution-NonCommercial 4.0 International License (CC-BY-NC-4.0)</a> and subject to [DISCLAIMER](DISCLAIMER.txt). 

## BibTeX Citation
```
@inproceedings{peechatt-etal-2026-modality-time-masking,
    title = "{Modality–Time Masking for Robust Multimodal Confusion Detection",
    author = "Peechatt, Michael  and
      Alm, Cecilia O. and
      Bailey, Reynold",
    booktitle = "Proceedings of ACII 2026",
    year = "2026"
}
```

## Contact
For any questions about this dataset, please contact Michael Peechatt at [mp6510@rit.edu](mailto:mp6510@rit.edu).
