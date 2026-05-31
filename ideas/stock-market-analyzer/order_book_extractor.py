import camelot  # pip install camelot-py[cv]
import os

def extract_order_book_from_pdf(pdf_path):
    tables = camelot.read_pdf(pdf_path, pages='1-end')
    for table in tables:
        df = table.df
        for row in df.values:
            if any('order' in str(cell).lower() and 'book' in str(cell).lower() for cell in row):
                print(f"Order book data found in {pdf_path}:")
                print(df)
                df.to_csv(f"orderbook_{os.path.basename(pdf_path)}.csv", index=False)

if __name__ == "__main__":
    pdf_folder = "annual_reports"
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            extract_order_book_from_pdf(os.path.join(pdf_folder, filename))
