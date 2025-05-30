# Analog Input/Output (AIO)

An **Analog Input/Output (AIO) Instrument** is a device used to measure and generate analog signals, converting physical phenomena into electrical signals and vice versa. It is widely used in industrial automation, process control, and data acquisition.

---

## **Key Features**

### **Analog Input (AI)**
- Measures real-world signals such as voltage, current, and temperature.  
- Converts analog signals into digital data for analysis.

### **Analog Output (AO)**
- Converts digital control signals into analog outputs.  
- Controls external devices like actuators and motors.

### **High Resolution and Accuracy**
- Ensures precise measurement and control of signals.  
- Provides high-resolution data for critical applications.

---

## **Applications**

### **Industrial Automation**
- Monitors and controls machinery and processes.  
- Ensures smooth and efficient system operation.

### **Data Acquisition**
- Collects real-time analog data from multiple sources.  
- Facilitates analysis and decision-making.

### **Environmental Monitoring**
- Measures parameters such as temperature and humidity.  
- Enables real-time control in sensitive environments.

---

## **Advantages**

### **Real-Time Monitoring and Control**
- Provides continuous feedback for optimal performance.  
- Allows immediate response to changing conditions.

### **Versatility and Flexibility**
- Supports various input and output types.  
- Adapts easily to different applications.

### **Seamless System Integration**
- Integrates with PLCs and industrial systems.  
- Enhances overall system functionality.

---

## **Abstract Methods**
---
### 1. `AdjustTiming`
#### Description
Configures the timing settings for data acquisition or generation, including the sample rate and timing source.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Samples per channel | Integer | - | 1000 |
| 4 | SampleRate | Double | - | 1000.00 |
| 5 | Source | String | - | - |
| 6 | Sample Mode | Enum | Finite Sample, Continuous Sample, Hardware Timed Single Point | Hardware Timed Single Point |

#### Output Parameters
None

### 2. `Close`
#### Description
Disconnects the AIO device and releases any allocated resources.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 3. `FetchMultiChannelData`
#### Description
Retrieves double-precision data from multiple channels for a specified number of samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout | Double | - | 10 |
| 4 | Samples per channel to Acquire | Integer | - | -1 |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Data | 2D-Array |

### 4. `FetchSingleChannelData`
#### Description
Retrieves double-precision data from a single channel for a specified number of samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout | Double | - | 10 |
| 4 | Samples per channel to Acquire | Integer | - | -1 |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Data | 1D-Array |

### 5. `Get Max Value`
#### Description
Retrieves the maximum value from the measurement data.

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Maximum Value | Double |

### 6. `Get Min Value`
#### Description
Retrieves the minimum value from the measurement data.

#### Input Parameters
| No. | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
| No. | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Minimum Value | Double |

### 7. `Initialize`
#### Description
Initializes the AIO device with the provided configuration parameters.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Type | String | - | - |
| 4 | Additional Input | Any | - | - |
| 5 | Maximum Value | Double  | - | 5 |
| 6 | Minimum Value | Double | - | -5 |
| 7 | Analog I/O Type | Enum | AI Voltage, AI Voltage RMS, AI Current, AI Current RMS, AO Voltage, AO Current | AI Voltage |

#### Output Parameters
None

### 8. `Initiate`
#### Description
Starts the AIO device to begin data acquisition or signal generation.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 9. `Reset`
#### Description
Returns the AIO device to its initial factory settings.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 10. `RetrieveMultiChannelWaveform`
#### Description
Obtains waveform data from multiple channels for a specified number of samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout | Double | - | 10 |
| 4 | Samples per channel to Acquire | Integer | - | -1 |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Data | 1D-Array |

### 11. `RetrieveSingleChannelWaveform`
#### Description
Obtains waveform data from a single channel for a specified number of samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout | Double | - | 10 |
| 4 | Samples per channel to Acquire | Integer | - | -1 |

#### Output Parameters
| S.No | Parameter | Type |
|:--:|:----------|:-----|
| 1 | Data | 1D-Array |

### 12. `SendMultiChannelData`
#### Description
Transfers double-precision data to multiple channels for a specified number of samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout | Double | - | 10 |
| 4 | Data | 2D-Array | - | - |

#### Output Parameters
None

### 13. `SendMultiChannelWaveform`
#### Description
Sends waveform data to multiple channels for a specified number of samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout | Double | - | 10 |
| 4 | Data | 1D-Array | - | - |

#### Output Parameters
None

### 14. `SendSingleChannelData`
#### Description
Transfers double-precision data to a single channel for a specified number of samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout | Double | - | 10 |
| 4 | Data | 1D-Array | - | - |

#### Output Parameters
None

### 15. `SendSingleChannelWaveform`
#### Description
Sends waveform data to a single channel for a specified number of samples.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Timeout | Double | - | 10 |
| 4 | Data | 1D-Array | - | - |

#### Output Parameters
None

### 16. `SetMaxValue`
#### Description
Sets the maximum allowable value for the AIO device.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Maximum Value | Double | - | 5 |

#### Output Parameters
None

### 17. `SetMinValue`
#### Description
Sets the minimum allowable value for the AIO device.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Minimum Value | Double | - | -5 |

#### Output Parameters
None

### 18. `SetSampleCount`
#### Description
Defines the number of samples to be processed for each channel.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Samples per Channel | Integer | - | - |

#### Output Parameters
None

### 19. `StartEdgeTrigger`
#### Description
Initiates operation of the AIO device using an edge-based trigger.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Trigger Edge | Enum | Rising, Falling | Rising |
| 4 | Source | String | - | - |

#### Output Parameters
None

### 20. `StartPatternTrigger`
#### Description
Initiates operation of the AIO device using a pattern-based trigger.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Source | String | - | - |
| 4 | Pattern | String | - | - |
| 5 | Trigger When | Enum | Pattern Matches, Pattern does Not Matches | Pattern Matches |

#### Output Parameters
None

### 21. `Stop`
#### Description
Stops all operations of the AIO device.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |

#### Output Parameters
None

### 22. `StopEdgeTrigger`
#### Description
Stops the AIO device using an edge-based trigger.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Source | String | - | - |
| 4 | Trigger Edge | Enum  | Rising, Falling | Rising |
| 5 | Pretrigger Samples per channel | Integer | - | 500 |

#### Output Parameters
None

### 23. `StopPatternTrigger`
#### Description
Stops the AIO device using a pattern-based trigger.

#### Input Parameters
| S.No | Parameter | Type | Options | Default |
|:--:|:----------|:-----|:--------|:--------|
| 1 | Instrument Address | String | - | - |
| 2 | Channel | String | - | - |
| 3 | Pretrigger Samples per channel | Integer | - | 500 |
| 4 | Source | String | - | - |
| 5 | Trigger When | Enum | Pattern Matches, Pattern does Not Matches | Pattern Matches |
| 6 | Pattern | String | - | - |

#### Output Parameters
None