from fpdf import FPDF

name = input("Student name: ").capitalize()
pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', 'B', 40)
pdf.set_y(20)
pdf.cell(0, txt='CS50 Shirtificate', align="C")
pdf.set_y(0)
pdf.image("shirtificate.png", x="C", y=70, w=pdf.epw)
pdf.set_text_color(200, 198, 140)
pdf.set_font_size(30)
pdf.cell(0, 300, txt=f"{name} took CS50", align="C")
pdf.output("shirtificate.pdf")
