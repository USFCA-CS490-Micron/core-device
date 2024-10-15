# Raspberry Pi Setup for AI Wearable Project

## Project Overview

This project aims to set up a Raspberry Pi to interface with Brilliant Frame glasses for local processing of AI models, using the Pi to handle Bluetooth communication with wearable devices. The following documentation details the step-by-step process I followed to set up the Raspberry Pi, install software, and establish communication between the Pi and the glasses.

## Table of Contents

- [Hardware Requirements](#hardware-requirements)
- [Initial Raspberry Pi Setup](#initial-raspberry-pi-setup)
- [Connecting to the Raspberry Pi via SSH](#connecting-to-the-raspberry-pi-via-ssh)
- [Installing Python, Virtual Environment, and Dependencies](#installing-python-virtual-environment-and-dependencies)
- [Setting Up Bluetooth Communication](#setting-up-bluetooth-communication)
- [Testing Bluetooth Communication](#testing-bluetooth-communication)
- [Setting Up Git and Pushing to GitHub](#setting-up-git-and-pushing-to-github)
- [Conclusion](#conclusion)

## Hardware Requirements

This is the hardware that I used:

- Raspberry Pi 4 or 5 (I used the 8GB RAM version)
- microSD Card (16GB or larger)
- Bluetooth keyboard and mouse (optional)
- HDMI monitor (for initial setup)
- Raspberry Pi power supply

## Initial Raspberry Pi Setup

### 1. Downloading Ubuntu Server

I started by downloading **Ubuntu Server (minimal)** from the [official Ubuntu website](https://ubuntu.com/download/raspberry-pi) to keep resource usage on the Pi low. Once I had the image, I flashed it onto a microSD card using [Balena Etcher](https://www.balena.io/etcher/), a tool that makes it easy to flash OS images to SD cards.

### 2. Booting the Raspberry Pi

Once the microSD card was ready, I inserted it into the Raspberry Pi and powered it on. I connected a monitor and keyboard initially to go through the standard setup process. During the setup, I created a username and password.

### 3. Updating the Raspberry Pi

After logging in for the first time, I updated the system by running:
