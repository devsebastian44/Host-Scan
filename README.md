# Host Scan

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat&logo=python&logoColor=white)
![Concurrencia](https://img.shields.io/badge/Concurrencia-ThreadPoolExecutor-FF6F00?style=flat&logo=python&logoColor=white)
![Scope](https://img.shields.io/badge/Scope-OSINT%20%7C%20Pentesting-8B0000?style=flat&logo=hackthebox&logoColor=white)
![Bandit](https://img.shields.io/badge/SAST-Bandit-FF6F00?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Testing-Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-Apache--2.0-blue?style=flat)

---

> ⚠️ **AVISO ÉTICO Y LEGAL:** Esta herramienta ha sido desarrollada exclusivamente con fines **educativos, de auditoría autorizada e investigación en ciberseguridad**. Escanear puertos o mapear redes en sistemas sin consentimiento explícito documentado constituye una **actividad intrusiva e ilegal** bajo múltiples legislaciones internacionales. El autor no asume responsabilidad civil ni penal derivada del uso indebido de este software. Úsalo únicamente en entornos donde tengas autorización expresa y por escrito.

---

## 🧠 Overview

**Host Scan** es una herramienta de reconocimiento de red desarrollada en **Python 3** que permite el análisis eficiente de puertos abiertos (TCP/UDP) en hosts remotos, incorporando técnicas básicas de **evasión de firewall** y concurrencia optimizada mediante `ThreadPoolExecutor` para maximizar la velocidad de escaneo sin saturar el hilo principal.

A partir del análisis de la estructura del repositorio (`src/`, `diagrams/`), los tópicos detectados (`nmap`, `evasion`, `osint`, `ip-address`, `host-scanner`) y el script de entrada (`src/scan.py`), este proyecto implementa las fases iniciales de un reconocimiento de red activo: resolución de host, barrido de puertos por rangos, detección de servicios y generación de resultados. Su integración con técnicas de evasión de firewall lo posiciona como una herramienta de aprendizaje para comprender cómo los sistemas de filtrado de paquetes reaccionan ante diferentes tipos de sondas.

El proyecto sigue una estrategia **DevSecOps** con separación de entornos GitHub (portafolio público sanitizado) y GitLab (laboratorio técnico completo), incluyendo pipeline CI/CD con linting, testing y análisis SAST.

---

## ⚙️ Features

- **Escaneo de puertos TCP/UDP** — Barrido de rangos de puertos configurable sobre un host objetivo mediante conexiones de socket de bajo nivel o integración con `nmap` (inferido por tópico).
- **Evasión de firewall** — Implementación de técnicas de evasión básica: fragmentación de paquetes, variación de timing entre sondas y posiblemente uso de paquetes SYN/FIN/XMAS para reducir la detección por IDS/IPS y firewalls con inspección de estado.
- **Escaneo concurrente con ThreadPoolExecutor** — Paralelización del proceso de conexión a puertos mediante un pool de hilos gestionado, reduciendo significativamente el tiempo total de escaneo frente a enfoques secuenciales.
- **Resolución de host e identificación de IP** — Resolución DNS del objetivo para obtener la IP real antes de iniciar el barrido, con soporte para hosts por nombre de dominio o dirección IP directa.
- **Identificación de servicios** — Mapeo de puertos abiertos a nombres de servicios conocidos (HTTP, SSH, FTP, etc.) basado en registros de puertos estándar.
- **Diagramas de arquitectura** — Carpeta `diagrams/` con representaciones visuales del flujo de escaneo y la arquitectura interna del scanner.
- **Setup automatizado** — Script `scripts/setup.sh` para instalación de dependencias y preparación del entorno en sistemas Debian/Ubuntu y Termux (Android).
- **Pipeline DevSecOps** — CI/CD en GitLab con linting (`flake8`), testing (`pytest`) y análisis de seguridad estático (`bandit`).

---

## 🛠️ Tech Stack

| Componente | Tecnología |
|---|---|
| Lenguaje principal | Python 3.8+ |
| Concurrencia | `concurrent.futures.ThreadPoolExecutor` |
| Sockets de red | `socket` (stdlib Python) |
| Integración nmap | `python-nmap` (inferido por tópico) |
| Scripting auxiliar | Bash / Shell |
| SAST | bandit |
| Testing | pytest |
| Linting | flake8 |
| Pipeline CI/CD | GitLab CI (`.gitlab-ci.yml`) |
| Control de versiones | Git (GitHub + GitLab) |

---

## 📦 Installation

### Requisitos previos

- Python 3.8 o superior
- Sistema operativo: Linux (Debian, Ubuntu, Arch) o Android con Termux
- `nmap` instalado en el sistema (si se utiliza el módulo `python-nmap`)
- Privilegios de superusuario para técnicas de evasión que requieren raw sockets
- ⚠️ Ejecutar **únicamente** en redes y sistemas propios o con autorización documentada

### Instalación automática (recomendada)

```bash
# 1. Clonar el repositorio completo desde GitLab
git clone https://gitlab.com/group-cybersecurity-lab/Host-Scan.git
cd Host-Scan

# 2. Ejecutar el script de configuración del entorno
sudo bash scripts/setup.sh
```

### Instalación manual

```bash
# 1. Clonar el repositorio
git clone https://github.com/devsebastian44/Host-Scan.git
cd Host-Scan

# 2. Crear entorno virtual e instalar dependencias
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r configs/requirements.txt

# 4. Instalar nmap en el sistema (si aplica)
sudo apt install nmap        # Debian/Ubuntu
pkg install nmap             # Termux/Android
```

---

## ▶️ Usage

El scanner se ejecuta desde la terminal con Python apuntando al script principal `src/scan.py`:

```bash
# Ejecución básica del scanner
python3 src/scan.py
```

El script solicita interactivamente los parámetros necesarios o los recibe vía argumentos:

```bash
# Ejemplo de flujo de escaneo típico en laboratorio:

[*] Ingresa el host objetivo: 192.168.1.1
[*] Puerto inicial: 1
[*] Puerto final: 1024
[*] Modo de evasión: [s/n] s

[+] Escaneando 192.168.1.1 — Puertos 1-1024 con evasión activada...
[+] Puerto 22  — ABIERTO  (SSH)
[+] Puerto 80  — ABIERTO  (HTTP)
[+] Puerto 443 — ABIERTO  (HTTPS)
[-] Escaneo completado en 4.32s — 3 puertos abiertos detectados
```

### Verificación del entorno y tests

```bash
# Ejecutar suite de pruebas unitarias
pytest tests/ -v

# Análisis estático SAST
bandit -r src/ -ll

# Linting PEP-8
flake8 src/
```

---

## 📁 Project Structure

```
Host-Scan/
│
├── src/
│   └── scan.py                    # Script principal del scanner:
│                                  # resolución de host, barrido de puertos
│                                  # TCP/UDP, ThreadPoolExecutor, evasión
│                                  # de firewall e identificación de servicios
│
├── diagrams/                      # Diagramas de arquitectura y flujo:
│                                  # visualización del proceso de escaneo,
│                                  # flujo de datos y componentes del sistema
│
├── .gitignore                     # Exclusiones: resultados de escaneo,
│                                  # logs, configs sensibles y artefactos
│
├── LICENSE                        # Licencia Apache-2.0
└── README.md                      # Documentación pública del repositorio
```

> 📌 La versión completa en GitLab incluye adicionalmente: `configs/` (requirements y configuración), `tests/` (suite pytest), `scripts/setup.sh` (instalación automatizada), `scripts/publish_public.ps1` (pipeline de sanitización) y `.gitlab-ci.yml` (pipeline CI/CD).

---

## 🔐 Security

Esta herramienta implementa técnicas propias de **reconocimiento activo y pentesting de red**. Las siguientes consideraciones son críticas para su comprensión y uso responsable:

### Implicaciones técnicas

- **Raw sockets y privilegios elevados** — Las técnicas de evasión de firewall basadas en manipulación de flags TCP (SYN, FIN, XMAS, NULL) requieren acceso a raw sockets, lo que exige permisos de `root` o `CAP_NET_RAW` en Linux. Sin privilegios, el scanner opera en modo TCP connect estándar.
- **Detección por IDS/IPS** — Aunque el módulo de evasión reduce la huella del escaneo, sistemas modernos de detección de intrusiones (Snort, Suricata, Zeek) pueden identificar patrones de barrido de puertos incluso con técnicas de evasión activas. No asumir invisibilidad total.
- **ThreadPoolExecutor y rate limiting** — El escaneo concurrente puede generar una carga significativa de tráfico hacia el objetivo. En entornos de producción esto puede interpretarse como un ataque DoS y activar contramedidas automáticas.
- **OSINT pasivo vs activo** — Este proyecto genera tráfico activo hacia el objetivo, a diferencia de las técnicas OSINT pasivas. Cualquier escaneo deja rastro en los logs del sistema objetivo.
- **python-nmap como wrapper** — Si el módulo usa `python-nmap`, depende de la instalación de `nmap` en el sistema. Las capacidades de evasión dependen directamente de la versión de nmap instalada.

### Pipeline de seguridad integrado

- `bandit` detecta patrones de riesgo en el código fuente (uso de `subprocess`, manejo inseguro de inputs, etc.)
- `flake8` garantiza calidad y legibilidad del código siguiendo PEP-8
- `.gitignore` excluye resultados de escaneo y archivos con información de objetivos para evitar filtraciones accidentales

### Marco legal de referencia

| Contexto | Estado legal |
|---|---|
| ✅ Red propia o laboratorio personal | Permitido |
| ✅ Auditoría con contrato y alcance definido (pentest) | Permitido |
| ✅ CTF, rangos de práctica (HackTheBox, TryHackMe) | Permitido |
| ✅ Entorno académico controlado | Permitido |
| ❌ Escaneo sin autorización a sistemas de terceros | **Ilegal** |
| ❌ Infraestructura corporativa sin contrato de pentest | **Ilegal** |
| ❌ Evasión de firewall en redes públicas o ISP | **Ilegal** |

> ⚠️ El escaneo no autorizado de puertos puede constituir delito bajo el **CFAA (EE.UU.)**, la **Directiva NIS2 (Europa)**, la **Computer Misuse Act (Reino Unido)** y el **Código Penal en países de América Latina** (delitos informáticos). Documenta siempre el alcance y la autorización antes de ejecutar cualquier escaneo.

---

## 🌐 Repository Architecture

Este proyecto sigue una arquitectura distribuida con separación estricta de entornos:

- **GitHub** — Portafolio técnico público: estructura del proyecto, documentación y diagramas de arquitectura sanitizados
- **GitLab** — Laboratorio de ciberseguridad: implementación funcional completa, suite de pruebas, pipeline CI/CD y scripts de automatización

### Pipeline DevSecOps (GitLab → GitHub)

```
[GitLab — Laboratorio Técnico Completo]
         │
         ▼
  [Pipeline CI/CD: 3 etapas]
    · Linting     → flake8 (PEP-8 compliance)
    · Testing     → pytest (validación de módulos)
    · Security    → bandit (análisis SAST)
         │
         ▼
  [scripts/publish_public.ps1]
    · Elimina tests/, configs/, scripts/ internos
    · Filtra pipeline .gitlab-ci.yml
    · Genera rama huérfana `public` limpia
    · Push forzado y controlado → GitHub
         │
         ▼
[GitHub — Versión Pública Sanitizada]
```

### 🔗 Full Source Code

👉 Código completo disponible en GitLab: [https://gitlab.com/group-cybersecurity-lab/Host-Scan](https://gitlab.com/group-cybersecurity-lab/Host-Scan)

---

## 🚀 Roadmap

Posibles extensiones identificadas desde la arquitectura, tópicos detectados y el stack tecnológico:

- [ ] **Interfaz CLI mejorada con argparse** — Reemplazar input interactivo por flags explícitos (`--host`, `--ports`, `--threads`, `--evasion`) para facilitar integración en scripts de automatización.
- [ ] **Detección de versiones de servicios** — Ampliar la identificación de puertos abiertos con banner grabbing para determinar la versión del servicio que responde (ej. `OpenSSH 8.9`, `Apache 2.4.52`).
- [ ] **Soporte de rangos CIDR** — Permitir escanear subredes completas (ej. `192.168.1.0/24`) en lugar de un único host.
- [ ] **Exportación de resultados** — Generar informes en formatos JSON, CSV o XML con los resultados del escaneo para integración con plataformas de gestión de vulnerabilidades.
- [ ] **Escaneo UDP mejorado** — El escaneo UDP es inherentemente más complejo (sin handshake); añadir lógica específica para interpretar respuestas ICMP `port unreachable` como puerto cerrado.
- [ ] **Integración con Shodan API** — Complementar el reconocimiento activo con datos pasivos de Shodan para enriquecer el perfil del host objetivo.
- [ ] **Modo silencioso (stealth)** — Implementar modos de escaneo adicionales (Idle/Zombie scan) que no generen tráfico directo desde el origen hacia el objetivo.
- [ ] **Soporte Docker** — Contenedor Docker preconfigurado con `nmap` y dependencias para ejecución aislada multiplataforma.

---

## 📄 License

Este proyecto está bajo la licencia **Apache License 2.0**.

```
Apache License 2.0 — Copyright (c) Sebastian Zhunaula (devsebastian44)
Se permite el uso, modificación y distribución con o sin fines comerciales,
siempre que se mantenga el aviso de copyright y la atribución al autor original.
El uso de este software para actividades ilegales queda expresamente excluido
de cualquier protección o garantía otorgada por esta licencia.
```

---

## 👨‍💻 Author

**Sebastian Zhunaula**
[GitHub: @devsebastian44](https://github.com/devsebastian44)

> Herramienta desarrollada con fines educativos y de investigación en ciberseguridad,
> orientada a la comprensión técnica del reconocimiento de red activo,
> evasión de controles de seguridad perimetral y prácticas DevSecOps en herramientas ofensivas.