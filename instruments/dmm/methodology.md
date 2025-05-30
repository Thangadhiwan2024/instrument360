# Digital Multimeter (DMM)

A **Digital Multimeter (DMM)** is a versatile electronic instrument used for measuring electrical parameters such as voltage, current, and resistance. It is an essential tool for diagnosing, troubleshooting, and testing electronic circuits and systems.

---

## **Key Features**
### **Accurate Voltage Measurement**
- Measures both **AC and DC voltage** with high precision.
- Supports a wide range of voltage levels for various applications.

### **Current Measurement**
- Measures **AC and DC current** with selectable ranges.
- Includes protection against overcurrent to prevent damage.

### **Resistance and Continuity Testing**
- Accurately measures resistance values across components.
- Provides a **continuity test** with audible alerts to detect closed circuits.

### **Capacitance and Frequency Measurement**
- Measures capacitance to verify the condition of capacitors.
- Analyzes signal frequency to ensure consistent waveform characteristics.

---

## **Applications**
### **Circuit Troubleshooting**
- Identifies faulty components and incorrect connections.
- Measures voltage drops, continuity, and current to diagnose issues.

### **Electrical System Testing**
- Ensures compliance with electrical standards by verifying system voltage and current.
- Validates wiring integrity through continuity and resistance tests.

### **Component Testing**
- Measures component characteristics such as resistance, capacitance, and frequency.
- Ensures that components function within expected tolerances.

---

## **Advantages**
### **High Measurement Accuracy**
- Delivers consistent and accurate readings across different ranges.
- Reduces uncertainty in measurement results.

### **Portability and Ease of Use**
- Compact and lightweight, making it ideal for field use.
- Simple interface with intuitive controls for quick operation.

### **Versatility and Multi-Functionality**
- Combines multiple measurement functions into one device.
- Suitable for use in various electrical and electronic applications.

---

## **Abstract Methods**
---

### 1. `StopMeasurement`
#### Description
Stops the previously initiated measurement. This function halts any ongoing measurements and returns the DMM to an idle state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 2. `TerminateSession`
#### Description
Terminates the instrument session. This function ends the connection with the DMM and releases system resources.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | operation | string | Close & Destroy, Destroy & Don't Close | Close & Destroy |

#### Output Parameters
None

### 3. `SetNPLC`
#### Description
Configures the number of Power Line Cycles (NPLC) in a DMM. This setting affects measurement integration time and noise rejection.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Function | Enum | DC Volts, AC Volts, DC Current, AC Current, Diode, Power Meter, Capacitance, Temperature, Frequency, 2-Wire Resistance, 4 Wire Resistance | DC Volts|
| 4 | NPLC | Double | - | 0.02 |

#### Output Parameters
None

### 4. `ConfigureMeasurement`
#### Description
Sets up the measurement function, range, and resolution in digits for a DMM. This function configures the basic measurement parameters.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Resolution in digits | Enum | 3 1/2, 4 1/2, 5 1/2, 6 1/2, 7 1/2, 8 1/2 | 8 1/2|
| 4 | Function | Enum | DC Volts, AC Volts, DC Current, AC Current, Diode, Power Meter, Capacitance, Temperature, Frequency, 2-Wire Resistance, 4 Wire Resistance | DC Volts|
| 5 | Range | Double | - | 0.02 |
| 6 | Additional info | Object | - | - |

#### Output Parameters
None

### 5. `ToggleDisplay`
#### Description
Enables or disables the display on the DMM. This function controls the front panel display visibility.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Display | Enum | ON, OFF | ON |

#### Output Parameters
None

### 6. `SetupMultiPointTrigger`
#### Description
Configures the trigger source, trigger count, readings per trigger event, and sample interval to enable multipoint functionality for automated measurements.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trigger Source | Enum | Auto, Immediate, External, Manual, Bus/Source | Immediate |
| 4 | Trigger Count | Integer | - | 1 |
| 5 | Sample Count | Integer | - | 1 |
| 6 | Sample Interval | Integer | - | 0 |

#### Output Parameters
None

### 7. `InitializeSession`
#### Description
Initializes the session of the DMM. This function establishes communication with the instrument and prepares it for operation.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Operation | Enum | Create New Session, Fetch Existing Session | Create New Session |

#### Output Parameters
None

### 8. `StartMeasurement`
#### Description
Starts the DMM for measurements. This function prepares the instrument to begin taking measurements based on the current configuration.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 9. `ReadMultipleMeasurements`
#### Description
Reads multiple measurements equal to the entered sample count in DMM.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 10. `ReadSingleMeasurement`
#### Description
Reads a single measurement equal to the entered sample count in DMM.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 11. `RestoreDefaults`
#### Description
Restores the DMM to its default settings. This function returns the instrument to a known state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None



