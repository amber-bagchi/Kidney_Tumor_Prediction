# 🩺 Kidney Tumor Prediction

## Overview
Welcome to the Kidney Tumor Prediction project! 🎉 This project focuses on predicting kidney tumors using machine learning and deep learning techniques. The goal is to effectively classify kidney images or related data to identify the presence of tumors.

## Workflows
- ### 🛠️ Update Configuration:

  - Update config.yaml with the necessary parameters for your model training and evaluation.

  - Update params.yaml for model hyperparameters and training settings.

- ### 🔍 Entity Management:

  - Update the entities as needed for your project structure.
  
- ### 🔧 Configuration Management:

  - Update the configuration manager in src/config.
  
- ### ⚙️ Component Updates:

  - Modify the components in the project based on your data and model needs.
  
- ### 🔄 Pipeline Updates:

  - Update the data processing and training pipeline according to your requirements.

- ### 📜 Main Script:

  - Modify main.py for the entry point of your application.
  
- ### 📊 DVC Configuration:

  - Update dvc.yaml to track data and model versions using DVC (Data Version Control).
  
- ### 🖥️ App Script:

  - Modify app.py to define how the model interacts with users and processes input data.
  
## How to Run?

### 🚀 STEPS:

#### Clone the Repository:
```bash
git clone https://github.com/amber-bagchi/Kidney-Tumor-Prediction.git
```
```bash
cd Kidney-Tumor-Prediction
```
#### 🌱 Create a Conda Environment: After opening the repository, create a conda environment:
```bash
conda create -n kidney_tumor python=3.8 -y
```
```bash
conda activate kidney_tumor
```
#### 📦 Install the Requirements: Install the necessary packages:
```bash
pip install -r requirements.txt
```

#### 🔄 Run DVC: Run DVC to reproduce the pipeline and ensure all data and models are up to date:
```bash
dvc repro
```

#### 🚀 Run the Application: Finally, run the following command:
```bash
python app.py
```

#### 🌐 Open Your Local Host:
```bash
http://localhost:8080 # Visit in your browser to view the application.
```
## About MLflow & DVC
### 🧪 MLflow
- Production Grade: MLflow helps you manage the machine learning lifecycle, including experimentation, reproducibility, and deployment.
- 📈 Experiment Tracking: Track and log your experiments, models, and results effectively.
  
### 📦 DVC
- Lightweight Experiment Tracker: DVC is designed for lightweight tracking of machine learning experiments.
- 🔗 Pipeline Orchestration: DVC can help you create and manage reproducible data pipelines.
  
