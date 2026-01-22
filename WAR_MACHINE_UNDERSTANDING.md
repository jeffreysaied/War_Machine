# War Machine Excel File - Comprehensive Understanding

## 📑 Table of Contents
- [Overview](#overview)
- [Quick Reference](#quick-reference)
- [Detailed Sheet Breakdown](#detailed-sheet-breakdown)
  - [Sheet 1: Leadership and comfort](#sheet-1-leadership-and-comfort)
  - [Sheet 2: Barracks](#sheet-2-barracks)
  - [Sheet 3: Favorite Units](#sheet-3-favorite-units)
  - [Sheet 4: ExtraSheet](#sheet-4-extrasheet)
  - [Sheet 5: Unit Sheet](#sheet-5-unit-sheet)
  - [Sheet 6: Players](#sheet-6-players)
  - [Sheet 7: Cost](#sheet-7-cost)
  - [Sheet 8: ExtraCost](#sheet-8-extracost)
  - [Sheet 9: Attendance](#sheet-9-attendance)
- [Key Insights](#key-insights)
- [Technical Details](#technical-details)

---

## Overview
The **War Machine.xlsx** file is a comprehensive game management spreadsheet for what appears to be a guild/house organization in the game "Conqueror's Blade". It tracks player information, unit preferences, leadership stats, barracks status, unit costs, and attendance.

**Total Sheets:** 9  
**Total Players Tracked:** ~57-67 active players  
**Total Unit Types:** 141 different units  

---

## Quick Reference

| Sheet Name | Primary Purpose | Key Data Points |
|------------|----------------|-----------------|
| Leadership and comfort | Player weapon classes & skill ratings | 57 players, 9 unit categories rated 0-10 |
| Barracks | Unit mastery tracking | 55 players, "Yes" for maxed units |
| Favorite Units | Player preferences | 49 players, Top 5 units each |
| ExtraSheet | Backup battle planning | 117 rows, defensive scenarios |
| Unit Sheet | Primary battle planning | 193 rows, player assignments |
| Players | Central player database | 67 players, leadership stats by armor |
| Cost | Unit costs & deployment | 141 units, cost tracking |
| ExtraCost | Alternative cost tracking | 141 units, backup scenarios |
| Attendance | Event participation | 117 rows, dated attendance |

---

## Detailed Sheet Breakdown

## Sheet 1: Leadership and comfort
**Purpose:** Track player information and their comfort level with different unit types

**Key Columns:**
- Name
- Primary Class (e.g., Spearshield, Longsword, Poleaxe, etc.)
- Secondary Class
- Leadership Primary Class (numerical values ~740-795)
- Leadership Second Class
- Purple set Leadership
- Unit Comfort Ratings (0-10 scale):
  - Frontline Infantry
  - DPS Infantry
  - Anti Cav
  - Cavalry
  - Coco
  - Shenji
  - Flames
  - Falco
  - Lionroar Crew

**Data:** 
- 57 active players listed
- Players rate their skill with different unit types from 0-10 (0 = don't use, 10 = top tier)
- Includes formula to calculate averages across all players

**Sample Players:**
- aaron polo (Spearshield, Leadership 792)
- AKBerserk (Longsword, Leadership 794)
- MilkTruck (Poleaxe, Leadership 795) - rates all units at 10/10

---

## Sheet 2: Barracks
**Purpose:** Track which units each player has maxed/mastered/doctrined

| Attribute | Value |
|-----------|-------|
| Players Tracked | 55 |
| Tracking Method | "Yes" for maxed units |
| Use Case | Quick deployment availability check |

**Key Information:**
- Lists player names
- Columns for various unit types (Zweihanders, etc.)
- "Yes" indicates a unit is fully maxed/mastered/doctrined

---

## Sheet 3: Favorite Units
**Purpose:** Track each player's top 5 favorite units in order of preference

| Attribute | Value |
|-----------|-------|
| Players Listed | 49 |
| Preference Slots | Top 5 units per player |
| Use Case | Optimize deployment strategy |

**Structure:**
- Player Name column
- Favorite Unit #1 through #5

**Sample Favorites:**
- aaronpolo: Spartans
- AKBerserk: Siphonarioi

---

## Sheet 4: ExtraSheet
**Purpose:** Auxiliary battle/defense planning sheet

| Attribute | Value |
|-----------|-------|
| Data Rows | 117 non-empty rows |
| Focus | Defensive scenarios |

**Key Columns:**
- Defense scenarios (Hidden City, etc.)
- Player assignments
- Player Leadership values
- Used for planning defensive lineups

---

## Sheet 5: Unit Sheet
**Purpose:** Main battle lineup planning sheet

| Attribute | Value |
|-----------|-------|
| Data Rows | 193 detailed rows |
| Focus | Primary battle planning |
| Role | Organizing battle deployments |

**Key Columns:**
- Defense scenarios (Wall Fort, etc.)
- Player assignments
- First Defense, Second Defense (unit assignments)
- Player Leadership values

**Use Case:** Primary tool for organizing who brings which units to specific battles

---

## Sheet 6: Players
**Purpose:** Central player database with leadership calculations

| Attribute | Value |
|-----------|-------|
| Players Tracked | 67 |
| Data Points | Leadership by armor class |

**Key Columns:**
- Player names
- Leadership values for:
  - Light armor
  - Medium armor  
  - Heavy armor
- Current leadership with selected weapon (calculated via formulas)

**Use Case:** Quick reference for player leadership stats with different armor classes

---

## Sheet 7: Cost
**Purpose:** Track unit costs and deployment statistics

| Attribute | Value |
|-----------|-------|
| Unit Types | 141 different units |
| Tracking | Cost + deployment count |

**Key Columns:**
- Units (unit names like Cataphract Lancer, Winged Hussars, Fire Lancers)
- Cost (numerical values, e.g., 305, 285)
- Attack (formulas counting unit appearances in 'Unit Sheet')
- Defense (formulas counting defensive deployments)
- Field (field battle deployments)
- Optimal artillery types (Grapeshot, Mortar, Culverin, Hwacha)

**Use Case:** Budget management and optimal unit selection for different battle scenarios

---

## Sheet 8: ExtraCost
**Purpose:** Alternative cost tracking (possibly for extra/backup battles)

| Attribute | Value |
|-----------|-------|
| Unit Types | 141 (same as Cost) |
| References | ExtraSheet data |

**Structure:** Similar to Cost sheet but references ExtraSheet instead of Unit Sheet

**Use Case:** Parallel cost tracking for secondary battle scenarios

---

## Sheet 9: Attendance
**Purpose:** Track player attendance at events/battles

| Attribute | Value |
|-----------|-------|
| Tracking Rows | 117 |
| Date Format | ISO format (e.g., 2025-03-02) |

**Key Column:**
- Attendance Tracker with dates
- Player names with tags (e.g., [CO] Skarlette, [HG]KingDingLing)

**Use Case:** Monitor player participation and availability

---

## Key Insights

### Player Management
The spreadsheet manages approximately **57-67 active players** with detailed information about:
- Their preferred weapon classes
- Leadership levels (ranging from ~720 to ~795)
- Skill levels with different unit types
- Which units they have mastered
- Favorite units for deployment

### Battle Planning
The system supports:
- Multiple battle scenarios (Attack, Defense, Field battles)
- Player assignments to specific roles
- Unit cost management and budgeting
- Optimal artillery selection per unit
- Primary and backup battle lineups (Unit Sheet vs ExtraSheet)

### Game Context: Conqueror's Blade
This appears to be for a large, organized guild/house in Conqueror's Blade where:
- Players have different weapon masteries (Longsword, Poleaxe, Maul, etc.)
- Leadership points determine which units can be commanded
- Units have costs (likely for territory wars/sieges)
- Different armor classes affect leadership values
- Coordination is critical for competitive play

### Sophistication Level
This is a **highly sophisticated organizational tool** showing:
- Advanced Excel formulas for automatic calculations
- Cross-sheet references for data consistency
- Multi-dimensional player tracking
- Strategic battle planning capabilities
- Historical attendance tracking

## Technical Details
- **Format:** .xlsx (Excel 2007+)
- **Total Dimensions:** Up to 1009 rows and 100+ columns across sheets
- **Formulas:** Extensive use of COUNTIF, IFS, AVERAGE functions
- **Data Validation:** Structured tracking with consistent formatting

## Repository Tools
The repository includes:
1. **read_excel.py** - Basic script to read and display all Excel content
2. **analyze_war_machine.py** - Enhanced analysis script with structured output
3. **requirements.txt** - Python dependencies (openpyxl)
4. **README.md** - Usage instructions

## Conclusion
The War Machine Excel file is a comprehensive **guild management system** for organizing 50+ players in a competitive gaming environment, tracking their capabilities, managing battle lineups, monitoring costs, and maintaining attendance records. It demonstrates professional-level organization and strategic planning for team-based competitive gameplay.
