import gradio as gr
from openai import OpenAI
import docx2txt
import PyPDF2



api_key = "sk-proj-CqJfTYchC9O2qM74Qbt1T3BlbkFJY0BSpxASw86qHGcthhRi"  # Replace with your key


def read_text_from_file(file_path):
    # Check the file type and read accordingly
    if file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    elif file_path.endswith('.pdf'):
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as txt_file:
            text = txt_file.read()

    
    return text

### Changed Theme to solf, and made primary color to Blue, and secondary to amber (doesnt appear to show with our layout)
with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="amber"), title=str("SJSU")) as demo:
    title="SJSU"
    ## Added a markdown to add a that this is an SJSU chatbot and to invite the EE 104 class to use it.
    gr.Markdown("""
                # SJSU Chatbot
                
                Hello EE104, please provide a file and ask a question!
                """)
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")
    filename = gr.File(file_count='multiple')


## Defining Chat user
    def user(user_message, history):
        return "", history + [[user_message, None]]


## Defining bot role
    def bot(msg, history,filename):
        history_openai_format = []
        for files in filename:
            file_contents = read_text_from_file(files)
            history_openai_format.append({"role": "user", "content": file_contents })
        
        for human, assistant in history:
            history_openai_format.append({"role": "user", "content": human })
            if assistant is not None:
                history_openai_format.append({"role": "assistant", "content":assistant})
        
        client = OpenAI(
        api_key=api_key,)
        response = client.chat.completions.create(
        messages=history_openai_format,
        # model="gpt-3.5-turbo" # gpt 3.5 turbo
        # model="gpt-4",
        model = "gpt-4-1106-preview", #gpt-4 turbo
        stream = True
        )
        history[-1][1] = ""
        partial_message = ""
        for chunk in response:
            text = (chunk.choices[0].delta.content)
            if text is not None:
                for character in text:
                        history[-1][1] += character
                        yield history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, [msg, chatbot,filename], chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)
    
demo.queue()
demo.launch(share=True)