# LLM API Experiment

## Overview
This project uses the OpenAI API to test how different prompts and parameters affect responses.

## What I Tested
- Multiple prompts about recursion
- Different temperature values (0.2, 0.7, 0.9)
- Different system messages:
  - Helpful assistant
  - Sarcastic assistant
  - Strict professor

## Observations
- Lower temperature (0.2) produced more consistent and factual responses
- Higher temperature (0.9) produced more creative and varied responses
- System messages strongly changed tone and style of answers
- Prompt wording significantly affected the output

## Files
- main.py → Python code for experiments
- results.txt → Output results from the model
