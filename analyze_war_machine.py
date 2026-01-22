#!/usr/bin/env python3
"""
Script to analyze and provide a comprehensive summary of the War Machine Excel file.

Features:
- View all sheets or specific sheets
- See dimensions, columns, and sample data
- Identify empty vs populated sheets
- Quick stats on data volume
"""

import openpyxl
import sys
import argparse
from collections import defaultdict


def analyze_war_machine(filename="War Machine.xlsx", sheets=None, verbose=False):
    """
    Analyze the War Machine Excel file and provide a comprehensive summary.
    
    Args:
        filename (str): Path to the Excel file
        sheets (list): List of specific sheet names to analyze (None = all sheets)
        verbose (bool): Show more detailed output including all columns
    """
    
    try:
        workbook = openpyxl.load_workbook(filename)
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return False
    except Exception as e:
        print(f"❌ Error opening file: {e}")
        return False
    
    print("=" * 80)
    print("WAR MACHINE EXCEL FILE - COMPREHENSIVE ANALYSIS")
    print("=" * 80)
    print(f"\nFile: {filename}")
    print(f"Total Sheets: {len(workbook.sheetnames)}")
    
    # Filter sheets if specified
    sheets_to_analyze = sheets if sheets else workbook.sheetnames
    if sheets:
        print(f"Analyzing Sheets: {', '.join(sheets_to_analyze)}")
    else:
        print(f"All Sheets: {', '.join(workbook.sheetnames)}")
    print("\n" + "=" * 80)
    
    # Analyze each sheet
    for sheet_name in sheets_to_analyze:
        if sheet_name not in workbook.sheetnames:
            print(f"\n⚠️  Sheet '{sheet_name}' not found in workbook. Skipping...")
            continue
            
        worksheet = workbook[sheet_name]
        print(f"\n📊 SHEET: {sheet_name}")
        print("-" * 80)
        
        # Get all rows
        rows = list(worksheet.iter_rows(values_only=True))
        
        if not rows:
            print("  ⚠️  Empty sheet")
            continue
        
        # Find actual data (non-empty rows)
        non_empty_rows = [row for row in rows if any(cell is not None for cell in row)]
        
        print(f"  Dimensions: {worksheet.dimensions}")
        print(f"  Total Rows: {len(rows)}")
        print(f"  Non-Empty Rows: {len(non_empty_rows)}")
        
        if non_empty_rows:
            # Show header row
            header = non_empty_rows[0] if non_empty_rows else None
            if header:
                non_empty_cols = [c for c in header if c]
                print(f"\n  📋 COLUMNS ({len(non_empty_cols)}):")
                
                # Show all columns if verbose, otherwise limit to first 15
                cols_to_show = non_empty_cols if verbose else non_empty_cols[:15]
                for i, col in enumerate(cols_to_show, 1):
                    print(f"    {i}. {col}")
                
                if not verbose and len(non_empty_cols) > 15:
                    print(f"    ... and {len(non_empty_cols) - 15} more columns (use --verbose to see all)")
            
            # Show first few data rows (skip header)
            if len(non_empty_rows) > 1:
                rows_to_show = 5 if verbose else 3
                print(f"\n  📝 SAMPLE DATA (first {rows_to_show} rows):")
                for i, row in enumerate(non_empty_rows[1:rows_to_show+1], 1):
                    # Only show non-None values
                    data = [str(cell)[:30] if cell is not None else '' for cell in row]
                    non_empty_data = [(idx, val) for idx, val in enumerate(data) if val]
                    if non_empty_data:
                        print(f"    Row {i}:")
                        cols_to_display = non_empty_data[:10] if not verbose else non_empty_data[:20]
                        for idx, val in cols_to_display:
                            if header and idx < len(header) and header[idx]:
                                print(f"      {header[idx]}: {val}")
        
        print("-" * 80)
    
    workbook.close()
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)
    return True


def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description='Analyze the War Machine Excel file structure and contents.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python analyze_war_machine.py                    # Analyze all sheets
  python analyze_war_machine.py --verbose          # Show more detail
  python analyze_war_machine.py --sheets "Players" "Cost"  # Specific sheets only
  python analyze_war_machine.py --file "custom.xlsx"       # Different file
        """
    )
    
    parser.add_argument(
        '--file', '-f',
        default='War Machine.xlsx',
        help='Path to Excel file (default: War Machine.xlsx)'
    )
    
    parser.add_argument(
        '--sheets', '-s',
        nargs='+',
        help='Specific sheet names to analyze (default: all sheets)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show more detailed output including all columns'
    )
    
    parser.add_argument(
        '--list-sheets', '-l',
        action='store_true',
        help='Just list available sheet names and exit'
    )
    
    args = parser.parse_args()
    
    # List sheets mode
    if args.list_sheets:
        try:
            workbook = openpyxl.load_workbook(args.file)
            print(f"Sheets in '{args.file}':")
            for i, sheet_name in enumerate(workbook.sheetnames, 1):
                print(f"  {i}. {sheet_name}")
            workbook.close()
            return 0
        except Exception as e:
            print(f"❌ Error: {e}")
            return 1
    
    # Run analysis
    success = analyze_war_machine(
        filename=args.file,
        sheets=args.sheets,
        verbose=args.verbose
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
