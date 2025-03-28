# Data Wrangling & Insights Project

This project demonstrates data wrangling and insights generation using the Titanic dataset. The project covers:

- **Data Loading:** Importing and inspecting the dataset.
- **Data Cleaning:** Handling missing values by filling or dropping them.
- **Feature Engineering:** Creating new features like `FamilySize`, `IsAlone`, and converting categorical variables.
- **Insights Generation:** Analyzing survival rates based on gender, family size, and passenger class.
- **Visualization:** Displaying a bar chart for survival rate by passenger class.

## Getting Started

### Prerequisites
- Python 3.x
- Libraries: Pandas, NumPy, Matplotlib

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <YOUR_REPOSITORY_URL>
   cd data_wrangling_project
2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv data-wrangling-env
    source data-wrangling-env/bin/activate
3. **install dependencies:**
    ```bash
    pip install pandas numpy matplotlib
4. **Download the Titanic dataset:**
    ```bash
    wget https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv -O titanic.csv
5. **Run the script:**
    ```bash
    data_wrangling_project/
    ├── data_wrangling.py
    ├── titanic.csv
    └── README.md
## Insights
    - Survival by Gender:

        - Male survival rate: ~18.9%

        - Female survival rate: ~74.2%

    - Survival by Family Size (IsAlone):

        - Passengers not alone (IsAlone=0): ~50.6%     survival

        - Passengers alone (IsAlone=1): ~30.4% survival

    - Survival by Passenger Class:

        - Class 1: ~62.96% survival

        - Class 2: ~47.28% survival

        - Class 3: ~24.24% survival

A bar chart visualizes the survival rate by passenger class.
