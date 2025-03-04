# pdf-extraction

  - For documents like PDFs & images, formatting information is visual.
  - Document image analysis (DIA) to extract formatting information and text
    - Document Layout Detection (DLD) - use object detection model to draw and label bounding boxes
      - Vision detection(YOLOX or Detectron2), Text Extraction (OCR if required)
      - requires two model calls (obj det + OCR) and less flexible   
    - Vision Transformer (ViT) - take document image as input and produce a text representation like JSON as output (can optionally include text prompt)
      - DONUT - Document Understanding Transformer. Implementation [here](https://github.com/clovaai/donut)
      - No OCR required, Image input is directly converted to text. Can train the model to output a valid JSON string.
      - model is generative, prone to hallucination, computationally expensive.
