# ${AI}^2R$ : Automated \& Adaptive Incident Response Leveraging CoT Reasoning, LLMs, and CTI
${AI}^2R$ : – A Chain-of-Thought Retrieval-Augmented Generation (CoT-RAG) framework for Incident Response, integrating Cyber Threat Intelligence (CTI) to improve alert triage, contextual enrichment, and analyst efficiency. Includes prompts, results (CoT vs no-CoT), and simulated alerts from experiments.

## 📂 Repository Organization

- **prompts/**  
  Contains all the prompt templates used in our proposed solution **${AI}^2R**.  
  - `prompts_templates.py`

- **results/**  
Contains structured experiment outputs including:  
  - The original **SIEM alert**.  
  - The corresponding **CTI enrichment** (extracted intelligence).  
  - The **generated response** from the model.  

  Files are separated by reasoning mode:
  - `results_CoT.json` → Results with Chain-of-Thought reasoning (step-by-step SOC, CTI, and IR responses).  
  - `results_noCoT.json` → Results without Chain-of-Thought reasoning.

  ## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/<username>/AI2R.git
   cd AI2R
 
  

