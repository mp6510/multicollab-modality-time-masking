# Supplementary Materials for ACII 2026

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

2. The program should run, showcasing each test configuration it is evaluating (t_w: Time Window, t_s: Time Steps, d_s: Dropping Strategy), periodically outputting the best model results for each dropping strategy.

3. The program will end with the last messages:
```
GENERATING FINAL ACII 2026 RESULTS...
Finished generating results. Please inspect ACII_avg_results.tsv and compare with paper submission.
```

4. Please examine the output results (both the averages and each individual configuration) as well as our implementation, and happy reviewing!

---
