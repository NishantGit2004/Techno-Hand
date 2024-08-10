from fpdf import FPDF
import os

def generate_pdf(form_data):
    pdf = FPDF()
    pdf.set_font("Arial", size=12)

    # Title and Header on the first page
    pdf.add_page()
    pdf.cell(200, 10, txt="Inspection Form Data", ln=True, align="C")
    
    # Handle Header Section first
    if "Header Section" in form_data:
        pdf.ln(10)  # Add some space after the title
        pdf.cell(200, 10, txt="Header Section", ln=True, align="L")
        pdf.ln(10)
        for key, value in form_data.items():
            if "Header Section" in key:
                pdf.multi_cell(0, 10, txt=f"{key}: {value}", align="L")
    
    # Handle other sections on subsequent pages
    sections = ["Tire Section", "Battery Section"]
    
    for section in sections:
        if section in form_data:
            pdf.add_page()  # Start a new page for each section
            pdf.cell(200, 10, txt=section.replace(" Section", ""), ln=True, align="L")
            pdf.ln(10)  # Add some space between the title and the content
            
            # Print all key-value pairs related to this section on the same page
            for key, value in form_data.items():
                if section in key:
                    pdf.multi_cell(0, 10, txt=f"{key}: {value}", align="L")

    # Handle any additional data not categorized under a section
    for key, value in form_data.items():
        if not any(section in key for section in sections + ["Header Section"]):
            pdf.add_page()
            pdf.cell(200, 10, txt=f"{key}", ln=True, align="L")
            pdf.multi_cell(0, 10, txt=f"{value}", align="L")

    pdf_file_name = f"Inspection_Form_{form_data['Inspection ID']}.pdf"
    pdf.output(pdf_file_name)

    print(f"\nForm Data Collected and saved to {pdf_file_name}")
    os.startfile(pdf_file_name)
