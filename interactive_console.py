<<<<<<< HEAD
import os
import xml.etree.ElementTree as ET

# Define paths to the XML files you want to scan (this is just an example)
xml_files = ['blocks.xml', 'loot.xml', 'items.xml']  # You can add more XML files as needed

# This function will scan XML files for missing tags
def scan_for_missing_tags(file):
    missing_tags = []
    tree = ET.parse(file)
    root = tree.getroot()
    
    # Example: Check if the 'item' tag is missing in each XML file
    for elem in root.findall(".//item"):  # You can modify the tag you're searching for
        if elem.tag != 'item':
            missing_tags.append(f"Missing item tag at line {elem.sourceline}")
    
    return missing_tags

# This function will check for cross-references between XML files
def check_cross_references(file1, file2):
    # Example: Compare the 'item' tags in two files for consistency
    tree1 = ET.parse(file1)
    root1 = tree1.getroot()
    
    tree2 = ET.parse(file2)
    root2 = tree2.getroot()
    
    items1 = {elem.attrib['name'] for elem in root1.findall(".//item")}
    items2 = {elem.attrib['name'] for elem in root2.findall(".//item")}
    
    missing_in_file2 = items1 - items2
    missing_in_file1 = items2 - items1
    
    return missing_in_file2, missing_in_file1

# Function to handle the interactive console interface
def interactive_console():
    print("Welcome to SilentSort - XML Tag Scanner")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Scan XML files for missing tags")
        print("2. Check cross-references between XML files")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            print("\nWhich file would you like to scan for missing tags?")
            print("Available files:", ", ".join(xml_files))
            file = input("Enter file name: ")
            
            if file in xml_files:
                missing_tags = scan_for_missing_tags(file)
                if missing_tags:
                    print(f"\nMissing tags found in {file}:")
                    for tag in missing_tags:
                        print(tag)
                else:
                    print(f"\nNo missing tags found in {file}.")
            else:
                print("Invalid file name. Please try again.")
        
        elif choice == '2':
            print("\nWhich two files would you like to check for cross-references?")
            print("Available files:", ", ".join(xml_files))
            file1 = input("Enter first file name: ")
            file2 = input("Enter second file name: ")
            
            if file1 in xml_files and file2 in xml_files:
                missing_in_file2, missing_in_file1 = check_cross_references(file1, file2)
                
                if missing_in_file2:
                    print(f"\nItems in {file1} but missing in {file2}:")
                    for item in missing_in_file2:
                        print(item)
                else:
                    print(f"\nNo missing items from {file1} in {file2}.")
                
                if missing_in_file1:
                    print(f"\nItems in {file2} but missing in {file1}:")
                    for item in missing_in_file1:
                        print(item)
                else:
                    print(f"\nNo missing items from {file2} in {file1}.")
            else:
                print("Invalid file names. Please try again.")
        
        elif choice == '3':
            print("\nExiting SilentSort. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

# Start the interactive console
interactive_console()
=======
import os
import xml.etree.ElementTree as ET

# Define paths to the XML files you want to scan (this is just an example)
xml_files = ['blocks.xml', 'loot.xml', 'items.xml']  # You can add more XML files as needed

# This function will scan XML files for missing tags
def scan_for_missing_tags(file):
    missing_tags = []
    tree = ET.parse(file)
    root = tree.getroot()
    
    # Example: Check if the 'item' tag is missing in each XML file
    for elem in root.findall(".//item"):  # You can modify the tag you're searching for
        if elem.tag != 'item':
            missing_tags.append(f"Missing item tag at line {elem.sourceline}")
    
    return missing_tags

# This function will check for cross-references between XML files
def check_cross_references(file1, file2):
    # Example: Compare the 'item' tags in two files for consistency
    tree1 = ET.parse(file1)
    root1 = tree1.getroot()
    
    tree2 = ET.parse(file2)
    root2 = tree2.getroot()
    
    items1 = {elem.attrib['name'] for elem in root1.findall(".//item")}
    items2 = {elem.attrib['name'] for elem in root2.findall(".//item")}
    
    missing_in_file2 = items1 - items2
    missing_in_file1 = items2 - items1
    
    return missing_in_file2, missing_in_file1

# Function to handle the interactive console interface
def interactive_console():
    print("Welcome to SilentSort - XML Tag Scanner")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Scan XML files for missing tags")
        print("2. Check cross-references between XML files")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            print("\nWhich file would you like to scan for missing tags?")
            print("Available files:", ", ".join(xml_files))
            file = input("Enter file name: ")
            
            if file in xml_files:
                missing_tags = scan_for_missing_tags(file)
                if missing_tags:
                    print(f"\nMissing tags found in {file}:")
                    for tag in missing_tags:
                        print(tag)
                else:
                    print(f"\nNo missing tags found in {file}.")
            else:
                print("Invalid file name. Please try again.")
        
        elif choice == '2':
            print("\nWhich two files would you like to check for cross-references?")
            print("Available files:", ", ".join(xml_files))
            file1 = input("Enter first file name: ")
            file2 = input("Enter second file name: ")
            
            if file1 in xml_files and file2 in xml_files:
                missing_in_file2, missing_in_file1 = check_cross_references(file1, file2)
                
                if missing_in_file2:
                    print(f"\nItems in {file1} but missing in {file2}:")
                    for item in missing_in_file2:
                        print(item)
                else:
                    print(f"\nNo missing items from {file1} in {file2}.")
                
                if missing_in_file1:
                    print(f"\nItems in {file2} but missing in {file1}:")
                    for item in missing_in_file1:
                        print(item)
                else:
                    print(f"\nNo missing items from {file2} in {file1}.")
            else:
                print("Invalid file names. Please try again.")
        
        elif choice == '3':
            print("\nExiting SilentSort. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

# Start the interactive console
interactive_console()
>>>>>>> 7bbe4a6ca3b562d53dd057982c2d239d10843f4d
