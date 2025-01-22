# Punktewolken_Dynamikerkennung

## Name
3D Bewegungserkennung in Punktewolken 

## Description
Mit Hilfe von Algorithmen wie ICP, Optical Flow und DBSCAN wurden Punkte in Punktwolken, die mit der menschlichen Bewegung zusammenhängen, extrahiert und visualisiert. 

## Requirements 
Packages: `open3d`, `numpy`, `plotpy`, `pandas`, `pathlib`, `sklearn` 

## Preparation
PCD-Files sollen zuerst von [DB3-Files](https://fh-aachen.sciebo.de/s/sjIpXh9bdL4hkNu ) mit [rosbag2_to_pcd](https://github.com/xmfcx/rosbag2_to_pcd ) extrahiert werden. Die Ergebnisse wurden in [raw_pcds](./raw_pcds/) gespeichert. 

## Usage
[Motion-Detection_from_Point-Clouds.ipynb](./Motion-Detection_from_Point-Clouds.ipynb) enthält 5 Schritte. Die Ergebnisse der einzelnen Schritte wurden in einem Ordner mit demselben Namen gespeichert. 
- 01 Laden und Filterung der Punktwolke 
- 02 Punktwolkenregistrierung (ICP) 
- 03 Bewegungserkennung (Optical Flow) 
- 04 Clustering und Objektextraktion (DBSCAN) 
- 05 Visualisierung 

P.S.
- Die Visualisierung kann mit Hilfe von [adjust_view.py](./adjust_view.py) angepasst werden. Die Ergebnisse werden in [saved_view.json](./saved_view.json) gespeichert. 


## License
Dieses Projekt ist unter der MIT-Lizenz lizenziert – Einzelheiten finden Sie in der Datei [LICENSE](./LICENSE). 
