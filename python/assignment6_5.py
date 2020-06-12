text = "X-DSPAM-Confidence:    0.8475";

text_end_pos = text.find(':')

num_text = text[text_end_pos+1:]

s_num_text = num_text.lstrip()

f_num = float(s_num_text)

print(f_num)