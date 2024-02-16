from fpdf import FPDF
import qrcode

class PDF(FPDF):
    def header(self):
        # Adding QR code and poster images to the header
        self.image("qr.png", 3, 10, 66)
        self.image("poster.jpg", 70, 0, 140)
        
        # Setting up font and displaying event details
        self.set_y(70)
        self.set_font('helvetica', "", 12)
        self.multi_cell(0, 10, "Harry Porter", ln=True)
        self.set_font('helvetica', "B", 14)
        self.multi_cell(0, 10, "yf75cc32nf77", ln=True)
        self.ln(4)
        self.set_font('helvetica', "B", 18)
        self.multi_cell(50, 7, f"The Philosopher's Stone\nVol. 02", ln=True)
        self.ln(4)
        
        # Additional event details
        self.set_font('helvetica', "", 10)
        self.set_text_color(80, 80, 80)
        self.multi_cell(50, 5, "This ticket admits one person. Minimum age of 21 years.", ln=True)
        self.ln(6)
        self.set_font('helvetica', "", 9)
        self.set_text_color(80, 80, 80)
        
        # Displaying event start, end, location, and address
        self.cell(10, 5, "Start:")
        self.set_x(30)
        self.cell(10, 5, "10-11-2001 at 18:00", ln=True)
        self.cell(10, 5, "End:")
        self.set_x(30)
        self.cell(10, 5, "10-11-2001 at 19:30", ln=True)
        self.cell(10, 5, "Location:")
        self.set_x(30)
        self.cell(10, 5, "United Kingdom", ln=True)
        self.cell(10, 5, "Address:")
        self.set_x(30)
        self.cell(10, 5, "Hogwarts School of Witchcraft and Wizardry", ln=True)
        self.ln(10)
        
        # Additional information about the event
        self.set_font('helvetica', "", 9)
        self.set_text_color(180, 180, 180)
        self.multi_cell(50, 5, "Your ID and ticket will be checked at the door.", ln=True)
        self.multi_cell(50, 5, "If your energy or ticket is not correct entrance will be denied.", ln=True)
        self.multi_cell(50, 5, "No ticket refunds, entrance on own risk.")

    def footer(self):
        # Adding disclaimer text from an external file and displaying page number
        self.set_y(-45)
        self.set_font("helvetica", "", 5)
        self.set_text_color(80, 80, 80)
        with open("disclaimer.txt", "r") as file:
            disclaimer_text = file.read()
        self.multi_cell(0, 5, disclaimer_text, ln=True)
        self.set_font("helvetica", "", 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

# Creating PDF instance, setting properties, and generating the PDF
pdf = PDF("P", "mm", "A4")
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.output("ticket.pdf")
