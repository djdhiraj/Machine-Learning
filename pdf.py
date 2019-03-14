from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
 
#----------------------------------------------------------------------
def colorFontsDemo(path):
    """
    Demo to show how to use fonts in Paragraphs
    """
    p_font = 12
    c = canvas.Canvas(path, pagesize=letter)
 
    ptext = """<font name=HELVETICA color=red size=%s>Welcome to Reportlab! (helvetica)</font>
    """ % p_font
    createParagraph(c, ptext, 20, 750)
 
    ptext = """<font name=courier color=blue size=%s>Welcome to Reportlab! (courier)</font>
    """ % p_font
    createParagraph(c, ptext, 20, 730)
 
    ptext = """<font name=times-roman color=green size=%s>Welcome to Reportlab! (times-roman)</font>
    """ % p_font
    createParagraph(c, ptext, 20, 710)
 
    c.save()
def createParagraph(c, text, x, y):
    """"""
    style = getSampleStyleSheet()
    width, height = letter
    p = Paragraph(text, style=style["Normal"])
    p.wrapOn(c, width, height)
    p.drawOn(c, x, y, mm)
 
if __name__ == "__main__":
    settingFontsDemo("/path/to/fontDemo.pdf")
