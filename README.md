# GPT Implementation from Scratch

This repository contains a Python implementation of a Generatively Pretrained Transformer (GPT) model, built from scratch following the principles outlined in the "Attention is All You Need" paper and inspired by OpenAI's GPT architecture. This implementation is based on Andrej Karpathy's tutorial on building GPT from scratch.

## Project Overview

This project implements a GPT-1 model that can generate Shakespeare-style text. The implementation focuses on understanding the core concepts of transformer architecture and applying them to create a functional language model.

### Key Features

- Implemented in PyTorch
- Trained on Shakespeare's poetry
- Multi-head self-attention mechanism
- Configurable hyperparameters:
  - Batch size: 64
  - Context length (block size): 256
  - Embedding dimension: 384
  - Number of attention heads: 8
  - Number of transformer layers: 6
  - Dropout rate: 0.2

## File Structure

```
JKLU_GPT/
├── data/
│   └── data.txt        # Shakespeare dataset
├── gpt/
│   ├── data.py         # Data loading and preprocessing
│   ├── generate.py     # Text generation script
│   ├── gpt.py          # Main GPT implementation and training logic
│   └── JKLU_GPT.pt     # Trained model weights
└── README.md           # Project documentation
```

## Requirements

- Python 3.6+
- PyTorch

## Installation

```bash
git clone https://github.com/codernothacker/JKLU_GPT.git
cd JKLU_GPT
```

## Usage

1. **Training the model**:
```bash
python gpt.py
```

2. **Generating text**:
```bash
python generate.py
```

## Training Details

- Maximum iterations: 10,000
- Evaluation interval: 500 iterations
- Learning rate: 1e-4
- Device: Automatically uses CUDA if available, falls back to CPU
- Evaluation iterations: 200

## Implementation Details

This implementation follows the architecture described in the "Attention is All You Need" paper, with some modifications inspired by GPT-2/GPT-3. Key components include:

- Multi-head self-attention mechanism
- Positional embeddings
- Layer normalization
- Feed-forward neural networks

## Acknowledgments

- Based on Andrej Karpathy's ["Let's build GPT from scratch"](https://www.youtube.com/watch?v=kCc8FmEb1nY) tutorial
- Inspired by the ["Attention is All You Need"](https://arxiv.org/abs/1706.03762) paper
- Architecture influenced by OpenAI's GPT-2 and GPT-3
