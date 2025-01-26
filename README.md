# Seat-Occupancy-Detection-YOLOv8

## **Built With**
- Python 3.11  
  [![Build Status](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/downloads/release/python-3110/)


This repository provides an example of using OpenCV in Python to detect whether seats are occupied or not in a video, and simultaneously render a “seat map” (a simple schematic) that displays seat statuses (occupied vs. not occupied) around a table.



## **Methodology**
### **1. Region of Interest (ROI):**
- Each seat is defined by a Region of Interest (ROI) in the frame, which is compared to a reference “empty seat” background.
- Changes in pixel values indicate whether a seat is likely occupied or not.

### **2. Dynamic Simulation Map:**
- A blank canvas (light gray) is created each frame to represent a simplified map view of the room or table.
- Each seat’s status is shown as a colored box (green for “Not Occupied,” red for “Occupied”) around the table, giving a quick schematic overview.
  
### **3. Live Video Preview**:
- The code also displays the original video feed (or webcam) with bounding boxes drawn around each seat, along with text indicating occupancy status.

---



