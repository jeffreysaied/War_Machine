# War Machine Excel File - Comprehensive Understanding

## Overview
The **War Machine.xlsx** file is a comprehensive game management spreadsheet for what appears to be a guild/house organization in the game "Conqueror's Blade". It tracks player information, unit preferences, leadership stats, barracks status, unit costs, and attendance.

## File Structure

### Total Sheets: 9

---

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

**Key Information:**
- Lists player names
- Columns for various unit types (Zweihanders, etc.)
- "Yes" indicates a unit is fully maxed/mastered/doctrined
- 55 players tracked

**Use Case:** Quickly see which players have which units available for deployment

---

## Sheet 3: Favorite Units
**Purpose:** Track each player's top 5 favorite units in order of preference

**Structure:**
- Player Name column
- Favorite Unit #1 through #5
- 49 players listed their preferences

**Sample Favorites:**
- aaronpolo: Spartans
- AKBerserk: Siphonarioi

**Use Case:** Helps commanders understand player preferences for optimal deployment strategy

---

## Sheet 4: ExtraSheet
**Purpose:** Appears to be an auxiliary battle/defense planning sheet

**Key Columns:**
- Defense scenarios (Hidden City, etc.)
- Player assignments
- Player Leadership values
- Likely used for planning defensive lineups

**Data:** 117 non-empty rows of battle planning data

---

## Sheet 5: Unit Sheet
**Purpose:** Main battle lineup planning sheet

**Key Columns:**
- Defense scenarios (Wall Fort, etc.)
- Player assignments
- First Defense, Second Defense (unit assignments)
- Player Leadership values

**Data:** 193 rows of detailed battle planning
**Use Case:** Primary tool for organizing who brings which units to specific battles

---

## Sheet 6: Players
**Purpose:** Central player database with leadership calculations

**Key Columns:**
- Player names
- Leadership values for:
  - Light armor
  - Medium armor  
  - Heavy armor
- Current leadership with selected weapon (calculated via formulas)

**Data:** 67 players tracked
**Use Case:** Quick reference for player leadership stats with different armor classes

---

## Sheet 7: Cost
**Purpose:** Track unit costs and deployment statistics

**Key Columns:**
- Units (unit names like Cataphract Lancer, Winged Hussars, Fire Lancers)
- Cost (numerical values, e.g., 305, 285)
- Attack (formulas counting unit appearances in 'Unit Sheet')
- Defense (formulas counting defensive deployments)
- Field (field battle deployments)
- Optimal artillery types (Grapeshot, Mortar, Culverin, Hwacha)

**Data:** 141 different unit types tracked
**Use Case:** Budget management and optimal unit selection for different battle scenarios

---

## Sheet 8: ExtraCost
**Purpose:** Alternative cost tracking (possibly for extra/backup battles)

**Structure:** Similar to Cost sheet but references ExtraSheet instead
**Data:** Same 141 unit types
**Use Case:** Parallel cost tracking for secondary battle scenarios

---

## Sheet 9: Attendance
**Purpose:** Track player attendance at events/battles

**Key Column:**
- Attendance Tracker with dates (e.g., 2025-03-02)
- Player names with tags (e.g., [CO] Skarlette, [HG]KingDingLing)

**Data:** 117 rows tracking attendance
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
