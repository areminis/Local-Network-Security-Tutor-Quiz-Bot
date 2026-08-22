# Network Security Tutor & Quiz Bot

## Overview
This project is a privacy-preserving, production-ready tutor and quiz bot for network security courses. It features:
- Q&A agent with citations and web search
- Quiz generation and automated grading
- Local document processing and embedding
- Security features: encryption, audit logging, network monitoring
- Modern React frontend and FastAPI backend

## Features
- Ask questions and get cited answers from uploaded documents
- Generate quizzes (MCQ, True/False, Open-ended) on any topic
- Upload and ingest PDF, DOCX, PPTX, TXT, and Markdown files
- Automated grading and feedback
- All data processed locally for privacy
- Security: encryption, audit logging, network monitoring

## Production Setup (Docker)

### Prerequisites
- Docker and Docker Compose installed
- (Optional) Ollama installed for local LLM

### Quick Start
1. Clone the repository:
  ```bash
  git clone <repo-url>
  cd chat-ver-1
  ```
2. Build and start all services:
  ```bash
  docker-compose up --build
  ```
3. Access the frontend at [http://localhost:3000](http://localhost:3000)
4. Access the backend API docs at [http://localhost:8000/docs](http://localhost:8000/docs)

### Customization
- Edit `.env` for environment variables (see sample in README)
- To use a custom Ollama model, update `OLLAMA_MODEL` in `.env` and ensure the model is pulled

### Stopping Services
```bash
docker-compose down
```

## Folder Structure
```
chat-ver-1/
├── backend/         # FastAPI backend
├── frontend/        # React frontend
├── data/            # Documents, uploads, ChromaDB
├── logs/            # Application logs
├── requirements.txt # Python dependencies
├── docker-compose.yml
├── README.md        # Unified documentation
```

## Troubleshooting
- Ensure Docker is running
- Check logs in `logs/` for errors
- Make sure Ollama is running and model is available
- For API issues, check `/health` endpoint

## License
MIT
```

## 📋 Prerequisites

### Required Software

1. **Python 3.9+**
2. **Node.js 18+** and npm
3. **Ollama** - For running Llama 3.2 locally

### Install Ollama

```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama service
ollama serve

# Pull Llama 3.2 3B model
ollama pull llama3.2:3b
```

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
cd chat-ver-1
```

### 2. Backend Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
.\venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env with your settings (optional)
# The defaults should work for local development
```

### 3. Frontend Setup

```bash
cd frontend
npm install
cd ..
```

### 4. Prepare Data Directory

```bash
# Create data directories
mkdir -p data/documents data/uploads data/chroma_db logs

# (Optional) Add your network security documents
# Place PDF, DOCX, PPTX, TXT, or MD files in data/documents/
```

## 🎯 Running the Application

### Start Backend Server

```bash
# Make sure you're in the project root and venv is activated
cd backend
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Or simply:
python main.py
```

Backend will be available at: `http://localhost:8000`
API Documentation: `http://localhost:8000/docs`

### Start Frontend Development Server

```bash
# In a new terminal
cd frontend
npm run dev
```

Frontend will be available at: `http://localhost:3000`

## 📚 Usage Guide

### 1. Upload Documents

1. Navigate to the **Documents** tab
2. Click "Choose a file" or drag and drop
3. Upload your network security materials:
   - Lecture slides (PDF, PPTX)
   - Textbooks (PDF)
   - Study guides (DOCX, MD, TXT)
4. Click "Upload and Index Document"

**Or** use batch ingestion:
```bash
# Place documents in data/documents/ then:
# Click "Ingest Directory" in the UI
# Or use the API endpoint
curl -X POST http://localhost:8000/api/documents/ingest-directory
```

### 2. Ask Questions (Q&A Tutor)

1. Navigate to the **Q&A Tutor** tab
2. Type your question (e.g., "What is a DDoS attack?")
3. Optionally enable "Include web search" for additional context
4. Click "Ask Question"
5. View answer with citations and confidence score

**Example Questions:**
- What is the difference between symmetric and asymmetric encryption?
- Explain how a firewall works
- What are common types of network attacks?
- Describe the OSI model layers

### 3. Take Quizzes

1. Navigate to the **Quiz** tab
2. Configure your quiz:
   - **Mode**: Random or Topic-Specific
   - **Topic**: (if topic-specific) e.g., "Firewalls", "Encryption"
   - **Number of Questions**: 3-15
   - **Question Types**: Select MCQ, True/False, and/or Open-Ended
3. Click "Generate Quiz"
4. Answer all questions
5. Click "Submit Quiz"
6. Review detailed feedback with grades and citations

### 4. Monitor System Health

1. Navigate to the **Dashboard** tab
2. Check system status:
   - Ollama connection
   - ChromaDB initialization
   - Document count
3. View privacy features and quick start guide

## 🔧 Configuration

### Environment Variables (.env)

```bash
# Application
APP_NAME="Network Security Tutor Bot"
DEBUG=True
HOST=0.0.0.0
PORT=8000

# Ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b

# ChromaDB
CHROMA_DB_PATH=./data/chroma_db
COLLECTION_NAME=network_security_docs

# Embedding Model
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Security
ENCRYPTION_KEY=<generate-your-key>
ENABLE_AUDIT_LOGGING=True

# Quiz
QUIZ_POOL_SIZE=100
MIN_SIMILARITY_THRESHOLD=0.7
```

### Generate Encryption Key

```python
from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())
```

## 📊 API Endpoints

### Health Check
```bash
GET /health
```

### Q&A Tutor
```bash
POST /api/qa/ask
{
  "question": "What is a VPN?",
  "include_web_search": false
}
```

### Quiz Generation
```bash
POST /api/quiz/generate
{
  "mode": "random",
  "topic": null,
  "num_questions": 5,
  "question_types": ["multiple_choice", "true_false", "open_ended"]
}
```

### Quiz Grading
```bash
POST /api/quiz/grade?quiz_id=<quiz_id>
[
  {
    "quiz_id": "<quiz_id>",
    "question_id": "<question_id>",
    "user_answer": "answer"
  }
]
```

### Document Upload
```bash
POST /api/documents/upload
Content-Type: multipart/form-data
```

## 🧪 Testing

### Test Backend API
```bash
# Check health
curl http://localhost:8000/health

# Test Q&A (after uploading documents)
curl -X POST http://localhost:8000/api/qa/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is encryption?", "include_web_search": false}'

# Get document count
curl http://localhost:8000/api/documents/count
```

## 🔐 Security & Privacy Features

### Data Privacy
- ✅ All document processing happens locally
- ✅ No external API calls for document analysis
- ✅ LLM runs locally via Ollama
- ✅ Embeddings generated locally
- ✅ ChromaDB stores data locally

### Encryption
```python
from backend.security import encryption_service

# Encrypt sensitive data
encrypted = encryption_service.encrypt("sensitive data")

# Decrypt
decrypted = encryption_service.decrypt(encrypted)
```

### Audit Logging
```python
from backend.security import audit_logger

# All API calls are automatically logged
# View logs at: logs/audit.log
```

### Network Monitoring
```python
from backend.security import network_monitor

# Verify local-only operation
report = network_monitor.verify_local_only_operation()
print(f"Is local only: {report['is_local_only']}")
```

## 📁 Project Structure

```
chat-ver-1/
├── backend/
│   ├── agents/
│   │   ├── qa_tutor_agent.py      # Q&A Agent implementation
│   │   └── quiz_agent.py          # Quiz Agent implementation
│   ├── services/
│   │   ├── embedding_service.py   # Sentence transformers + ChromaDB
│   │   ├── ollama_service.py      # Ollama client
│   │   ├── document_processor.py  # PDF/DOCX/PPTX processing
│   │   └── web_search_service.py  # DuckDuckGo search
│   ├── security/
│   │   ├── encryption.py          # Data encryption
│   │   ├── audit_logger.py        # Audit logging
│   │   └── network_monitor.py     # Network monitoring
│   ├── config.py                  # Configuration
│   ├── models.py                  # Pydantic models
│   └── main.py                    # FastAPI app
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx      # Dashboard component
│   │   │   ├── QATutor.jsx        # Q&A interface
│   │   │   ├── QuizInterface.jsx  # Quiz interface
│   │   │   └── DocumentUpload.jsx # Document upload
│   │   ├── api/
│   │   │   └── api.js             # API client
│   │   ├── App.jsx                # Main app component
│   │   ├── main.jsx               # React entry point
│   │   └── index.css              # Global styles
│   ├── package.json
│   └── vite.config.js
├── data/
│   ├── documents/                 # Source documents
│   ├── uploads/                   # Uploaded files
│   └── chroma_db/                 # Vector database
├── logs/                          # Application logs
├── requirements.txt
├── .env.example
└── README.md
```

## 🎓 Sample Network Security Topics

## 🐳 Running with Docker (portable / any machine)

These steps let you run the entire stack (frontend, backend, Ollama) with Docker Compose so the app works the same on any machine with Docker.

Prerequisites:
- Docker Engine & Docker Compose (Docker Desktop on macOS/Windows or docker + compose plugin on Linux)

1) Build images and start the stack

```zsh
# From project root
docker compose pull        # (optional) pull images like the Ollama image
docker compose build       # build backend/frontend images (backend image includes pre-baked embedding model)
docker compose up -d --build       # start all services (frontend, backend, ollama). '--build' ensures images are rebuilt when needed.
```

2) Pull / preload the Ollama model (one-time, large download)

Ollama models are large. Pull the model into the Ollama container so the backend sees it as available:

```zsh
# Pull the model into the running ollama container
docker compose exec ollama ollama pull llama3.2:3b

# You can tail the logs to watch progress
docker compose logs -f ollama
```

3) Monitor services and verify health

```zsh
# Show running containers
docker compose ps

# Tail logs for backend and frontend
docker compose logs -f backend frontend

# Check health endpoint
curl -s http://localhost:8000/health | jq .
```

4) Notes & tips for portability

- The backend image pre-downloads the SentenceTransformers embedding model at build time to reduce cold-start latency. This increases image size but avoids runtime downloads.
- Ollama still needs to pull its Llama model at runtime. Consider using a smaller or quantized model if you want much faster downloads and lower memory usage.
- If you're on macOS and the backend should talk to an Ollama running on your host (not in Docker), set `OLLAMA_BASE_URL` to `http://host.docker.internal:11434` in `docker-compose.yml` or in a `.env` file.
- If Docker Compose complains about the `version:` field being obsolete, you can safely remove the top-level `version:` line from `docker-compose.yml` (the compose plugin uses the file contents directly).

5) Troubleshooting

- If the backend startup is slow, ensure the pre-baked image was used (`docker compose build` after changing Dockerfile). Logs will show whether the embedding model download happened at build-time or runtime.
- If Ollama reports the model as missing, run the `docker compose exec ollama ollama pull <model>` command above and wait for it to finish.
- For persistent Ollama / model storage across container restarts, add a host volume for Ollama's model directory in `docker-compose.yml`.

6) Optional: warm models on startup

If you want the system to be fully responsive immediately after compose up, you can trigger the background warmers (the backend includes a lazy loader and background preloader). Alternatively you can add a simple warm endpoint or call `/health` repeatedly until models are ready.

The bot can answer questions and generate quizzes on:

- Network fundamentals (TCP/IP, OSI model)
- Firewalls and packet filtering
- Encryption (symmetric, asymmetric, hashing)
- Authentication and access control
- VPNs and secure tunneling
- Intrusion Detection/Prevention Systems (IDS/IPS)
- Common attacks (DDoS, MITM, phishing, SQL injection)
- Wireless security (WPA, WPA2, WPA3)
- Network protocols (SSL/TLS, IPSec, SSH)
- Security policies and best practices

## 🐛 Troubleshooting

### Ollama not available
```bash
# Start Ollama service
ollama serve

# Verify model is installed
ollama list

# Pull model if missing
ollama pull llama3.2:3b
```

### ChromaDB errors
```bash
# Clear and reinitialize
curl -X DELETE http://localhost:8000/api/documents/clear
```

### Frontend can't connect to backend
- Verify backend is running on port 8000
- Check CORS settings in `backend/main.py`
- Try accessing `http://localhost:8000/health` directly

### Low quality quiz questions
- Upload more diverse documents
- Increase document pool size
- Try different topics

## 🚀 Performance Optimization

### For faster inference:
1. Use GPU acceleration with Ollama (if available)
2. Reduce `num_questions` for quizzes
3. Use smaller embedding model
4. Limit context retrieval to top 3-5 results

### For better accuracy:
1. Upload high-quality, comprehensive documents
2. Include multiple sources on each topic
3. Enable web search for supplementary information
4. Increase similarity threshold for grading

## 📄 License

This project is created for educational purposes.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📧 Support

For questions or issues, please open a GitHub issue or contact the development team.

---

*Privacy-First • Locally-Powered • AI-Enhanced*

**Docker-Commands**

docker compose exec ollama ollama pull llama3.2:3b
docker compose build frontend
docker compose build backend
docker compose up -d --build
docker compose ps
docker compose logs --tail 200 backend frontend ollama
curl -sS http://localhost:8000/health


