import matplotlib.pyplot as plt

def generate_graph(data, output_path, column_name):
    """Generates a graph from the provided data and saves it to output_path."""
    plt.figure(figsize=(10, 6))

    # Check if the specified column exists in the data
    if column_name in data.columns:
        plt.hist(data[column_name], bins=30, alpha=0.7, color='blue')
        plt.title(f'Histogram of {column_name.capitalize()}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
    else:
        print(f"Column '{column_name}' not found in data for visualization.")
        return

    plt.savefig(output_path)
    plt.close()

from fpdf import FPDF

def generate_pdf_paper(title, introduction, literature_review, methods, results, discussion, conclusion, references, graph_path):
    """Generates a PDF report from the provided sections."""
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='C')

    # Introduction
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Introduction: {introduction}")
    pdf.multi_cell(0, 10, f"Literature Review: {literature_review}")
    pdf.multi_cell(0, 10, f"Methods: {methods}")
    pdf.multi_cell(0, 10, f"Results: {results}")
    pdf.multi_cell(0, 10, f"Discussion: {discussion}")
    pdf.multi_cell(0, 10, f"Conclusion: {conclusion}")
    pdf.multi_cell(0, 10, f"References: {references}")

    # Add Graph
    pdf.image(graph_path, x=10, y=pdf.get_y(), w=180)
    pdf.output('/workspaces/epidemic-research-ai/reports/full_paper.pdf')
