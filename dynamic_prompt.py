from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
  

MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

@st.cache_resource #this is because it was loading the model every time and so it was taking much load and failed so by making def it will load only once
def load_chat_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    hf_model = AutoModelForCausalLM.from_pretrained(MODEL_ID)

    pipe = pipeline(
        "text-generation",
        model=hf_model,
        tokenizer=tokenizer,
        max_new_tokens=128,
        temperature=0.7
    )

    llm = HuggingFacePipeline(pipeline=pipe)
    return ChatHuggingFace(llm=llm)

model = load_chat_model()

st.header("Research Tool")
# user_input = st.text_input("Enter your Prompt:")

paper_input = st.selectbox("Select Research Paper Name", ["Select...", "Attention Is All You Need","BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:

# Explanation Style: {style_input}
# Explanation Length: {length_input}

# 1. Mathematical Details:
# - Include relevant mathematical equations if present in the paper.
# - Explain the mathematical concepts using simple, intuitive examples or pseudo-code.

# 2. Analogies:
# - Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with:
# "Insufficient information available"

# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
#     input_variables=["paper_input", "style_input", "length_input"]
# )

template = load_prompt("template.json")


#fill placeholders in the template
prompt = template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
)


if st.button("Summarize"):
    model.invoke(prompt)
    result = model.invoke(prompt)
    st.write(result.content) 
