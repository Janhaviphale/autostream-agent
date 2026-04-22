# AutoStream - Social to Lead Agentic Workflow

## Project Overview

This project implements a Conversational AI Agent for AutoStream, a fictional SaaS platform providing automated video editing tools for content creators.

The agent is capable of:
- Identifying user intent
- Answering pricing and feature questions using RAG
- Detecting high-intent users
- Capturing leads using a mock API
- Maintaining conversation memory

---

## Features

### 1. Intent Detection
The agent classifies user input into:

- Greeting
- Product/Pricing Inquiry
- High Intent Lead

### 2. RAG Powered Knowledge Retrieval

The agent retrieves information from a local knowledge base containing:

Pricing Plans:
- Basic Plan ($29/month)
- Pro Plan ($79/month)

Company Policies:
- No refunds after 7 days
- 24/7 support for Pro users

### 3. Lead Capture Tool

When a user shows high intent, the agent collects:

- Name
- Email
- Creator Platform

Then calls a mock API:
