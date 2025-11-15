# Future TO - Future Engineers
### World Robot Olympiad 2025

This repository contains all our hard work and resources necessary to build **'Tigresa del Oriente'** (Eastern Tigress), the autonomous robot developed by Team Future TO for the World Robot Olympiad Future Engineers category.

---

## Table of Contents
- [Team Information](#team-information)
- [About the Competition](#about-the-competition)
- [General Description of the Robot](#general-description-of-the-robot)
- [Software Architecture](#software-architecture)
  
---

## Team Information

**Team Name:** Future TO  
**Country:** El Salvador 🇸🇻  
**Coach:** Sergio Cuellar

### Team Members:
- **Manuel Vásquez** - Team Leader, Programming and Control Systems
- **Antonio Borst** - Mechanical Design and Construction
- **Daniel Salazar** - Technical Documentation and Compliance

  <img width="480" height="640" alt="image" src="https://github.com/user-attachments/assets/30f723d8-ead9-4799-beed-589bfc20c642" />

---

## About the Competition

The Future Engineers category challenges teams to design self-driving robots capable of navigating complex circuits autonomously. Our robot must complete two main challenges:

### Open Challenge
- Complete three laps around a circuit
- Navigate with randomly determined: circuit size, starting position, and direction of travel
- Detect and follow blue/orange lines to determine direction (clockwise/counterclockwise)

### Obstacle Challenge
- Navigate a fixed circuit layout
- Avoid randomly placed obstacles (red and green blocks)
- Make real-time decisions based on obstacle color and position

---

## General Description of the Robot

**Tigresa del Oriente** is built primarily using LEGO Technic components, enhanced with third-party sensors and processing units for advanced autonomous capabilities.

### Key Design Features:

**Differential Drive System**
- Utilizes LEGO Technic differential piece
- Allows wheels to rotate at different speeds during turns
- Provides stable and controlled movement through tight corners
- Distributes torque efficiently between rear wheels

**Steering System**
- Inspired by Haltenberger Linkage design
- Features gear reduction for enhanced precision
- Example: 10° motor rotation = 1° tire rotation (10:1 ratio)
- Minimizes the impact of minor motor positioning errors

**Autonomous Navigation**
- IMU-based precise turning (not time or distance-based)
- Multi-sensor fusion for environment perception
- Real-time decision making for obstacle avoidance
- Continuous repositioning to maintain centered trajectory


<img width="480" height="640" alt="image" src="https://github.com/user-attachments/assets/122e201e-83ff-4903-ac93-9a858525a70a" />

---

## Hardware Components

### Main Components
| Component | Model | Quantity | Purpose |
|-----------|-------|----------|---------|
| Main Controller | LEGO Mindstorms Inventor Hub | 1 | Central processing and motor control |
| Battery | Inventor Hub Battery | 1 | Primary power source |
| Drive Motor | LEGO Mindstorms Motor | 1 | Forward/backward movement |
| Steering Motor | LEGO Mindstorms Motor | 1 | Front wheel orientation |

### Sensors and Perception
| Sensor Type | Model | Quantity | Purpose |
|-------------|-------|----------|----------|
| Color Sensor | LEGO Mindstorms | 1 | Floor line detection (blue/orange) |
| Ultrasonic Sensors | LEGO Mindstorms | 2 | Lateral wall distance measurement |
| ToF Laser Sensors | VL53L0X | 3 | Precise distance measurement (1 front, 2 at 45°) |
| AI Camera | HuskyLens | 1 | Object and color detection at distance |
| IMU | Built into Inventor Hub | 1 | Precise angle measurement for turns |

### Additional Electronics
| Component | Purpose |
|-----------|---------|
| LMS-ESP32 Board | Sensor data processing and Hub communication |
| LED Lighting System | Controlled illumination for camera stability |
| AAA Battery Pack (6x) | Independent power for lighting system |
| Relay Module | Lighting control via ESP32 |
| Optocoupler | Safe relay activation |

---

## Software Architecture

### Programming Languages & Platforms
- **Main Program:** Python 3 with Pybricks (LEGO Inventor Hub)
- **Sensor Processing:** Python with Thonny (LMS-ESP32)

### Code Structure

**LEGO Inventor Hub (Main Controller)**
```
├── Motor Control Functions
│   ├── Steering calibration and control
│   ├── Drive motor management
│   └── IMU-based precise turning
│
├── Sensor Reading Functions
│   ├── Color sensor (HSV processing)
│   ├── Ultrasonic sensors (lateral positioning)
│   └── ESP32 data reception (PUPRemote)
│
├── Navigation Logic
│   ├── Open Challenge: Line detection and repositioning
│   ├── Obstacle Challenge: Object detection and avoidance
│   └── Continuous feedback loop
│
└── Main Execution Loop
    ├── Sensor data collection
    ├── Decision making
    └── Action execution
```

**LMS-ESP32 (Sensor Coprocessor)**
```
├── Sensor Data Acquisition
│   ├── VL53L0X ToF sensors (I²C)
│   ├── HuskyLens camera (UART)
│   └── Lighting system control
│
├── Data Processing
│   ├── Filter and validate readings
│   ├── Convert to LEGO-compatible format
│   └── Package for transmission
│
└── PUPRemote Communication
    └── Send processed data to Inventor Hub
```

### Key Programming Features

**Modular Design**
- Independent functions for each robot behavior
- Easy maintenance and debugging
- Clear separation of responsibilities

**Quasi-Asynchronous Operation**
- Multiple tasks appear to run simultaneously
- Sensor reading doesn't block movement
- Continuous decision-making cycle
- Rapid response to environmental changes

**Calibration Systems**
- Automatic steering calibration on startup
- Color sensor HSV threshold configuration
- Battery voltage monitoring (79% performance threshold)

**Navigation Algorithms**

*Open Challenge:*
- Calculate distance ratio: R = Right Distance / Left Distance
- Tolerance range: 0.58 ≤ R ≤ 1.67
- Corrective steering when outside tolerance
- Line detection triggers turn sequences

*Obstacle Challenge:*
- HuskyLens detects block color (red/green)
- Execute appropriate evasive maneuver
- Controlled turn -> advance -> counter-turn -> recenter
- Ultrasonic verification of centered position

---

## Contact

For questions or collaboration opportunities:
- **Team Email:** [gamechanger.info2022@gmail.com]
- **Coach:** Sergio Cuellar

---

**Team Future TO** | El Salvador 🇸🇻 | WRO 2025 Future Engineers

