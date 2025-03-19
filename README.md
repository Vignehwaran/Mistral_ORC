

# 📄 Mistral OCR App (Pixtral-12B Powered)

Transform your documents into structured, readable text using **Mistral’s Pixtral-12B model**. This OCR app extracts content from uploaded images — including plain text and tabular data — with high accuracy using powerful vision-language models.

---

## 🚀 Features

- ✅ Optical Character Recognition (OCR) using Mistral Pixtral-12B
- 📸 Upload image files (JPG, PNG, JPEG)
- 📄 Extract both plain text and structured tables
- 🧠 Built-in prompt to guide the model for better accuracy
- 🖥️ Simple and beautiful UI using Streamlit

---

## 🧠 Model Used

- **Model**: [`mistralai/pixtral-12b`](https://huggingface.co/mistralai/pixtral-12b)
- **Type**: Vision-to-Text / Vision2Seq
- **Task**: OCR (Document Image to Structured Text)

---

## 🛠️ Tech Stack

- `Python 3.10+`
- `Streamlit`
- `Transformers (HuggingFace)`
- `PyTorch`
- `Pillow (PIL)`
- `dotenv`

---

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/mistral-ocr-app.git
cd mistral-ocr-app
```

2. **Create Virtual Environment & Install Requirements**

```bash
python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate
pip install -r requirements.txt
```

3. **(Optional) Add Your API Keys**  
If you're using `.env` for future integrations:

```env
Mistral_API_KEY=your_api_key_here
```

4. **Run the App**

```bash
streamlit run app.py
```

---

## 📷 Example Use Case

- Upload an image with printed or handwritten text
- The app uses Mistral’s Pixtral model to extract all visible content
- If it detects a table, output will be structured accordingly

---

## 💡 Sample Prompt Used

```
Extract all visible text from this image. If the image contains tables, present them in clear tabular format using rows and columns.
```

---

## 🤝 Contributing

Feel free to fork, improve or submit issues & PRs. Let's build better OCR systems together!

---

## 📬 Contact

Made with ❤️ by **Vigneshwaran (Vicky)**  
📫 [LinkedIn](https://www.linkedin.com/in/vigneshwaran-p-613661264/) | 📧 vickythevgn@gmail.com

---

## 🪄 License

This project is open-source and free to use under the [MIT License](LICENSE).
```

---

### ✅ Bonus Tip:
Include this as your `README.md` file in the root of your project folder. It'll show up automatically on your GitHub repo page.

Want help creating a nice project **cover image/banner** for GitHub or adding **demo GIFs**? Just say the word 😎📸
