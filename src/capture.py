import argparse
import sys
from analyzer import pcap_to_dataframe, summary
from visualizer import (
    plot_protocol_distribution,
    plot_traffic_over_time,
    plot_top_ips
)


def main():
    parser = argparse.ArgumentParser(
        description="NET-01: Analizador de tráfico de red"
    )
    parser.add_argument(
        "pcap_file",
        help="Ruta al archivo .pcap a analizar"
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="No guardar gráficas en disco"
    )
    args = parser.parse_args()

    print(f"\n[*] Analizando: {args.pcap_file}")
    print("-" * 50)

    df = pcap_to_dataframe(args.pcap_file)

    if df.empty:
        print("[!] No se encontraron paquetes IP en el archivo.")
        sys.exit(1)

    stats = summary(df)
    print(f"[+] Total de paquetes : {stats['total_packets']}")
    print(f"[+] Total de bytes    : {stats['total_bytes']:,}")
    print(f"[+] Tamaño promedio   : {stats['avg_packet_size']} bytes")
    print(f"[+] Protocolo top     : {stats['top_protocol']}")
    print(f"[+] IPs únicas        : {stats['unique_ips']}")
    print("-" * 50)

    save = not args.no_save
    plot_protocol_distribution(df, save=save)
    plot_traffic_over_time(df, save=save)
    plot_top_ips(df, save=save)

    print("\n[✓] Análisis completado.")


if __name__ == "__main__":
    main()
