import tui
import csv
import visual

def read_data(file_path):
    """
    Reads the dataset from a CSV file.
    Returns: A list of lists representing the review rows.
    """
    data = []
    with open(file_path, "r", encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # Skip the header row
        for row in csv_reader:
            data.append(row)
    
    print(f"Successfully loaded {len(data)} rows.")
    return data

def process_submenu_a(data):
    """Handles user interactions for viewing data statistics."""
    while True:
        submenu_choice = tui.submenu_a()
        try:
            if submenu_choice == 'A':
                visual.park(data)
            elif submenu_choice == 'B':
                visual.specific_park(data)
            elif submenu_choice == 'C':
                visual.average(data)
            elif submenu_choice == 'D':
                visual.avg_score_per_park_by_location(data)
            else:
                break
        except Exception as e:
            print(f"An error occurred while processing data: {e}")

def process_submenu_b(data):
    """Handles user interactions for data visualization (Charts)."""
    while True:
        submenu_choice = tui.submenu_b()
        try:
            if submenu_choice == 'A':
                visual.pie_chart_reviews_per_park(data)
            elif submenu_choice == 'B':
                visual.bar_chart_avg_scores_per_park(data)
            elif submenu_choice == 'C':
                visual.top_locations(data)
            else:
                break
        except Exception as e:
            print(f"An error occurred while generating visuals: {e}")