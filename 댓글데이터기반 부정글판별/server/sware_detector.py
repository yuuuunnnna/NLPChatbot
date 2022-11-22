from xml.dom.minidom import Element
import pandas as pd
import matplotlib.pyplot as plt
import torch
from transformers import AutoTokenizer,AutoModelForSequenceClassification, TrainingArguments, Trainer
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import torch

def sentence_predict(sent):
  
  print("input_sent= " + sent)
  pt_model = 'C:\pydata\sware_model_train32_eval64_epochs10.pt'
  print(pt_model)
  device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
  print("device:",device)
  
  device = "cuda" if torch.cuda.is_available() else "cpu"
  model = torch.load(pt_model, map_location=device)
  print(model)

  MODEL_NAME = "beomi/KcELECTRA-base" # hugging face 에 등록된 모델
  tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
  
  model.eval() # 평가

  # 입력문장 토크나이징
  tokenized_sent = tokenizer(
      sent,
      return_tensors="pt",
      truncation=True, 
      add_special_tokens=True, 
      max_length=128
      )

  # 모델 위치 gpu이동
  tokenized_sent.to(device)

  # 예측
  with torch.no_grad():
    outputs = model(
        input_ids=tokenized_sent["input_ids"],
        attention_mask=tokenized_sent["attention_mask"],
        token_type_ids=tokenized_sent["token_type_ids"],
    )

  # 결과
  logits = outputs[0]   ## 마지막 노드에서 아무런 Activation Function을 거치지 않은 값을 Logit
  logits = logits.detach().cpu()
  result = logits.argmax(-1)
  if result == 0:
    result = sent + ">> 악성글로 판단됩니다. 조심하세요."
    
  elif result ==1:
    result= sent + ">> 악의적인 내용이 보이지 않습니다."
    
  return result

# while True:
#   sentence = input("댓글을 입력 해주세요:")
#   if sentence == "0":
#       break
#   print(sentence_predict(sentence))
#   print("\n")