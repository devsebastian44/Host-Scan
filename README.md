# Host Scan

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)
![Concurrencia](https://img.shields.io/badge/Concurrencia-ThreadPoolExecutor-FF6F00?style=flat&logo=python&logoColor=white)
![Scope](https://img.shields.io/badge/Scope-OSINT%20%7C%20Pentesting-8B0000?style=flat&logo=hackthebox&logoColor=white)
![Bandit](https://img.shields.io/badge/SAST-Bandit-FF6F00?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Testing-Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat&logo=github-actions&logoColor=white)

---

> [!IMPORTANT]
> **This project is for educational and ethical cybersecurity purposes only.**
> Unauthorized scanning of systems is illegal and unethical. Use it only on networks and systems where you have explicit, written authorization.

---

## 🧠 Overview

**Host Scan** is a professional network reconnaissance tool developed in **Python 3**. It enables efficient analysis of open ports (TCP/UDP) on remote hosts using optimized concurrency with `ThreadPoolExecutor`.

The project is designed with a **DevSecOps** mindset, featuring automated linting, security analysis, and unit testing to ensure code quality and safety.

## ⚙️ Features

- **TCP/UDP Port Scanning** — High-speed scanning using low-level socket connections.
- **Concurrent Execution** — Optimized thread pool management for rapid results.
- **Service Identification** — Basic mapping of open ports to standard services.
- **Modular Architecture** — Clean separation between core logic and CLI interaction.
- **CI/CD Integrated** — Automated validation via GitHub Actions.

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.8+ |
| Concurrency | `concurrent.futures.ThreadPoolExecutor` |
| Sockets | `socket` (Python stdlib) |
| SAST | Bandit |
| Testing | Pytest |
| Linting | Flake8 |
| CI/CD | GitHub Actions |

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- Linux (Debian, Ubuntu, Arch) or Android (Termux) recommended

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/devsebastian44/Host-Scan.git
cd Host-Scan

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r configs/requirements.txt
pip install -r configs/requirements-dev.txt
```

## ▶️ Usage

Run the scanner from the terminal:

```bash
python3 src/scan.py
```

### Running Tests & Quality Checks

```bash
# Run unit tests
pytest tests/

# Security analysis (SAST)
bandit -r src/

# Linting check
flake8 src/
```

## 📁 Project Structure

```
Host-Scan/
├── src/
│   └── scan.py           # Core scanner logic and CLI
├── tests/
│   └── test_scan.py      # Unit tests with socket mocking
├── configs/
│   ├── requirements.txt  # Production dependencies
│   └── requirements-dev.txt # Development dependencies
├── diagrams/             # Architecture diagrams
├── .github/workflows/    # CI/CD configuration
└── README.md             # Project documentation
```

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create.

1. **Fork** the Project
2. **Create your Feature Branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your Changes** (`git commit -m 'feat: Add some AmazingFeature'`)
4. **Push to the Branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Commitment to Quality
- Ensure all tests pass.
- Follow PEP-8 guidelines.
- Use Conventional Commits.

## 📄 License

Distributed under the Apache License 2.0. See `LICENSE` for more information.

## 👨‍💻 Author

**Sebastian Zhunaula** - [@devsebastian44](https://github.com/devsebastian44)