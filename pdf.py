import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io

st.set_page_config(page_title="PDF Viewer", page_icon="📄", layout="wide")
st.title("📄 PDF Viewer")

pdf_path = "/Users/rakhamugathishaik/MSR-Coder/Cook/SatvikCookPDF/Satvic_food_book_1.pdf"
pdf_document = fitz.open(pdf_path)

for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    pix = page.get_pixmap()
    img_data = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_data))
    st.image(img, caption=f"Page {page_num + 1}", use_container_width=True)

pdf_document.close()
