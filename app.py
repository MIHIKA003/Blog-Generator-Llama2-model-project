import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## function to get response from Llama 2 model
def getLlamaresponse(input_text, no_words, blog_style):
    
    ## Llama2 model
    llm=CTransformers(model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':128,
                              'temperature':0.01})
    
    ## prompt template
    
    template="""
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_words} words.
    """
    
    prompt=PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                          template=template)
    
    
    ## Generate the response form Llama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="BlogBot",
                   page_icon="(<-|->)",
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("BlogBot (<-|->)")

input_text = st.text_input("Enter the topic for your blog")

## creating 2 more columns for additional fields
col1, col2 = st.columns([5,5])

with col1:
    no_words=st.text_input('Number of words')
with col2:
    blog_style=st.selectbox('Writing the blog for',('Researchers','Data Scientists','Common People','Students'), index=0)


submit=st.button("Generate") 

## final response
if submit:
    st.write(getLlamaresponse(input_text, no_words, blog_style))