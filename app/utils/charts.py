import matplotlib.pyplot as plt
import io
import base64

def generate_chart(data):
    estados = [item["_id"] for item in data]
    counts = [item["count"] for item in data]

    plt.figure(figsize=(6,4))
    plt.bar(estados, counts, color="skyblue")
    plt.xlabel("Estado")
    plt.ylabel("Cantidad de paquetes")
    plt.title("Paquetes por estado")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    buf.close()
    return img_base64