# -*- coding: utf-8 -*-
"""Short_story_gen.ipynb

Original file is located at
    https://colab.research.google.com/drive/1NYJ27Xx3CdQBemzQ-UmezoiN4A-KNW94
"""

!pip install transformers gradio torch --quiet

!pip install --upgrade gradio

from transformers import pipeline,set_seed

story_generator = pipeline('text-generation',model='gpt2')
set_seed(42)

def generate_story(theme,character,location):
  prompt=f"once upon a time in {location},there lived a {character} who loved {theme}.one day,"
  story=story_generator(prompt,max_length=200,num_return_sequences=1)[0]['generated_text']
  return story

import gradio as gr
interface=gr.Interface(fn=generate_story,inputs=[
    gr.Textbox(label="Theme (e.g.,adventure,kkindness,magic)"),
    gr.Textbox(label="Main character(e.g.,unicorn,robot,fairy)"),
    gr.Textbox(label="Location(e.g.,enhanced forest,outer space,jungle)")
    ],
                       outputs=gr.Textbox(label="generated Story"),
                       title="StoryCrafter-Short Story Generator for kids",
                       description="Enter a theme ,aharacter,and location to generate")
interface.launch()
