from io import BytesIO

from PIL import Image
import streamlit as st

from stage2_inference import Stage2CaptionService


st.set_page_config(
    page_title="Stage 2 Image Captioning",
    page_icon="📷",
    layout="centered",
)


@st.cache_resource
def load_service():
    return Stage2CaptionService()


try:
    service = load_service()
    info = service.info()
except Exception as error:
    st.title("Stage 2 Image Captioning")
    st.error(str(error))
    st.code(
        "torch.save({\n"
        "    'model_state_dict': model.state_dict(),\n"
        "    'vocab': vocab,\n"
        "    'embed_size': embed_size,\n"
        "    'hidden_size': hidden_size,\n"
        "    'num_layers': num_layers,\n"
        "    'max_caption_words': MAX_CAPTION_WORDS,\n"
        "}, 'caption_model_stage2_checkpoint.pth')",
        language="python",
    )
    st.stop()


st.title("Новое веб-приложение для Stage 2")
st.write("Загрузите фотографию, и модель сгенерирует текстовое описание на основе уже обученных весов.")

with st.sidebar:
    st.subheader("Конфигурация модели")
    st.write(f"Устройство: `{info['device']}`")
    st.write(f"Checkpoint: `{info['checkpoint']}`")
    st.write(f"Размер словаря: `{info['vocab_size']}`")
    st.write(f"Максимум слов: `{info['max_caption_words']}`")

uploaded_file = st.file_uploader(
    "Загрузите изображение",
    type=["jpg", "jpeg", "png", "bmp", "webp"],
)

if uploaded_file is None:
    st.info("Добавьте изображение, чтобы получить описание.")
    st.stop()

image_bytes = uploaded_file.getvalue()
image = Image.open(BytesIO(image_bytes)).convert("RGB")
st.image(image, caption="Загруженное изображение", use_container_width=True)

max_words = st.slider(
    "Максимальная длина описания",
    min_value=3,
    max_value=20,
    value=min(10, info["max_caption_words"]),
)

if st.button("Сгенерировать описание", type="primary", use_container_width=True):
    with st.spinner("Модель обрабатывает изображение..."):
        caption = service.predict(image, max_len=max_words)
    st.subheader("Описание")
    st.success(caption)
