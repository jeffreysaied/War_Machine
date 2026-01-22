# War Machine

This repository contains tools to read, analyze, and understand the War Machine Excel file - a comprehensive guild management system for Conqueror's Blade tracking 50+ players, battle planning, and resource management.

## 📋 Quick Links

- **[WAR_MACHINE_UNDERSTANDING.md](WAR_MACHINE_UNDERSTANDING.md)** - Detailed documentation of all 9 sheets and their purposes
- **[EXCEL_IMPROVEMENT_RECOMMENDATIONS.md](EXCEL_IMPROVEMENT_RECOMMENDATIONS.md)** - Recommendations for improving the Excel file
- **War Machine.xlsx** - The master Excel file (9 sheets)

## 🔧 Requirements

- Python 3.6 or higher
- openpyxl library

## 📦 Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### View Raw Excel Data
To read and display all contents of the War Machine Excel file:

```bash
python read_excel.py
```

Or specify a different Excel file:

```bash
python read_excel.py "path/to/your/file.xlsx"
```

### Analyze Excel Structure
To get a structured analysis showing sheet dimensions, columns, and sample data:

```bash
python analyze_war_machine.py
```

This provides:
- Sheet names and dimensions
- Column headers for each sheet
- Sample data from first few rows
- Non-empty row counts

### Understand the Data
For a comprehensive guide to what each sheet contains and how to use them:

```bash
cat WAR_MACHINE_UNDERSTANDING.md
# or open in your favorite markdown viewer
```

## 📁 Files

- **`War Machine.xlsx`** - The Excel data file (guild management system)
- **`read_excel.py`** - Raw data viewer - displays all cell contents
- **`analyze_war_machine.py`** - Structure analyzer - shows organized summary
- **`WAR_MACHINE_UNDERSTANDING.md`** - Complete documentation guide
- **`EXCEL_IMPROVEMENT_RECOMMENDATIONS.md`** - Recommendations for Excel file improvements
- **`requirements.txt`** - Python dependencies (openpyxl)

## 📊 What's Inside

The War Machine Excel file contains 9 sheets managing:

1. **Leadership and comfort** - Player weapon classes and unit skill ratings
2. **Barracks** - Unit mastery tracking per player
3. **Favorite Units** - Top 5 unit preferences
4. **ExtraSheet** - Backup battle planning scenarios
5. **Unit Sheet** - Primary battle lineup planning
6. **Players** - Central player database with leadership stats
7. **Cost** - Unit costs and deployment tracking (141 units)
8. **ExtraCost** - Alternative cost tracking
9. **Attendance** - Event participation tracking

See [WAR_MACHINE_UNDERSTANDING.md](WAR_MACHINE_UNDERSTANDING.md) for detailed information on each sheet.
