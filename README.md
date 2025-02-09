🐵 Monkey Classification Project
📌 Overview

This project is a Python-based classification system designed to distinguish between different ape species based on various physical characteristics (e.g., weight, height, fur color). The project is structured into multiple scripts to ensure modularity, maintainability, and scalability.

It is part of a Python ecosystem exploration lab, emphasizing:
✅ Object-Oriented Programming (OOP)
✅ Functional Programming concepts
✅ Best practices for Python project development
✅ Test-Driven Development (TDD) & debugging techniques
🚀 Features

    Data Preprocessing: Handles missing labels (~25%) and malformed data (~1%).
    Machine Learning Model: Implements a classification algorithm for ape species.
    Visualization Tools: Generates plots to analyze data distributions.
    Testing & Debugging: Uses TDD principles with pytest and debugging with pdb.

📂 Project Structure

├── monkey_classif.py      # Main script for classification
├── monkey_visualize.py    # Visualization logic
├── monkey_model.py        # OOP logic for monkey representation
├── utils.py               # Utility functions
├── tests.py               # Test cases for the project
├── monkeys.csv            # Dataset (~3K records)
├── README.md              # Project documentation

🔧 Installation & Usage

1️⃣ Clone the repository:

git clone https://github.com/your-username/monkey-classification.git
cd monkey-classification

2️⃣ Install dependencies:

pip install -r requirements.txt

3️⃣ Run the classification script:

python monkey_classif.py

4️⃣ Run tests:

pytest tests.py

📊 Dataset

The dataset consists of 3,000 labeled records of three different monkey species. Some data points contain missing or malformed values, requiring preprocessing.
🎯 Goals

    Develop a fully functional Python project with modular scripts.
    Apply best coding practices for maintainable and scalable development.
    Gain experience with data science workflows, debugging, and testing methodologies.

🏗️ Future Improvements

    Implement more advanced ML models (e.g., Random Forest, Neural Networks).
    Enhance data cleaning and feature engineering.
    Improve visualizations for better interpretability.
