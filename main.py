import tui
import process
from exporter import DataExporter

def export_data(data):
    "Handles the sub-menu logic for exporting data to various formats."
    exporter = DataExporter(data)
    while True:
        export_choice = tui.export_menu()
        if export_choice == 'D':
            break
            
        try:
            file_path = input("Enter the filename/path for export: ")
            if export_choice == 'A':
                exporter.export_to_txt(file_path)
            elif export_choice == 'B':
                exporter.export_to_csv(file_path)
            elif export_choice == 'C':
                exporter.export_to_json(file_path)
            print(f"Successfully exported to {file_path}")
        except Exception as e:
            print(f"Error during export: {e}")

def run():
    """Main entry point of the application."""
    print("-" * 26)
    print("Disneyland Review Analyzer")
    print("-" * 26)

    try:
        # Check if dataset exists before starting
        data = process.read_data("disneyland_reviews.csv")
    except FileNotFoundError:
        print("Error: 'disneyland_reviews.csv' not found. Please ensure the file is in the project folder.")
        return

    while True:
        selection = tui.menu()
        if selection == 'A':
            process.process_submenu_a(data)
        elif selection == 'B':
            process.process_submenu_b(data)
        elif selection == 'C':
            export_data(data)
        elif selection == 'X':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()