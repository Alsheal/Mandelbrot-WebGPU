# Mandelbrot WebGPU

A browser-based Mandelbrot set renderer that compares CPU and GPU computation using JavaScript, WebGPU, and WGSL.

## Overview

Mandelbrot WebGPU visualizes the Mandelbrot fractal and demonstrates the performance benefits of GPU-accelerated parallel computation.

The application runs the rendering algorithm on both CPU and GPU, allowing users to compare execution time, acceleration, and output accuracy.

## Features

- Mandelbrot set visualization
- CPU rendering with JavaScript
- GPU rendering with WebGPU and WGSL
- Adjustable zoom and coordinate offsets
- Configurable maximum iteration count
- Adjustable color intensity
- CPU and GPU execution time measurement
- Performance acceleration calculation
- Pixel-by-pixel output comparison

## Technologies

- HTML5
- JavaScript
- WebGPU API
- WGSL
- Python 3

## Performance

Example benchmark results at 1920 × 1080 resolution:

| Metric | Result |
|---|---:|
| CPU execution time | 697.80 ms |
| GPU execution time | 81.60 ms |
| GPU acceleration | **8.55×** |
| Mean pixel difference | 0.0608 |
| Maximum pixel difference | 255 |

The CPU and GPU output images look visually identical.

*Performance measurements may vary depending on hardware, browser, and GPU implementation.*

## Default Configuration

| Parameter | Value |
|---|---:|
| Resolution | 1920 × 1080 |
| Zoom | 2.40 |
| Offset X | -0.10 |
| Offset Y | 0.65 |
| Maximum iterations | 320 |
| Color power | 0.50 |

## Getting Started

### Requirements

- A modern browser with WebGPU support
- Python 3.x

### Run locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mandelbrot-webgpu.git
cd mandelbrot-webgpu
```

Start the local server:

```bash
python start_server.py
```

Open the application:

http://localhost:8000

## How It Works

The application implements the Mandelbrot iteration algorithm in two environments:

- **CPU:** JavaScript performs the calculations sequentially.
- **GPU:** WGSL compute shaders distribute calculations across GPU workgroups through WebGPU.

The application measures execution time and compares the resulting pixel data to evaluate performance and numerical differences.


