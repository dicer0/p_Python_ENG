[![MasterHead](http://dicer0.com/wp-content/uploads/2023/09/Python-di_cer0-Banner.png)](https://dicer0.com/)
# p_Python_ENG
<h6 align="justify">
  <ul>
    <li>p_ Indicates that this technology belongs to the programming category.</li>
    <li>_ENG means that the documentation is in English</li>
  </ul>
</h6>
And this specific repository contains documentation about the Python programming language, which is used to develop multiple applications with Artificial Intelligence, Machine Learning, Artificial Vision, Data Science, Virtual Instrumentation, etc.
&nbsp;
<br/>
&nbsp;

## Thomson Reuters Assignment

In `main.py`, we have provided a shell of a FastAPI app. It includes one route that demonstrates streaming data using Server-Sent Events (SSEs)

In `llm.py`, we have provided some code for prompting the Large Language Model (LLM) both synchronously and asynchronously. The prompts can be left as-is for this assignment. But we want to see aptitude in calling the LLM API and properly handling the response. See https://platform.openai.com/docs/api-reference/chat and https://platform.openai.com/docs/guides/text-generation/chat-completions-api?lang=python for more information about OpenAI's Chat Completions service. See https://github.com/openai/openai-cookbook/blob/main/examples/How_to_stream_completions.ipynb for information about receiving streaming results.

Please modify the file (or add your own files and organize them in any way you like) such that:
- The API provides a barebones Chat service that a front-end client can use.
- The service should have the following capabilities:
    - an HTTP client can create a new chat session
    - given a chat session (e.g. its ID), an HTTP client can send a message on behalf of the user, and receive the "AI" response from the LLM.
    - responses from the AI should be streamed using the SSE mechanism mentioned above.
    - an HTTP client can also fetch the entire message history for a given session

You'll likely need some sort of persistence. It's 100% acceptable to store chat messages in memory, but if you want to show off, feel free to use any of SQLite, Postgres, Redis, or just flat files for persistence. If you do this, make sure the rest of the functional requirements are met.

Do not worry about things like user authentication or really any other production consideration not already mentioned above.

[![Python](http://dicer0.com/wp-content/uploads/2024/03/p_Python.png)](https://dicer0.com/#skills)
