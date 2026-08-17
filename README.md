# 🛡️ Ransomware Detection Framework

A Python-based defensive cybersecurity framework designed to detect suspicious file-system behavior associated with ransomware activity.

The framework combines multiple detection signals including:

- File entropy analysis
- Mass file activity detection
- Suspicious file-extension detection
- Risk scoring
- File-system monitoring
- Security event logging

Developed by **MUZAFFAR MUSHTAQ**.

---

## 1. 📌 Project Overview

The Ransomware Detection Framework is an educational and defensive cybersecurity project that monitors file-system activity and identifies suspicious behavior.

Instead of relying on a single detection method, the framework combines multiple indicators to improve detection confidence.

The main detection signals are:

1. High file entropy
2. Suspicious file extensions
3. Mass file activity

These signals are combined by the Risk Engine to produce a numerical risk score and risk level.

### Risk Levels

| Risk Score | Risk Level |
|---:|---|
| 0–29 | LOW |
| 30–69 | MEDIUM |
| 70–100 | CRITICAL |

---

## 2. 🎯 Project Objectives

The main objectives of this project are:

- Learn defensive ransomware detection techniques
- Monitor file-system activity
- Analyze file entropy
- Detect suspicious file extensions
- Detect mass file activity
- Combine multiple security indicators
- Generate risk scores
- Log security events
- Build a modular Python security framework
- Practice Linux and Git/GitHub development

---

## 3. 🏗️ Project Architecture

The framework follows a modular detection architecture:

```text
                    ┌──────────────────────┐
                    │     File System      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    File Monitor      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Detection Engine    │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
      │   Entropy   │   │   Activity  │   │  Extension  │
      │   Analyzer  │   │   Detector   │   │  Detector   │
      └──────┬──────┘   └──────┬──────┘   └──────┬──────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │     Risk Engine      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Risk Classification│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Logger         │
                    └──────────────────────┘
4.## 🔍 Detection Components

The framework consists of several independent components that work together.

Component	Purpose
File Monitor	Watches the monitored directory
Entropy Analyzer	Measures file randomness
Activity Detector	Detects mass file activity
Extension Detector	Identifies suspicious extensions
Detection Engine	Combines detection signals
Risk Engine	Calculates the final risk score
Logger	Records security events
Configuration	Stores configurable settings

The components are implemented as separate Python modules to keep the framework modular and easier to maintain.

5. ##📊 Entropy Analyzer

The entropy analyzer calculates the Shannon entropy of a file.

Entropy measures how random the data inside a file appears to be.

Higher entropy can be associated with encrypted or compressed data.

The framework uses the following default threshold:

7.5
Normal File Example

A normal text file produced a relatively low entropy value:

entropy = 3.8389
high_entropy = False
High-Entropy Test Example

A controlled high-entropy test file produced:

entropy = 7.9568
high_entropy = True

The entropy analyzer is implemented in:

src/entropy_analyzer.py
6. 📈 Activity Detector

The activity detector monitors file events within a configurable time window.

Default configuration:

Activity threshold: 20 files
Time window: 10 seconds

If a large number of unique files are created or modified within the configured time window, the framework marks the activity as suspicious.

Normal Activity
unique_files = 1
mass_activity = False
Suspicious Mass Activity

During the combined detection test, the framework detected:

mass_activity = True

The activity detector is implemented in:

src/activity_detector.py
7. 🔐 Extension Detector

The extension detector checks whether a file uses an extension configured as suspicious.

Test Examples
document.txt       → suspicious=False
important.locked   → suspicious=True
backup.encrypted   → suspicious=True

The extension detector is implemented in:

src/extension_detector.py
Test Command
python src/extension_detector.py
Expected Output
----- EXTENSION DETECTOR TEST -----
document.txt | extension=.txt | suspicious=False
important.locked | extension=.locked | suspicious=True
backup.encrypted | extension=.encrypted | suspicious=True
8. ⚖️ Risk Engine

The risk engine combines the detection signals into a numerical risk score.

The current scoring model is:

Detection Signal	Score
Suspicious Extension	+20
High Entropy	+30
Mass File Activity	+40

The maximum theoretical score is:

100
Example
Suspicious extension = 20
High entropy         = 30
Mass activity        = 40


Total = 90/100

The risk engine is implemented in:

src/risk_engine.py
9. 🧠 Detection Engine

The detection engine is the central component that combines the different detection modules.

It performs the following operations:

Validates the file
Records file activity
Calculates entropy
Checks suspicious characteristics
Calculates the risk score
Determines the risk level
Returns the detection result

The detection engine is implemented in:

src/detector.py
Example Normal Result
file: data/detection_test.txt
event_type: modified
entropy: 3.8389
high_entropy: False
unique_files: 1
mass_activity: False
extension: .txt
suspicious_extension: False
risk_score: 0
risk_level: LOW
10. 👁️ File Monitor

The file monitor watches the configured directory for file-system activity.

It detects events such as:

created
modified

When a file-system event occurs, the file is passed to the detection engine.

The detection engine then analyzes the file and generates a risk result.

The file monitor is implemented in:

src/file_monitor.py
11. 📝 Logger

The logging component records detection events for later analysis.

Example log:

INFO | DETECTION |
file=/home/muzaffar/ransomware-detection-framework/data/test.locked |
event=modified |
entropy=7.9568 |
mass_activity=True |
risk_score=90 |
risk_level=CRITICAL

The logger is implemented in:

src/logger.py

Runtime logs are stored under:

results/

The project excludes runtime log files from Git tracking through .gitignore.

12. ⚙️ Configuration

Project configuration is stored in:

config/config.yaml

Important configurable values include:

Entropy threshold
Activity threshold
Monitoring time window
Monitoring settings

Example configuration:

entropy_threshold: 7.5
activity_threshold: 20
time_window: 10

Configuration allows detection behavior to be adjusted without changing the main detection logic.

13. 📥 Installation
Clone the Repository
git clone https://github.com/mushtaqmuzaffar875-a11y/Ransomware-Detection-Framework.git
Enter the Project Directory
cd ransomware-detection-framework
Create Virtual Environment
python3 -m venv venv
Activate Virtual Environment
source venv/bin/activate
Install Dependencies

If a requirements.txt file is available:

pip install -r requirements.txt
14. ▶️ Running the Framework

Run the framework from the project root:

python src/main.py

Expected startup output:

==========================================================
       RANSOMWARE DETECTION FRAMEWORK
==========================================================
       Developed by: MUZAFFAR MUSHTAQ
==========================================================


[+] Monitoring: /home/muzaffar/ransomware-detection-framework/data
[+] Detection engine: ACTIVE
[+] Logging: ACTIVE
[+] Press Ctrl+C to stop.

The framework will continue monitoring until stopped with:

Ctrl+C
15. 🧪 Individual Component Testing
Extension Detector Test

Run:

python src/extension_detector.py

Expected output:

----- EXTENSION DETECTOR TEST -----
document.txt | extension=.txt | suspicious=False
important.locked | extension=.locked | suspicious=True
backup.encrypted | extension=.encrypted | suspicious=True
Detection Engine Test

Run:

python src/detector.py

Example result:

----- DETECTION ENGINE TEST -----
file: data/detection_test.txt
event_type: modified
entropy: 3.8389
high_entropy: False
unique_files: 1
mass_activity: False
extension: .txt
suspicious_extension: False
risk_score: 0
risk_level: LOW
Suspicious Extension Test

Run:

python -c "from src.detector import DetectionEngine; d=DetectionEngine(); print(d.analyze_file('data/test_document.locked'))"

Expected result:

extension: .locked
suspicious_extension: True
risk_score: 20
risk_level: LOW
High Entropy Test

Run:

python -c "from src.detector import DetectionEngine; d=DetectionEngine(); print(d.analyze_file('data/high_entropy_test.locked'))"

Expected result:

entropy: 7.9568
high_entropy: True
extension: .locked
suspicious_extension: True
risk_score: 50
risk_level: MEDIUM
16. 🔬 Combined Detection Test

The framework was tested using multiple harmless test files containing several suspicious indicators.

The combined test included:

Suspicious Extension
        +
High Entropy
        +
Mass File Activity

The framework detected the combined behavior with a high risk score.

Example:

entropy=7.9496
mass_activity=True
risk_score=90
risk_level=CRITICAL

Example detection output:

[DETECTION] CREATED  | Risk: CRITICAL | Score: 90/100

Modified event:

[DETECTION] MODIFIED | Risk: CRITICAL | Score: 90/100

This demonstrates the framework's multi-signal detection approach.

17. 📊 Test Results
Normal File
File:
data/detection_test.txt


Entropy:
3.8389


High Entropy:
False


Mass Activity:
False


Suspicious Extension:
False


Risk Score:
0/100


Risk Level:
LOW
Suspicious Extension
File:
data/test_document.locked


Entropy:
3.4859


High Entropy:
False


Mass Activity:
False


Suspicious Extension:
True


Risk Score:
20/100


Risk Level:
LOW
High Entropy + Suspicious Extension
File:
data/high_entropy_test.locked


Entropy:
7.9568


High Entropy:
True


Mass Activity:
False


Suspicious Extension:
True


Risk Score:
50/100


Risk Level:
MEDIUM
Combined Suspicious Activity
Entropy:
approximately 7.95


High Entropy:
True


Mass Activity:
True


Suspicious Extension:
True


Risk Score:
90/100


Risk Level:
CRITICAL
18. 🎯 Risk Scoring

The framework uses multiple signals to calculate the final risk score.

Detection Signal	Score
Suspicious Extension	+20
High Entropy	+30
Mass File Activity	+40
No Suspicious Indicators
0 + 0 + 0 = 0
Suspicious Extension
20 + 0 + 0 = 20
Suspicious Extension + High Entropy
20 + 30 + 0 = 50
Suspicious Extension + High Entropy + Mass Activity
20 + 30 + 40 = 90
Risk Classification
0–29   → LOW
30–69  → MEDIUM
70–100 → CRITICAL
19. 🚨 Example Detection Logs
Medium Risk
INFO | DETECTION |
file=/home/muzaffar/ransomware-detection-framework/data/combined_test/test_1.locked |
event=created |
entropy=7.9512 |
mass_activity=False |
risk_score=50 |
risk_level=MEDIUM

Console:

[DETECTION] CREATED | Risk: MEDIUM | Score: 50/100
Critical Risk
INFO | DETECTION |
file=/home/muzaffar/ransomware-detection-framework/data/combined_test/test_20.locked |
event=created |
entropy=7.9496 |
mass_activity=True |
risk_score=90 |
risk_level=CRITICAL

Console:

[DETECTION] CREATED  | Risk: CRITICAL | Score: 90/100

Modified event:

[DETECTION] MODIFIED | Risk: CRITICAL | Score: 90/100
20. 📁 Project Structure
ransomware-detection-framework/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── detection_test.txt
│   ├── high_entropy_test.locked
│   ├── safe_test.txt
│   ├── test_document.locked
│   └── test files
│
├── results/
│   └── ransomware_detection.log
│
├── simulator/
│   └── safe_activity_simulator.py
│
├── src/
│   ├── __init__.py
│   ├── activity_detector.py
│   ├── detector.py
│   ├── entropy_analyzer.py
│   ├── extension_detector.py
│   ├── file_monitor.py
│   ├── logger.py
│   ├── main.py
│   └── risk_engine.py
│
├── .gitignore
└── README.md
21. 🔐 Safety

This project is intended for:

Cybersecurity education
Defensive security research
File-system monitoring research
Ransomware detection experiments
Security laboratory environments
Python security automation learning

Testing should be performed using harmless test files and controlled laboratory data.

This project does not require executing real ransomware.

Do not test against systems, files, or networks without authorization.

22. ⚠️ Limitations

This framework is an educational and research-oriented detection system.

It should not be considered a replacement for a complete enterprise endpoint security solution.

Possible limitations include:

False positives
False negatives
Entropy alone cannot identify ransomware
Suspicious extensions can also be legitimate
Mass file activity can occur during normal operations
Detection thresholds may require tuning
The framework does not guarantee complete ransomware detection
Advanced ransomware may use behavior that is not covered by the current rules

The framework therefore combines multiple indicators to improve detection confidence.

23. 🔮 Future Improvements

Potential future improvements include:

Machine-learning based ransomware detection
Process behavior monitoring
File-hash analysis
YARA rule integration
Improved anomaly detection
More advanced behavioral analysis
Configurable extension lists
Configurable risk weights
Alert notifications
Email alerts
Web-based monitoring dashboard
Database-backed event storage
Automatic incident reports
File quarantine capabilities
Process identification
Advanced event correlation
Historical detection analytics
24. 🧰 Technologies Used

The project uses:

Python 3
Linux
Kali Linux
File-system monitoring
Shannon entropy
Behavioral detection
Risk scoring
YAML configuration
Python virtual environment
Git
GitHub
25. 🎓 Learning Objectives

This project demonstrates practical cybersecurity concepts including:

Defensive cybersecurity
Ransomware behavior analysis
File-system monitoring
File entropy analysis
Suspicious extension detection
Behavioral anomaly detection
Risk-based security decisions
Security event logging
Python programming
Modular software architecture
Linux security tooling
Git and GitHub project management
26. 👨‍💻 Author

MUZAFFAR MUSHTAQ

Cybersecurity Student / Cybersecurity Aspirant

This project was developed as part of practical cybersecurity learning and defensive security research.

27. 📄 License

This project is intended for educational and defensive cybersecurity research purposes.

Use responsibly and only in authorized environments.

No real ransomware is required or included for testing.

⭐ Project Summary

The Ransomware Detection Framework demonstrates how multiple security signals can be combined to identify suspicious file behavior.

The framework analyzes:

File Activity
      ↓
Entropy
      ↓
File Extension
      ↓
Mass Activity
      ↓
Risk Score
      ↓
Risk Level
      ↓
Security Log

Example:

.locked extension
       +
High entropy
       +
Mass file activity
       ↓
Risk Score: 90/100
       ↓
CRITICAL

The project provides a practical foundation for learning ransomware detection, behavioral monitoring, Python security automation, and defensive cybersecurity engineering.

🌟 Final Status

Project Status: Completed and Tested

Tested components:

[✓] Entropy Analyzer
[✓] Activity Detector
[✓] Extension Detector
[✓] Risk Engine
[✓] Detection Engine
[✓] File Monitor
[✓] Logger
[✓] Main Framework
[✓] Individual Tests
[✓] Combined Detection Test
[✓] Critical Risk Detection

Developed by MUZAFFAR MUSHTAQ

