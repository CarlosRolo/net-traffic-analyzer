import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

sns.set_theme(style="darkgrid")
OUTPUT_DIR = "reports/figures"


def plot_protocol_distribution(df: pd.DataFrame, save: bool = True):
    """Gráfica de barras: distribución de protocolos."""
    counts = df["protocol"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    counts.plot(kind="bar", ax=ax, color="steelblue", edgecolor="white")
    ax.set_title("Top 10 Protocolos en el Tráfico Capturado", fontsize=14)
    ax.set_xlabel("Protocolo")
    ax.set_ylabel("Número de Paquetes")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    if save:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        path = f"{OUTPUT_DIR}/protocol_distribution.png"
        plt.savefig(path, dpi=150)
        print(f"[+] Gráfica guardada en {path}")
    plt.show()


def plot_traffic_over_time(df: pd.DataFrame, save: bool = True):
    """Gráfica de línea: volumen de tráfico en el tiempo."""
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    df.set_index("timestamp", inplace=True)
    traffic = df["length"].resample("1s").sum()

    fig, ax = plt.subplots(figsize=(12, 5))
    traffic.plot(ax=ax, color="tomato", linewidth=1.5)
    ax.set_title("Volumen de Tráfico en el Tiempo (bytes/segundo)", fontsize=14)
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Bytes por segundo")
    plt.tight_layout()

    if save:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        path = f"{OUTPUT_DIR}/traffic_over_time.png"
        plt.savefig(path, dpi=150)
        print(f"[+] Gráfica guardada en {path}")
    plt.show()


def plot_top_ips(df: pd.DataFrame, save: bool = True):
    """Gráfica de barras horizontales: IPs con más tráfico."""
    top_src = df.groupby("src")["length"].sum().nlargest(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    top_src.plot(kind="barh", ax=ax, color="mediumseagreen", edgecolor="white")
    ax.set_title("Top 10 IPs Origen por Volumen de Tráfico", fontsize=14)
    ax.set_xlabel("Bytes totales")
    ax.set_ylabel("IP Origen")
    plt.tight_layout()

    if save:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        path = f"{OUTPUT_DIR}/top_ips.png"
        plt.savefig(path, dpi=150)
        print(f"[+] Gráfica guardada en {path}")
    plt.show()
