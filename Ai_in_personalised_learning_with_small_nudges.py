{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Kesharwani-123/Ai-in-personalised-learning-with-small-nudges/blob/main/Ai_in_personalised_learning_with_small_nudges.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qQUvuv9gFE-5",
        "outputId": "c1dd803e-1c88-413a-c637-0235272cc4eb"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.48.1-py3-none-any.whl.metadata (9.5 kB)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (2.2.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.11/dist-packages (2.0.2)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.11/dist-packages (3.10.0)\n",
            "Requirement already satisfied: plotly in /usr/local/lib/python3.11/dist-packages (5.24.1)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.11/dist-packages (1.6.1)\n",
            "Requirement already satisfied: nltk in /usr/local/lib/python3.11/dist-packages (3.9.1)\n",
            "Requirement already satisfied: textblob in /usr/local/lib/python3.11/dist-packages (0.19.0)\n",
            "Requirement already satisfied: transformers in /usr/local/lib/python3.11/dist-packages (4.55.0)\n",
            "Collecting pyngrok\n",
            "  Downloading pyngrok-7.3.0-py3-none-any.whl.metadata (8.1 kB)\n",
            "Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.2.1)\n",
            "Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (25.0)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.3.0)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.5)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.14.1)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m2.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.45)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.2)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (1.3.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (4.59.0)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (1.4.9)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib) (3.2.3)\n",
            "Requirement already satisfied: scipy>=1.6.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (1.16.1)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (1.5.1)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (3.6.0)\n",
            "Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.11/dist-packages (from nltk) (2024.11.6)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.11/dist-packages (from nltk) (4.67.1)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from transformers) (3.18.0)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.34.0 in /usr/local/lib/python3.11/dist-packages (from transformers) (0.34.4)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.11/dist-packages (from transformers) (6.0.2)\n",
            "Requirement already satisfied: tokenizers<0.22,>=0.21 in /usr/local/lib/python3.11/dist-packages (from transformers) (0.21.4)\n",
            "Requirement already satisfied: safetensors>=0.4.3 in /usr/local/lib/python3.11/dist-packages (from transformers) (0.6.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.1.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.34.0->transformers) (2025.3.0)\n",
            "Requirement already satisfied: hf-xet<2.0.0,>=1.1.3 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub<1.0,>=0.34.0->transformers) (1.1.7)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.3)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.8.3)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.4.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.0)\n",
            "Downloading streamlit-1.48.1-py3-none-any.whl (9.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.9/9.9 MB\u001b[0m \u001b[31m67.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pyngrok-7.3.0-py3-none-any.whl (25 kB)\n",
            "Downloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m115.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m6.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pyngrok, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 pyngrok-7.3.0 streamlit-1.48.1 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit pandas numpy matplotlib plotly scikit-learn nltk textblob transformers pyngrok\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "-V3vXUb-Fb16"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "\n",
        "folders = [\"data\", \"app\", \"models\"]\n",
        "for folder in folders:\n",
        "    os.makedirs(folder, exist_ok=True)\n",
        "\n",
        "# Create empty CSV for goals\n",
        "import pandas as pd\n",
        "pd.DataFrame(columns=[\"Goal\", \"Deadline\", \"Progress\", \"Created_At\"]).to_csv(\"data/goals.csv\", index=False)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Zsmmv1lYFhyL",
        "outputId": "1fe63d27-5199-42bd-d4e7-1a850dc52f55"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Writing app/goal_manager.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app/goal_manager.py\n",
        "import pandas as pd\n",
        "from datetime import datetime\n",
        "\n",
        "GOAL_FILE = \"data/goals.csv\"\n",
        "\n",
        "def load_goals():\n",
        "    try:\n",
        "        return pd.read_csv(GOAL_FILE)\n",
        "    except FileNotFoundError:\n",
        "        return pd.DataFrame(columns=[\"Goal\", \"Deadline\", \"Progress\", \"Created_At\"])\n",
        "\n",
        "def save_goals(df):\n",
        "    df.to_csv(GOAL_FILE, index=False)\n",
        "\n",
        "def add_goal(goal, deadline):\n",
        "    df = load_goals()\n",
        "    new_entry = {\"Goal\": goal, \"Deadline\": deadline, \"Progress\": 0, \"Created_At\": datetime.now()}\n",
        "    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)\n",
        "    save_goals(df)\n",
        "    return df\n",
        "\n",
        "def update_progress(goal, progress):\n",
        "    df = load_goals()\n",
        "    df.loc[df[\"Goal\"] == goal, \"Progress\"] = progress\n",
        "    save_goals(df)\n",
        "    return df\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H4A5MoFTMv32",
        "outputId": "ae003ff3-bdd1-4e24-aa0a-98a156c3c222"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Overwriting app/sentiment_analysis.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app/sentiment_analysis.py\n",
        "from transformers import pipeline\n",
        "\n",
        "# Load transformer-based sentiment pipeline (distilbert fine-tuned for sentiment)\n",
        "sentiment_pipeline = pipeline(\"sentiment-analysis\")\n",
        "\n",
        "def analyze_sentiment(text):\n",
        "    if not text.strip():\n",
        "        return \"Neutral\", 0.0\n",
        "    result = sentiment_pipeline(text)[0]\n",
        "    label = result['label']\n",
        "    score = result['score']\n",
        "    # Normalize to Positive / Neutral / Negative\n",
        "    if label.lower() == \"positive\":\n",
        "        sentiment = \"Positive\"\n",
        "    elif label.lower() == \"negative\":\n",
        "        sentiment = \"Negative\"\n",
        "    else:\n",
        "        sentiment = \"Neutral\"\n",
        "    return sentiment, score\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "n5L-GTL_NE3m"
      },
      "outputs": [],
      "source": [
        "%%writefile app/motivation_engine.py\n",
        "import random\n",
        "\n",
        "positive_quotes = [\n",
        "    \"Great job! Keep up the momentum! 🚀\",\n",
        "    \"You're doing amazing, stay consistent! 💪\",\n",
        "    \"Success is the sum of small efforts, repeated daily. 🌟\"\n",
        "]\n",
        "\n",
        "negative_quotes = [\n",
        "    \"Every setback is a setup for a comeback! 🔥\",\n",
        "    \"Don’t give up, you’re closer than you think! 💡\",\n",
        "    \"Tough times don’t last, but tough people do. 🌈\"\n",
        "]\n",
        "\n",
        "progress_quotes = [\n",
        "    \"You're making solid progress — stay on track! 📈\",\n",
        "    \"Halfway there! Keep pushing towards your goal. 🏁\",\n",
        "    \"Outstanding! You're nearly done — finish strong! 🥇\"\n",
        "]\n",
        "\n",
        "def get_motivation(sentiment, progress=None):\n",
        "    if progress is not None:\n",
        "        if progress >= 80:\n",
        "            return random.choice(progress_quotes)\n",
        "        elif progress >= 50:\n",
        "            return \"You're halfway through — keep going strong! 💪\"\n",
        "    if sentiment == \"Positive\":\n",
        "        return random.choice(positive_quotes)\n",
        "    else:\n",
        "        return random.choice(negative_quotes)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-KCigPvDI0pE",
        "outputId": "65c00040-8191-4002-8867-fdad3503c36a"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m43.9/43.9 kB\u001b[0m \u001b[31m1.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for cloudflared (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit pandas numpy matplotlib plotly scikit-learn nltk textblob transformers cloudflared --quiet\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cCVlA05uNUEE",
        "outputId": "bd62d9c5-a225-48dc-8979-cffac3dd5351"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2025-08-15 05:30:34.857 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.858 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.859 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.860 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.861 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.861 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.862 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.863 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.864 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.864 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.865 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.867 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.867 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.869 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.870 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:30:34.871 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "# ---------- Daily Reflection ----------\n",
        "st.subheader(\"📝 Daily Reflection & Motivation\")\n",
        "reflection = st.text_area(\"How do you feel about your learning today?\")\n",
        "if st.button(\"Analyze Sentiment\"):\n",
        "    sentiment, polarity = analyze_sentiment(reflection)\n",
        "    save_reflection(datetime.now().date(), reflection, sentiment, polarity)\n",
        "\n",
        "    # If any goal selected, pass its progress\n",
        "    progress_for_feedback = None\n",
        "    if not load_goals().empty:\n",
        "        selected_goal_for_motivation = st.selectbox(\"Select Goal for Feedback\", load_goals()[\"Goal\"])\n",
        "        goal_df = load_goals()\n",
        "        progress_for_feedback = goal_df.loc[goal_df[\"Goal\"] == selected_goal_for_motivation, \"Progress\"].values[0]\n",
        "\n",
        "    st.write(f\"Sentiment: **{sentiment}** (Confidence: {polarity:.2f})\")\n",
        "    st.info(get_motivation(sentiment, progress_for_feedback))\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Y9reuuClNiy3"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uYtspmUzL7Ik",
        "outputId": "91f1cfdd-5372-4467-9ba0-be13e35f1eb8"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "2025-08-15 05:24:32.385 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.387 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.578 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-08-15 05:24:32.581 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.582 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.584 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.586 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.586 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.587 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.588 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.588 Session state does not function when running a script without `streamlit run`\n",
            "2025-08-15 05:24:32.590 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.591 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.592 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.593 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.594 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.595 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.596 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.597 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.598 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.599 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.600 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.601 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.603 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.603 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.605 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.605 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.606 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.614 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.615 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.617 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.618 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.618 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.619 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.621 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.622 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.623 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.624 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.625 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.628 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.629 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.630 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.632 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.634 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.635 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.636 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.636 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.637 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.641 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.642 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.642 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.646 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.647 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.648 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.648 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.649 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.650 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.651 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.651 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.652 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.653 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.654 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.654 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.655 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.655 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.656 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.656 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.659 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.660 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.661 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.661 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-08-15 05:24:32.662 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "from datetime import datetime\n",
        "import plotly.express as px\n",
        "\n",
        "from app.goal_manager import add_goal, update_progress, load_goals\n",
        "from app.sentiment_analysis import analyze_sentiment\n",
        "from app.motivation_engine import get_motivation\n",
        "\n",
        "# ========================\n",
        "# Data files\n",
        "GOAL_FILE = \"data/goals.csv\"\n",
        "REFLECTION_FILE = \"data/reflections.csv\"\n",
        "\n",
        "# ========================\n",
        "# Load Reflections\n",
        "def load_reflections():\n",
        "    try:\n",
        "        return pd.read_csv(REFLECTION_FILE)\n",
        "    except FileNotFoundError:\n",
        "        return pd.DataFrame(columns=[\"Date\", \"Reflection\", \"Sentiment\", \"Polarity\"])\n",
        "\n",
        "def save_reflection(date, reflection, sentiment, polarity):\n",
        "    df = load_reflections()\n",
        "    new_entry = {\"Date\": date, \"Reflection\": reflection, \"Sentiment\": sentiment, \"Polarity\": polarity}\n",
        "    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)\n",
        "    df.to_csv(REFLECTION_FILE, index=False)\n",
        "\n",
        "# ========================\n",
        "# App Layout\n",
        "st.set_page_config(page_title=\"AI Learning Goal Tracker\", layout=\"wide\")\n",
        "st.title(\"🎯 AI Learning Goal Tracker\")\n",
        "\n",
        "# ---------- Add Goal ----------\n",
        "with st.expander(\"➕ Add a New Goal\"):\n",
        "    goal = st.text_input(\"Goal\")\n",
        "    deadline = st.date_input(\"Deadline\")\n",
        "    if st.button(\"Add Goal\"):\n",
        "        df = add_goal(goal, deadline)\n",
        "        st.success(\"Goal added successfully!\")\n",
        "        st.dataframe(df)\n",
        "\n",
        "# ---------- Update Progress ----------\n",
        "with st.expander(\"📈 Update Progress\"):\n",
        "    goals_df = load_goals()\n",
        "    if not goals_df.empty:\n",
        "        selected_goal = st.selectbox(\"Select Goal\", goals_df[\"Goal\"])\n",
        "        progress = st.slider(\"Progress %\", 0, 100)\n",
        "        if st.button(\"Update Progress\"):\n",
        "            df = update_progress(selected_goal, progress)\n",
        "            st.success(\"Progress updated!\")\n",
        "            st.dataframe(df)\n",
        "\n",
        "# ---------- Show Goals with Progress Bars ----------\n",
        "if not load_goals().empty:\n",
        "    st.subheader(\"📊 Goal Progress Overview\")\n",
        "    for _, row in load_goals().iterrows():\n",
        "        st.write(f\"**{row['Goal']}** (Deadline: {row['Deadline']})\")\n",
        "        st.progress(int(row['Progress']))\n",
        "\n",
        "# ---------- Daily Reflection ----------\n",
        "st.subheader(\"📝 Daily Reflection & Motivation\")\n",
        "reflection = st.text_area(\"How do you feel about your learning today?\")\n",
        "if st.button(\"Analyze Sentiment\"):\n",
        "    sentiment = analyze_sentiment(reflection)\n",
        "    polarity = round(pd.Series(reflection).apply(lambda x: analyze_sentiment(x) == \"Positive\").mean(), 2)\n",
        "    save_reflection(datetime.now().date(), reflection, sentiment, polarity)\n",
        "    st.write(f\"Sentiment: **{sentiment}**\")\n",
        "    st.info(get_motivation(sentiment))\n",
        "\n",
        "# ---------- Sentiment Trend ----------\n",
        "ref_df = load_reflections()\n",
        "if not ref_df.empty:\n",
        "    st.subheader(\"📅 Weekly Sentiment Trend\")\n",
        "    fig = px.line(ref_df, x=\"Date\", y=\"Polarity\", title=\"Sentiment Polarity Over Time\", markers=True)\n",
        "    st.plotly_chart(fig)\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "szq9p4RjNqNZ",
        "outputId": "34b76555-509d-44f4-81a7-cb8bfbe89c8d"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Writing app/filename.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile app/filename.py\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true,
          "base_uri": "https://localhost:8080/"
        },
        "id": "Fy5djnCsNv4T",
        "outputId": "3b77600b-5d87-4f0e-b7b6-d730de3c68c1"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K⠼\u001b[1G\u001b[0K⠴\u001b[1G\u001b[0K⠦\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.23.246.119:8501\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[1G\u001b[0K⠧\u001b[1G\u001b[0K⠇\u001b[1G\u001b[0K⠏\u001b[1G\u001b[0K⠋\u001b[1G\u001b[0K⠙\u001b[1G\u001b[0K⠹\u001b[1G\u001b[0K⠸\u001b[1G\u001b[0K\u001b[90m2025-08-15T05:32:29Z\u001b[0m \u001b[32mINF\u001b[0m Thank you for trying Cloudflare Tunnel. Doing so, without a Cloudflare account, is a quick way to experiment and try it out. However, be aware that these account-less Tunnels have no uptime guarantee, are subject to the Cloudflare Online Services Terms of Use (https://www.cloudflare.com/website-terms/), and Cloudflare reserves the right to investigate your use of Tunnels for violations of such terms. If you intend to use Tunnels in production you should use a pre-created named tunnel by following: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps\n",
            "\u001b[90m2025-08-15T05:32:29Z\u001b[0m \u001b[32mINF\u001b[0m Requesting new quick Tunnel on trycloudflare.com...\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m +--------------------------------------------------------------------------------------------+\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m |  https://unnecessary-pathology-new-filename.trycloudflare.com                              |\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m +--------------------------------------------------------------------------------------------+\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m Cannot determine default configuration path. No file [config.yml config.yaml] in [~/.cloudflared ~/.cloudflare-warp ~/cloudflare-warp /etc/cloudflared /usr/local/etc/cloudflared]\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m Version 2025.8.0 (Checksum c7d3a69da0f7b9b1bc1ddcb0597d3552bcd7c15f8bbaba463dc489b94b7544ee)\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m GOOS: linux, GOVersion: go1.24.4, GoArch: amd64\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m Settings: map[ha-connections:1 no-autoupdate:true protocol:quic url:http://localhost:8501]\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m cloudflared will not automatically update when run from the shell. To enable auto-updates, run cloudflared as a service: https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/configure-tunnels/local-management/as-a-service/\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m Generated Connector ID: 5c3f315a-b806-4df6-83af-c7762f691040\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m Initial protocol quic\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m ICMP proxy will use 172.28.0.12 as source for IPv4\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m ICMP proxy will use :: as source for IPv6\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[1m\u001b[31mERR\u001b[0m\u001b[0m Cannot determine default origin certificate path. No file cert.pem in [~/.cloudflared ~/.cloudflare-warp ~/cloudflare-warp /etc/cloudflared /usr/local/etc/cloudflared]. You need to specify the origin certificate path by specifying the origincert option in the configuration file, or set TUNNEL_ORIGIN_CERT environment variable \u001b[36moriginCertPath=\u001b[0m\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m ICMP proxy will use 172.28.0.12 as source for IPv4\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m ICMP proxy will use :: as source for IPv6\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m Starting metrics server on 127.0.0.1:20241/metrics\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m Tunnel connection curve preferences: [X25519MLKEM768 CurveP256] \u001b[36mconnIndex=\u001b[0m0 \u001b[36mevent=\u001b[0m0 \u001b[36mip=\u001b[0m198.41.200.23\n",
            "2025/08/15 05:32:33 failed to sufficiently increase receive buffer size (was: 208 kiB, wanted: 7168 kiB, got: 416 kiB). See https://github.com/quic-go/quic-go/wiki/UDP-Buffer-Sizes for details.\n",
            "\u001b[90m2025-08-15T05:32:33Z\u001b[0m \u001b[32mINF\u001b[0m Registered tunnel connection \u001b[36mconnIndex=\u001b[0m0 \u001b[36mconnection=\u001b[0m6dbc5c02-3b53-492f-b944-3758572d4f95 \u001b[36mevent=\u001b[0m0 \u001b[36mip=\u001b[0m198.41.200.23 \u001b[36mlocation=\u001b[0matl10 \u001b[36mprotocol=\u001b[0mquic\n",
            "2025-08-15 05:33:17.480999: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:467] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
            "WARNING: All log messages before absl::InitializeLog() is called are written to STDERR\n",
            "E0000 00:00:1755235997.509142    9533 cuda_dnn.cc:8579] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
            "E0000 00:00:1755235997.517575    9533 cuda_blas.cc:1407] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n",
            "W0000 00:00:1755235997.539602    9533 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.\n",
            "W0000 00:00:1755235997.539643    9533 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.\n",
            "W0000 00:00:1755235997.539647    9533 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.\n",
            "W0000 00:00:1755235997.539651    9533 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.\n",
            "2025-08-15 05:33:17.546554: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.\n",
            "To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.\n",
            "No model was supplied, defaulted to distilbert/distilbert-base-uncased-finetuned-sst-2-english and revision 714eb0f (https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).\n",
            "Using a pipeline without specifying a model name and revision in production is not recommended.\n",
            "config.json: 100% 629/629 [00:00<00:00, 3.03MB/s]\n",
            "model.safetensors: 100% 268M/268M [00:10<00:00, 25.7MB/s]\n",
            "tokenizer_config.json: 100% 48.0/48.0 [00:00<00:00, 244kB/s]\n",
            "vocab.txt: 232kB [00:00, 7.28MB/s]\n",
            "Device set to use cpu\n",
            "2025-08-15 05:34:22.960 Serialization of dataframe to Arrow table was unsuccessful. Applying automatic fixes for column types to make the dataframe Arrow-compatible.\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/streamlit/dataframe_util.py\", line 821, in convert_pandas_df_to_arrow_bytes\n",
            "    table = pa.Table.from_pandas(df)\n",
            "            ^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"pyarrow/table.pxi\", line 4751, in pyarrow.lib.Table.from_pandas\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/pyarrow/pandas_compat.py\", line 625, in dataframe_to_arrays\n",
            "    arrays = [convert_column(c, f)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/pyarrow/pandas_compat.py\", line 625, in <listcomp>\n",
            "    arrays = [convert_column(c, f)\n",
            "              ^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/pyarrow/pandas_compat.py\", line 612, in convert_column\n",
            "    raise e\n",
            "  File \"/usr/local/lib/python3.11/dist-packages/pyarrow/pandas_compat.py\", line 606, in convert_column\n",
            "    result = pa.array(col, type=type_, from_pandas=True, safe=safe)\n",
            "             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
            "  File \"pyarrow/array.pxi\", line 360, in pyarrow.lib.array\n",
            "  File \"pyarrow/array.pxi\", line 87, in pyarrow.lib._ndarray_to_array\n",
            "  File \"pyarrow/error.pxi\", line 92, in pyarrow.lib.check_status\n",
            "pyarrow.lib.ArrowTypeError: (\"Expected bytes, got a 'datetime.date' object\", 'Conversion failed for column Deadline with type object')\n",
            "2025-08-15 05:42:27.943 Session with id a2b4fcc8-d54e-4f18-a77c-03826311e154 is already connected! Connecting to a new session.\n",
            "2025-08-15 05:42:29.815 Session with id 5ecd8468-1f42-483f-b173-96ca489e9db4 is already connected! Connecting to a new session.\n"
          ]
        }
      ],
      "source": [
        "!kill -9 $(lsof -t -i:8501) 2>/dev/null || true\n",
        "!streamlit run streamlit_app.py --server.port 8501 & npx cloudflared tunnel --url http://localhost:8501 --no-autoupdate\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPaQsb95i+uh4DDWC/N5V0q",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
