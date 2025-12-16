from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
import streamlit as st

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
user_input = st.text_input("Enter your Prompt:")

if st.button("Summarize") and user_input:
    result = model.invoke(user_input)
    st.write(result.content)
