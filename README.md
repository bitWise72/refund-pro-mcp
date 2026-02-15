# Refund Pro

Refund Pro is a specialized tool designed to assist with airline refund claims and compensation disputes. It provides a set of utilities to calculate compensation, find legal precedents, and generate formal demand notices.

## Overview

This project implements a Model Context Protocol (MCP) server that exposes several functions to help users navigate consumer rights, specifically within the context of Indian aviation regulations and consumer protection laws. It is built using Python and performs tasks ranging from calculating delay penalties to drafting legal notices.

![Refund Pro Demo](image.png)

## Features

The application includes the following capabilities:

*   **Legal Precedent Engine**: Retrieves specific legal wins and case numbers for supported airlines to strengthen consumer claims.
*   **Aggression Optimizer**: Analyzes the sentiment of the interaction and suggests the appropriate tone for the legal notice, ranging from firm requests to intense warnings.
*   **Compensation Calculator**: Computes the total claim amount by adding applicable penalties for delays to the base ticket cost.
*   **Ombudsman Bridge**: Provides direct access to government grievance portals like AirSewa for immediate escalation.
*   **Notice UI Generator**: Creates a professional HTML layout for the legal demand notice, suitable for printing or saving as a PDF.

## Architecture

The system is built as a lightweight microservice.

*   **Runtime**: Python 3.11
*   **Framework**: FastMCP (for exposing the tools)
*   **Containerization**: Docker

The core logic resides in `tools.py`, which defines the tools and handles the HTTP transport.

## Installation and Usage

### Prerequisites

*   Docker (recommended)
*   Python 3.11 or higher (if running locally without Docker)

### Running with Docker

1.  Build the container image:
    ```bash
    docker build -t refund-pro .
    ```

2.  Run the container:
    ```bash
    docker run -p 8080:8080 refund-pro
    ```

The server will start listening on port 8080.

### Running Locally

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Start the server:
    ```bash
    python tools.py
    ```

## Development

To extend the functionality, modify `tools.py` to add new tools using the `@mcp.tool()` decorator. Ensure any new dependencies are added to `requirements.txt`.

## Acknowledgements

This project utilizes specific technologies for development and asset creation:

*   **Google Nano Banana**: Used for image generation.
*   **Gemini Models**: Used for coding assistance.
