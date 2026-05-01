import pyshark
import pandas as pd


def pcap_to_dataframe(filepath: str) -> pd.DataFrame:
    """
    Lee un archivo .pcap y retorna un DataFrame con los paquetes.
    
    Args:
        filepath: Ruta al archivo .pcap
    
    Returns:
        DataFrame con columnas: timestamp, src, dst, protocol, length
    """
    cap = pyshark.FileCapture(filepath)
    
    packets = []
    for pkt in cap:
        try:
            packets.append({
                "timestamp": float(pkt.sniff_timestamp),
                "src":       pkt.ip.src,
                "dst":       pkt.ip.dst,
                "protocol":  pkt.highest_layer,
                "length":    int(pkt.length)
            })
        except AttributeError:
            # Paquetes sin capa IP (ARP, etc.) se omiten
            continue
    
    cap.close()
    return pd.DataFrame(packets)


def summary(df: pd.DataFrame) -> dict:
    """Retorna estadísticas básicas del tráfico."""
    return {
        "total_packets":   len(df),
        "total_bytes":     df["length"].sum(),
        "avg_packet_size": round(df["length"].mean(), 2),
        "top_protocol":    df["protocol"].value_counts().idxmax(),
        "unique_ips":      df["src"].nunique() + df["dst"].nunique()
    }
