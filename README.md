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
@inproceedings{peechatt-etal-2024-multicollab-multimodal,
    title = "{Modality–Time Masking for \\Robust Multimodal Confusion Detection",
    author = "Peechatt, Michael  and
      Alm, Cecilia Ovesdotter  and
      Bailey, Reynold",
    editor = "",
    booktitle = "Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)",
    month = may,
    year = "2024",
    address = "Torino, Italy",
    publisher = "ELRA and ICCL",
    url = "https://aclanthology.org/2024.lrec-main.1023",
    pages = "11713--11722",
    abstract = "This paper addresses an existing resource gap for studying complex emotional states when a speaker collaborates with a partner to solve a task. We present a novel dialogue resource {---} the MULTICOLLAB corpus {---} where two interlocutors, an instructor and builder, communicated through a Zoom call while sensors recorded eye gaze, facial action units, and galvanic skin response, with transcribed speech signals, resulting in a unique, heavily multimodal corpus. The builder received instructions from the instructor. Half of the builders were privately told to disobey the instructor{'}s directions. After the task, participants watched the Zoom recording and annotated their instances of frustration. In this study, we introduce this new corpus and perform computational experiments with time series transformers, using early fusion through time for sensor data and late fusion for speech transcripts. We then average predictions from both methods to recognize instructor frustration. Using sensor and speech data in a 4.5 second time window, we find that the fusion of both models yields 21{\%} improvement in classification accuracy (with a precision of 79{\%} and F1 of 63{\%}) over a comparison baseline, demonstrating that complex emotions can be recognized when rich multimodal data from transcribed spoken dialogue and biophysical sensor data are fused.",
}
```

## Contact
For any questions about this dataset, please contact Michael Peechatt at [mp6510@rit.edu](mailto:mp6510@rit.edu).
