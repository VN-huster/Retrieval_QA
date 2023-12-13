from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import random
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from llmbackbone import language_model

api_key = []

def check_polite_question(text):
    #input = translate_input(text)
    llm = OpenAI(temperature=.7, openai_api_key=random.choice(api_key)) 
    template = """Chuỗi dưới đây có mang ý tiêu cực không? 
    Question: {text}
    Answer:
    """
    prompt_template = PromptTemplate(input_variables=["text"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)
    answer = answer_chain.run(input)
    return answer.strip()


def answer_base_content(question, context):
    llm = OpenAI(temperature=.7, openai_api_key=random.choice(api_key))
    template = """Từ nội dung Quy chế sau "context", trả lời câu hỏi "question", nếu không có thông tin thì trả lời ngắn gọn "Tôi không có thông tin".:
    Câu hỏi: {question}
    {context}
    """
    prompt_template = PromptTemplate(input_variables=["context", "question"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)
    answer = answer_chain.run(question=question, context=context)
    return answer


def answer_base_content2(question, context):
    llm = language_model()
    template = """Từ nội dung Quy chế sau "context", trả lời câu hỏi "question", nếu không có thông tin thì trả lời ngắn gọn "Tôi không có thông tin".:
    Câu hỏi: {question}
    {context}
    """
    prompt_template = PromptTemplate(input_variables=["context", "question"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)
    answer = answer_chain.run(question=question, context=context)
    return answer


greet = ["hi", "hello", "hey", "này", "ê", "chào", "xin chào", "chào buổi sáng"]
utter_greet = "Tôi là Minh Nguyệt, cán bộ tư vấn đào tạo của Trường Đại học Công nghệ. Tôi giúp gì được cho bạn."

farewell = ["bye", "goodbye", "bye bye", "tạm biệt", "hẹn gặp lại"]
utter_farewell = "Tạm biệt bạn."

ask_name = ["cậu tên gì", "bạn tên gì", "bạn là ai", "cậu là ai", "bạn tên là gì", "cậu tên là gì", "tên bạn là gì", "tên cậu là gì"]
utter_ask_name = "Tôi là Minh Nguyệt, cán bộ tư vấn đào tạo của Trường Đại học Công nghệ."

thanks = ["cảm ơn", "cám ơn", "thanks", "thank you"]
utter_thansks = "Rất vui được nói chuyện với bạn."



def take_score(text, choice):
  score = process.extract(text, choice, limit=1, scorer=fuzz.token_sort_ratio )
  return score[0][1]

def sort_score(text):
  score = {}
  score.update({utter_greet: take_score(text, greet)})
  score.update({utter_farewell: take_score(text, farewell)})
  score.update({utter_ask_name: take_score(text, ask_name)})
  score.update({utter_thansks: take_score(text, thanks)})
 

  sorted_data = dict(sorted(score.items(), key=lambda item: item[1], reverse=True))
  print(sorted_data)
  responce = next(iter(sorted_data.items()))

  if responce[1] > 80:
    return responce[0]
  return "Tôi không có thông tin"
