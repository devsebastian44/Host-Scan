# Host-Scan Architecture Diagram

This document illustrates the high-level architecture, thread lifecycle, and DevSecOps isolation flow of the **Host-Scan** project.

---

## 🏗️ 1. Core Execution Flow

The core engine uses `concurrent.futures.ThreadPoolExecutor` to perform ultra-fast, concurrent socket evaluations across TCP and UDP protocols.

```mermaid
graph TD
    A[Usuario / Sistema Base] -->|Inicia scan.py| B[Host Scan Engine]
    B -->|Pregunta por IP Target| C([Entrada IP])
    B -->|Ajusta ulimit -n 5100| D{ThreadPoolExecutor\nMax Workers: 5000}
    D -->|Mapeo TCP| E(Thread Pool: TCP)
    D -->|Mapeo UDP| F(Thread Pool: UDP)
    
    E -->|s.connect| G[TCP Ports 1-65535]
    F -->|DNS Query si port=53 o b''| H[UDP Ports 1-65535]
    
    G -->|Abierto| I((Puerto Añadido a Lista TCP))
    H -->|Abierto| J((Puerto Añadido a Lista UDP))
    
    I --> K[Sincronización Final]
    J --> K
    
    K --> L[xclip: Copia puertos resultantes a Portapapeles del SO]
```

## 🛡️ 2. DevSecOps & Pipeline Flow

Demonstration of how the laboratory code separates into public portfolio and private execution.

```mermaid
sequenceDiagram
    participant Dev local
    participant GitLab (Private)
    participant PowerShell (Sanitization)
    participant GitHub (Public)

    Dev local->>GitLab (Private): Push full code (tests, configs, scripts, pipeline)
    rect rgb(30, 30, 60)
    Note over GitLab (Private): CI/CD Execution
    GitLab (Private)->>GitLab (Private): flake8 (Linting)
    GitLab (Private)->>GitLab (Private): pytest (Automated testing)
    GitLab (Private)->>GitLab (Private): bandit (Static security check - SAST)
    end
    
    Dev local->>PowerShell (Sanitization): Runs `publish_public.ps1`
    Note over PowerShell (Sanitization): Orchestration started on branch 'main'
    PowerShell (Sanitization)->>PowerShell (Sanitization): Create detached branch 'public'
    PowerShell (Sanitization)->>PowerShell (Sanitization): git rm --cached 'tests/', 'configs/', 'scripts/', '.gitlab-ci.yml'
    PowerShell (Sanitization)->>GitHub (Public): Force push branch public:main (Sanitized code)
    PowerShell (Sanitization)->>Dev local: Return to branch 'main' securely
```

## 🔐 3. Configuration Management Strategy

Environmental configurations strictly handled via `configs/` folder and ignored by Git to avoid secrets leakage.

```mermaid
graph LR
    A[Entorno de Sistema] -->|.env File Local| B(configs/.env)
    B -.->|GITIGNORE| C[🚫 Repositorio GitLab/GitHub]
    D[Pipeline GitLab CI] -->|Secret Variables UI| E{Inyectado en Runtime}
    E --> F((scan.py execution))
    B --> F
```
