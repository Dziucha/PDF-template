from fpdf import FPDF
import pandas

topics = pandas.read_csv("topics-2.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in topics.iterrows():
    number_of_pages = int(row["Pages"])

    for i in range(number_of_pages):
        pdf.add_page()
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=0, h=12, txt=f"{row['Topic']} page {i+1}", align="L", ln=1)

pdf.output("output.pdf")
