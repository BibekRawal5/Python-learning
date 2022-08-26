import fpdf

pdf = fpdf.FPDF()
pdf.add_page()
pdf.image("shirtificate.png")
pdf.write(0, 0, "Hello World")
pdf.output("hello_world.pdf")