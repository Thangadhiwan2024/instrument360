# Network Analyzer

A **Network Analyzer** is a precision instrument used to measure the electrical characteristics of high-frequency networks, such as **RF circuits**, **antennas**, and **microwave components**. It is essential for analyzing signal transmission and reflection properties in communication and radar systems.  

---

## **Key Features**  

### **S-Parameter Measurement**  
- Measures **scattering parameters (S-parameters)** to analyze how signals propagate through a network.  
- Helps determine signal gain, loss, reflection, and transmission properties.  

### **Vector Network Analysis (VNA)**  
- Provides both **magnitude** and **phase** information of signals.  
- Offers high precision for RF and microwave circuit design and testing.  

### **Wide Frequency Range**  
- Operates from a few kHz up to several GHz or even THz.  
- Supports testing of components across different frequency bands.  

---

## **Applications**  

### **RF & Microwave Circuit Design**  
- Evaluates **filters, amplifiers, mixers, and antennas** for performance optimization.  
- Ensures minimal signal distortion in high-frequency applications.  

### **Antenna & Wireless Communication Testing**  
- Measures return loss, insertion loss, and impedance matching.  
- Optimizes antenna design for maximum efficiency and minimal signal reflection.  

### **Material & Component Characterization**  
- Analyzes dielectric properties of materials used in RF designs.  
- Validates PCB traces, connectors, and other RF components.  

---

## **Advantages**  

### **High Accuracy & Resolution**  
- Offers **precise phase and magnitude measurements** for critical designs.  
- Supports advanced error correction techniques for improved results.  

### **Real-time Analysis & Calibration**  
- Provides real-time visualization of signal behavior.  
- Features built-in **calibration techniques** to minimize measurement errors.  

### **Automation & Remote Operation**  
- Supports **automated test setups** for consistent and repeatable measurements.  
- Interfaces with software for enhanced data analysis and reporting.  

---

## **Abstract Methods**
---

### 1. `Close`
#### Description
This method is used to close the instrument session of the Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |

#### Output Parameters
None

### 2. `FetchData`
#### Description
This method is used to configure the Data Format and read the Output Frequency & Trace data in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Data Format       | Any    | -       | -       |
| 4   | Output Data Type  | Enum   | Real-Imaginary, Mag_Phase | Real-Imaginary |

#### Output Parameters
| No. | Parameter       | Type   |
|:--:|:----------------|:------:|
| 1   | Stimulus Frequencies | 1D-Array |
| 2   | Real/Mag Data    | 1D-Array |
| 3   | Imaginary/Phase  | 1D-Array |

### 3. `FetchMarkerData`
#### Description
This method is used to read out the response value of selected marker for the active trace of selected Channel in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Marker            | Integer| -       | 1       |

#### Output Parameters
| No. | Parameter       | Type   |
|:--:|:----------------|:------:|
| 1   | X Value         | Double |
| 2   | Y Real Value    | Double |
| 3   | Y Imaginary Value | Double |

### 4. `Get Amplitude & Phase at Required Frequency`
#### Description
Read the Amplitude & Phase of entered marker and trace for the given Frequency in a Network Analyzer.

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Frequency (Hz) | Double | - | - |
| 4 | Trace | I32 | - | - |
| 5 | Marker | I32 | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Amplitude | Double |
| 2 | Phase | Double |

### 5. `Get Parameter List`
#### Description
Get the Measurement Parameter List for a Network Analyzer.

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Parameter List | Array |

### 6. `GetBWSearchResult`
#### Description
Read out the bandwidth search results like Bandwidth, Loss, and Q Value for the active trace of selected channel in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Marker            | Integer| -       | 1       |

#### Output Parameters
| No. | Parameter       | Type   |
|:--:|:----------------|:------:|
| 1   | Bandwidth       | Double |
| 2   | Loss            | Double |
| 3   | Q Value         | Double |
| 4   | Center Frequency| Double |

### 7. `Init`
#### Description
Initializes a new session for the Network Analyzer with specified model configuration.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Model Name        | String | -       | -       |

#### Output Parameters
None

### 8. `LoadSettings`
#### Description
This method is used to load the saved settings to the instrument and configure the instrument from the entered Path/Register Name in a Network Analyzer. Enter appropriate Path/Register name depending on the instrument.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Path/Register Name| String | -       | -       |

#### Output Parameters
| No. | Parameter       | Type   |
|:--:|:----------------|:------:|
| 1   | File Not Found  | Boolean|

### 9. `PerformCalibration`
#### Description
This method is used to perform Calibration in a Network Analyzer. User should wait for the calibration to be completed before performing any other operation (Add required Wait time after this API).

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Measurement Parameter | Any | -       | -       |
| 4   | Calibration Type  | Any    | -       | -       |

#### Output Parameters
None

### 10. `SaveSettings`
#### Description
This method is used to store the Instrument settings to the specified Path/Register Name in a Network Analyzer. Enter appropriate Path/Register Name depending on the instrument.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Path/Register Name| String | -       | -       |

#### Output Parameters
None

### 11. `SearchAmplitude`
#### Description
This method is used to Configure Marker Search and read the Marker Data in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Target Amplitude  | Double | -       | 0.0     |
| 4   | Marker            | Integer| -       | 1       |
| 5   | Start Frequency   | Double | -       | -       |
| 6   | Stop Frequency    | Double | -       | -       |
| 7   | Direction         | Enum U16 | -     | Right   |
| 8   | Search Mode       | Enum U16 | -     | First Point |

#### Output Parameters
| No. | Parameter       | Type   |
|:--:|:----------------|:------:|
| 1   | Measured Frequency | Double |

### 12. `SearchMarker`
#### Description
This method is used to configure the Marker Search & return position and value of the found marker.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Function          | Enum   | Maximum, Minimum, Peak,Left Peak, Right Peak, Target, Left Target, Right Target | Maximum |
| 4   | Peak Polarity     | Enum   | Both, Positive, Negative | Positive |
| 5   | Peak Excursion    | Double | -       | 3.0     |
| 6   | Stop Value        | Double | -       | 0.0     |
| 7   | Start Value       | Double | -       | 0.0     |
| 8   | Marker            | Integer| -       | 1       |

#### Output Parameters
| No. | Parameter       | Type   |
|:--:|:----------------|:------:|
| 1   | X Value         | Double |
| 2   | Y Value         | Double |

### 13. `SetActiveChannel`
#### Description
Configures the specified channel as the Active channel for the Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Active Channel    | Integer| -       | 1       |

#### Output Parameters
None

### 14. `SetActiveMarker`
#### Description
This method is used to configure the Active Marker in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Marker            | Integer| -       | -       |

#### Output Parameters
None

### 15. `SetAveraging`
#### Description
Configures the averaging settings for the active channel in the Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Enable Averaging  | Boolean| True, False | False |
| 4   | Averaging Factor  | Integer| -       | -       |

#### Output Parameters
None

### 16. `SetBWSearch`
#### Description
This method is used to configure the bandwidth marker search in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Enable Bandwidth Search | Boolean | true, false | true |
| 4   | Bandwidth Definition Value | Double | -       | -3     |
| 5   | Marker            | Integer| -       | -       |

#### Output Parameters
None

### 17. `SetBandwidthResolution`
#### Description
This method is used to configure Resolution Bandwidth Value in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Resolution        | Double | -       | -       |

#### Output Parameters
None

### 18. `SetDataFormat`
#### Description
This method is used to configure the Data Format to be displayed for the given Trace(if applicable) in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Active Trace      | Integer| -       | 1       |
| 4   | Data Format       | Any    | -       | -       |

#### Output Parameters
None

### 19. `SetDisplayScale`
#### Description
This method is used to Configure the Display Scale Settings for the given Trace(if applicable) in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Auto Mode         | Boolean| -       | True    |
| 4   | Scale/Div         | Double | -       | -       |
| 5   | Trace             | Integer| -       | 1       |
| 6   | Reference value   | Integer| -       | -       |
| 7   | Reference value   | Integer| -       | -       |

#### Output Parameters
None

### 20. `SetFrequencyRange`
#### Description
This method is used to configure the Start & Stop Frequency (in Hz) for a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Start Freq        | Double | -       | -       |
| 4   | Stop Freq         | Double | -       | -       |

#### Output Parameters
None

### 21. `SetIFBandwidth`
#### Description
This method is used to configure the IF Bandwidth (in Hz) for a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | IF BW             | Double | -       | -       |

#### Output Parameters
None

### 22. `SetInputOutputImpedance`
#### Description
This method is deprecated. Use "Set Input Output Impedance_v2" available at Functions Palette->ADI->ZCG->HAL->Network Analyzer->Configure. Reason for deprecating: Added Port input.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Input Impedance   | Double | -       | -       |
| 4   | Output Impedance  | Double | -       | -       |
| 5   | Port              | Integer| 1       | -       |

#### Output Parameters
None

### 23. `SetMarker`
#### Description
This method is used to configure the Marker settings in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Enable Marker     | Boolean| -       | -       |
| 4   | Stimulus          | Double | -       | -       |
| 5   | Marker            | Integer| -       | 1       |

#### Output Parameters
None

### 24. `SetMarkerMode`
#### Description
This method is used to configure the Marker mode of a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Marker            | Integer| -       | -       |
| 4   | Coupled           | Any    | -       | -       |
| 5   | Reference Marker Mode | Any | -       | -       |
| 6   | Marker Mode       | Any    | -       | -       |

#### Output Parameters
None

### 25. `SetMeasurementParameter`
#### Description
This method is used to configure the parameter to be measured for the given Trace(if applicable) in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Active Trace      | Integer| -       | 1       |
| 4   | Parameter         | Any    | -       | -       |

#### Output Parameters
None

### 26. `SetMeasurementType`
#### Description
This method is used to configure the Measurement type (e.g., FFT, Swept Network) of a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Measurement Type  | Enum   | -       | -       |

#### Output Parameters
None

### 27. `SetPowerLevelAndRange`
#### Description
This method is used to configure the Power level & Attenuation value for a range for the entered port in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Port              | Integer| -       | 1       |
| 4   | Auto Mode         | Boolean| -       | False   |
| 5   | Level             | Double | -       | -       |
| 6   | Range             | Double | -       | -       |

#### Output Parameters
None

### 28. `SetSweep`
#### Description
This method is used to configure the Sweep Type, number of measurement points, and the sweep time for manual sweep in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Sweep Mode        | Any    | -       | -       |
| 4   | Measurement Points| Integer| -       | 201     |
| 5   | Sweep Time        | Double | -       | -       |
| 6   | Sweep Type        | Any    | -       | -       |

#### Output Parameters
None

### 29. `SetTrace`
#### Description
This method is used to configure the Number of Traces and Active Trace for a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Active Trace      | Integer| -       | 1       |
| 4   | Number of Traces  | Integer| -       | 1       |

#### Output Parameters
None

### 30. `SetTrigger`
#### Description
This method is used to configure the Trigger Parameters of a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Trigger Source    | Any    | -       | -       |
| 4   | Continuous Sweep  | Boolean| -       | -       |
| 5   | Point Trigger     | Boolean| -       | -       |

#### Output Parameters
None

### 31. `StartMeasurement`
#### Description
This method is used to set the trigger system to a continuously initiated state.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |

#### Output Parameters
None

### 32. `StopMeasurement`
#### Description
Immediately stops the current measurement in the Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |

#### Output Parameters
None

### 33. `ToggleSourcePower`
#### Description
This method is used to Switch ON/OFF the stimulus signal output in a Network Analyzer. To perform measurement, it should be turned ON.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |
| 3   | Source Power      | Boolean| -       | False   |

#### Output Parameters
None

### 34. `TriggerDataCapture`
#### Description
This method is used to send a trigger and capture data in a Network Analyzer.

#### Input Parameters
| No. | Parameter       | Type   | Options | Default |
|:--:|:----------------|:------:|:--------|:--------|
| 1   | Instrument Address | String | -       | -       |
| 2   | Channel           | String | -       | -       |

#### Output Parameters
None

