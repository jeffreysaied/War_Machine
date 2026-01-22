#!/usr/bin/env python3
"""
Script to implement recommended improvements to the War Machine Excel file.

This script creates an optimized version of the Excel file with:
- Unused rows removed (space optimization)
- Duplicate entries removed
- Formula errors wrapped with IFERROR
- Freeze panes enabled
- Data validation added
- Conditional formatting for visual indicators
"""

import openpyxl
from openpyxl.styles import PatternFill, Font
from openpyxl.formatting.rule import CellIsRule
from openpyxl.worksheet.datavalidation import DataValidation
import sys
import os
from datetime import datetime


def backup_file(filename):
    """Create a backup of the original file."""
    backup_name = filename.replace('.xlsx', f'_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx')
    import shutil
    shutil.copy2(filename, backup_name)
    print(f"✓ Created backup: {backup_name}")
    return backup_name


def remove_unused_rows(ws, keep_buffer=20):
    """Remove unused rows, keeping a small buffer."""
    # Find the last row with data
    last_row = ws.max_row
    for row in range(ws.max_row, 0, -1):
        if any(cell.value is not None for cell in ws[row]):
            last_row = row
            break
    
    # Calculate rows to delete
    target_max_row = last_row + keep_buffer
    if ws.max_row > target_max_row:
        rows_to_delete = ws.max_row - target_max_row
        ws.delete_rows(target_max_row + 1, rows_to_delete)
        return rows_to_delete
    return 0


def remove_duplicates_in_attendance(ws):
    """Remove duplicate entries in the Attendance sheet."""
    if ws.title != "Attendance":
        return 0
    
    seen = set()
    rows_to_delete = []
    
    for row_idx in range(2, ws.max_row + 1):
        # Create a tuple of the row values
        row_values = tuple(cell.value for cell in ws[row_idx])
        if row_values in seen:
            rows_to_delete.append(row_idx)
        else:
            seen.add(row_values)
    
    # Delete in reverse order to maintain indices
    for row_idx in reversed(rows_to_delete):
        ws.delete_rows(row_idx, 1)
    
    return len(rows_to_delete)


def wrap_formulas_with_iferror(ws):
    """Wrap formulas with IFERROR to handle errors gracefully."""
    wrapped_count = 0
    
    for row in ws.iter_rows():
        for cell in row:
            if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                # Check if it's not already wrapped with IFERROR
                if not cell.value.upper().startswith('=IFERROR('):
                    # Get the original formula (without the =)
                    formula = cell.value[1:]
                    # Wrap it with IFERROR
                    cell.value = f'=IFERROR({formula}, "")'
                    wrapped_count += 1
    
    return wrapped_count


def add_freeze_panes(ws):
    """Add freeze panes to keep headers visible."""
    # Freeze the top 2 rows and first column
    ws.freeze_panes = 'B3'


def add_leadership_conditional_formatting(ws):
    """Add color coding for leadership levels."""
    if ws.title not in ["Leadership and comfort", "Players"]:
        return
    
    # Define color fills
    green_fill = PatternFill(start_color="90EE90", end_color="90EE90", fill_type="solid")
    yellow_fill = PatternFill(start_color="FFFF99", end_color="FFFF99", fill_type="solid")
    orange_fill = PatternFill(start_color="FFB366", end_color="FFB366", fill_type="solid")
    
    # Find leadership columns (typically columns with numbers 700-800)
    for col_idx in range(1, ws.max_column + 1):
        col_letter = openpyxl.utils.get_column_letter(col_idx)
        
        # Check if this column might contain leadership values
        has_leadership = False
        for row_idx in range(2, min(10, ws.max_row)):
            cell_value = ws.cell(row=row_idx, column=col_idx).value
            if isinstance(cell_value, (int, float)) and 700 <= cell_value <= 800:
                has_leadership = True
                break
        
        if has_leadership:
            # Add conditional formatting for this column
            range_str = f"{col_letter}2:{col_letter}{ws.max_row}"
            
            # Green for 780+
            ws.conditional_formatting.add(range_str, 
                CellIsRule(operator='greaterThanOrEqual', formula=['780'], 
                          fill=green_fill))
            
            # Orange for 760-779
            ws.conditional_formatting.add(range_str,
                CellIsRule(operator='between', formula=['760', '779'],
                          fill=orange_fill))
            
            # Yellow for 750-759
            ws.conditional_formatting.add(range_str,
                CellIsRule(operator='between', formula=['750', '759'],
                          fill=yellow_fill))


def add_data_validation(wb):
    """Add data validation for player names across sheets."""
    # Get player names from Players sheet
    if "Players" not in wb.sheetnames:
        return
    
    players_ws = wb["Players"]
    
    # Create a named range for players (assuming column A)
    player_range = f"Players!$A$2:$A${players_ws.max_row}"
    
    # Create data validation
    dv = DataValidation(type="list", formula1=player_range, allow_blank=True)
    dv.error = 'Please select a valid player name'
    dv.errorTitle = 'Invalid Entry'
    
    # Apply to relevant sheets
    target_sheets = ["Leadership and comfort", "Barracks", "Favorite Units", "Unit Sheet", "ExtraSheet"]
    
    for sheet_name in target_sheets:
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            # Apply to column A (player names) for a reasonable range
            ws.add_data_validation(dv)
            dv.add(f"A2:A{min(100, ws.max_row)}")


def optimize_excel_file(input_file, output_file=None):
    """
    Apply all optimizations to the Excel file.
    
    Args:
        input_file: Path to input Excel file
        output_file: Path to output file (if None, creates _optimized version)
    """
    if output_file is None:
        output_file = input_file.replace('.xlsx', '_optimized.xlsx')
    
    print(f"Loading workbook: {input_file}")
    wb = openpyxl.load_workbook(input_file)
    
    print("\nApplying optimizations...")
    print("=" * 60)
    
    total_rows_deleted = 0
    total_formulas_wrapped = 0
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        print(f"\n📊 Processing: {sheet_name}")
        
        # 1. Remove unused rows
        rows_deleted = remove_unused_rows(ws)
        if rows_deleted > 0:
            print(f"  ✓ Removed {rows_deleted} unused rows")
            total_rows_deleted += rows_deleted
        
        # 2. Remove duplicates (Attendance only)
        if sheet_name == "Attendance":
            dupes_removed = remove_duplicates_in_attendance(ws)
            if dupes_removed > 0:
                print(f"  ✓ Removed {dupes_removed} duplicate entries")
        
        # 3. Wrap formulas with IFERROR
        wrapped = wrap_formulas_with_iferror(ws)
        if wrapped > 0:
            print(f"  ✓ Wrapped {wrapped} formulas with IFERROR")
            total_formulas_wrapped += wrapped
        
        # 4. Add freeze panes
        add_freeze_panes(ws)
        print(f"  ✓ Added freeze panes")
        
        # 5. Add conditional formatting for leadership
        if sheet_name in ["Leadership and comfort", "Players"]:
            add_leadership_conditional_formatting(ws)
            print(f"  ✓ Added leadership color coding")
    
    # 6. Add data validation across sheets
    print(f"\n📋 Adding data validation for player names...")
    add_data_validation(wb)
    print(f"  ✓ Data validation added")
    
    # Save the optimized file
    print(f"\n💾 Saving optimized file: {output_file}")
    wb.save(output_file)
    wb.close()
    
    print("\n" + "=" * 60)
    print("OPTIMIZATION COMPLETE!")
    print("=" * 60)
    print(f"\nSummary:")
    print(f"  • Total rows removed: {total_rows_deleted}")
    print(f"  • Formulas wrapped with IFERROR: {total_formulas_wrapped}")
    print(f"  • Freeze panes added to all sheets")
    print(f"  • Leadership color coding added")
    print(f"  • Data validation configured")
    print(f"\n✓ Optimized file: {output_file}")
    
    # Calculate file size reduction
    if os.path.exists(input_file) and os.path.exists(output_file):
        original_size = os.path.getsize(input_file)
        new_size = os.path.getsize(output_file)
        reduction = (original_size - new_size) / original_size * 100
        print(f"  File size: {original_size:,} → {new_size:,} bytes ({reduction:.1f}% reduction)")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Optimize the War Machine Excel file with recommended improvements.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python optimize_excel.py                           # Optimize War Machine.xlsx
  python optimize_excel.py --input custom.xlsx       # Optimize custom file
  python optimize_excel.py --output optimized.xlsx   # Specify output name
  python optimize_excel.py --backup                  # Create backup first
        """
    )
    
    parser.add_argument(
        '--input', '-i',
        default='War Machine.xlsx',
        help='Input Excel file (default: War Machine.xlsx)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output Excel file (default: <input>_optimized.xlsx)'
    )
    
    parser.add_argument(
        '--backup', '-b',
        action='store_true',
        help='Create a backup of the original file first'
    )
    
    parser.add_argument(
        '--in-place',
        action='store_true',
        help='Modify the file in-place (overwrites original)'
    )
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"❌ Error: File '{args.input}' not found.")
        return 1
    
    # Create backup if requested
    if args.backup:
        backup_file(args.input)
    
    # Determine output file
    if args.in_place:
        output = args.input
        if not args.backup:
            print("⚠️  Warning: Modifying file in-place without backup!")
            response = input("Continue? (yes/no): ")
            if response.lower() != 'yes':
                print("Cancelled.")
                return 0
    else:
        output = args.output
    
    # Run optimization
    try:
        optimize_excel_file(args.input, output)
        return 0
    except Exception as e:
        print(f"❌ Error during optimization: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
