# Ayah-Snap 📖

Ayah-Snap is a web app that displays random verses (Ayahs) from the Quran along with their translation. It uses Flask as the backend framework, fetches data from the [Al-Quran Cloud API](https://alquran.cloud/), and dynamically renders the information on the frontend.

## Features
- Displays a random Ayah from the Quran.
- Shows the Surah name and Ayah number.
- Offers a button to fetch the translation of the Ayah.
- Beautiful, modern user interface with smooth animations.
- Mobile-friendly and responsive design.
- Floating refresh button for generating a new Ayah.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **API**: Al-Quran Cloud API (to fetch Ayahs and their translations)
- **Styling**: CSS (with animations and transitions)
- **Fonts**: Google Fonts (Poppins and Amiri)

## Installation

### Prerequisites

Ensure you have Python 3.x installed. You will also need `pip` to install the required Python packages.

### Clone the repository

```bash
git clone https://github.com/RasikhAli/Ayah-Snap.git
cd Ayah-Snap
```

### Install required packages

```bash
pip install -r requirements.txt
```

### Run the Flask app

To start the app locally, run the following command:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

## Usage

Once the application is running:

1. Open `http://127.0.0.1:5000/` in your browser.
2. You will see a random Ayah displayed along with the Surah name and Ayah number.
3. Click the **Translate** button to see the English translation of the Ayah.
4. Use the **Refresh** button to generate a new random Ayah.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and create a pull request. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes locally.
5. Submit a pull request with a clear description of your changes.

## License

This project is open-source and available under the [MIT License](LICENSE).