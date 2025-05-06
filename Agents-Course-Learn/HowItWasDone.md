# Course Onboarding: Running Models Locally & Understanding Agents

![Image Description](share.png)

## Step 1: Running Models Locally with Ollama

*(In case you run into credit limits)*

```bash
ollama pull qwen2:7b  # Check out ollama website for more models
```

```python
from smolagents import LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/qwen2:7b",
    api_base="http://127.0.0.1:11434",  # Default Ollama local server
    num_ctx=8192,
)
```

---

## Step 2: What are Agents?

**An Agent** = An AI model capable of reasoning, planning, and interacting with its environment.

> We call it an *Agent* because it has **agency** — the ability to act and influence the environment.

### The Brain (AI Model)

* Handles **thinking**: reasoning, planning.
* Decides which **Actions** to take based on the situation.

### The Body (Capabilities and Tools)

* Everything the Agent can *do*.
* The actions depend on what the Agent is equipped with.
* Example: Humans can walk, run, grab, but can't fly.

---

## The Spectrum of Agency

| Agency Level | Description                                              | What it’s called | Example Pattern                                    |
| :----------: | :------------------------------------------------------- | :--------------- | :------------------------------------------------- |
|      ☆☆☆     | Agent output has no impact on program flow               | Simple processor | `process_llm_output(llm_response)`                 |
|      ★☆☆     | Agent output determines basic control flow               | Router           | `if llm_decision(): path_a() else: path_b()`       |
|      ★★☆     | Agent output determines function execution               | Tool caller      | `run_function(llm_chosen_tool, llm_chosen_args)`   |
|      ★★★     | Agent output controls iteration and program continuation | Multi-step Agent | `while llm_should_continue(): execute_next_step()` |
|      ★★★     | One agentic workflow can start another agentic workflow  | Multi-Agent      | `if llm_trigger(): execute_agent()`                |

---

An Agent can perform any task we implement via **Tools** to complete **Actions**.

> Tools provide the Agent with the ability to execute actions a text-generation model cannot perform natively, such as making coffee or generating images.

Note that Actions are not the same as Tools. An Action, for instance, can involve the use of multiple Tools to complete.

Allowing an agent to interact with its environment allows real-life usage for companies and individuals.

#### **Example 1: Personal Virtual Assistants**

Virtual assistants like Siri, Alexa, or Google Assistant, work as agents when they interact on behalf of users using their digital environments.

They take user queries, analyze context, retrieve information from databases, and provide responses or initiate actions (like setting reminders, sending messages, or controlling smart devices).

#### **Example 2: Customer Service Chatbots**

Many companies deploy chatbots as agents that interact with customers in natural language.

These agents can answer questions, guide users through troubleshooting steps, open issues in internal databases, or even complete transactions.

Their predefined objectives might include improving user satisfaction, reducing wait times, or increasing sales conversion rates. By interacting directly with customers, learning from the dialogues, and adapting their responses over time, they demonstrate the core principles of an agent in action.

#### **Example 3: AI Non-Playable Character in a video game**

AI agents powered by LLMs can make Non-Playable Characters (NPCs) more dynamic and unpredictable.

Instead of following rigid behavior trees, they can respond contextually, adapt to player interactions, and generate more nuanced dialogue. This flexibility helps create more lifelike, engaging characters that evolve alongside the player’s actions.

#### **To summarize,** 

* an Agent is a system that uses an AI Model (typically an LLM) as its core reasoning engine, to:

* Understand natural language: Interpret and respond to human instructions in a meaningful way.

* Reason and plan: Analyze information, make decisions, and devise strategies to solve problems.

* Interact with its environment: Gather information, take actions, and observe the results of those actions.

---

## Step 3: What are LLMs?

An LLM is a type of AI model that excels at understanding and generating human language. They are trained on vast amounts of text data, allowing them to learn patterns, structure, and even nuance in language. These models typically consist of many millions of parameters.

Most LLMs nowadays are built on the Transformer architecture—a deep learning architecture based on the “Attention” algorithm, that has gained significant interest since the release of BERT from Google in 2018.

There are **3** types of transformers:

#### Encoders
An encoder-based Transformer takes text (or other data) as input and outputs a dense representation (or embedding) of that text.

Example: BERT from Google
Use Cases: Text classification, semantic search, Named Entity Recognition
Typical Size: Millions of parameters

#### Decoders
A decoder-based Transformer focuses on generating new tokens to complete a sequence, one token at a time.

Example: Llama from Meta
Use Cases: Text generation, chatbots, code generation
Typical Size: Billions (in the US sense, i.e., 10^9) of parameters

#### Seq2Seq (Encoder–Decoder)
A sequence-to-sequence Transformer combines an encoder and a decoder. The encoder first processes the input sequence into a context representation, then the decoder generates an output sequence.

Example: T5, BART
Use Cases: Translation, Summarization, Paraphrasing
Typical Size: Millions of parameters

Although Large Language Models come in various forms, LLMs are typically decoder-based models with billions of parameters.

> The underlying principle of an LLM is simple yet highly effective: its objective is to predict the next token, given a sequence of previous tokens. A “token” is the unit of information an LLM works with. You can think of a “token” as if it was a “word”, but for efficiency reasons LLMs don’t use whole words.


