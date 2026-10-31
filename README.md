# Global Multi-Biome Geohazard Early Warning System

An unsupervised, multi-physics LSTM Autoencoder framework for real-time macro-surveillance, dynamic failure horizon detection, and contagion-free 72-hour municipal evacuation routing across 17 global tectonic, catch-basin, and alpine fault corridors.

---

## Key Features

- **Multi-Physics Telemetry Channels:** Integrates five core physical signals:
  1. Thermal Expansion Delta ($T_\sim$)
  2. Hydrological Soak / Inundation ($M_\sim$)
  3. Ground Displacement Acceleration ($W_{\text{strain}}$)
  4. Ridge & Coastal Wind Buffeting ($W_{\sim\text{wind}}$)
  5. Barometric Pressure Drop ($P_{\sim\text{bar}}$)
- **Dynamic Dual Anomaly Gates:**
  - **Amber Advisory Threshold:** $\tau_1 = \mu + 3.0\sigma$
  - **Red Alert Breach Gate:** $\tau_2 = \mu + 6.0\sigma$
- **Region-Specific Noise Calibration:** Dynamically scales localized strain acceleration ($k_{\text{strain}}$) to filter background seismic and ambient meteorological noise.
- **Contagion-Free Safe-Haven Scanner:** Evaluates $5\text{ km} \times 5\text{ km}$ spatial grid tiles to verify candidate evacuation zones free of adjacent Level-2 or Level-3 risks.
- **Spatial Reverse Geocoder:** Converts grid centroid WGS84 coordinates directly into physical municipal addresses (`geopy` / OpenStreetMap) and interactive Google Maps links.

---

## 17 Global Macro-Surveillance Hotspots

The system actively monitors and back-tests 17 distinct geophysical corridors:

1. **Nanda Devi Basin, Uttarakhand** (*Himalayan Rock-Ice*)
2. **Pisco Fault Segment, Peru** (*Andean Fault Zone*)
3. **Wayanad Escarpment, Kerala** (*SE Asian Monsoon Clay*)
4. **Val Bondasca / Piz Cengalo** (*Alps Glacial Moraine*)
5. **Gorkha-Barpak Fault, Nepal** (*Himalayan Tectonic*)
6. **Oso Slide Corridor, Washington** (*Rocky Mountain Slope*)
7. **Mount Ontake Flank, Nagano** (*Japanese Volcanic Fault*)
8. **Karmadon Gorge, North Ossetia** (*Caucasus High Altitude*)
9. **Mount Elgon Slopes, Uganda** (*East African Rift Valley*)
10. **Southern Alps West Coast** (*New Zealand Alpine Fault*)
11. **Tafjord Fjord Wall, Norway** (*Scandi Fjord Slope*)
12. **Southern Appalachian Corridor** (*Appalachian Weathered*)
13. **Aksu Border Catchment** (*Tian Shan Cryosphere*)
14. **Southern Patagonian Ice Field** (*Patagonian Glacial Edge*)
15. **Langtang Lirung** (*Nepal-Tibet Border*)
16. **Langtang-Trishuli Valley** (*Secondary Flood Rehabilitation*)
17. **Visakhapatnam-Kakinada Corridor, Andhra Pradesh** (*Coastal Cyclonic Surge*)

---

## Repository Structure

```text
geohazard-early-warning-system/
├── README.md
├── requirements.txt
├── config/
│   └── regions_config.json
├── src/
│   ├── __init__.py
│   ├── feature_engineering.py
│   ├── model.py
│   └── geo_translator.py
└── notebooks/
    └── Almost_Final_Production_Bench.ipynb