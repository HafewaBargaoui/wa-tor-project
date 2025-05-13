# 🐟 🦈 Wa-Tor Simulation —  Simplon HDF
  

Welcome to one of the most fishy and shark-infested projects from the **Data Engineering Bootcamp – Simplon HDF 2025**.  

Our mission: simulate a marine ecosystem where hungry sharks chase peaceful fish across an infinite toroidal ocean.

Over the course of 9 days, we tackled this brief by designing and building an object-oriented simulation tool that helps explore predator-prey dynamics.

Dive in. The fish won’t save themselves. 🐟🦈
  
  
# 📌 Project Description  
  
The **Wa-Tor Simulation** is a simplified predator-prey ecosystem model represented on a toroidal grid. It features two species:  
- 🐟 **Fish** — peaceful swimmers  
- 🦈 **Sharks** — hungry hunters  
  
🔗 [Rules of the Wa-Tor simulation](https://en.wikipedia.org/wiki/Wa-Tor#Rules)  
🔗 [Example of a Wa-Tor simulation online](https://wa-tor.saidone.org/)


## 📜 License  
  
This project is licensed under the MIT License ©️ 2025.  
You are free to use, modify, and distribute this project with proper attribution.  
  
## 🛠️ Technologies Used  
  
-   🐍 Python
  
- 🎮 pygame (if GUI)  
  
-   📈  matplotlib (if visualization)  

## 📁Project Structure  
  
```
wa-tor-project/
├── back/
│   ├── fish.py
│   ├── shark.py
│   ├── constants.py
│   ├── grid.py
│   └── main.py
│
├── config/
│   └── config.ini
│
├── images/
│   └── wa-tor.gif
│
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
```
  
  
## 🖼️ Example Output  
  
Here’s a glimpse of the simulation in action:  
  

![Simulation demo](images/wa-tor.gif)
  
  
## 🚀Getting Started  
  
### Installation  
  
```bash  
git clone https://github.com/HafewaBargaoui/wa-tor-project.git
cd wa-tor-project
pip install -r requirements.txt
```
## ⚙️ Configuration

The simulation behavior can be customized via the `config/config.ini` file. You can adjust the following parameters:

- **Grid dimensions** — set the width and height of the toroidal grid.  
- **Initial number of fish and sharks** — control how populated the ocean is at the start.  
- **Fish breeding time** — number of simulation steps before a fish reproduces.  
- **Shark breeding time** — number of steps before a shark reproduces.  
- **Shark starvation time** — number of steps a shark can survive without eating.  
- **Simulation speed** — control the refresh rate or delay between simulation steps.

## 🧪 How to Run

Once the dependencies are installed and the configuration is set, you can launch the simulation with:

```bash
python back/main.py

## 👥 Team

This project was developed as part of the **Simplon HDF Data Engineering Bootcamp 2025** by a team of 3 apprenants:

- 🔗 [Sébastien Dewaelle](https://github.com/cebdewaelle)  
- [**Jean-Pierre Elias*](https://github.com/seiyakazana)
- [**Hafawa Bargaoui**](https://github.com/HafewaBargaoui)  
