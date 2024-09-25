# Network Automation Using Python

The purpose of this project is to make it easier for network engineers to set up devices remotely by providing a set of predefined functions that will help automate network configuration. This project incorporates both Python and networking knowledge, offering an easy-to-use tool for network configuration.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Code Overview](#code-overview)
  
## Introduction

In modern networking, setting up devices can be a time-consuming and error-prone task. This project aims to streamline the configuration process by providing automated scripts that can configure multiple devices.
With built-in error handling and logging, users can ensure their configurations are applied correctly. 

## Features

- **Automated Device Configuration**: Predefined functions for configuring various network devices, including switches and routers.
- **Multi-Device Support**: Ability to handle configurations for multiple devices in one run.
- **Error Handling**: Built-in mechanisms to manage errors during configuration.
- **Logging**: Detailed logs of configuration changes for auditing and troubleshooting.
- **Extensibility**: Easily add new device types and configuration templates.

## Prerequisites

- **Python**: Version 3.12 or higher
- **Network Devices**: Routers and switches accessible via SSH
- **SSH Credentials**: Username and password for SSH access
- **Operating System**: Tested on Windows and Linux

## Code Overview

This project is designed to automate network device configuration using a modular architecture. Below are the key components, organized by their respective files:

### Device Abstraction

The tool employs Object-Oriented Programming (OOP) to abstract network devices:

- **Base Class**: 
  - `Device`: This serves as the foundation for most device types.
- **Router Class**: 
  - `Router`: Inherits from `Device` and implements router-specific functionality.
- **Switch Class**: 
  - `Switch`: Inherits from `Device` and includes switch-specific methods.

**Key Methods**:
- `connect()`: Establishes an SSH connection to the device.
- `send_command(command)`: Sends a command via SSH and returns the result.
- `disconnect()`: Closes the SSH connection to free resources.

### SSH Connection Handling

SSH connections are managed using a singleton pattern to ensure only one connection per device:

- **Class**: 
  - `Connection`: This class manages the SSH connection lifecycle.

### Application Navigation

Navigation in the application is managed using 3 different methods.
- **main**: Manages the startup menu and is responsible for allowing the user to execute opperations on devices if the target device is a known device.
- **ConfigMenuRouter**: Menu displayed if the target device is identified as beeing a router.
- **ConfigMenuSwitch**: Menu displayed if the target device is identified as beeing a switch.
  
This structured approach not only enhances maintainability but also allows for easy extension of the tool to accommodate additional device types and configuration scenarios.
