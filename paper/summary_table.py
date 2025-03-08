import os
import pandas as pd
import argparse
from openpyxl import load_workbook
from openpyxl.styles import Alignment

def extract_info_from_md(md_content):
    """Extracts relevant information from a Markdown file using markdown parsing."""
    md_lines = md_content.split('\n')
    sections = {}
    metadata = {}
    current_section = None
    in_metadata = False
    
    for line in md_lines:
        line = line.strip()
        if line.startswith("!["):
            continue
        
        if line == "---":
            in_metadata = not in_metadata
            continue
        
        if in_metadata:
            if ":" in line:
                key, value = line.split(":", 1)
                metadata[key.strip()] = value.strip().replace("\'", "").replace('\"', "")
        elif line.startswith('# '):
            current_section = line[2:].strip()
            sections[current_section] = ""
        elif current_section:
            sections[current_section] += line.replace("  ", "\t") + "\n"
    
    print(metadata)
    # return dict(title=metadata["title"]).update({
    return {
        key: sections.get(key, metadata.get(key, "Unknown")
        ) for key in sections.keys()
    }

def decorate_excel(df, output_file):
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        
        # 각 열 너비를 100px로 설정
        for col in worksheet.columns:
            worksheet.column_dimensions[
                col[0].column_letter
            ].width = 20

        # 셀 텍스트 자동 줄 바꿈 설정
        for c in (c for row in worksheet.iter_rows() for c in row):
            c.alignment = Alignment(wrap_text=True)
    return df

def process_markdown_files(directories, output_file):
    def _file_generator():
        for path in (
            os.path.join(d, f)
            for d in directories 
            for f in os.listdir(d) 
            if f.endswith(".md")
        ):
            yield path
    
    records = []
    for filepath in _file_generator():
        with open(filepath, "r", encoding="utf-8") as file:
            records.append(extract_info_from_md(file.read()))
    
    df = decorate_excel(pd.DataFrame(records), output_file)
    print(f"Excel file saved as {output_file} - {len(df)} records processed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown files to an Excel table.")
    parser.add_argument("-d", "--directories", nargs='+', type=str,
     help="Paths to directories containing Markdown files.")
    parser.add_argument("-o", "--output", type=str, default="output.xlsx", help="Path to save the output Excel file.")
    args = parser.parse_args()
    
    process_markdown_files(args.directories, args.output)
