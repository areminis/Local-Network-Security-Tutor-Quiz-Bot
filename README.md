# 🧠 AI-Powered Network Security Tutor and Quiz Bot  
**Course:** CS5342 – Network Security  
**Group:** 8  
**Project Type:** Privacy-Preserving Offline Intelligent Tutor  
**University:** Texas Tech University  

---

## 📘 Project Description  

The **AI-Powered Network Security Tutor and Quiz Bot** is a **local intelligent agent** that assists students in understanding core **network security concepts** and allows them to take **auto-generated quizzes**, all while operating fully **offline** to ensure **data privacy**.  

The system uses locally hosted **LLMs (Ollama - LLaMA 3.2)**, **ChromaDB**, and **SentenceTransformer embeddings** to provide intelligent responses and assessments based on course materials such as lecture slides, textbooks, and quizzes.  

---

## 🎯 Objectives  

- Develop a **local AI tutor** that answers questions with relevant explanations and references.  
- Create a **quiz generator** capable of multiple question types (MCQ, True/False, Open-ended).  
- Implement **grading and feedback** using similarity metrics and contextual reasoning.  
- Ensure complete **data privacy** by executing all logic on the **local system**.  

---

## 🏷️️ System Architecture  

**Architecture Components:**  
1. **Frontend (Flask Web App):**  
   - User interface for Tutor and Quiz Agents.  
   - Developed using Flask + Bootstrap.  

2. **Backend (Python Flask Server):**  
   - Handles all app logic, API routes, and integration with models.  

3. **Embedding Engine (SentenceTransformer – all-MiniLM-L6-v2):**  
   - Converts course content and user questions into dense vector representations.  

4. **Vector Database (ChromaDB):**  
   - Stores pre-embedded lecture and textbook data locally for retrieval.  

5. **Local LLM (Ollama – LLaMA 3.2):**  
   - Generates context-based responses and quiz content offline.  

6. **Grading Engine:**  
   - Compares user answers with reference answers using similarity scoring (`difflib.SequenceMatcher`).  

7. **Privacy Layer:**  
   - Ensures all communication occurs via `localhost (127.0.0.1)`; no external API calls.  

---

## 🧩 System Flow  

**1. Data Preparation:**  
- PDF and text files (lectures, books, quizzes) are cleaned using `pdfplumber`.  
- Extracted text is chunked (400–500 words per piece).  
- Chunks are embedded and stored in ChromaDB.  

**2. Question/Quiz Processing:**  
- User enters question or selects topic.  
- Flask queries ChromaDB for top context.  
- Context and question are passed to Ollama LLM for response generation.  

**3. Answer Evaluation:**  
- Quiz responses are graded locally using string similarity.  
- Feedback and reasoning are generated using the LLM.  

---

## ⚙️ Prerequisites  

**Software Requirements:**  
- Python 3.10+  
- Flask  
- ChromaDB  
- SentenceTransformers  
- Ollama (with LLaMA 3.2 model downloaded)  
- pdfplumber  
- difflib, json, re, logging  

**Hardware Requirements:**  
- CPU: Quad-core or higher (Ryzen 7 / i7 recommended)  
- RAM: Minimum 16 GB  
- Storage: 10 GB free space  

**Operating System:**  
- Windows 10/11 or Ubuntu 22.04  

---

## 🔧 Installation and Setup  

### Step 1: Clone the Repository  
```bash
git clone https://github.com/<your-username>/Local-Network-Security-Tutor-Quiz-Bot.git
cd Local-Network-Security-Tutor-Quiz-Bot
```

### Step 2: Create and Activate Virtual Environment  
```bash
python -m venv .venv
.venv\Scripts\activate  # (Windows)
# OR
source .venv/bin/activate  # (Linux/Mac)
```

### Step 3: Install Dependencies  
```bash
pip install -r requirements.txt
```

### Step 4: Setup Data Directory  
```
data/
 ├── textbooks/
 ├── lecture_slides/
 ├── quizzes/
 └── internet_sources/
```
Add cleaned text or PDF files in respective folders.

### Step 5: Generate Embeddings  
```bash
python app/build_embeddings.py
```

### Step 6: Run the Flask Application  
```bash
python app.py
```

Access it in your browser at **http://127.0.0.1:5000**  

---

## 🧪 Features  

| Feature | Description |
|----------|-------------|
| 🧠 **Q&A Tutor Agent** | Answers course questions using local embeddings and LLM reasoning. |
| 🧩 **Quiz Agent** | Generates quizzes with MCQs, True/False, and Open-ended questions. |
| 📚 **Source Citations** | Displays document sources for transparency. |
| 🔐 **Privacy-Preserving** | Fully offline; no internet or API calls. |
| ⚡ **Local Processing** | Uses Ollama to execute models on local CPU. |
| 🧮 **Auto-Grading** | Grades user responses with similarity scoring and reasoning. |

---

## 📂 Training Data and Format  

| Source Type | Description | Format | Example File |
|--------------|--------------|---------|---------------|
| **Lecture Slides** | 25 PDFs from course lectures | `.pdf` / `.txt` | `lecture_1.pdf` |
| **Textbooks** | Stallings, Katz & Lindell | `.pdf` / `.txt` | `Katz_Lindell_IntroModernCrypto.txt` |
| **Quizzes** | Course quiz datasets | `.txt` | `quiz_week3.txt` |
| **Internet Sources** | Verified references only | `.txt` | `cybersecurity_basics.txt` |

Each file is embedded as ~400–500 word chunks using SentenceTransformer and indexed in ChromaDB.  

---

## 🧠 Example Workflow  

**Tutor Interaction:**  
1. User asks: “Explain the RSA algorithm.”  
2. System retrieves context from Stallings textbook.  
3. LLaMA model generates a structured explanation.  
4. Sources and formatted output are displayed.  

**Quiz Interaction:**  
1. User selects topic: “Network Attacks”, 5 questions.  
2. Quiz Agent generates MCQ, True/False, Open-ended questions.  
3. User submits responses → Auto-graded results displayed with explanations.  

---

## 🥪 Captured Data and Validation  

Each group member captured 5 prompts (3 Tutor + 2 Quiz).  
Captured data includes:
- Tutor/Quiz app screenshot  
- Wireshark trace showing local packet flow  
- Mapping of **Step 1 (Prompt)** → **Step 4 (Trace Response)**  

All network traffic confirmed to be **localhost (127.0.0.1)** only.  

---

## 🧩 Documentation and Deliverables  

| Deliverable | Description |
|--------------|-------------|
| `group8_prototype.zip` | Full source code + embeddings + screenshots |
| `student_name.docx` | Captured data explanation (5 prompts) |
| `student_name.pcap` | Wireshark trace file |
| `group8_round2.pptx` | Project presentation slides |
| `README.md` | GitHub repository documentation |
| `architecture_diagram.png` | System architecture visual |

---

## 🎥 Demonstration Video (if applicable)  

**Video Overview (Optional for GitHub):**  
- Step-by-step explanation of system execution  
- Tutor and Quiz demo  
- Wireshark validation snippet  
*(Add YouTube or local file link here once recorded)*  

---

## 🚀 Future Enhancements  

- Voice-based tutor using SpeechRecognition  
- GPU-accelerated local inference  
- Dashboard for user analytics  
- Multi-user mode with session tracking  
- Integration with classroom environments  

---

## 📚 References  

1. William Stallings, *Network Security Essentials*, 6th Edition.  
2. Katz & Lindell, *Introduction to Modern Cryptography*.  
3. Ollama – [https://ollama.ai](https://ollama.ai)  
4. ChromaDB – [https://docs.trychroma.com](https://docs.trychroma.com)  
5. SentenceTransformers – [https://www.sbert.net](https://www.sbert.net)  
6. Flask Framework – [https://flask.palletsprojects.com](https://flask.palletsprojects.com)  
7. Wireshark – [https://www.wireshark.org](https://www.wireshark.org)  

---

