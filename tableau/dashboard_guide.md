# Tableau Dashboard Step-by-Step Guide
**Project:** Student Mental Health & Burnout

The goal of this dashboard is to show University Administrators exactly what factors are driving student burnout.

---

## Step 1: Connect to Your Data
1. Open **Tableau Public** on your computer.
2. On the left side under *Connect -> To a File*, click **Text file**.
3. Navigate to your project folder and select: `DVA_CAPSTONE2/data/processed/tableau_ready_dataset.csv`.
4. Wait for the data preview to load, then click **Sheet 1** at the bottom left to start building.

---

## Step 2: Build the "Executive View" (High-Level KPIs)

**Chart 1: Total Students by Burnout Level (Bar Chart)**
*Goal: Show how many students are facing high burnout.*
1. Drag **`burnout_level`** to the **Columns** shelf.
2. Drag **`student_id`** to the **Rows** shelf.
3. Click the little arrow on `student_id` in the Rows shelf, go to **Measure**, and select **Count (Distinct)**.
4. Drag **`burnout_level`** to the **Color** mark.
5. Rename the sheet at the bottom to "Burnout Distribution".

**Chart 2: Average Academic Pressure by Course (Horizontal Bar Chart)**
*Goal: Show which university course has the highest academic pressure.*
1. Create a **New Sheet**.
2. Drag **`course`** to the **Rows** shelf.
3. Drag **`academic_pressure_score`** to the **Columns** shelf.
4. Change the `academic_pressure_score` measure from *Sum* to **Average**.
5. Sort the bars from highest to lowest.
6. Rename the sheet to "Pressure by Course".

---

## Step 3: Build the "Operational View" (Deep Dives)

**Chart 3: Anxiety vs. Academic Pressure (Scatter Plot)**
*Goal: Prove visually that higher pressure equals higher anxiety.*
1. Create a **New Sheet**.
2. Drag **`academic_pressure_score`** to the **Columns** shelf (change Measure to **Average**).
3. Drag **`anxiety_score`** to the **Rows** shelf (change Measure to **Average**).
4. Drag **`course`** to the **Detail** mark (this creates a dot for each course).
5. Drag **`burnout_level`** to the **Color** mark (so we see if the high-pressure dots are also high-burnout).
6. Rename the sheet to "Pressure vs Anxiety".

**Chart 4: Sleep Quality vs. Study Hours (Box Plot or Bar Chart)**
*Goal: Show the tradeoff between studying and physical recovery.*
1. Create a **New Sheet**.
2. Drag **`sleep_quality`** to the **Columns** shelf.
3. Drag **`daily_study_hours`** to the **Rows** shelf (change to **Average**).
4. Rename the sheet to "Study Hours vs Sleep Quality".

---

## Step 4: Assemble the Dashboard
1. At the bottom, click the **New Dashboard** icon (it looks like a square divided into four).
2. On the left side, change the **Size** to **Automatic** so it fills the screen.
3. Drag a **Text** object to the very top to create a title: *"University Student Mental Health & Burnout Analysis"*.
4. Drag your four sheets from the left panel onto the canvas. Arrange them so the Bar Charts are at the top (Executive View) and the Scatter Plot is at the bottom (Operational View).

---

## Step 5: Add Interactivity (Mandatory Requirement)
1. Go to your **"Burnout Distribution"** chart on the dashboard.
2. Click the chart to select it, and look for the tiny **Funnel icon** on the right side of its grey border. Click it to **"Use as Filter"**.
3. Now, if you click on the "High" burnout bar, all the other charts in the dashboard will instantly update to show data *only* for high-burnout students!
4. *(Optional)*: Drag the **`Year`** field into the Filters shelf of one of your sheets, then right-click the filter in the dashboard and select "Apply to Worksheets -> All Using This Data Source". This lets the user filter the whole dashboard by 1st, 2nd, 3rd, or 4th-year students.

---

## Step 6: Publish and Submit
1. Go to **File -> Save to Tableau Public**.
2. Sign in to your Tableau Public account if prompted.
3. Once it successfully uploads, a browser window will open with your dashboard.
4. **Copy the URL** from your browser and paste it into `tableau/dashboard_links.md` in your VS Code.
5. Take a screenshot of the dashboard and save it in `tableau/screenshots/`.
6. Commit these final additions to GitHub!
