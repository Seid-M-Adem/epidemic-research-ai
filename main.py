from src.data_processing import load_data, preprocess_data
from src.data_imputation import impute_missing_data
from src.literature_review import generate_literature_review_with_urls
from src.report_generator import generate_pdf_paper, generate_word_paper

# Step 1: Load and preprocess data
data = load_data()
data = preprocess_data(data)

# Step 2: Impute missing data (if any)
columns_to_impute = ['confirmed_cases', 'deaths', 'recovered', 'vaccinated']
data_imputed = impute_missing_data(data, columns=columns_to_impute)

# Step 3: Generate literature review (from sample URLs in literature_fetcher)
generate_literature_review_with_urls()

# Step 4: Generate scientific report
title = "Epidemic Research: Real-World Data Analysis"
introduction = "This study explores the impact of a real-world epidemic across multiple countries."
methods = "Data was collected from a real-world-like dataset, missing values were imputed using the mean strategy."
results = f"Data Imputation Results: {data_imputed.describe()}"
discussion = "The results indicate trends in infection, death, and recovery rates across the studied countries."
conclusion = "Future research involves creating predictive models for epidemic outbreaks."
references = open('/workspaces/epidemic-research-ai/references/literature_input.txt').read()

# Generate reports
generate_pdf_paper(title, introduction, methods, results, discussion, conclusion, references)
generate_word_paper(title, introduction, methods, results, discussion, conclusion, references)
