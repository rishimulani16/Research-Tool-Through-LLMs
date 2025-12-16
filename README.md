# 📚 Research Tool Through LLMs  
### Static vs Dynamic Prompting using Streamlit, LangChain & TinyLlama

A **Streamlit-based interactive research assistant** that demonstrates the **difference, importance, and practical advantages** of **static prompting** and **dynamic prompting** in Large Language Models (LLMs).

This project is built to showcase **prompt engineering concepts** using a clean UI created with the **Streamlit library**, making the application simple, interactive, and beginner-friendly.

Unlike API-based LLM applications, this project loads the model directly from Hugging Face and performs on-device inference, ensuring zero API dependency.

Note: The output quality may be limited because this project uses TinyLlama, a lightweight (~2 GB) model. It was intentionally chosen to minimize memory usage and system load. If your system supports larger models, you can easily replace it with a more powerful Hugging Face model to achieve higher-quality results.

---

## 🚀 Project Overview

Prompt engineering plays a critical role in how effectively an LLM understands and responds to user input.  
This project focuses on comparing two prompting strategies:

- **Static Prompting** – direct user input with no enforced structure  
- **Dynamic Prompting** – structured, template-based prompts generated from UI selections  

The tool allows users to generate **research paper summaries** with different styles and levels of detail while observing how prompt design impacts the output quality.

---

## 🎨 User Interface (UI)

The complete user interface of this project is built using **Streamlit**.

### Why Streamlit?
- Rapid UI development in Python
- Interactive widgets (dropdowns, buttons, text inputs)
- Seamless integration with ML and LLM pipelines
- Ideal for prototyping AI tools

The UI enables users to:
- Select a research paper
- Choose explanation style and length
- Generate summaries with a single click

---

## 🧠 Prompting Strategies Explained


## 🔹 Static Prompting

**Static prompting** allows the user to directly type a prompt, which is passed as-is to the LLM.

#### Characteristics
- No predefined structure
- High user freedom
- Minimal processing


###🔹 Output for Static Prompting
<img width="793" height="507" alt="image" src="https://github.com/user-attachments/assets/53f7af14-fbcc-4cc7-9337-36715e4fc5d4" />


## 🔹 Dynamic Prompting

Dynamic prompting constructs the final prompt **programmatically** using structured inputs selected through the Streamlit UI.  
Instead of relying on free-form text, the prompt is generated using a predefined template, ensuring **consistency, clarity, and better control** over the LLM’s response.

### Characteristics
- Predefined prompt structure
- Controlled and guided user input
- Consistent and predictable outputs
- Reduced ambiguity and hallucinations
- Suitable for production and research tools
- 

###🔹 Output for Dynamic Prompting

<img width="758" height="891" alt="image" src="https://github.com/user-attachments/assets/01beb110-7a92-4776-95ed-a67717b6bdff" />

