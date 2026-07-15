import gradio as gr
from ui.callbacks import chat, clear_chat


def create_interface(pipeline):
    """
    Create the user interface
    """

    with gr.Blocks(title="Documentation-Expet") as gradio_ui:

        # chat_history created purely for UI 
        chat_history = gr.State([])

        with gr.Row():
            
            # single line grouped checkboxes, choices tuples -> (what user sees, what is passed to backend)
            selected_libraries = gr.CheckboxGroup(
                choices=[
                    ("Python", "python"),
                    ("Pandas", "pandas"),
                    ("Langchain", "langchain")
                    ], 
                label="Select libraries"
                )

        with gr.Row():

            # not ChatInterface since we need to add libray selection, buttons, etc
            chatbox = gr.Chatbot(height=600, type="messages")
            
        with gr.Row():

            # Textbox for user questions
            user_input = gr.Textbox(
                label="Question", 
                placeholder="Ask a question about Python, Pandas or Langchain",
                lines=2
                )

        with gr.Row():

            # clear button on left, empty markdown gives space between them, send button on the right
            clear_button = gr.Button(value="Clear Conversation", variant="stop")
            gr.Markdown("")
            send_button = gr.Button(value="Send", variant="primary")


        # lambda fucntion to pass pipeline to the chat function.
        # On button click, pipeline - python object is passed to chat fn and 
        # question - user_input, libraries - selected_libraries, chat_history -> gradio components are passed to chat fn
        # pipeline cannot be passed inside inputs list since it is not a gradio component    
        send_button.click(
            fn= lambda question, libraries, chat_history:
                chat(pipeline=pipeline, question=question, libraries=libraries, chat_history=chat_history),
                inputs=[user_input, selected_libraries, chat_history],
                outputs=[chatbox, chat_history, user_input]
        )

        clear_button.click(
            fn=lambda chat_history:
                clear_chat(pipeline=pipeline, chat_history=chat_history),
            inputs=[chat_history],
            outputs=[chatbox, chat_history, user_input]
        )

    return gradio_ui