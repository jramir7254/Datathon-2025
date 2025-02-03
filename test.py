from fpdf import FPDF

def clean_text(text):
    """Fix encoding issues by replacing smart quotes, dashes, and other special characters."""
    return (text.replace("’", "'")  # Convert smart single quotes
                .replace("“", "\"").replace("”", "\"")  # Convert double smart quotes
                .replace("–", "-").replace("•", "-")  # Replace dashes and bullet points
                .replace("…", "..."))  # Replace ellipses

def generate_pdf(output_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)

    # Title
    pdf.cell(200, 10, "Datathon 2025 - Deliverables Overview", ln=True, align="C")
    pdf.ln(10)

    # Section: Overview
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Overview", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, clean_text(
        "Participants will submit a comprehensive analysis of their findings, structured into key deliverables. "
        "These include predictive model outputs, feature importance analysis, and visualizations that support "
        "their conclusions. The deliverables should clearly communicate how weather conditions impact emissions, "
        "backed by data-driven insights."
    ))
    pdf.ln(5)

    # Section: Predictive Model Output
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Predictive Model Output", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, clean_text(
        "Participants will use a predictive model to estimate emissions levels based on weather conditions. "
        "The model’s performance should be evaluated using appropriate accuracy metrics. The goal is to "
        "demonstrate the ability to make reasonable forecasts and assess model reliability."
    ))
    pdf.ln(2)

    pdf.set_font("Arial", style="I", size=10)
    pdf.cell(0, 6, "Key Points:", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, clean_text(
        "1. Training and validating the model using historical data.\n"
        "2. Making predictions for future emissions levels based on available weather conditions.\n"
        "3. Evaluating the accuracy of predictions using appropriate performance metrics.\n"
        "4. Comparing predicted emissions with real values to assess effectiveness.\n"
        "5. Discussing challenges and potential improvements to the model."
    ))
    pdf.ln(5)

    # Section: Feature Importance Analysis
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Feature Importance Analysis", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, clean_text(
        "This section highlights which weather and operational parameters most influence emissions. "
        "Understanding these relationships helps determine which factors contribute most to pollution levels "
        "and can inform decision-making in emissions management."
    ))
    pdf.ln(2)

    pdf.set_font("Arial", style="I", size=10)
    pdf.cell(0, 6, "Key Points:", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, clean_text(
        "1. Identifying which variables have the strongest impact on emissions levels.\n"
        "2. Using statistical methods or model-based techniques to determine feature importance.\n"
        "3. Explaining why certain variables matter more than others in influencing emissions.\n"
        "4. Discussing real-world implications of identified key features.\n"
        "5. Suggesting additional factors that could improve analysis in future research."
    ))
    pdf.ln(5)

    # Section: Visualization
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Visualization", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, clean_text(
        "Participants should create visualizations to effectively communicate their findings. "
        "Graphs, charts, and other data visualizations should highlight key trends, relationships, "
        "and insights from the analysis."
    ))
    pdf.ln(2)

    pdf.set_font("Arial", style="I", size=10)
    pdf.cell(0, 6, "Key Points:", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 6, clean_text(
        "1. Creating scatter plots to show relationships between weather and emissions variables.\n"
        "2. Using correlation heatmaps to identify key trends and dependencies.\n"
        "3. Presenting time-series graphs to illustrate emissions changes over time.\n"
        "4. Highlighting feature importance using bar charts or ranking tables.\n"
        "5. Ensuring clarity in visualizations with proper labels, legends, and concise explanations."
    ))
    pdf.ln(5)

    # Save the PDF
    pdf.output(output_path)

# Example usage
output_pdf_path = "Datathon_2025_Deliverables.pdf"
generate_pdf(output_pdf_path)
print(f"PDF successfully generated: {output_pdf_path}")
