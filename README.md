# Advanced Image Processing Application with PyQt5 & OpenCV

This is a powerful desktop application for applying **morphological operations** to images using **OpenCV** and **PyQt5**. The tool provides a user-friendly GUI with real-time feedback and customization options such as kernel size adjustment, operation selection, and comparison mode.

---

## ✨ Features

- 📂 Load and process any local image
- 🧠 Apply 7 types of **morphological transformations**:
  - Erosion
  - Dilation
  - Opening
  - Closing
  - Morphological Gradient
  - Top Hat
  - Black Hat
- ⚙️ Adjustable **kernel size** via slider (odd values up to 21)
- 🔀 **Live comparison** mode (original vs. processed)
- 💾 Save processed output in PNG, JPG, or BMP formats
- 🎨 Elegant and responsive **PyQt5 GUI** design

---

## 🖥️ GUI Overview

| Section             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Left Panel**      | Controls: dropdown for operation, kernel slider, load/save buttons          |
| **Right Panel**     | Image display: original and processed (or side-by-side in comparison mode)  |

---

## 🧰 Requirements

- Python 3.7+
- PyQt5
- OpenCV (cv2)
- NumPy

You can install the dependencies using pip:

```bash
pip install pyqt5 opencv-python numpy
```

🚀 How to Run

Clone this repository or copy the Python script:

```bash
git clone https://github.com/yourusername/morph-app.git
cd morph-app
```

Run the application:

```bash
python morph_app.py
```

⚠️ Make sure the file is named appropriately (e.g., morph_app.py) and that you have an icon file icon.png in the same directory, or adjust the icon path.


🧪 Morphological Operations Explained
Erosion: Removes pixels on object boundaries.

Dilation: Adds pixels to the boundaries.

Opening: Erosion followed by dilation (removes small objects).

Closing: Dilation followed by erosion (closes small holes).

Gradient: Difference between dilation and erosion.

Top Hat: Original - Opening (highlights bright regions).

Black Hat: Closing - Original (highlights dark regions).

