import os
from src.data_processing import load_data, preprocess_data
from src.report_generator import generate_pdf_paper, generate_graph

def main():
    # Step 1: Load Data
    raw_data_path = 'data/raw/your_raw_data.csv'  # Update with your actual file path
    if not os.path.exists(raw_data_path):
        print(f"Error: Data file {raw_data_path} does not exist.")
        return

    # Load the data
    data = load_data(raw_data_path)

    # Step 2: Preprocess Data
    processed_data = preprocess_data(data)

    # Print columns of processed data
    print("Columns in the processed data:")
    print(processed_data.columns.tolist())

    # Step 3: Generate Graphs
    graph_path = 'reports/sample_graph.png'
    column_to_visualize = 'cases'  # Change this to the actual column you want to visualize
    generate_graph(processed_data, graph_path, column_to_visualize)

    # Step 4: Prepare Content for the Report
    title = "Epidemic Research AI"
    introduction = "This paper discusses the impacts of epidemics on society and various factors affecting the spread of diseases."
    literature_review = "Previous studies show that understanding the spread of diseases is crucial for public health."
    methods = "Data was collected from various public health sources and analyzed using statistical methods."
    results = "The results indicate a significant correlation between public health measures and the rate of infection."
    discussion = "These results suggest that timely interventions can effectively control the spread of diseases."
    conclusion = "In conclusion, this study highlights the importance of data-driven approaches in epidemic management."
    references = "Author A et al. (Year), Author B et al. (Year)..."

    # Step 5: Generate PDF Report
    generate_pdf_paper(title, introduction, literature_review, methods, results, discussion, conclusion, references, graph_path)

if __name__ == "__main__":
    main()
