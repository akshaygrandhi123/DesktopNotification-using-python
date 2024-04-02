import pywhatkit as pw

txt="""Python is an interpreted high-level general-purpose programming
Its design philosophy emphasizes code readability with its"""

pw.text_to_handwriting(txt, "1.png", [0, 0,138])
print(" END ")