from fpdf import FPDF
import pandas as pd

topics = pd.read_csv("topics-2.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in topics.iterrows():
    number_of_pages = int(row["Pages"])

    for i in range(number_of_pages):
        pdf.add_page()
        pdf.set_text_color(100, 100, 100)
        pdf.set_font(family="Times", size=24, style="B")
        if i == 0:
            pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align="L", ln=1)
            pdf.ln(265)
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)
        else:
            pdf.ln(277)
            for y in range(10, 298, 10):
                pdf.line(10, y, 200, y)
        pdf.set_text_color(180, 180, 180)
        pdf.set_font(family="Times", size=8, style="I")
        pdf.cell(w=0, h=12, txt=f"{row['Topic']} page {i+1}", align="R", ln=1)

pdf.output("output.pdf")
