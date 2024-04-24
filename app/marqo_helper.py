import io
import marqo
import streamlit as st


## VARIABLES ##
index_name = "notes"
model="hf/e5-base-v2"
mq = marqo.Client(url="http://marqo.fmarchal.net:8882")
mq_nb_result = 5

@st.cache_data
def create_index():
    try:
        mq.delete_index(index_name)
    except:
        pass
    mq.create_index(index_name, model=model)

def import_data(txt_files):


    for txt_file in txt_files:
        print (txt_file.name)
        content = io.TextIOWrapper(txt_file, encoding='utf-8').read()
        print (content)
        mq.index(index_name).add_documents(
        [
            {
                "note": content,
                "_id": txt_file.name,
            },
        ],
        tensor_fields=["note"],
        )


def mq_search(question):
    results = mq.index(index_name).search(
        q=question, limit=mq_nb_result
    )
    return results