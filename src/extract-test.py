import PyPDF2
import sys
import os

def extract_pdf_to_text(pdf_path, output_path=None):
    """
    Extract text content from a PDF file and save it to a text file.
    
    Args:
        pdf_path (str): Path to the input PDF file
        output_path (str): Path to the output text file (optional)
    """
    try:
        # If output path not specified, create one based on PDF filename
        if output_path is None:
            base_name = os.path.splitext(pdf_path)[0]
            output_path = f"{base_name}.txt"
        
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Get total number of pages
            num_pages = len(pdf_reader.pages)
            print(f"Processing {num_pages} pages...")
            
            # Extract text from all pages
            all_text = []
            for page_num in range(num_pages):
                # Get page object
                page = pdf_reader.pages[page_num]
                
                # Extract text from page
                text = page.extract_text()
                
                # Add page separator and text
                all_text.append(f"\n--- Page {page_num + 1} ---\n")
                all_text.append(text)
                
                print(f"Processed page {page_num + 1}/{num_pages}")
            
            # Join all text
            full_text = ''.join(all_text)
            
            # Save to text file
            with open(output_path, 'w', encoding='utf-8') as text_file:
                text_file.write(full_text)
            
            print(f"\n✅ PDF content successfully extracted to: {output_path}")
            print(f"Total characters extracted: {len(full_text)}")
            
    except FileNotFoundError:
        print(f"❌ Error: PDF file '{pdf_path}' not found.")
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")

def main():
    # You can modify these paths or pass them as command line arguments
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
    else:
        # Default paths - modify as needed
        pdf_path = "What is Redadair Group v2-221118-075411.pdf"
        output_path = "extracted_text.txt"  # Change this to desired output path
    
    extract_pdf_to_text(pdf_path, output_path)

if __name__ == "__main__":
    main()