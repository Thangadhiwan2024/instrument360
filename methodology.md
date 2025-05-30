# Thermostream

A **Thermostream** is a temperature forcing system used to rapidly heat or cool electronic devices and components. It provides precise temperature control, making it ideal for thermal testing, component characterization, and environmental stress testing.

---

## **Key Features**

### **Rapid Temperature Cycling**
- Quickly transitions between high and low temperatures.
- Ensures accurate temperature control within a wide operating range.

### **Non-Contact Temperature Forcing**
- Delivers controlled airflow to the **Device Under Test (DUT)**.
- Minimizes thermal lag and ensures uniform temperature distribution.

### **User-Programmable Profiles**
- Allows creation of custom temperature profiles for various test scenarios.
- Supports automation for consistent and repeatable results.

---

## **Applications**

### **Semiconductor Testing**
- Validates device performance across extreme temperature ranges.
- Detects thermal failures and ensures reliability in harsh environments.

### **Component Characterization**
- Evaluates passive and active components under temperature variations.
- Measures component stability and response to thermal stress.

### **Environmental Stress Testing (EST)**
- Simulates real-world environmental conditions to assess device durability.
- Identifies potential failure points by exposing devices to thermal extremes.

---

## **Advantages**

### **Precision Temperature Control**
- Maintains stable temperatures with minimal fluctuations.
- Enables accurate evaluation of device behavior under thermal conditions.

### **Reduced Test Time**
- Accelerates thermal cycling for faster test completion.
- Improves overall efficiency in high-volume testing environments.

### **Flexibility and Versatility**
- Adapts to various device sizes and shapes.
- Suitable for testing different materials and components.

---

## **Abstract Methods**
---

### 1. `Abort`
#### Description
Terminates any ongoing processes and returns the Thermostream to a safe state.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 2. `Close`
#### Description
Disables the air flow and closes the instrument session of the Thermostream, ensuring proper shutdown.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 3. `ConfigureSetpoint`
#### Description
Sets the temperature parameters for the Thermostream.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Number | Integer | -  | - |
| 4 | Enable | Boolean | - | - |
| 5 | Temperature | Double | - | - |
| 6 | Window | Double | - | - |
| 7 | Soak Time | Integer | - | - |
| 8 | Ramp Rate | Double | - | - |

#### Output Parameters
None

### 4. `ConfigureSetpointTemp`
#### Description
Sets the temperature setpoint for the Thermostream.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | sample_count | Integer | - | - |
| 4 | setpoint_temp | Double | - | - |

#### Output Parameters
None

### 5. `ConfigureTemperatureMeasurement`
#### Description
Configures the temperature measurement mode and thermocouple type of the Thermostream.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | measurement_mode | Enum | DUT Temperature, Air Temperature | DUT Temperature |
| 4 | thermocouple_type | Enum | No Sensor, K-Type | K-Type |

#### Output Parameters
None

### 6. `ControlCompressor`
#### Description
Manages the compressor state of the Thermostream unit.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | compressor_state | Enum | On, Off | Off |

#### Output Parameters
None

### 7. `Get Setpoint SoakTime`
#### Description
Read the Setpoint's Soak Time(in seconds) of the instrument.

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Soak Time (seconds) | Integer |

### 8. `Get Temperature`
#### Description
Read the temperature from Active mode(Air Temperature when in Air Control Mode, DUT Temperature when in DUT Control Mode).

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Temperature | Double |

### 9. `Init`
#### Description
Initializes the session of the Thermostream.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | thermostream_type | String | - | - |
| 2 | Baud Rate | Integer | - | - |
| 3 | Flow Control | Enum | - | - |
| 4 | Parity | Enum | - | - |
| 5 | Data Bits | Integer | - | - |
| 6 | Stop Bits | Integer | - | - |

#### Output Parameters
None

### 10. `Reset`
#### Description
Resets the instrument to the cycle screen and clears any device-specific errors.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 11. `SendDeviceCommand`
#### Description
Sends a device command to the Thermostream.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | device_command | Enum | Head Down & Air On, Head Up & Air Off, Air Flow Off, Air Flow On, Compressor Off, Compressor On | - |

#### Output Parameters
None

### 12. `ToggleAirFlow`
#### Description
Starts or stops the air flow. Deprecated: Use "WriteDeviceCommand" for air flow control.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | setpoint_temp | Double | - | - |
| 4 | start_air_flow | Boolean | - | - |

#### Output Parameters
None
