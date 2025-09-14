import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import io

st.set_page_config(page_title="PDF Viewer", page_icon="📄", layout="wide")
st.title("📄 PDF Viewer")

pdf_path = "Satvic_food_book_1.pdf"
pdf_document = fitz.open(pdf_path)

for page_num in range(len(pdf_document)):
    page = pdf_document.load_page(page_num)
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Higher resolution
    img_data = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_data))
    
    # Split page if width > height (landscape/double page)
    if img.width > img.height:
        mid = img.width // 2
        left_page = img.crop((0, 0, mid, img.height))
        right_page = img.crop((mid, 0, img.width, img.height))
        
        st.image(left_page, caption=f"Page {page_num + 1}a", use_container_width=True)
        st.image(right_page, caption=f"Page {page_num + 1}b", use_container_width=True)
    else:
        st.image(img, caption=f"Page {page_num + 1}", use_container_width=True)

pdf_document.close()

# import streamlit as st
# import fitz  # PyMuPDF
# from PIL import Image
# import io

# st.set_page_config(page_title="PDF Viewer", page_icon="📄", layout="wide")
# st.title("📄 PDF Viewer")

# pdf_path = "Satvic_food_book_1.pdf"
# pdf_document = fitz.open(pdf_path)

# for page_num in range(len(pdf_document)):
#     page = pdf_document.load_page(page_num)
#     pix = page.get_pixmap()
#     img_data = pix.tobytes("png")
#     img = Image.open(io.BytesIO(img_data))
#     st.image(img, caption=f"Page {page_num + 1}", use_container_width=True)

# pdf_document.close()
